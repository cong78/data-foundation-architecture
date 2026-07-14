#!/usr/bin/env python3
"""Conservatively compare two structured data contract artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CLASSIFICATION_RANK = {
    "public": 0,
    "internal": 1,
    "confidential": 2,
    "restricted": 3,
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot read {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def field_map(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    fields = contract.get("data", {}).get("schema", {}).get("fields", [])
    if not isinstance(fields, list):
        raise ValueError("data.schema.fields must be an array")
    result: dict[str, dict[str, Any]] = {}
    for field in fields:
        if not isinstance(field, dict) or not isinstance(field.get("name"), str):
            raise ValueError("Each schema field must be an object with a string name")
        result[field["name"]] = field
    return result


def major_version(version: str) -> int | None:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    return int(match.group(1)) if match else None


def compare(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    for key in ("contract_id", "contract_type", "version"):
        if not isinstance(before.get(key), str) or not isinstance(after.get(key), str):
            raise ValueError(f"Both artifacts require a string {key}")
    if before["contract_id"] != after["contract_id"]:
        raise ValueError("Contract ids differ; compare versions of the same contract")
    if before["contract_type"] != after["contract_type"]:
        raise ValueError("Contract type changes are not version-compatible")

    changes: list[dict[str, str]] = []
    breaking = False
    additive = False

    old_fields = field_map(before)
    new_fields = field_map(after)

    for name in sorted(old_fields.keys() - new_fields.keys()):
        breaking = True
        changes.append({"level": "major", "area": "schema", "detail": f"Removed field: {name}"})

    for name in sorted(new_fields.keys() - old_fields.keys()):
        required = bool(new_fields[name].get("required"))
        if required:
            breaking = True
            level = "major"
            detail = f"Added required field: {name}"
        else:
            additive = True
            level = "minor"
            detail = f"Added optional field: {name}"
        changes.append({"level": level, "area": "schema", "detail": detail})

    for name in sorted(old_fields.keys() & new_fields.keys()):
        old = old_fields[name]
        new = new_fields[name]
        if old.get("type") != new.get("type"):
            breaking = True
            changes.append({
                "level": "major",
                "area": "schema",
                "detail": f"Changed type for {name}: {old.get('type')} -> {new.get('type')}",
            })
        if not bool(old.get("required")) and bool(new.get("required")):
            breaking = True
            changes.append({"level": "major", "area": "schema", "detail": f"Made field required: {name}"})

    old_class = before.get("data", {}).get("classification")
    new_class = after.get("data", {}).get("classification")
    if old_class != new_class:
        old_rank = CLASSIFICATION_RANK.get(str(old_class).lower(), -1)
        new_rank = CLASSIFICATION_RANK.get(str(new_class).lower(), -1)
        level = "major" if new_rank > old_rank or -1 in (old_rank, new_rank) else "minor"
        breaking = breaking or level == "major"
        additive = additive or level == "minor"
        changes.append({"level": level, "area": "classification", "detail": f"Changed classification: {old_class} -> {new_class}"})

    old_uses = set(before.get("purpose", {}).get("valid_uses", []))
    new_uses = set(after.get("purpose", {}).get("valid_uses", []))
    widened = sorted(new_uses - old_uses)
    if widened:
        breaking = True
        changes.append({"level": "major", "area": "purpose", "detail": f"Widened valid uses: {', '.join(widened)}"})

    for area in ("trust", "control"):
        if before.get(area, {}) != after.get(area, {}):
            breaking = True
            changes.append({
                "level": "major",
                "area": area,
                "detail": f"Changed {area} terms; executable evidence is required to prove compatibility",
            })

    if breaking:
        recommendation = "major"
        status = "breaking"
    elif additive:
        recommendation = "minor"
        status = "compatible"
    else:
        recommendation = "patch"
        status = "compatible"
        if before != after:
            changes.append({"level": "patch", "area": "metadata", "detail": "Only non-classified metadata changed; confirm that behavior and meaning are unchanged"})
        else:
            changes.append({"level": "patch", "area": "none", "detail": "No contract term changes detected"})

    old_major = major_version(before["version"])
    new_major = major_version(after["version"])
    version_consistent = None
    if old_major is not None and new_major is not None:
        version_consistent = new_major > old_major if recommendation == "major" else new_major == old_major

    return {
        "contract_id": before["contract_id"],
        "contract_type": before["contract_type"],
        "before_version": before["version"],
        "after_version": after["version"],
        "status": status,
        "recommended_version": recommendation,
        "version_consistent": version_consistent,
        "changes": changes,
        "note": "Structural comparison is conservative; semantic and runtime compatibility still require accountable evidence.",
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# Compatibility: {result['contract_id']}",
        "",
        f"- Status: **{result['status']}**",
        f"- Recommended version: **{result['recommended_version']}**",
        f"- Compared: `{result['before_version']}` -> `{result['after_version']}`",
        f"- Supplied version is consistent: **{result['version_consistent']}**",
        "",
        "## Changes",
        "",
    ]
    lines.extend(f"- **{item['level']} · {item['area']}:** {item['detail']}" for item in result["changes"])
    lines.extend(["", f"> {result['note']}"])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    try:
        result = compare(load_json(args.before), load_json(args.after))
    except ValueError as error:
        print(f"Compatibility assessment failed: {error}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

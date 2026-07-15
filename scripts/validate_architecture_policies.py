#!/usr/bin/env python3
"""Validate architecture policy documents and their executable references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


KEYWORD_PATTERN = re.compile(r"\b(?:MUST NOT|SHOULD NOT|MUST|SHOULD|MAY)\b")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schema_path = root / "policies/schema/architecture-policy.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    documents = sorted((root / "policies/examples").glob("*.policy.yaml"))

    if not documents:
        errors.append("No architecture policy examples found")

    for path in documents:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "document"
            errors.append(f"{path.relative_to(root)}:{location}: {error.message}")

        if not isinstance(document, dict):
            continue

        identifiers: list[str] = []
        spec = document.get("spec", {})
        principle = spec.get("principle", {}) if isinstance(spec, dict) else {}
        if isinstance(principle, dict) and isinstance(principle.get("id"), str):
            identifiers.append(principle["id"])

        implementation = document.get("implementation", {})
        entrypoint = implementation.get("entrypoint") if isinstance(implementation, dict) else None
        rules = spec.get("rules", []) if isinstance(spec, dict) else []
        for rule in rules if isinstance(rules, list) else []:
            if not isinstance(rule, dict):
                continue
            rule_id = rule.get("id")
            if isinstance(rule_id, str):
                identifiers.append(rule_id)
            level = rule.get("level")
            keywords = KEYWORD_PATTERN.findall(str(rule.get("statement", "")))
            if keywords != [level]:
                errors.append(
                    f"{path.relative_to(root)}:{rule_id}: statement must contain exactly its declared keyword {level}"
                )
            outcome = rule.get("enforcement", {}).get("outcome")
            if level in {"MUST", "MUST NOT"} and outcome != "block":
                errors.append(f"{path.relative_to(root)}:{rule_id}: mandatory rules must block")
            for criterion in rule.get("criteria", []):
                if not isinstance(criterion, dict):
                    continue
                criterion_id = criterion.get("id")
                if isinstance(criterion_id, str):
                    identifiers.append(criterion_id)
                if criterion.get("decisionRef") != entrypoint:
                    errors.append(
                        f"{path.relative_to(root)}:{criterion_id}: decisionRef must match implementation.entrypoint"
                    )

        if len(identifiers) != len(set(identifiers)):
            errors.append(f"{path.relative_to(root)}: policy identifiers must be unique")

        if isinstance(implementation, dict):
            for field in ("modules", "tests"):
                for reference in implementation.get(field, []):
                    if not (root / reference).is_file():
                        errors.append(f"{path.relative_to(root)}: missing {field} reference {reference}")

    if errors:
        print("Architecture policy validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(documents)} architecture policy document(s) against JSON Schema 2020-12.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

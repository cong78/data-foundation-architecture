#!/usr/bin/env python3
"""Validate the portable Data Contract Designer skill package."""

from __future__ import annotations

import json
import re
from pathlib import Path


REQUIRED_MANIFEST_FIELDS = {
    "id", "version", "name", "description", "capabilities", "side_effects",
    "authorization", "data_policy", "idempotency", "reliability", "approval",
    "observability", "tests",
}
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "manifest.json",
    "references/guidance-map.md",
    "references/evidence-rules.md",
    "references/output-contracts.md",
    "schemas/contract-request.schema.json",
    "schemas/compatibility-request.schema.json",
    "schemas/contract-result.schema.json",
    "assets/creation-request.example.json",
    "assets/creation-result.example.json",
    "assets/compatibility-before.example.json",
    "assets/compatibility-after.example.json",
    "scripts/assess_compatibility.py",
    "scripts/validate_examples.py",
    "scripts/verify_guidance_map.py",
)


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (skill_dir / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not frontmatter:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        metadata = frontmatter.group(1)
        if not re.search(r"^name:\s*data-contract-designer\s*$", metadata, re.MULTILINE):
            errors.append("SKILL.md name must be data-contract-designer")
        if not re.search(r"^description:\s*\S", metadata, re.MULTILINE):
            errors.append("SKILL.md description is required")

    try:
        manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"Invalid manifest.json: {error}")
        manifest = {}
    if not isinstance(manifest, dict):
        errors.append("manifest.json root must be an object")
        manifest = {}
    missing = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
    if missing:
        errors.append(f"manifest.json missing fields: {', '.join(missing)}")
    if manifest.get("id") != "data-contract-designer":
        errors.append("manifest id must be data-contract-designer")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        errors.append("manifest version must use semantic versioning")
    capabilities = manifest.get("capabilities", [])
    ids = {item.get("id") for item in capabilities if isinstance(item, dict)}
    if ids != {"design", "review", "compatibility", "change-impact"}:
        errors.append("manifest capabilities are incomplete")
    for item in capabilities:
        if not isinstance(item, dict):
            errors.append("Each capability must be an object")
            continue
        for field in ("input_schema", "output_schema"):
            reference = item.get(field)
            if not isinstance(reference, str) or not (skill_dir / reference).is_file():
                errors.append(f"Capability {item.get('id')} has invalid {field}: {reference}")

    for path in sorted((skill_dir / "schemas").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid JSON schema {path.name}: {error}")

    for test in manifest.get("tests", []):
        script = test.split()[0] if isinstance(test, str) else ""
        if not script or not (skill_dir / script).is_file():
            errors.append(f"Manifest test references a missing script: {script}")

    if errors:
        print("Skill package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated portable skill {manifest['id']} v{manifest['version']} with {len(capabilities)} capabilities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

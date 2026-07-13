#!/usr/bin/env python3
"""Validate the portable Data Foundation Architect skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_MANIFEST_FIELDS = {
    "id",
    "version",
    "name",
    "description",
    "capabilities",
    "side_effects",
    "authorization",
    "data_policy",
    "idempotency",
    "reliability",
    "approval",
    "observability",
    "tests",
}

def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    skill_file = skill_dir / "SKILL.md"
    manifest_file = skill_dir / "manifest.json"
    required_files = [
        skill_file,
        manifest_file,
        skill_dir / "references/guidance-map.md",
        skill_dir / "references/evidence-rules.md",
        skill_dir / "references/output-contracts.md",
        skill_dir / "scripts/validate_examples.py",
        skill_dir / "schemas/domain-assessment-input.schema.json",
        skill_dir / "schemas/domain-assessment-output.schema.json",
        skill_dir / "schemas/task-request.schema.json",
        skill_dir / "schemas/task-result.schema.json",
        skill_dir / "assets/domain-assessment.example.json",
        skill_dir / "assets/task-request.example.json",
    ]
    for path in required_files:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(skill_dir)}")

    if skill_file.is_file():
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not frontmatter:
            errors.append("SKILL.md must start with YAML frontmatter")
        else:
            metadata = frontmatter.group(1)
            if not re.search(r"^name:\s*data-foundation-architect\s*$", metadata, re.MULTILINE):
                errors.append("SKILL.md name must be data-foundation-architect")
            if not re.search(r"^description:\s*\S", metadata, re.MULTILINE):
                errors.append("SKILL.md description is required")

    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        errors.append(f"Invalid manifest.json: {error}")
        manifest = {}

    if not isinstance(manifest, dict):
        errors.append("manifest.json root must be an object")
        manifest = {}

    missing_fields = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
    if missing_fields:
        errors.append(f"manifest.json missing fields: {', '.join(missing_fields)}")
    if manifest.get("id") != "data-foundation-architect":
        errors.append("manifest.json id must be data-foundation-architect")
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("manifest.json version must use semantic versioning")
    capabilities = manifest.get("capabilities", [])
    capability_ids = {item.get("id") for item in capabilities if isinstance(item, dict)}
    if capability_ids != {"assess", "design", "review", "generate"}:
        errors.append("manifest capabilities must be assess, design, review, and generate")
    for capability in capabilities:
        if not isinstance(capability, dict):
            errors.append("Each manifest capability must be an object")
            continue
        for field in ("input_schema", "output_schema"):
            reference = capability.get(field)
            if not isinstance(reference, str) or not (skill_dir / reference).is_file():
                errors.append(
                    f"Capability {capability.get('id', 'unknown')} has invalid {field}: {reference}"
                )

    for schema in sorted((skill_dir / "schemas").glob("*.json")):
        try:
            json.loads(schema.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid JSON schema {schema.name}: {error}")

    for test in manifest.get("tests", []):
        if not isinstance(test, str) or not test.strip():
            errors.append("Each manifest test must be a non-empty string")
            continue
        script = test.split()[0]
        if not (skill_dir / script).is_file():
            errors.append(f"Manifest test references a missing script: {script}")

    if errors:
        print("Skill package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validated portable skill {manifest['id']} v{manifest['version']} "
        f"with {len(capabilities)} capabilities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

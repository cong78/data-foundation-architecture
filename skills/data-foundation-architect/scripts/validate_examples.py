#!/usr/bin/env python3
"""Validate bundled examples and scorer output against local JSON Schemas."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

from assess_maturity import score_assessment


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_ref(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError(f"Only local schema references are supported: {reference}")
    value: Any = root
    for part in reference[2:].split("/"):
        key = part.replace("~1", "/").replace("~0", "~")
        value = value[key]
    if not isinstance(value, dict):
        raise ValueError(f"Schema reference does not resolve to an object: {reference}")
    return value


def matches_type(value: Any, expected: str) -> bool:
    checks = {
        "object": lambda item: isinstance(item, dict),
        "array": lambda item: isinstance(item, list),
        "string": lambda item: isinstance(item, str),
        "boolean": lambda item: isinstance(item, bool),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
        "null": lambda item: item is None,
    }
    return checks[expected](value)


def validate(value: Any, schema: dict[str, Any], root: dict[str, Any], path: str = "$") -> list[str]:
    if "$ref" in schema:
        return validate(value, resolve_ref(root, schema["$ref"]), root, path)

    errors: list[str] = []
    expected = schema.get("type")
    if isinstance(expected, str) and not matches_type(value, expected):
        return [f"{path}: expected {expected}, got {type(value).__name__}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in {schema['enum']!r}")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")
        if schema.get("format") == "date":
            try:
                date.fromisoformat(value)
            except ValueError:
                errors.append(f"{path}: expected ISO date")

    if isinstance(value, int) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value is below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: value is above maximum")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than minItems")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate(item, item_schema, root, f"{path}[{index}]"))

    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing required property {required!r}")

        properties = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        for key, item in value.items():
            if key in properties:
                errors.extend(validate(item, properties[key], root, f"{path}.{key}"))
            elif additional is False:
                errors.append(f"{path}: unexpected property {key!r}")
            elif isinstance(additional, dict):
                errors.extend(validate(item, additional, root, f"{path}.{key}"))

    return errors


def check(value: Any, schema: dict[str, Any], label: str) -> list[str]:
    return [f"{label}: {error}" for error in validate(value, schema, schema)]


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    schemas = skill_dir / "schemas"
    assets = skill_dir / "assets"

    assessment_input = load_json(assets / "domain-assessment.example.json")
    task_input = load_json(assets / "task-request.example.json")
    assessment_output = score_assessment(assessment_input)
    task_output = {
        "task_id": task_input["task_id"],
        "capability": task_input["capability"],
        "status": "draft",
        "scope": task_input["scope"],
        "summary": "Schema validation example.",
        "guidance_used": task_input.get("context_references", []),
    }

    contracts = [
        (assessment_input, load_json(schemas / "domain-assessment-input.schema.json"), "assessment input"),
        (assessment_output, load_json(schemas / "domain-assessment-output.schema.json"), "assessment output"),
        (task_input, load_json(schemas / "task-request.schema.json"), "task request"),
        (task_output, load_json(schemas / "task-result.schema.json"), "task result"),
    ]

    errors: list[str] = []
    for value, schema, label in contracts:
        errors.extend(check(value, schema, label))

    if errors:
        print("Example schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(contracts)} example and generated contracts against local schemas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

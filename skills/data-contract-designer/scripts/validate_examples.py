#!/usr/bin/env python3
"""Validate the bundled Data Contract Designer examples."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain an object")
    return value


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    assets = skill_dir / "assets"
    request = load_object(assets / "creation-request.example.json")
    result = load_object(assets / "creation-result.example.json")
    errors: list[str] = []

    if request.get("operation") != "design" or request.get("contract_type") != "data_product_creation":
        errors.append("Creation request must exercise data_product_creation design")
    if result.get("task_id") != request.get("task_id"):
        errors.append("Creation result task_id must match request")
    for key in ("readiness", "contract_type", "summary", "findings", "evidence_gaps", "approvals_required", "next_actions", "guidance_used"):
        if key not in result:
            errors.append(f"Creation result is missing {key}")

    command = [
        sys.executable,
        str(skill_dir / "scripts/assess_compatibility.py"),
        str(assets / "compatibility-before.example.json"),
        str(assets / "compatibility-after.example.json"),
        "--format", "json",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        errors.append(f"Compatibility example failed: {completed.stderr.strip()}")
    else:
        compatibility = json.loads(completed.stdout)
        if compatibility.get("status") != "breaking" or compatibility.get("recommended_version") != "major":
            errors.append("Compatibility example must produce a breaking major recommendation")
        if compatibility.get("version_consistent") is not True:
            errors.append("Compatibility example version must be consistent with the major recommendation")

    if errors:
        print("Example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validated design request/result and breaking-change compatibility examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

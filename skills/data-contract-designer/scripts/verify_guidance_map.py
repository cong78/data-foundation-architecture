#!/usr/bin/env python3
"""Verify that repository paths referenced by the skill exist."""

from __future__ import annotations

import re
from pathlib import Path


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    repo_root = skill_dir.parents[1]
    files = [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]
    references: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        references.update(re.findall(r"`((?:docs|skills)/[^`]+\.(?:md|json|py))`", text))
    missing = sorted(reference for reference in references if not (repo_root / reference).is_file())
    if missing:
        print("Guidance map validation failed:")
        for reference in missing:
            print(f"- Missing: {reference}")
        return 1
    print(f"Validated {len(references)} repository paths from {len(files)} skill files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

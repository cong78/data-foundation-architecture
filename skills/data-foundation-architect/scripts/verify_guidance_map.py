#!/usr/bin/env python3
"""Verify that repository Markdown paths referenced by the skill still exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOC_PATH = re.compile(r"`(docs/[A-Za-z0-9_./-]+\.md)`")


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    repo_root = skill_dir.parents[1]
    sources = [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]
    references: set[str] = set()
    for source in sources:
        references.update(DOC_PATH.findall(source.read_text(encoding="utf-8")))

    missing = [path for path in sorted(references) if not (repo_root / path).is_file()]
    if missing:
        print("Missing guidance paths:")
        for path in missing:
            print(f"- {path}")
        return 1

    print(f"Validated {len(references)} guidance paths from {len(sources)} skill files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

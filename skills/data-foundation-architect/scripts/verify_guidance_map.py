#!/usr/bin/env python3
"""Verify that repository Markdown paths referenced by the skill still exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOC_PATH = re.compile(r"`(docs/[A-Za-z0-9_./-]+\.md)`")

REQUIRED_GUIDANCE = {
    "docs/foundation/foundation-in-one-view.md",
    "docs/architecture/architecture-to-delivery.md",
    "docs/services/index.md",
    "docs/services/data-service-portal.md",
    "docs/services/data-foundation-operations-service.md",
    "docs/architecture/design-map.md",
    "docs/architecture/integration-design.md",
    "docs/reference-solutions/service-runbook-template.md",
}


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    repo_root = skill_dir.parents[1]
    sources = [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]
    references: set[str] = set()
    for source in sources:
        references.update(DOC_PATH.findall(source.read_text(encoding="utf-8")))

    missing = [path for path in sorted(references) if not (repo_root / path).is_file()]
    missing_coverage = sorted(REQUIRED_GUIDANCE - references)
    if missing:
        print("Missing guidance paths:")
        for path in missing:
            print(f"- {path}")
    if missing_coverage:
        print("Required guidance is not mapped by the skill:")
        for path in missing_coverage:
            print(f"- {path}")
    if missing or missing_coverage:
        return 1

    print(f"Validated {len(references)} guidance paths from {len(sources)} skill files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail when Markdown pages are missing from navigation or nav targets do not exist."""

from pathlib import Path

from mkdocs.config import load_config


def collect_nav_pages(items: list[object]) -> list[str]:
    pages: list[str] = []
    for item in items:
        if isinstance(item, str):
            pages.append(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    pages.append(value)
                elif isinstance(value, list):
                    pages.extend(collect_nav_pages(value))
    return pages


def main() -> int:
    config = load_config()
    docs_dir = Path(config["docs_dir"])
    nav_pages = collect_nav_pages(config.get("nav") or [])

    existing = {
        path.relative_to(docs_dir).as_posix()
        for path in docs_dir.rglob("*.md")
    }
    referenced = set(nav_pages)
    missing = sorted(referenced - existing)
    orphaned = sorted(existing - referenced)

    if missing:
        print("Navigation targets that do not exist:")
        for path in missing:
            print(f"  - {path}")
    if orphaned:
        print("Markdown pages missing from navigation:")
        for path in orphaned:
            print(f"  - {path}")
    if missing or orphaned:
        return 1

    print(
        f"Validated {len(existing)} Markdown pages across "
        f"{len(nav_pages)} navigation entries ({len(referenced)} unique)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate internal links, anchors, and assets in a generated MkDocs site."""

from __future__ import annotations

import argparse
import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


SKIPPED_SCHEMES = {"data", "javascript", "mailto", "tel"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attribute in ("id", "name"):
            if values.get(attribute):
                self.anchors.add(values[attribute] or "")

        if tag in {"a", "link"} and values.get("href"):
            self.references.append(("href", values["href"] or ""))
        if tag in {"img", "script", "source"} and values.get("src"):
            self.references.append(("src", values["src"] or ""))


def public_path(file_path: Path, site_dir: Path) -> str:
    relative = file_path.relative_to(site_dir).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def target_file(path: str, site_dir: Path) -> Path:
    relative = path.lstrip("/")
    candidate = site_dir / relative
    if path.endswith("/") or candidate.is_dir():
        return candidate / "index.html"
    return candidate


def resolve_path(reference: str, source_public_path: str) -> tuple[str, str]:
    parsed = urlsplit(reference)
    path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)

    if not path:
        return source_public_path, fragment
    if path.startswith("/"):
        resolved = posixpath.normpath(path)
    else:
        source_directory = source_public_path if source_public_path.endswith("/") else posixpath.dirname(source_public_path)
        resolved = posixpath.normpath(posixpath.join(source_directory, path))

    if path.endswith("/") and not resolved.endswith("/"):
        resolved += "/"
    if not resolved.startswith("/"):
        resolved = "/" + resolved
    return resolved, fragment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site_dir", nargs="?", default="site", type=Path)
    args = parser.parse_args()
    site_dir = args.site_dir.resolve()

    if not site_dir.is_dir():
        print(f"Site directory does not exist: {site_dir}", file=sys.stderr)
        return 2

    pages: dict[str, tuple[Path, PageParser]] = {}
    for html_file in sorted(site_dir.rglob("*.html")):
        page = PageParser()
        page.feed(html_file.read_text(encoding="utf-8"))
        pages[public_path(html_file, site_dir)] = (html_file, page)

    errors: list[str] = []
    checked = 0

    for source_path, (source_file, page) in pages.items():
        for attribute, reference in page.references:
            parsed = urlsplit(reference)
            if parsed.scheme in {"http", "https"} or parsed.scheme in SKIPPED_SCHEMES or parsed.netloc:
                continue

            checked += 1
            resolved_path, fragment = resolve_path(reference, source_path)
            destination = target_file(resolved_path, site_dir)

            if not destination.exists():
                errors.append(
                    f"{source_file.relative_to(site_dir)}: broken {attribute} '{reference}' -> '{resolved_path}'"
                )
                continue

            if fragment and destination.suffix == ".html":
                destination_public = public_path(destination, site_dir)
                destination_page = pages.get(destination_public)
                if destination_page and fragment not in destination_page[1].anchors:
                    errors.append(
                        f"{source_file.relative_to(site_dir)}: missing anchor '#{fragment}' in '{resolved_path}'"
                    )

    if errors:
        print("Internal link validation failed:")
        for error in sorted(errors):
            print(f"- {error}")
        print(f"\n{len(errors)} error(s) across {checked} internal references.")
        return 1

    print(f"Validated {checked} internal references across {len(pages)} HTML pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

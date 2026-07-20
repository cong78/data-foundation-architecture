#!/usr/bin/env python3
"""Build the deterministic documentation knowledge-graph dataset."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
OUTPUT = DOCS / "assets" / "data" / "guidance-graph.json"
REGISTRY = DOCS / "assets" / "data" / "architecture-registry.yaml"

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"href=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
WORD = re.compile(r"\b[\w][\w'-]*\b", re.UNICODE)


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def route_for(path: str) -> str:
    if path == "index.md":
        return ""
    if path.endswith("/index.md"):
        return path[: -len("index.md")]
    return path[: -len(".md")] + "/"


def title_and_words(path: str) -> tuple[str, int]:
    source = (DOCS / path).read_text(encoding="utf-8")
    heading = HEADING.search(source)
    title = heading.group(1).strip() if heading else Path(path).stem.replace("-", " ").title()
    body = re.sub(r"```.*?```", " ", source, flags=re.DOTALL)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"[#*_`|>\[\]()]", " ", body)
    return title, len(WORD.findall(body))


def load_navigation() -> list[dict[str, object]]:
    source = MKDOCS.read_text(encoding="utf-8")
    marker = "\nnav:\n"
    if marker not in source:
        raise ValueError("mkdocs.yml has no nav section")
    nav_only = yaml.safe_load("nav:\n" + source.split(marker, 1)[1])
    return nav_only["nav"]


def flatten_navigation(nav: list[dict[str, object]]) -> tuple[list[dict], list[dict], dict[str, dict]]:
    root_id = "nav:data-foundation-architecture-guide"
    nodes: list[dict] = [
        {
            "id": root_id,
            "kind": "root",
            "title": "Data Foundation Architecture Guide",
            "navLabel": "Guide",
            "group": "Documentation",
            "breadcrumbs": ["Data Foundation Architecture Guide"],
            "url": "/",
            "words": 0,
        }
    ]
    links: list[dict] = []
    pages: dict[str, dict] = {}

    def walk(items: list[dict[str, object]], parent: str | None, ancestors: list[str]) -> None:
        for item in items:
            if not isinstance(item, dict) or len(item) != 1:
                raise ValueError(f"Unsupported navigation item: {item!r}")
            label, value = next(iter(item.items()))
            breadcrumbs = [*ancestors, label]
            group = breadcrumbs[0]
            if isinstance(value, str):
                title, words = title_and_words(value)
                node = {
                    "id": value,
                    "kind": "page",
                    "title": title,
                    "navLabel": label,
                    "group": group,
                    "breadcrumbs": breadcrumbs,
                    "url": "/" + route_for(value),
                    "words": words,
                }
                nodes.append(node)
                pages[value] = node
                if parent:
                    links.append({"source": parent, "target": value, "type": "contains"})
                continue
            if not isinstance(value, list):
                raise ValueError(f"Unsupported navigation branch: {label!r}")
            node_id = "nav:" + "/".join(slug(part) for part in breadcrumbs)
            nodes.append(
                {
                    "id": node_id,
                    "kind": "group" if not ancestors else "section",
                    "title": label,
                    "navLabel": label,
                    "group": group,
                    "breadcrumbs": breadcrumbs,
                    "url": None,
                    "words": 0,
                }
            )
            if parent:
                links.append({"source": parent, "target": node_id, "type": "contains"})
            walk(value, node_id, breadcrumbs)

    walk(nav, root_id, [])
    return nodes, links, pages


def candidate_targets(source_path: str, raw_target: str, route_map: dict[str, str]) -> list[str]:
    target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("#", "mailto:", "tel:", "javascript:")):
        return []
    clean = unquote(parsed.path)
    if not clean:
        return []

    candidates: list[str] = []
    if clean.endswith(".md"):
        candidates.append(posixpath.normpath(posixpath.join(posixpath.dirname(source_path), clean)))

    source_route = "/" + route_for(source_path)
    resolved_route = urljoin(source_route, clean).lstrip("/")
    if resolved_route in route_map:
        candidates.append(route_map[resolved_route])
    if resolved_route.rstrip("/") + "/" in route_map:
        candidates.append(route_map[resolved_route.rstrip("/") + "/"])
    if clean.startswith("/"):
        absolute_route = clean.lstrip("/")
        if absolute_route in route_map:
            candidates.append(route_map[absolute_route])
    return candidates


def reference_links(pages: dict[str, dict]) -> list[dict]:
    route_map = {route_for(path): path for path in pages}
    edges: set[tuple[str, str]] = set()
    for source_path in pages:
        source = (DOCS / source_path).read_text(encoding="utf-8")
        targets = MARKDOWN_LINK.findall(source) + HTML_LINK.findall(source)
        for target in targets:
            for resolved in candidate_targets(source_path, target, route_map):
                if resolved in pages and resolved != source_path:
                    edges.add((source_path, resolved))
                    break
    return [
        {"source": source, "target": target, "type": "references"}
        for source, target in sorted(edges)
    ]


def architecture_links(pages: dict[str, dict]) -> tuple[list[dict], dict]:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    entities = registry["entities"]
    links: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    for relationship in registry["relationships"]:
        source_entity = relationship["source"]
        target_entity = relationship["target"]
        source = entities[source_entity]["page"].split("#", 1)[0]
        target = entities[target_entity]["page"].split("#", 1)[0]
        relation_type = relationship["type"]
        if source == target or source not in pages or target not in pages:
            continue
        key = (source, relation_type, target)
        if key in seen:
            continue
        seen.add(key)
        links.append(
            {
                "source": source,
                "target": target,
                "type": "architecture",
                "relationshipType": relation_type,
                "sourceEntity": source_entity,
                "targetEntity": target_entity,
            }
        )
    return sorted(links, key=lambda link: (link["relationshipType"], link["source"], link["target"])), registry


def build() -> dict:
    nodes, hierarchy_links, pages = flatten_navigation(load_navigation())
    references = reference_links(pages)
    architecture, registry = architecture_links(pages)
    incoming = Counter(link["target"] for link in references)
    outgoing = Counter(link["source"] for link in references)
    architecture_incoming = Counter(link["target"] for link in architecture)
    architecture_outgoing = Counter(link["source"] for link in architecture)
    for node in nodes:
        node["incoming"] = incoming[node["id"]]
        node["outgoing"] = outgoing[node["id"]]
        node["architectureIncoming"] = architecture_incoming[node["id"]]
        node["architectureOutgoing"] = architecture_outgoing[node["id"]]

    group_counts = Counter(node["group"] for node in pages.values())
    orphans = sorted(
        (
            node
            for node in pages.values()
            if incoming[node["id"]] == 0
            and node["id"] != "index.md"
            and node["group"] != "Decisions"
        ),
        key=lambda node: node["title"],
    )
    largest = sorted(pages.values(), key=lambda node: (-node["words"], node["title"]))[:8]
    referenced = sorted(pages.values(), key=lambda node: (-node["incoming"], node["title"]))[:8]
    max_depth = max(len(node["breadcrumbs"]) for node in pages.values())

    return {
        "schemaVersion": 2,
        "metrics": {
            "pages": len(pages),
            "navigationNodes": len(nodes) - len(pages),
            "navigationRelationships": len(hierarchy_links),
            "referenceRelationships": len(references),
            "architectureRelationships": len(architecture),
            "architectureRelationshipTypes": dict(sorted(Counter(link["relationshipType"] for link in architecture).items())),
            "registryEntities": len(registry["entities"]),
            "referenceDensity": round(len(references) / len(pages), 1),
            "topLevelSections": len(group_counts),
            "maximumNavigationDepth": max_depth,
            "orphanPages": [{"title": node["title"], "path": node["id"]} for node in orphans],
            "groupPageCounts": dict(sorted(group_counts.items())),
            "largestPages": [
                {"title": node["title"], "path": node["id"], "words": node["words"]}
                for node in largest
            ],
            "mostReferencedPages": [
                {"title": node["title"], "path": node["id"], "incoming": node["incoming"]}
                for node in referenced
            ],
        },
        "nodes": sorted(nodes, key=lambda node: node["id"]),
        "links": sorted(hierarchy_links + references + architecture, key=lambda link: (link["type"], link["source"], link["target"])),
    }


def render(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=True, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when the committed graph is stale")
    args = parser.parse_args()
    content = render(build())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            print("Documentation graph is stale. Run: python scripts/build_guidance_graph.py", file=sys.stderr)
            return 1
        print(f"Documentation graph is current: {OUTPUT.relative_to(ROOT)}")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

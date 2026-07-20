#!/usr/bin/env python3
"""Validate the typed architecture registry and its documentation targets."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import json
import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = DOCS / "assets" / "data" / "architecture-registry.yaml"
SCHEMA = ROOT / "schemas" / "architecture-registry.schema.json"
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda item: list(item.path))
    messages = [f"schema: {'/'.join(map(str, error.path)) or '<root>'}: {error.message}" for error in errors]

    entities = data.get("entities", {})
    relationships = data.get("relationships", [])
    seen: set[tuple[str, str, str]] = set()
    by_source: dict[str, Counter] = defaultdict(Counter)

    for entity_id, entity in entities.items():
        page_ref = entity.get("page", "")
        page_path, _, anchor = page_ref.partition("#")
        path = DOCS / page_path
        if not path.is_file():
            messages.append(f"entity {entity_id}: page does not exist: {page_path}")
            continue
        if anchor:
            headings = {slug(match.group(1)) for match in HEADING.finditer(path.read_text(encoding="utf-8"))}
            if anchor not in headings:
                messages.append(f"entity {entity_id}: anchor does not exist: {page_ref}")

    for index, relationship in enumerate(relationships):
        source = relationship.get("source")
        relation_type = relationship.get("type")
        target = relationship.get("target")
        triple = (source, relation_type, target)
        if source not in entities:
            messages.append(f"relationship {index}: unknown source: {source}")
        if target not in entities:
            messages.append(f"relationship {index}: unknown target: {target}")
        if source == target:
            messages.append(f"relationship {index}: self-relationship is not allowed: {source}")
        if triple in seen:
            messages.append(f"relationship {index}: duplicate relationship: {triple}")
        seen.add(triple)
        by_source[source][relation_type] += 1

    required_core_pages = {
        "architecture/reference-architecture.md",
        "architecture/integration-design.md",
        "architecture/platform-governance-design.md",
        "architecture/data-contract-design.md",
        "architecture/data-domain-design.md",
        "architecture/data-product-design.md",
        "architecture/semantic-context-design.md",
        "architecture/unified-access-design.md",
        "architecture/platform-enablement-design.md",
        "architecture/developer-experience-design.md",
        "architecture/agentic-data-foundation.md",
    }
    registered_design_pages = {
        entity["page"].split("#", 1)[0]
        for entity in entities.values()
        if entity.get("type") == "design"
    }
    for page in sorted(required_core_pages - registered_design_pages):
        messages.append(f"core design is not registered: {page}")

    for entity_id, entity in entities.items():
        if entity.get("type") != "service":
            continue
        counts = by_source[entity_id]
        if counts["implements"] + counts["depends_on"] == 0:
            messages.append(f"service {entity_id}: requires an implements or depends_on relationship")
        if counts["constrained_by"] == 0:
            messages.append(f"service {entity_id}: requires a constrained_by relationship")
        if counts["participates_in"] == 0:
            messages.append(f"service {entity_id}: requires a participates_in relationship")

    if messages:
        print("Architecture registry validation failed:", file=sys.stderr)
        for message in messages:
            print(f"- {message}", file=sys.stderr)
        return 1

    type_counts = Counter(entity["type"] for entity in entities.values())
    relation_counts = Counter(item["type"] for item in relationships)
    print(
        "Validated architecture registry: "
        f"{len(entities)} entities {dict(sorted(type_counts.items()))}, "
        f"{len(relationships)} relationships {dict(sorted(relation_counts.items()))}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate publication metadata and canonical guidance structure."""

from __future__ import annotations

import re
from pathlib import Path

from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

SERVICES = [
    "data-service-portal.md",
    "data-service-ai-assistant.md",
    "data-ingestion-service.md",
    "data-product-creation-service.md",
    "data-consumption-service.md",
    "data-sharing-service.md",
    "platform-enablement-service.md",
    "data-observability-service.md",
    "data-foundation-operations-service.md",
]

SERVICE_SECTIONS = [
    "Purpose and Definition",
    "Scope and Boundaries",
    "Architecture Alignment",
    "Service Architecture",
    "Agentic Interaction",
    "Core Capabilities",
    "Contracts and Interfaces",
    "Integrations and Dependencies",
    "Controls and Evidence",
    "Action Checklist",
    "Reference Solutions",
    "Done Criteria",
]

REFERENCE_SOLUTIONS = [
    "data-ingestion-design.md",
    "data-product-creation-design.md",
    "data-consumption-design.md",
    "data-sharing-design.md",
    "observability-design.md",
]

ADR_SECTIONS = [
    "Status",
    "Context",
    "Decision",
    "Consequences",
    "Evidence",
    "Applicable Policy Decisions",
    "Review Date",
]

GLOSSARY_TERMS = {
    "Aggregate data product",
    "AI-ready data",
    "Consumer-aligned data product",
    "Data contract",
    "Data foundation",
    "Data product",
    "Data product go-live",
    "Data product port",
    "Data Service Portal",
    "Evidence",
    "Foundation service",
    "Reference solution",
    "Shared capability",
    "Source-aligned data product",
    "System telemetry",
}


def headings(path: Path, level: int) -> list[str]:
    found: list[str] = []
    in_fence = False
    marker = "#" * level + " "
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith(marker):
            found.append(line.removeprefix(marker).strip())
    return found


def require_order(path: Path, required: list[str], errors: list[str]) -> None:
    actual = headings(path, 2)
    positions: list[int] = []
    for section in required:
        if section not in actual:
            errors.append(f"{path.relative_to(ROOT)}: missing section '{section}'")
        else:
            positions.append(actual.index(section))
    if positions != sorted(positions):
        errors.append(f"{path.relative_to(ROOT)}: canonical sections are out of order")


def require_reference(target: Path, registries: list[Path], errors: list[str]) -> None:
    for registry in registries:
        if target.name not in registry.read_text(encoding="utf-8"):
            errors.append(
                f"{registry.relative_to(ROOT)}: does not reference {target.name}"
            )


def normalize_markdown(text: str) -> str:
    """Expose prose terms while ignoring link destinations and inline code paths."""
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]+", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def main() -> int:
    errors: list[str] = []
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        errors.append(f"VERSION is not valid Semantic Versioning: {version!r}")

    config = load_config(config_file_path=str(ROOT / "mkdocs.yml"))
    docs_version = str((config.get("extra") or {}).get("docs_version", ""))
    if docs_version != version:
        errors.append(f"mkdocs extra.docs_version {docs_version!r} does not match VERSION {version!r}")

    for name in ("README.md", "SUPPORT.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        if f"Version `{version}`" not in text:
            errors.append(f"{name}: does not declare Version `{version}`")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if not re.search(rf"^## {re.escape(version)} - \d{{4}}-\d{{2}}-\d{{2}}$", changelog, re.MULTILINE):
        errors.append(f"CHANGELOG.md: missing dated release heading for {version}")

    license_path = ROOT / "LICENSE"
    if not license_path.exists():
        errors.append("LICENSE: missing distribution license")
    elif "Apache License" not in license_path.read_text(encoding="utf-8") or "Version 2.0" not in license_path.read_text(encoding="utf-8"):
        errors.append("LICENSE: expected the approved Apache License 2.0 text")

    for page in sorted(DOCS.rglob("*.md")):
        page_h1 = headings(page, 1)
        if len(page_h1) != 1:
            errors.append(f"{page.relative_to(ROOT)}: expected one H1, found {len(page_h1)}")

    for name in SERVICES:
        path = DOCS / "services" / name
        if not path.exists():
            errors.append(f"Missing canonical service page: {path.relative_to(ROOT)}")
            continue
        require_order(path, SERVICE_SECTIONS, errors)
        require_reference(
            path,
            [
                DOCS / "architecture" / "target-architecture.md",
                DOCS / "architecture" / "design-map.md",
                DOCS / "standards" / "index.md",
                DOCS / "foundation" / "architecture-to-delivery.md",
            ],
            errors,
        )

    standards = sorted((DOCS / "standards").glob("*-standard.md"))
    for path in standards:
        text = path.read_text(encoding="utf-8")
        if 'class="decision-brief"' not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing decision brief")
        if "Minimum Done Criteria" not in headings(path, 2):
            errors.append(f"{path.relative_to(ROOT)}: missing Minimum Done Criteria")
        require_reference(path, [DOCS / "standards" / "index.md"], errors)

    for path in sorted((DOCS / "playbooks").glob("*.md")):
        if path.name != "index.md" and "Done Criteria" not in headings(path, 2):
            errors.append(f"{path.relative_to(ROOT)}: missing Done Criteria")
        if path.name != "index.md":
            require_reference(path, [DOCS / "playbooks" / "index.md"], errors)

    for name in REFERENCE_SOLUTIONS:
        path = DOCS / "reference-solutions" / name
        require_order(path, ["Executive Recommendation", "Done Criteria"], errors)

    for path in sorted((DOCS / "decisions").glob("adr-*.md")):
        require_order(path, ADR_SECTIONS, errors)
        if not re.search(r"^Accepted -?[^\n]*\d{4}-\d{2}-\d{2}$", path.read_text(encoding="utf-8"), re.MULTILINE):
            errors.append(f"{path.relative_to(ROOT)}: status is not a dated Accepted decision")
        require_reference(path, [DOCS / "implementation" / "architecture-decisions.md"], errors)

    decision_register = DOCS / "implementation" / "architecture-decisions.md"
    decision_reference = re.compile(
        r"\badr(?:s|-?\d+)?\b|architecture decision records?|"
        r"implementation/architecture-decisions|decisions/adr-",
        re.IGNORECASE,
    )
    for path in sorted(DOCS.rglob("*.md")):
        if path == decision_register or path.parent == DOCS / "decisions":
            continue
        if decision_reference.search(path.read_text(encoding="utf-8")):
            errors.append(
                f"{path.relative_to(ROOT)}: published guidance must not depend on decision records"
            )

    reference_index = DOCS / "reference-solutions" / "index.md"
    for path in sorted((DOCS / "reference-solutions").glob("*.md")):
        if path != reference_index:
            require_reference(path, [reference_index], errors)

    glossary = (DOCS / "foundation" / "glossary.md").read_text(encoding="utf-8")
    present_terms = set(re.findall(r"^\| ([^|]+?) \|", glossary, re.MULTILINE))
    missing_terms = sorted(GLOSSARY_TERMS - present_terms)
    if missing_terms:
        errors.append("Glossary is missing canonical terms: " + ", ".join(missing_terms))

    stale_terms = (
        "foundation capability groups",
        "platform foundations",
        "platform foundation design",
        "platform foundation and integration",
    )
    for content_root in (DOCS, ROOT / "skills"):
        for path in content_root.rglob("*.md"):
            searchable = normalize_markdown(path.read_text(encoding="utf-8"))
            for stale in stale_terms:
                if stale in searchable:
                    errors.append(
                        f"{path.relative_to(ROOT)}: outdated architecture term remains: {stale}"
                    )

    if errors:
        print("Release-readiness validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Release {version} metadata and canonical structure validated: "
        f"{len(SERVICES)} services, {len(standards)} standards, "
        f"{len(REFERENCE_SOLUTIONS)} reference solutions, and "
        f"{len(list((DOCS / 'decisions').glob('adr-*.md')))} ADRs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

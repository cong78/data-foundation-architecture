# ADR-002: Unity Catalog as Technical Catalog Standard

## Status

Accepted — 2026-07-15

## Context

The foundation needs one technical inventory and authorization surface for Databricks-managed data and AI assets. Multiple independently editable catalogs would fragment identifiers, grants, audit, lineage, discovery, and lifecycle reconciliation.

The technical catalog must not become the only authority for product meaning, contracts, semantic context, policy, or telemetry. Those artifacts need portable canonical representations and may span platforms beyond Databricks.

## Decision

Use Unity Catalog as the standard technical catalog and native data-authorization surface for foundation-managed data and AI assets.

Register or project tables, views, volumes, functions, models, features, and governed external assets into Unity Catalog using stable foundation identifiers. Keep product descriptors inside their publishing contracts and keep contract, semantic, policy, and telemetry authorities portable. Project only the identifiers and selected state needed for discovery, authorization, lineage, and reconciliation.

## Consequences

- Technical inventory, namespace, native grants, audit, and platform lineage have one standard control surface.
- The Data Service Portal can build read projections without becoming another authoritative catalog.
- Product and contract meaning remains exportable and independently testable.
- Cross-platform assets require governed external registration or synchronized projections.
- Catalog synchronization, drift reconciliation, ownership, and failure handling become explicit Platform Enablement responsibilities.
- A Unity Catalog outage or incompatible platform change requires tested continuity and export paths.

## Evidence

- [Semantic and Context Design](../architecture/semantic-context-design.md)
- [Unified Access Design](../architecture/unified-access-design.md)
- [Data Catalog and Storage Standard](../standards/catalog-storage-standard.md)
- [Platform Enablement Service](../services/platform-enablement-service.md)

## Applicable Policy Decisions

- The [Data Catalog and Storage Standard](../standards/catalog-storage-standard.md) governs technical registration and storage bindings.
- The [Data Contract Standard](../standards/data-contract-standard.md) preserves portable product and contract authority.
- A non-Unity technical catalog requires an approved exception with canonical export, identifier preservation, authorization equivalence, and migration evidence.

## Review Date

2027-07-15, or earlier if the platform estate, catalog interoperability, authorization model, or regulatory requirements materially changes.

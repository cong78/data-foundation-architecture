# ADR-001: Central and Federated Product Ownership

## Status

Accepted — 2026-07-15

## Context

Source onboarding and ingestion require reusable connectors, security controls, source reconciliation, quarantine, replay, retention, and operational support. Allowing every domain to recreate these capabilities would duplicate source extraction, weaken source accountability, and produce inconsistent source-aligned data.

Aggregate and consumer-aligned products require business context, semantic ownership, consumer feedback, and domain prioritization. Central ownership of these products would create a delivery bottleneck and separate product decisions from the teams accountable for their meaning and value.

## Decision

The Data Foundation Platform Team centrally manages source onboarding, ingestion, raw landing state, validation, and source-aligned products.

Federated domain data teams own aggregate and consumer-aligned products. They use shared product-creation, contract, catalog, storage, access, observability, and operational capabilities supplied by the foundation.

Ownership transfers only through a published product port and contract. Domain teams do not depend directly on ingestion pipelines or raw storage, and the foundation team does not own domain product semantics or consumer outcomes.

## Consequences

- Source extraction, reconciliation, replay, retention, and source incidents have one accountable operating path.
- Domains receive stable source-aligned product promises instead of rebuilding source integrations.
- Domain teams retain accountability for aggregate and consumer-aligned meaning, quality, lifecycle, and value.
- The handoff requires explicit publishing contracts, product ports, service levels, lineage, support, and escalation.
- The central ingestion service must scale as a shared service and avoid becoming a manual onboarding queue.
- Exceptions for domain-managed ingestion require an explicit risk, operating, interoperability, and migration decision.

## Evidence

- [Definition and Scope](../foundation/definition-and-scope.md)
- [Data Foundation Model](../architecture/data-foundation-model.md)
- [Data Ingestion Service](../services/data-ingestion-service.md)
- [Data Product Creation Service](../services/data-product-creation-service.md)

## Applicable Policy Decisions

- The [Data Contract Standard](../standards/data-contract-standard.md) governs the ownership handoff.
- The [Data Product Management Standard](../standards/data-product-management-standard.md) governs product ownership and lifecycle.
- No ADR-specific executable policy is active; implementation evidence remains scoped to each adopter.

## Review Date

2027-07-15, or earlier if source ownership, domain funding, service boundaries, or platform topology materially changes.

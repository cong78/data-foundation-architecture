# ADR-003: Delta as Default Durable Tabular Storage

## Status

Accepted — 2026-07-15

## Context

Durable tabular products need consistent transaction behavior, schema evolution, time travel, recovery, change data handling, optimization, access integration, and operational evidence. Supporting many physical table formats as equal defaults would increase platform complexity and weaken repeatable recovery and support.

Not every product is a durable table. Event streams, APIs, operational lookups, files, retrieval indexes, non-tabular assets, federated queries, and legitimate interoperability cases may require another physical form.

## Decision

Use Unity Catalog managed Delta tables as the default physical storage for new durable tabular source-aligned, aggregate, and consumer-aligned products.

Expose products through governed logical ports rather than physical Delta paths. Permit another storage format or access pattern only when the product requirement cannot be met appropriately by the default and an approved exception defines ownership, controls, recovery, observability, portability, and exit behavior.

## Consequences

- Product teams receive a consistent table lifecycle, transaction, recovery, optimization, and support model.
- Unity Catalog authorization, lineage, and audit integrate directly with the default storage binding.
- Workload templates and runbooks can automate common deployment and rollback behavior.
- Delta-specific optimization remains an implementation concern rather than part of the consumer contract.
- Alternative formats remain possible but carry explicit conformance, operational, and migration obligations.
- Consumers must not infer product semantics or compatibility from a Delta schema alone.

## Evidence

- [Data Foundation Model](../architecture/data-foundation-model.md)
- [Unified Access Design](../architecture/unified-access-design.md)
- [Data Catalog and Storage Standard](../standards/catalog-storage-standard.md)
- [Data Product Workload Standard](../standards/data-product-workload-standard.md)

## Applicable Policy Decisions

- The [Data Catalog and Storage Standard](../standards/catalog-storage-standard.md) governs physical storage defaults and exceptions.
- The [Data Product Workload Standard](../standards/data-product-workload-standard.md) governs deployment and recovery behavior.
- An alternative requires a versioned exception and evidence that product contracts, access decisions, telemetry, recovery, and export remain equivalent.

## Review Date

2027-07-15, or earlier if open table-format interoperability, platform support, recovery objectives, or cost materially changes.

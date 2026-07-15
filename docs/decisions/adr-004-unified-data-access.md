# ADR-004: Unified Data Access Above Physical Storage

## Status

Accepted — 2026-07-15

## Context

Consumers include named users, applications, platforms, external recipients, agents, and models. They need SQL, API, event, file, feature, retrieval, and sharing interfaces across distributed physical stores.

Direct physical-storage access exposes implementation details, bypasses product contracts, mixes service authorization with data entitlement, and makes purpose, obligations, usage, change, and revocation difficult to govern consistently.

## Decision

Place a unified data access layer above physical product storage. Consumers bind to versioned product ports under a Data Product Consumption Contract.

Every access request resolves actor and subject identity, purpose, product and contract version, selected port, service authorization, data authorization, obligations, runtime adapter, and evidence correlation. Unity Catalog provides native authorization for Databricks assets; other adapters must preserve equivalent decision and evidence semantics.

The unified layer is a logical control and product-interface model, not one mandatory query engine or data-copying tier.

## Consequences

- Consumers depend on stable product promises rather than tables, paths, pipelines, or vendor-specific implementation details.
- Service permission and data entitlement remain separate and independently auditable.
- Named-user, workload, delegated, and recipient identities follow one decision model.
- Policy obligations such as masking, row filtering, minimization, expiry, and revocation can be applied consistently.
- Runtime adapters must expose compatible health, audit, and failure behavior.
- Latency-sensitive or source-system interactions may still use direct APIs or MCP interfaces when replication is unjustified, but they remain outside data-product consumption unless explicitly contracted.

## Evidence

- [Unified Access Design](../architecture/unified-access-design.md)
- [Access Control Standard](../standards/access-control-standard.md)
- [Data Consumption Service](../services/data-consumption-service.md)
- [Data Contract Standard](../standards/data-contract-standard.md)

## Applicable Policy Decisions

- The [Access Control Standard](../standards/access-control-standard.md) governs service and data authorization.
- The [Data Contract Standard](../standards/data-contract-standard.md) governs product and consumer boundaries.
- AI and external-sharing uses apply the corresponding standards and consumption-contract profiles.

## Review Date

2027-07-15, or earlier if identity architecture, access platforms, source-connect guidance, or consumption interfaces materially changes.

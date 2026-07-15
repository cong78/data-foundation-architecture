# Data Catalog and Storage Standard

<div class="decision-brief"><div><small>Use when</small><strong>Registering an asset or selecting physical product storage.</strong></div><div><small>Decision</small><strong>How will the asset be cataloged, governed, stored, and accessed?</strong></div><div><small>Owner</small><strong>Data platform owner with architecture and governance owners.</strong></div><div><small>Output</small><strong>Unity Catalog registration, Delta binding, controls, evidence, or approved exception.</strong></div></div>

This standard establishes **Unity Catalog as the data catalog standard** and **Delta Lake as the default physical table storage format** for the data foundation.

The defaults create one governed technical inventory and one reliable tabular storage profile. They do not require every source to be copied, make every catalog object a data product, or replace portable product, contract, semantic, policy, and telemetry authorities.

## Standard Decision

| Concern | Required Default | Boundary |
| --- | --- | --- |
| Data catalog | Register every foundation-managed data and AI asset in Unity Catalog directly, through a governed external or foreign binding, or through a synchronized metadata projection. | Unity Catalog is authoritative for technical object identity, namespace, native privileges, governed tags, platform lineage, and audit evidence. |
| Tabular storage | Use Delta Lake for new durable source-aligned and data-product tables. Prefer Unity Catalog managed Delta tables unless external lifecycle ownership is required. | Delta is the physical table binding, not the consumer contract or product identity. |
| Product access | Resolve stable logical product ports to Unity Catalog objects and approved adapters. | Consumers use product ports, SQL, APIs, events, sharing, semantic, feature, or retrieval interfaces rather than storage paths. |
| Portable control state | Keep canonical data contracts with embedded product descriptors, semantic context, policy intent, workload intent, and telemetry conventions in open machine-readable artifacts. | Unity Catalog projects and enforces selected state but is not the only recoverable copy of foundation meaning or approval. |

Unity Catalog provides a three-level namespace and governance for securable data and AI objects, including tables, views, volumes, functions, models, services, connections, external locations, and shares. Delta Lake combines Parquet data files with an open transaction log and is the Databricks default for table operations. [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) · [Delta Lake](https://docs.databricks.com/aws/en/delta) · [Delta Lake OSS](https://docs.delta.io/)

## Authority Boundaries

| Authority | System of Record |
| --- | --- |
| Technical asset name, object type, location binding, native owner, privilege, governed tag, platform lineage and audit | Unity Catalog. |
| Product identity, purpose, owner, lifecycle, logical ports and go-live state | Product registry governed by the Data Product Management Standard. |
| Schema, semantics, quality, SLO, compatibility, usage and sharing terms | Data contract registry. |
| Business terms, metric meaning, relationships and usage context | Semantic context package and linked glossary or knowledge authorities. |
| Enterprise policy intent, purpose decision and entitlement | Policy and entitlement authorities, projected into Unity Catalog controls where supported. |
| Cross-platform system and product telemetry | Data Observability Service using OpenTelemetry conventions. |

Unity Catalog may present synchronized projections of these authorities. A projection must retain the canonical identifier, version, source authority, synchronization time, and reconciliation status.

## Unity Catalog Profile

1. Use a regional metastore boundary and attach only approved workspaces.
2. Use catalogs as deliberate isolation and ownership boundaries; use schemas for products or bounded product families.
3. Provision users, groups, and service principals at account level and grant privileges to groups or dedicated workload identities.
4. Apply workspace bindings, least-privilege grants, governed tags and ABAC, row filters, column masks, and storage controls according to the access policy.
5. Register source connections, tables, views, volumes, functions, models, shares, and approved external or federated assets with stable foundation identifiers.
6. Prohibit consumer and product-pipeline access by unmanaged cloud-storage path when a governed Unity Catalog object is available.
7. Export catalog metadata, grants, tags, lineage, audit, and physical bindings on the defined retention schedule and reconcile them with canonical foundation records.

## Delta Storage Profile

Use Unity Catalog managed Delta tables by default because the catalog controls both metadata and storage lifecycle. Use external Delta tables only when an approved ownership, migration, shared-storage, or multi-engine requirement needs an externally managed location.

Every production Delta binding must define:

- Stable product, port, contract, release, owner, classification, and Unity Catalog object identifiers.
- Schema enforcement and controlled schema evolution.
- Write pattern, concurrency, idempotency, merge or append behavior, and recovery procedure.
- Retention, time-travel, deletion, vacuum, legal hold, backup, RPO, and RTO behavior.
- File layout, optimization, statistics, partitioning or clustering, and cost controls appropriate to the workload.
- Reader and writer compatibility, enabled table features, independent-client evidence where required, and an exit path.
- Encryption, storage isolation, credential ownership, regional placement, audit, lineage, quality, freshness, and usage telemetry.

Physical table names and locations remain implementation bindings. Consumers must not depend on object-storage paths or an internal table name that is not declared as a stable product port.

## Allowed Exceptions

| Exception | Use when | Required evidence |
| --- | --- | --- |
| Direct source API or MCP | The need is a current-state lookup, source-owned command, transaction, or bounded tool action. | Registered logical port, interface contract, identity, purpose, rate, SLO, dependency, audit, and lifecycle evidence. |
| Federated or foreign data | Data must remain at source and query federation meets policy, latency, availability, source-capacity, and telemetry requirements. | Unity Catalog registration or projection, pushdown proof, source-owner acceptance, failure behavior, and exit decision. |
| Event platform | The product interface is an event stream rather than a durable table. | AsyncAPI, CloudEvents, schema, ordering, replay, retention, lineage, and consumer evidence. |
| Non-tabular asset | Files, documents, media, models, indexes, graph structures, or other assets require a different physical representation. | Unity Catalog object or linked inventory record, contract, format profile, controls, retention, and governed access adapter. |
| Operational or serving store | Millisecond latency, transactions, search, vector retrieval, graph traversal, or serving behavior cannot be met by Delta. | Product-port contract, synchronization and reconciliation, source lineage, freshness, recovery, expiry, and ownership. |
| Apache Iceberg table | A proven external ecosystem or engine requirement needs Iceberg and cannot be met through a Delta-compatible interface or adapter. | Technology assessment, independent-client test, policy parity, performance and cost proof, migration plan, and time-bound exception review. |

An exception changes the physical binding, not the requirement for Unity Catalog registration, logical product identity, contracts, policy, observability, and lifecycle management. If Unity Catalog cannot govern the asset directly, maintain a synchronized catalog projection with a tested link to the authoritative external object.

## Enforcement

| Gate | Required check |
| --- | --- |
| Source onboarding | Decide direct, federated, projected, or replicated access before storage is provisioned. |
| Product design | Declare Unity Catalog representation, Delta binding or exception, stable ports, data location, ownership, and access pattern. |
| CI/CD | Validate catalog naming, tags, privileges, storage type, contract schema, table properties, retention, and policy intent. |
| Product go-live | Prove object registration, contract match, allow and deny behavior, lineage, quality, freshness, recovery, portability, and telemetry. |
| Runtime | Detect unmanaged paths, unregistered assets, privilege drift, metadata drift, incompatible table features, stale projections, and retention violations. |
| Reassessment | Review exceptions, external tables, federation, direct source dependencies, storage cost, client compatibility, and exit evidence at least annually or after material change. |

## Minimum Done Criteria

- Every live foundation asset resolves to a Unity Catalog object or governed synchronized projection.
- Every new durable tabular product uses Delta Lake or has an approved, expiring exception.
- Unity Catalog native identity, privilege, classification, workspace, row, and column controls pass applicable allow and deny tests.
- Product and contract identifiers reconcile with Unity Catalog objects and Delta table bindings.
- No consumer requires unmanaged storage credentials or undeclared physical paths.
- Catalog, data, metadata, lineage, policy evidence, and configuration can be exported for recovery and migration.
- At least one representative Delta product passes an independent read or migration test for its declared interoperability profile.
- Exceptions name an owner, rationale, compensating controls, review date, migration trigger, and exit path.

# Data Ingestion Service

<div class="decision-brief"><div><small>Use when</small><strong>Onboarding or operating a source channel.</strong></div><div><small>Decision</small><strong>Which governed ingestion pattern and contract apply?</strong></div><div><small>Owner</small><strong>Foundation ingestion owner.</strong></div><div><small>Output</small><strong>Validated source-aligned product and handoff.</strong></div></div>

## Definition

The data ingestion service brings data from source systems into the foundation through standardized, governed patterns. It makes onboarding repeatable while preserving provenance, enforcing baseline controls, and preparing data for product creation.

For a selected implementation profile, see [Data Ingestion Design](../architecture/data-ingestion-design.md), which maps this service to Lakeflow Connect, Auto Loader, Databricks streaming runtimes, and Unity Catalog while preserving the Source System Ingestion Contract and source-aligned boundary.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| File inbox push, connector-based pull, API extraction, CDC, and event-based streaming. | Business transformation into live data products. |
| Source onboarding, schema registration, landing, validation, quarantine, and ingestion telemetry. | Source system ownership or upstream business process quality. |
| Source-aligned storage with raw and validated states, metadata, lineage, classification, and retention controls. | Consumer-facing semantic models or product go-live approval. |

## Central Ownership Model

The Data Foundation Platform Team is accountable for this service and for the complete source-aligned lifecycle. It centrally manages source onboarding, connector and pipeline operation, raw and validated states, quarantine, replay, source-aligned contracts, access, retention, lineage, telemetry, incidents, and retirement.

The source system team remains accountable for source availability, source meaning, delivery obligations, and change communication. Domain data teams may define downstream acceptance needs and stewardship input, but they consume the validated source-aligned contract rather than creating separate extraction pipelines or owning source-aligned storage.

Regional runtimes or delegated operators are implementation choices. They must use the central service contract, controls, identities, evidence model, and operating ownership.

## Supported Patterns

| Pattern | Use When | Required Controls |
| --- | --- | --- |
| File inbox push | Source teams can produce files on a schedule or event trigger. | File contract, checksum, schema validation, retention, quarantine. |
| Connector-based pull | The foundation connects to APIs, databases, SaaS platforms, or enterprise applications. | Credential management, incremental extraction, throttling, schema drift detection. |
| Event-based streaming ingestion | Business events or operational changes must be captured near real time. | Schema registry, replay strategy, ordering expectations, dead-letter handling. |

Use OpenAPI for source APIs and AsyncAPI plus CloudEvents for event sources. Connector-specific configuration stays in an adapter; source identity, contract, schema, checkpoint, and lineage metadata remain canonical.

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Onboarding | Source registration and pattern selection | Source owner, identity, classification, contract, delivery pattern, SLO, recovery need, and support route are approved before activation. |
| Contracts | Source System Ingestion Contract and schema management | Canonical schema, semantics, delivery expectations, compatibility rules, and change ownership are versioned and testable. |
| Connectivity | Managed source adapters | File inbox, connector pull, API, CDC, and event-stream adapters authenticate securely and preserve source identity. |
| Transport | Reliable incremental movement | Checkpoints, idempotency, ordering, deduplication, backpressure, retries, and replay meet the Source System Ingestion Contract. |
| Landing | Source-aligned raw state | Faithful, timestamped, provenance-rich source data is retained under restricted access for replay and audit. |
| Validation | Validated source-aligned state | Contract-conformant records are separated from invalid or suspect records before downstream handoff. |
| Exceptions | Quarantine and remediation | Rejected records have reason, owner, evidence, correction path, and controlled replay. |
| Security | Credentials and source protection | Secrets, network paths, workload identity, encryption, classification, and least privilege are centrally enforced. |
| Evidence | Lineage and telemetry | Source, adapter, run, schema, record outcome, landing state, and incident context are correlated through lineage and OpenTelemetry. |
| Lifecycle | Change, recovery, and portability | Schema change, connector replacement, backfill, recovery, retention, and retirement preserve the canonical source identity and contract. |

## Architecture Guidance

The ingestion service should separate **transport**, **validation**, and **storage** concerns. This allows a source to change its delivery mechanism without forcing downstream data products to be redesigned.

The raw state of source-aligned data should retain enough context for traceability, replay, audit, and forensic analysis. Standard metadata should include source system, ingestion timestamp, batch or event identifier, schema version, data classification, and processing status.

Replication is not the default outcome of source onboarding. Apply the [Direct, Federated, or Replicated Access Decision](data-consumption-service.md#direct-federated-or-replicated-access-decision) first. Use direct source APIs or MCP tools for bounded current-state operations, federated access where data can remain authoritative at source, selective projections for narrow decoupled needs, and ingestion when history, transformation, scale, reuse, isolation, or reproducibility justifies a source-aligned copy.

## Controls

- Source System Ingestion Contract exists and is approved.
- Data classification is known or assigned during onboarding.
- Schema validation is active.
- Invalid records are routed to a managed exception path.
- Access to raw data is restricted to approved roles.
- Ingestion telemetry is emitted using the foundation OpenTelemetry conventions.

## Done Criteria

- Source is registered in the catalog.
- Ingestion pattern and owner are documented.
- The foundation platform owner and source-system owner are explicit; no domain team is the default ingestion or source-aligned owner.
- Landing, validation, quarantine, and retention behavior are tested.
- Lineage from source to landing is available.
- Operational dashboard and alerting are active.
- Downstream data product teams can use the landed data without custom source extraction.
- The source can move to another supported connector or runtime without changing its canonical contract or source identifier.

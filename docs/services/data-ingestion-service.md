# Data Ingestion Service

## Definition

The data ingestion service brings data from source systems into the foundation through standardized, governed patterns. It makes onboarding repeatable while preserving provenance, enforcing baseline controls, and preparing data for product creation.

For a selected implementation profile, see [Data Ingestion Design](../architecture/data-ingestion-design.md), which maps this service to Lakeflow Connect, Auto Loader, Databricks streaming runtimes, and Unity Catalog while preserving the source contract and source-aligned boundary.

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

- Source onboarding workflow.
- Data contract and schema registration.
- Secure credential and secret handling.
- Source-aligned raw landing with source metadata and timestamps.
- Automated validation and quarantine.
- Change data capture and incremental load support.
- Event stream subscription and replay.
- Operational monitoring, alerting, and incident hooks.
- Lineage capture from source to the source-aligned landing state.
- OpenTelemetry-compatible traces, metrics, logs, and events.

## Architecture Guidance

The ingestion service should separate **transport**, **validation**, and **storage** concerns. This allows a source to change its delivery mechanism without forcing downstream data products to be redesigned.

The raw state of source-aligned data should retain enough context for traceability, replay, audit, and forensic analysis. Standard metadata should include source system, ingestion timestamp, batch or event identifier, schema version, data classification, and processing status.

## Controls

- Source contract exists and is approved.
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

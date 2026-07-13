# Reference Architecture

The reference architecture shows the minimum building blocks needed to implement the target architecture. Technology can vary; these capabilities should not.

## Architecture View

Read each lane from left to right. **Build** and **Access** carry the runtime data flow; **Engage** and **Govern** control every journey without becoming duplicate systems of record.

These lanes organize the delivery journey; they are not additional target architecture planes. Use the [Target Architecture](target-architecture.md) for cross-cutting plane responsibilities and this view for capability interaction.

<div class="standards-map reference-map" role="img" aria-label="Reference architecture organized into engage, govern, build, and access lanes">
  <div class="standards-map-head" aria-hidden="true">
    <span>Inputs</span><i></i><span>Foundation capabilities</span><i></i><span>Outcomes</span>
  </div>

  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Engage</small><strong>People · Teams · Systems</strong><p>Named users, workloads, product teams, consumers, and platform operators.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="/services/data-service-portal/"><strong>Data Service Portal</strong></a><a href="/architecture/data-product-developer-experience/"><strong>Developer Workspace</strong></a><a href="/services/data-service-ai-assistant/"><strong>Data Service AI Assistant</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Intent and task context</strong><p>Discovery, requests, workspaces, approvals, status, evidence, and action receipts.</p></div>
  </section>

  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Govern</small><strong>Identity · Purpose · Product</strong><p>Authenticated actor and subject, product identity, use case, classification, and environment.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Catalog · Contract · Semantics</strong><strong>Policy · Workflow · Entitlement</strong><strong>Lineage · Quality · Go-Live</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Decisions and controls</strong><p>Versioned metadata, policy decisions, obligations, lifecycle state, and audit evidence.</p></div>
  </section>

  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Build</small><strong>Files · Databases · APIs · Events</strong><p>Enterprise sources and approved external inputs.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="/services/data-ingestion-service/"><strong>Data Ingestion</strong></a><a href="/services/data-product-creation-service/"><strong>Product Creation</strong></a><strong>Physical Product Storage</strong><a href="/services/data-observability-service/"><strong>Data Observability</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Live data products</strong><p>Source-aligned, aggregate, and consumer-aligned outputs with contracts, context, SLOs, and lineage.</p></div>
  </section>

  <section class="standards-map-lane lane-access">
    <div class="standards-map-cell"><small>Access</small><strong>Product · Port · Consumer Purpose</strong><p>Stable product interfaces above distributed physical storage.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="/architecture/unified-access-design/"><strong>Unified Access Design</strong></a><a href="/services/data-sharing-service/"><strong>Data Sharing</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Governed outcomes</strong><p>BI, applications, platforms, APIs, events, partners, agents, models, features, and retrieval.</p></div>
  </section>
</div>

## Capability Map

| Domain | Capabilities |
| --- | --- |
| Portal | Intent-led journeys, product discovery, product detail, agreements, portfolio, contracts, product health. |
| Ingestion | Files, APIs, connectors, CDC, streams, validation. |
| Storage and processing | Source-aligned raw and validated states, product storage, archive, batch, and streaming. |
| Products | Registry, contracts, semantics, ownership, lifecycle, go-live approval. |
| Consumption | Unified product and port resolution, SQL, semantic layer, APIs, events, files, features, retrieval, context, federation, and runtime adapters. |
| Sharing | Internal exchange, external packages, APIs, clean rooms, revocation. |
| Observability | OpenTelemetry, SLOs, health, incidents, usage, lineage correlation. |
| Agentic AI | Data Service AI Assistant, agent gateway, agent and skill registry, LLM gateway, context, memory, approval, evaluation. |
| Governance and security | Named-user and workload identity, policy administration and decision, service and data enforcement, entitlement, classification, masking, audit. |

## Interoperability Boundaries

| Boundary | Portable Contract |
| --- | --- |
| Portal to control plane | Stable APIs; portal stores workflow state, not duplicate product truth. |
| Product to catalog | ODPS-compatible descriptor and DCAT-compatible catalog exchange. |
| Producer to consumer | Stable logical product port with ODCS contract plus OpenAPI, AsyncAPI, table, query, file, feature, retrieval, semantic, or context interface definition. |
| Runtime to lineage | OpenLineage-compatible run, job, and dataset events. |
| Runtime to observability | OpenTelemetry semantic conventions and OTLP export. |
| Provider to external recipient | Open sharing protocol or documented, tested export adapter with revocation. |

See the [Open Interoperability Standard](../standards/open-interoperability-standard.md) for profiles and conformance tests.

The [Data Service Portal Design](data-service-portal-model.md) defines how portal journeys compose these boundaries without becoming an additional system of record.

## Reference Flow

```mermaid
sequenceDiagram
    participant Source as Source System
    participant Portal as Data Service Portal
    participant Ingest as Ingestion Service
    participant Store as Foundation Storage
    participant Product as Data Product Service
    participant Catalog as Catalog and Product Registry
    participant Contract as Contract Registry
    participant Policy as Policy and Entitlement
    participant Consume as Consumption Service
    participant Observe as Observability Service
    participant User as Consumer

    User->>Portal: Discover product, request access, or manage contract
    Portal->>Catalog: Read product metadata and lifecycle state
    Portal->>Contract: Read product contract and compatibility status
    Observe-->>Portal: Return current health and observation time
    Source->>Ingest: Push file, expose connector, or publish event
    Ingest->>Catalog: Register source, schema, classification
    Ingest->>Store: Land source-aligned raw state with provenance
    Product->>Store: Transform and validate trusted dataset
    Product->>Catalog: Publish product descriptor and ports
    Product->>Contract: Publish approved contract version
    Portal->>Policy: Submit purpose-bound access request
    Policy->>Consume: Return entitlement, decision, and obligations
    Consume->>User: Provide dataset, API, semantic, or AI-ready access
    Ingest->>Observe: Emit OpenTelemetry traces, metrics, logs, and events
    Product->>Observe: Emit quality, freshness, lineage, and product health signals
    Consume->>Observe: Emit usage, latency, access, and consumer experience signals
```

## Cross-Cutting Services

- Identity and access management
- Workload identity, delegated identity, policy decision, service and data enforcement, entitlement lifecycle, and revocation
- Secrets and key management
- Metadata and catalog
- Data quality and observability
- OpenTelemetry collection and telemetry correlation
- Policy enforcement and audit
- Schema registry and contract testing
- Lineage and impact analysis
- Platform monitoring and cost controls
- Agent and skill registry, model gateway, evaluation service, scoped memory, and human approval

## Readability Notes

- Use the diagram to explain component interaction.
- Use the capability map to check scope coverage.
- Use the reference flow to validate an end-to-end design.
- Use standards pages for mandatory contract, product, AI, and telemetry rules.
- Use conformance tests to prove that architecture boundaries are portable in practice.

<div class="read-next">
  <strong>Next:</strong> use the Architecture Blueprint to turn this into delivery work.
</div>

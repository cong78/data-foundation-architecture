# Reference Architecture

The reference architecture shows the minimum building blocks needed to implement the target architecture. Technology can vary; these capabilities should not.

## Architecture View

```mermaid
flowchart TB
    subgraph Source["Source Layer"]
        S1[Enterprise Applications]
        S2[Files and Documents]
        S3[APIs and Databases]
        S4[Events and Streams]
    end

    subgraph Foundation["Data Foundation Services"]
        PORTAL[Data Service Portal]
        I[Data Ingestion]
        P[Data Product Creation]
        C[Data Consumption]
        X[Data Sharing]
        O[Data Observability]
    end

    subgraph Control["Governance and Control Plane"]
        G1[Catalog and Metadata]
        G2[Policy and Access]
        G3[Lineage and Quality]
        G4[Security and Audit]
    end

    subgraph Consumer["Consumer Layer"]
        B[BI and Analytics]
        A[Applications and Platforms]
        M[AI Agents and Models]
        E[Customers, Suppliers, Partners]
    end

    Source --> I --> P
    PORTAL --> I
    PORTAL --> P
    PORTAL --> C
    PORTAL --> X
    PORTAL --> O
    P --> C --> B
    C --> A
    C --> M
    P --> X --> E
    I -. telemetry .-> O
    P -. telemetry .-> O
    C -. telemetry .-> O
    X -. telemetry .-> O
    Control -. policies and metadata .-> Foundation
```

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

The [Data Service Portal model](data-service-portal-model.md) defines how portal journeys compose these boundaries without becoming an additional system of record.

## Reference Flow

```mermaid
sequenceDiagram
    participant Source as Source System
    participant Portal as Data Service Portal
    participant Ingest as Ingestion Service
    participant Store as Foundation Storage
    participant Product as Data Product Service
    participant Catalog as Catalog and Policy
    participant Consume as Consumption Service
    participant Observe as Observability Service
    participant User as Consumer

    User->>Portal: Discover product, request access, or manage contract
    Portal->>Catalog: Read product metadata, policy, contract, and health status
    Source->>Ingest: Push file, expose connector, or publish event
    Ingest->>Catalog: Register source, schema, classification
    Ingest->>Store: Land source-aligned raw state with provenance
    Product->>Store: Transform and validate trusted dataset
    Product->>Catalog: Publish product metadata and contract
    Portal->>Catalog: Submit access, onboarding, or contract workflow
    Catalog->>Consume: Enforce access and usage policies
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

# Architecture Overview

<div class="decision-brief"><div><small>Use when</small><strong>Explaining or reviewing the foundation as a whole.</strong></div><div><small>Decision</small><strong>Which responsibility, boundary, or relationship must the architecture make clear?</strong></div><div><small>Owner</small><strong>Architecture owner with service and product owners.</strong></div><div><small>Output</small><strong>Agreed architecture intent, responsibility placement, and decision path.</strong></div></div>

## Purpose

The data foundation turns distributed source data into governed data products that people, applications, platforms, partners, AI agents, and models can use with confidence.

The architecture exists to make five things explicit:

1. Where data enters and where trust is created.
2. Which capabilities are shared and which outcomes remain domain-owned.
3. Which contracts, policies, and lifecycle decisions govern each boundary.
4. How products are discovered, accessed, shared, observed, changed, and retired.
5. How every important decision can be traced to evidence and an accountable owner.

## Core Logic

<div class="architecture-core-map" role="group" aria-label="Core architecture logic from source authority through foundation services and governed data products to purpose-bound use">
  <div class="architecture-core-flow">
    <a class="architecture-core-stage stage-source" href="../../services/data-ingestion-service/"><small>1 · Source authority</small><strong>Distributed sources</strong><span>Operational systems · files · events · APIs · external data</span></a>
    <i aria-hidden="true">→</i>
    <a class="architecture-core-stage stage-service" href="../../services/"><small>2 · Shared delivery</small><strong>Foundation services</strong><span>Ingest · create · consume · share · enable · observe · operate</span></a>
    <i aria-hidden="true">→</i>
    <a class="architecture-core-stage stage-product" href="../data-product-design/"><small>3 · Managed promise</small><strong>Governed data products</strong><span>Source-aligned · aggregate · consumer-aligned · stable product ports</span></a>
    <i aria-hidden="true">→</i>
    <a class="architecture-core-stage stage-use" href="../../services/data-consumption-service/"><small>4 · Purpose-bound value</small><strong>Consumers and AI</strong><span>Analytics · applications · platforms · partners · models · AI agents</span></a>
  </div>
  <div class="architecture-core-rails">
    <a href="../platform-governance-design/"><small>Governs every boundary</small><strong>Ownership · contracts · semantic context · identity · policy · lifecycle</strong><span>Declares who decides, what is promised, which use is allowed, and where controls are enforced.</span></a>
    <a href="../../services/data-observability-service/"><small>Proves trust continuously</small><strong>Lineage · quality · telemetry · SLOs · incidents · operations</strong><span>Compares actual service and product behavior with the published promise.</span></a>
  </div>
  <div class="architecture-core-rule"><strong>Core rule</strong><span>Services create and operate the reusable capability; data products carry the managed promise; governance controls every boundary; evidence shows whether the promise is true now.</span></div>
</div>

This is not a pipeline-only design. Contracts, policy, identity, semantics, lineage, and observability apply across the journey rather than appearing as final review steps.

## Responsibility Layers

Read the model from user intent to platform execution. Each layer has one primary reason to exist.

<div class="architecture-stack">
  <section class="architecture-layer layer-experience"><span class="layer-number">1</span><div><strong>Experience and Access</strong><p>Make foundation capabilities understandable and usable through coherent journeys and interfaces.</p></div></section>
  <div class="layer-connector">Captures intent</div>
  <section class="architecture-layer layer-control"><span class="layer-number">2</span><div><strong>Governance and Control</strong><p>Turn ownership, meaning, contracts, policy, lifecycle, and evidence into authoritative decisions.</p></div></section>
  <div class="layer-connector">Governs execution</div>
  <section class="architecture-layer layer-services"><span class="layer-number">3</span><div><strong>Foundation Services</strong><p>Provide reusable ingestion, creation, consumption, sharing, enablement, observability, and operational capabilities.</p></div></section>
  <div class="layer-connector">Creates and serves</div>
  <section class="architecture-layer layer-products"><span class="layer-number">4</span><div><strong>Governed Data Products</strong><p>Carry owned meaning, quality, interfaces, policy, service levels, and lifecycle promises.</p></div></section>
  <div class="layer-connector">Runs on</div>
  <section class="architecture-layer layer-platform"><span class="layer-number">5</span><div><strong>Platform Runtime</strong><p>Supply replaceable storage, processing, integration, access, and telemetry technology.</p></div></section>
</div>

| Layer | Why It Exists | Boundary That Keeps It Clear |
| --- | --- | --- |
| Experience and access | Give users and systems one coherent way to discover, request, build, consume, and operate. | It does not replace catalog, contract, policy, or workflow authorities. |
| Governance and control | Make decisions consistent, enforceable, and explainable. | It defines and records control intent; services enforce it at real boundaries. |
| Foundation services | Avoid rebuilding ingestion, product creation, access, sharing, and operations for every use case. | Services own reusable capability outcomes, not domain product meaning. |
| Governed data products | Make data independently understandable, trustworthy, and reusable. | A table, pipeline, dashboard extract, or private model input is not automatically a product. |
| Platform runtime | Execute the architecture reliably and at scale. | Selected technology implements the architecture; it does not define the authoritative architecture contract. |

## Three Design Classes

Every architecture concern belongs to one of three design classes. This prevents duplicated shared controls and hidden integration responsibilities.

| Design Class | Use It When | It Must Explain |
| --- | --- | --- |
| **Service-specific design** | One foundation service owns the outcome. | Purpose, scope, capabilities, interfaces, controls, service levels, dependencies, and evidence. |
| **Shared capability design** | Several services require the same authority or runtime capability. | Common responsibility, ownership, reuse boundary, policy, lifecycle, and how services consume it. |
| **Integration design** | The outcome crosses service or trust boundaries. | Handoffs, identifiers, state, policy propagation, failure behavior, recovery, and end-to-end evidence. |

The [Architecture Design Map](design-map.md) relates these design classes to each foundation service and target plane.

## Ownership Logic

The platform team centrally owns source onboarding, ingestion, source-aligned states, shared capabilities, and the reliability of paved paths. Domain teams own the meaning, fitness, lifecycle, and outcomes of aggregate and consumer-aligned products.

This balance exists for a reason:

- Central ownership keeps source capture, controls, interoperability, and operation consistent.
- Federated ownership keeps business meaning and consumer value close to accountable domains.
- Contracts make the handoff explicit without transferring all responsibility to either side.
- Shared services reduce duplication without becoming owners of every data product.

See the [Data Foundation Model](data-foundation-model.md) for the ownership boundaries, product layers, and detailed rationale.

## Architecture Principles

1. **Product before platform object.** Design around a trusted product outcome, not a table, workspace, pipeline, or tool.
2. **Contracts define the data promise.** At every material data handoff, make provider and consumer obligations for meaning, structure, quality, freshness, permitted use, change, and support versioned, testable, and visible.
3. **One authority for each decision.** Catalogs, contracts, policies, lineage, semantics, and telemetry may reference each other but must not silently duplicate ownership.
4. **Govern access independently from storage.** People, workloads, and agents use logical product interfaces with separate service and data authorization.
5. **Trust requires current evidence.** Quality, freshness, lineage, usage, reliability, and incidents must be observable throughout product operation.
6. **Every service is agentic by design.** Service specialist agents expose typed skills and collaborate through the Data Service AI Assistant without replacing deterministic service authority.
7. **Autonomy is explicitly bounded.** An agent may act only within its verified identity, declared purpose, approved skill and tool scope, risk policy, workflow gates, and revocation controls. Data contracts supply requirements, but policy and service authority decide whether an action is allowed and which evidence it must produce.
8. **AI follows the same foundation rules.** Agents and models use governed products, declared purposes, bounded interfaces, evaluations, and traceable identities.
9. **Technology remains replaceable.** Authoritative meaning, policy, contracts, and evidence survive implementation changes.

Principle 2 governs **what data is promised across a boundary**. Principle 7 governs **who or what may act on that promise, under which controls**.

## Architecture Views

Do not read every architecture page in sequence. Start at the level of the decision, then move down only when more detail is required.

<div class="journey-sequence journey-sequence--compact" aria-label="Architecture view selection path">
  <a class="journey-sequence-step" href="../target-architecture/"><span>1</span><strong>Compose</strong><p>See the complete foundation across six cooperating planes.</p><small>Architecture Blueprint → completeness and gaps</small></a>
  <i class="journey-sequence-arrow" aria-hidden="true"></i>
  <a class="journey-sequence-step" href="../data-foundation-model/"><span>2</span><strong>Define</strong><p>Understand product types, core objects, relationships, and ownership handoffs.</p><small>Data Foundation Model → shared conceptual language</small></a>
  <i class="journey-sequence-arrow" aria-hidden="true"></i>
  <a class="journey-sequence-step" href="../design-map/"><span>3</span><strong>Locate</strong><p>Classify the concern as service-specific, shared capability, or integration design.</p><small>Architecture Design Map → accountable design owner</small></a>
  <i class="journey-sequence-arrow" aria-hidden="true"></i>
  <a class="journey-sequence-step" href="../../services/"><span>4</span><strong>Resolve</strong><p>Open the detailed architecture or service page that owns the decision.</p><small>Core Guidance or Services → actionable design</small></a>
  <i class="journey-sequence-arrow" aria-hidden="true"></i>
  <a class="journey-sequence-step" href="../../reference-solutions/"><span>5</span><strong>Realize</strong><p>Map an approved technology choice to the technology-neutral design.</p><small>Reference Solutions → implementation profile</small></a>
</div>

### Route a Detailed Question

| If the decision concerns | Use this authoritative view | Expected result |
| --- | --- | --- |
| Whether a complete user outcome works across services | [End-to-End Service Scenarios](../services/end-to-end-service-scenarios.md) | Accepted sequence, failure behavior, and evidence |
| Which owner or record is authoritative for a decision | [Architecture Decision Process](../decisions/architecture-decision-process.md) | Decision level, authority, recording path, enforcement, and evidence |
| Platform capabilities and runtime interactions | [Platform Architecture](reference-architecture.md) | Required capability and interface map |
| Decision rights, controls, enforcement, or assurance | [Platform Governance Design](platform-governance-design.md) | Authority, control placement, and evidence |
| A promise at a source, creation, or consumption boundary | [Data Contract Design](data-contract-design.md) | Contract type, parties, enforcement, and evidence |
| Business accountability and product portfolio boundaries | [Data Domain Design](data-domain-design.md) | Domain ownership and adoption obligations |
| Product definition, type, ports, lifecycle, or go-live | [Data Product Design](data-product-design.md) | Product boundary and lifecycle design |
| Meaning, business context, catalog metadata, or graph projection | [Semantic and Context Design](semantic-context-design.md) | Authoritative semantic context package |
| Identity, authorization, entitlement, and logical product access | [Unified Access Design](unified-access-design.md) | Governed access path above physical storage |
| A capability reused by several foundation services | [Platform Enablement Design](platform-enablement-design.md) | Shared provider boundary and service interfaces |
| Engineer self-service paths and paved delivery workflows | [Developer Experience Design](developer-experience-design.md) | Declarative developer journey and controls |
| Agent skills, orchestration, autonomy, and human approval | [Agentic Data Service Design](agentic-data-foundation.md) | Bounded agent behavior and execution evidence |
| State or failure crossing service boundaries | [Integration Design](integration-design.md) | Handoff, recovery, and end-to-end evidence design |
| One service's user outcome, capability, interface, SLO, or support | [Services](../services/index.md) | Authoritative service-specific design |

The [Information Graph](../foundation/information-graph.md#architecture-information-graph) page helps explore architecture relationships and terminology. It is a navigation view, not a separate source of architecture authority.

<div class="read-next"><strong>Next:</strong> use the Architecture Blueprint for completeness or the Architecture Design Map to locate an owning design.</div>

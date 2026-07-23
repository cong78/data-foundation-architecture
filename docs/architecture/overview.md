# Architecture Overview

<div class="decision-brief"><div><small>Use when</small><strong>You need to locate or review an architecture decision.</strong></div><div><small>Start with</small><strong>The user outcome or boundary that must become clear.</strong></div><div><small>Owner</small><strong>Architecture owner with the affected service and product owners.</strong></div><div><small>Result</small><strong>One responsible design, its relationships, and the next delivery action.</strong></div></div>

## Purpose

The data foundation turns distributed source data into governed data products that people, applications, platforms, partners, AI agents, and models can use with confidence.

The architecture makes five things explicit:

1. Where data enters and where trust is created.
2. Which capabilities are shared and which outcomes remain domain-owned.
3. Which contracts, policies, and lifecycle decisions govern each boundary.
4. How products are discovered, accessed, shared, observed, changed, and retired.
5. How every important decision can be traced to evidence and an accountable owner.

## Start with the Question

Do not read every architecture page in sequence. Select the question that matches the decision being made.

| I need to understand or design... | Start here | Result |
| --- | --- | --- |
| The complete foundation and whether anything is missing | [Architecture Blueprint](target-architecture.md) | Plane placement, relationships, and completeness gaps |
| Product types, ownership, and central-to-federated handoffs | [Data Foundation Model](data-foundation-model.md) | Shared concepts and ownership boundaries |
| A trusted product, its promise, meaning, domain, or lifecycle | [Data Product Design](data-product-design.md) | Product boundary, contract, context, ports, and lifecycle |
| Shared platform capabilities, governed access, or cross-service flow | [Platform Architecture](reference-architecture.md) | Platform capability, access, and integration boundaries |
| Decision rights, control enforcement, or design traceability | [Platform Governance Design](platform-governance-design.md) | Authority, control placement, and evidence |
| AI assistant, specialist agents, skills, or bounded autonomy | [Agentic Data Service Design](agentic-data-foundation.md) | Governed agent responsibilities and execution boundaries |
| How architecture becomes owned and operable capability | [Architecture to Delivery](architecture-to-delivery.md) | Owning service, action path, acceptance evidence, and operation |
| One service's user outcome, interface, SLO, or support model | [Services](../services/index.md) | Authoritative service-specific design |

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

The foundation is not only a data pipeline. Contracts, policy, identity, semantics, lineage, and observability apply across the whole product journey.

## Responsibility Layers

Read the model from user intent to platform execution. Each layer answers one user or delivery need.

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

## Three Design Classes

Classify a concern once so ownership remains clear:

| Design Class | Use It When | It Must Explain |
| --- | --- | --- |
| **Service-specific design** | One foundation service owns the outcome. | Purpose, scope, capabilities, interfaces, controls, service levels, dependencies, and evidence. |
| **Shared capability design** | Several services require the same authority or runtime capability. | Common responsibility, ownership, reuse boundary, policy, lifecycle, and how services consume it. |
| **Integration design** | The outcome crosses service or trust boundaries. | Handoffs, identifiers, state, policy propagation, failure behavior, recovery, and end-to-end evidence. |

Use the [Architecture Design Map](design-map.md) when a concern crosses several pages or services.

## Ownership Logic

The platform team centrally owns source onboarding, ingestion, source-aligned states, shared capabilities, and the reliability of paved paths. Domain teams own the meaning, fitness, lifecycle, and outcomes of aggregate and consumer-aligned products.

Central ownership keeps source capture and common controls consistent. Federated ownership keeps product meaning and consumer value close to accountable domains. Data contracts make each handoff explicit, while shared services remove duplication without taking ownership of domain outcomes.

See the [Data Foundation Model](data-foundation-model.md) for the detailed product and ownership model.

## Review Rules

1. Start with a user or service outcome, not a platform component.
2. Give every decision and operational outcome one accountable owner.
3. Use shared capabilities across services without creating hidden ownership.
4. Make cross-service state, failure, recovery, and evidence explicit in integration design.
5. Apply the [Design Principles](../foundation/definition-and-scope.md#design-principles) and verify mandatory requirements in [Standards](../standards/index.md).

The [Information Graph](../foundation/information-graph.md#architecture-information-graph) helps locate related guidance and terminology. It is a navigation aid, not a separate source of authority.

<div class="read-next"><strong>Next:</strong> choose one question from the table above and open only the guidance needed to resolve it.</div>

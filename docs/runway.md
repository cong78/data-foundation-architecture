# Runway

<div class="decision-brief"><div><small>Use when</small><strong>Sequencing foundation adoption and investment.</strong></div><div><small>Decision</small><strong>Which workstream blocks the next outcome gate?</strong></div><div><small>Owner</small><strong>Foundation sponsor and capability owners.</strong></div><div><small>Output</small><strong>Funded increment with exit evidence.</strong></div></div>

The runway is a sequenced path for maturing the data foundation. Each phase produces a usable shared capability, not merely a collection of components.

Use the phases as **outcome gates**. Teams may prepare later capabilities early, but should not claim a phase until its exit evidence is operating with real services, products, and consumers.

!!! note "Adoption maturity, not a product lifecycle"
    The four runway phases sequence foundation capability and investment. Individual domains, sources, and products still move through **Frame → Establish → Deliver → Use → Operate** in [Foundation in One View](foundation/foundation-in-one-view.md).

!!! info "Runway is not a runbook"
    The **runway** sequences foundation adoption. A **runbook** is an executable operating procedure for a service, product, or known condition. Use [Architecture to Delivery](foundation/architecture-to-delivery.md) to connect both through the owning data service.

## Runway at a Glance

<div class="standards-map reference-map" role="img" aria-label="Four-phase data foundation delivery runway">
  <div class="standards-map-head" aria-hidden="true">
    <span>Starting need</span><i></i><span>Phase focus</span><i></i><span>Exit outcome</span>
  </div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Phase 1</small><strong>Establish control</strong><p>Fragmented delivery, unclear ownership, and inconsistent trust.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Foundation Baseline</strong><p>Architecture, services, portal, controls, contracts, operations, and first product.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Governed path proven</strong><p>One source-to-consumer flow passes product go-live and operates with evidence.</p></div>
  </section>
  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Phase 2</small><strong>Scale adoption</strong><p>Working patterns exist but still depend on specialist coordination.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Trusted Reuse</strong><p>Self-service creation, lifecycle, semantics, unified access, reliability, and portability.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Reusable foundation</strong><p>Multiple domains deliver and consume live products through repeatable services.</p></div>
  </section>
  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Phase 3</small><strong>Enable governed AI</strong><p>Trusted products exist, but AI context and actions need explicit controls.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>AI-Ready Foundation</strong><p>Approved AI data, lineage, gateways, evaluations, assistant, agents, and skills.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Traceable AI use</strong><p>AI consumption and actions are purpose-bound, evaluated, and evidenced.</p></div>
  </section>
  <section class="standards-map-lane lane-access">
    <div class="standards-map-cell"><small>Phase 4</small><strong>Extend the boundary</strong><p>Internal reuse is mature and external exchange must remain governable.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Ecosystem Sharing</strong><p>Recipients, Data Product Consumption Contracts, open exchange, collaboration, expiry, and revocation.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Controlled ecosystem</strong><p>Customer, supplier, and partner sharing is portable, auditable, and revocable.</p></div>
  </section>
</div>

## Workstreams Across the Runway

| Workstream | Phase 1: Baseline | Phase 2: Trusted Reuse | Phase 3: AI Ready | Phase 4: Ecosystem |
| --- | --- | --- | --- | --- |
| Experience | Core portal journeys | Rich product, domain, support, and workspace journeys | AI and assistant journeys | Recipient and sharing journeys |
| Products and contracts | Three contract templates and go-live gates | Lifecycle, portfolio, compatibility, and subscriptions | AI-ready products and AI consumption profiles | External-sharing consumption profiles and recipient packages |
| Platform services | First ingestion-to-consumption path plus baseline storage, contract, identity, security, integration, and automation enablement | Self-service creation, unified access, semantics, adapters, and reconciled platform resources | Agent, model, context, skill, and evaluation gateways with governed machine identities | Sharing and controlled-collaboration patterns with external identity and revocation |
| Governance and security | Identity, classification, policy, lineage, ownership | Purpose-bound access and reusable domain controls | AI identity, data use, autonomy, and approval | Legal basis, minimization, expiry, and revocation |
| Observability and operations | Telemetry conventions, service records, support and incident model | Product health, cost, problem, change, release, continuity, and improvement | Model, agent, evaluation, and AI-use telemetry | Recipient activity, delivery health, audit, and revocation evidence |
| Interoperability | Stable ids plus one ODCS contract artifact with an embedded ODPS-compatible descriptor | Open metadata, lineage, API, event, telemetry, and independent-client proof | Portable AI context and action evidence | Open sharing interface and federated identity proof |

## Phase 1: Foundation Baseline

**Objective:** establish one governed, supportable path from source onboarding to live product consumption.

| Workstream | Deliverables | Exit evidence |
| --- | --- | --- |
| Direction and ownership | Published architecture, service portfolio, accountable owners, support model, and decision rights. | Published scope, service owners, escalation routes, and approval evidence. |
| Portal and journeys | Data Service Portal with source onboarding, product creation, consumption, product health, and task-status journeys. | Real users complete the first journey through authoritative service APIs. |
| Source and product delivery | Standard ingestion patterns, product template, contract template, workload profile, and mandatory product go-live gates. | At least one source-aligned input and one governed product pass go-live. |
| Control foundation | Catalog, classification, lineage, identity, access workflow, contract approval, and stable enterprise identifiers. | Product, contract, lineage, policy, owner, and access evidence resolve consistently. |
| Platform enablement | Supported storage lifecycle, contract system, identity and security bindings, catalog synchronization, integration interfaces, provisioning, and deprovisioning patterns. | One real product is provisioned and retired through governed APIs with correlated policy, contract, catalog, runtime, and lifecycle evidence. |
| Observability and operations | OpenTelemetry conventions, production service records, SLOs, support, incident roles, escalation, change classes, continuity targets, and readiness criteria. | Service and product health are visible; one support and incident path is exercised. |
| Portability | Authoritative ODCS publishing data contracts with embedded ODPS-compatible descriptors stored independently of runtime-native metadata. | The combined data-contract artifact validates against both pinned profiles and retains stable identifiers. |

### Phase 1 Gate

Proceed when a real source-to-consumer product demonstrates ownership, contract, quality, lineage, access, telemetry, support, recovery, and go-live evidence end to end.

## Phase 2: Trusted Reuse

**Objective:** turn the proven path into repeatable self-service capabilities used by multiple domains and consumers.

| Workstream | Deliverables | Exit evidence |
| --- | --- | --- |
| Product management | Contract registry, compatibility checks, subscriptions, lifecycle, portfolio review, quality gates, deprecation, and retirement. | Breaking changes identify consumers; duplicate, unhealthy, unused, and ownerless products are governed. |
| Developer experience | Portal, API, and CLI parity; isolated environments; deployment preview; policy checks; promotion; release evidence; rollback. | A domain team delivers a product without a platform-specific delivery ticket. |
| Consumption and semantics | Standard semantic, SQL, API, event, retrieval, and feature patterns through unified access. | Representative BI, application, platform, and AI consumers use governed product ports. |
| Portal experience | Product discovery, access, domain, use-case, workspace, saved-product, consumption-contract, portfolio, support, status, change, and knowledge views. | Users can discover, request, track, support, and understand products in one experience. |
| Trust and operations | Product health, freshness, quality, usage, cost, incident communication, problem, release, error budget, recovery exercise, and improvement workflows. | System and product recovery is proven; service reviews use measured health and operational evidence. |
| Platform enablement | Self-service resource plans, policy previews, environment promotion, drift reconciliation, exception expiry, retention automation, and deprovisioning. | Multiple domain teams reuse supported capabilities without duplicating identity, storage, contract, security, or integration controls. |
| Interoperability | DCAT, OpenAPI, AsyncAPI, CloudEvents, OTLP, and portable lineage adapters plus clean-room import/export. | An independent client consumes a product and portable source artifacts survive export and import. |

### Phase 2 Gate

Proceed when multiple domains use the shared services, products are reused by independent consumers, operational SLOs are measured, and delivery no longer depends on one specialist team.

## Phase 3: AI-Ready Data Foundation

**Objective:** make governed data and foundation actions safely usable by AI models, assistants, and agents.

| Workstream | Deliverables | Exit evidence |
| --- | --- | --- |
| AI-ready products | Approved datasets, feature sets, retrieval indexes, evaluation datasets, usage policies, and prohibited-use rules. | Each AI use resolves product, contract, snapshot or index, identity, purpose, quality, and lineage. |
| AI platform | Agent Gateway, agent and skill registry, LLM gateway, context gateway, memory controls, and evaluation service. | Gateways enforce identity, policy, model profile, budget, approval, audit, and suspension. |
| Portal journeys | MCP product, AI agent, AI model, AI evaluation, and AI-use approval journeys. | AI teams complete governed onboarding and can see dependencies, decisions, and evidence. |
| Data Service AI Assistant | Grounded Ask and Plan modes, read-only discovery and explanation skills, then bounded write skills with previews and receipts. | Responses cite authoritative evidence; write actions require typed scope and correct approval. |
| AI observability | Product-level AI usage, model and agent lineage, prompt and embedding controls, evaluation outcomes, quality feedback, safety, reliability, and cost. | One AI interaction traces end to end from source product through model or agent outcome. |
| Evaluation and release | Versioned quality, policy, safety, reliability, and cost evaluations for models, agents, and skills. | Failed thresholds block release; approved versions have reproducible evaluation evidence. |

### Phase 3 Gate

Proceed when AI use cannot bypass product, identity, purpose, access, evaluation, approval, lineage, observability, or operational controls.

## Phase 4: Ecosystem Sharing

**Objective:** extend governed products to customers, suppliers, and partners without losing control after delivery.

| Workstream | Deliverables | Exit evidence |
| --- | --- | --- |
| Sharing patterns | Standard internal, customer, supplier, partner, and controlled-collaboration patterns. | Each pattern has owner, contract, identity, delivery, support, monitoring, expiry, and revocation. |
| Data Product Consumption Contracts and entitlement | Automated external-sharing consumption profiles, recipient identity, minimized scope, approval, entitlement, renewal, and offboarding. | Technical package and entitlement reconcile with the approved Data Product Consumption and Creation Contracts. |
| Open exchange | Open sharing interface, federated identity, independent recipient test, and portable recipient package. | At least one partner completes exchange without relying on provider-only consumer tooling. |
| Operations and assurance | Delivery health, recipient activity, incident communication, audit export, retention, expiry, suspension, and revocation testing. | Access is revoked within the target; exported evidence shows who received what, why, when, and under which version. |

### Phase 4 Gate

The phase is established when at least one real external exchange is contract-based, minimized, observable, independently consumable, auditable, expiring, and demonstrably revocable.

## Progression Rules

| Rule | Application |
| --- | --- |
| Prove before scaling | Use real sources, products, identities, consumers, incidents, and changes; demonstrations without operational evidence do not pass a gate. |
| Keep earlier controls active | Later phases add capability but do not replace ownership, contracts, access, product go-live, observability, or operations. |
| Advance by workstream | A workstream may be ahead or behind the overall phase; record its evidence and gaps separately. |
| Fund the constraint | Prioritize the weakest workstream blocking the next outcome instead of launching every component at once. |
| Preserve portability | Every phase retains portable source artifacts, stable identifiers, open interfaces, export paths, and tested exit options. |
| Measure adoption | A deployed capability without active users, products, and operating ownership is not mature. |

## Success Measures

| Outcome | Measures |
| --- | --- |
| Delivery flow | Source onboarding time, product lead time, go-live cycle time, deployment frequency, rollback success, and self-service completion. |
| Product trust and reuse | Live products with owner, contract, quality, lineage and SLO; reuse by independent consumers; duplicate pipeline reduction; consumer satisfaction. |
| Operations and reliability | Service SLO attainment, acknowledge and recovery time, recurrence, change success, emergency-change rate, support experience, recovery exercise success, and toil removed. |
| Interoperability | Products passing required conformance, artifact round-trip success, independent-client consumption, and unresolved vendor-specific exceptions. |
| AI outcomes | Governed AI systems, trace-complete agent runs, task success, unsupported-claim rate, approval accuracy, safety and reliability pass rate, and cost per task. |
| Ecosystem control | Active external-sharing Data Product Consumption Contracts, delivery SLOs, recipient incidents, expired access removed, revocation test success, and complete audit evidence. |

<div class="read-next">
  <strong>Next:</strong> use the Data Foundation Maturity Assessment to score each workstream, then convert the weakest progression gate into funded delivery increments.
</div>

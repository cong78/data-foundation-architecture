# Architecture to Delivery

<div class="decision-brief"><div><small>Use when</small><strong>Turning architecture intent into an owned foundation capability.</strong></div><div><small>Decision</small><strong>Which data service delivers, operates, and evidences the outcome?</strong></div><div><small>Owner</small><strong>Architect with the accountable data-service owner.</strong></div><div><small>Output</small><strong>One service delivery trace from design to evidence.</strong></div></div>

Architecture is realized through data services. Each service is a delivery entity for a coherent foundation capability: it has an accountable owner, explicit consumers, interfaces, controls, implementation increments, SLOs, runbooks, and evidence. Use this map during design review, planning, service onboarding, production readiness, and continual improvement.

## The Delivery Chain

<div class="model-strip delivery-stage-strip">
  <div class="model-step"><strong>1 · Architecture direction</strong>Defines the outcome, boundaries, structure, interactions, qualities, and current approved direction.</div>
  <div class="model-step"><strong>2 · Service ownership</strong>Assigns the reusable capability, accountable owner, consumers, interfaces, SLOs, and support.</div>
  <div class="model-step"><strong>3 · Delivery design</strong>Defines the increment, dependencies, integration, acceptance criteria, and optional technology profile.</div>
  <div class="model-step"><strong>4 · Build and validate</strong>Implements the increment and proves standards, policy, security, interoperability, and recovery behavior.</div>
  <div class="model-step"><strong>5 · Release / go-live</strong>Confirms readiness, approval, deployment, rollback, communication, and exact released versions.</div>
  <div class="model-step"><strong>6 · Operate and improve</strong>Measures outcomes, meets SLOs, supports users, recovers safely, and feeds learning into the next change.</div>
</div>

<div class="delivery-feedback"><strong>Feedback loop</strong><span>Usage, incidents, cost, product health, consumer outcomes, and recovery exercises can trigger a new decision or delivery increment.</span></div>

| Stage | Decision Question | Authoritative Output |
| --- | --- | --- |
| Architecture direction | What outcome, boundary, interaction, and quality apply now? | Current architecture and service guidance incorporating approved decisions. |
| Service ownership | Which reusable capability owns delivery and operation? | Versioned service definition, accountable owner, service registry record, support model, and lifecycle state. |
| Delivery design | What is the smallest useful increment and how will it fit? | Delivery backlog, integration design, acceptance scenarios, dependency plan, runway alignment, and optional reference solution. |
| Build and validate | Does the implementation satisfy the required behavior and controls? | Versioned implementation, data-contract and policy results, tests, conformance evidence, operational readiness, and rollback proof. |
| Release / go-live | May this exact service or product version enter use? | Readiness decision, approvals, release record, deployment receipt, communication, rollback target, and current catalog or registry state. |
| Operate and improve | Is the capability reliable, useful, recoverable, and still conformant? | SLO and health state, support and incident records, exercised runbooks, usage and cost outcomes, recovery evidence, and improvement backlog. |

This is a traceability chain, not a waterfall plan. Teams may iterate across stages, but they cannot skip ownership, controls, readiness, operation, or evidence. The [Runway](../runway.md) schedules when capabilities are introduced and scaled; it is planning context, not a delivery stage or proof of operational readiness. [Reference Solutions](../reference-solutions/index.md) may accelerate delivery design and implementation, but they never redefine the architecture direction or service boundary.

## Data Services as Delivery Entities

A data service is the manageable unit through which the data foundation is built and evolved. Architecture planes and shared capabilities describe the whole system, but they are not independently deliverable. A data service packages the relevant parts into an outcome that people, systems, agents, and other services can request and rely on.

| Delivery Property | What Every Data Service Must Make Explicit |
| --- | --- |
| Outcome | The foundation capability and user or system need the service fulfills. |
| Accountability | One service owner responsible for value, lifecycle, risk, reliability, cost, and improvement. |
| Service definition | Scope, consumers, interfaces, inputs, outputs, controls, SLOs, support, and evidence. |
| Build boundary | The implementation increments, platform capabilities, team responsibilities, and release unit needed to realize the service. |
| Integration | Upstream and downstream service interactions, data contracts, failure behavior, and end-to-end correlation. |
| Operation | Telemetry, support model, incidents, changes, continuity, runbooks, and recovery objectives. |
| Proof | Conformance, release, adoption, product impact, reliability, cost, and improvement evidence. |

The service is the delivery entity; it is not necessarily one team or one deployment. Central platform teams may deliver ingestion, platform enablement, observability, and operations capabilities, while federated domain teams use those services to create aggregate and consumer-aligned data products. Cross-service outcomes still require one accountable outcome owner and an explicit integration design.

## Design to Delivery

Each service follows the same path from architecture to an executable user or operator journey.

| Outcome | Architecture | Owning Service | Primary Playbook |
| --- | --- | --- | --- |
| Discover, request, and track work | [Data Service Portal architecture](../services/data-service-portal.md#service-architecture) | [Data Service Portal](../services/data-service-portal.md) | [Choose an Action](../playbooks/index.md) |
| Coordinate governed multi-agent guidance and action | [Data Service AI Assistant architecture](../services/data-service-ai-assistant.md#service-architecture) | [Data Service AI Assistant](../services/data-service-ai-assistant.md) with the selected service owner | The selected foundation playbook; the assistant and specialist agents do not create a parallel process. |
| Onboard a source | [Data Ingestion Service architecture](../services/data-ingestion-service.md#service-architecture) | [Data Ingestion Service](../services/data-ingestion-service.md) | [Onboard a Source](../playbooks/onboard-source.md) |
| Create or change a product | [Data Product Creation Service architecture](../services/data-product-creation-service.md#service-architecture) | [Data Product Creation Service](../services/data-product-creation-service.md) | [Create or Change a Data Product](../playbooks/create-change-data-product.md) and [Approve Product Go-Live](../playbooks/approve-product-go-live.md) |
| Consume a product | [Data Consumption Service architecture](../services/data-consumption-service.md#service-architecture) | [Data Consumption Service](../services/data-consumption-service.md) | [Consume a Data Product](../playbooks/consume-data-product.md) |
| Share a product | [Data Sharing Service architecture](../services/data-sharing-service.md#service-architecture) | [Data Sharing Service](../services/data-sharing-service.md) | [Share a Data Product](../playbooks/share-data-product.md) |
| Provision common controls and resources | [Platform Enablement Service architecture](../services/platform-enablement-service.md#service-architecture) | [Platform Enablement Service](../services/platform-enablement-service.md) | Invoked by each applicable foundation playbook; it is not a separate user journey. |
| Observe service and product health | [Data Observability Service architecture](../services/data-observability-service.md#service-architecture) | [Data Observability Service](../services/data-observability-service.md) | [Operate a Service or Product](../playbooks/operate-service-product.md) |
| Coordinate support and recovery | [Data Foundation Operations architecture](../services/data-foundation-operations-service.md#service-architecture) | [Data Foundation Operations Service](../services/data-foundation-operations-service.md) | [Operate a Service or Product](../playbooks/operate-service-product.md) |

Use the [Standards Overview](../standards/index.md) to identify the standards that constrain each service. Record implementation choices and evidence with the delivered capability without creating a reverse dependency from published design guidance.

When a row involves more than one service, add an [Integration Design](integration-design.md) that names the outcome owner, interface specifications, failure behavior, correlation identifiers, and end-to-end evidence.

## Agentic Delivery Overlay

Every service adds the same agentic trace to its architecture-to-delivery chain. This overlay does not replace service ownership, deterministic controls, playbooks, runbooks, or evidence.

| Trace Element | Required Record |
| --- | --- |
| User intent | Initiating actor, delegated identity, purpose, target outcome, and constraints. |
| Declarative authority | Exact data contract versions, policy decisions, lifecycle state, and approval state. |
| Delegation | Assistant task, service specialist agent, parent and child task ids, scope, autonomy ceiling, budget, and completion owner. |
| Execution | Registered skill and version, deterministic service operation, idempotency key, parameters, and obligations. |
| Outcome | Service receipt, changed state, evidence gaps, compensation or recovery state, and user-visible result. |
| Operation | End-to-end trace, evaluation, cost, incident route, suspension control, and retained audit evidence. |

## Operate Delivered Services

Each service must map its material failure modes to an exercised runbook and authoritative evidence.

| Service | Runbook Focus | Minimum Evidence |
| --- | --- | --- |
| Data Service Portal | Availability, search projection freshness, workflow handoff, task recovery, and authority reconciliation. | Synthetic journey, projection lag, workflow status, failed-task recovery, and reconciliation result. |
| Data Service AI Assistant | Model, agent or skill degradation, grounding failure, unsafe delegation, interrupted approvals, cancellation, and fallback. | Delegation chain, contract versions, evaluation result, policy decision, approval record, service receipts, trace, fallback outcome, and retained audit event. |
| Data Ingestion Service | Connection failure, schema change, backlog, replay, duplicate or lost delivery, quarantine growth, and source recovery. | Source and contract ids, run status, checkpoint, counts, quarantine reason, lineage, and validated handoff. |
| Data Product Creation Service | Build or deployment failure, quality breach, incompatibility, drift, rollback, and product-health validation. | Contract and product versions, test result, release record, lineage, quality state, rollback result, and go-live decision. |
| Data Consumption Service | Resolution, policy or entitlement failure, adapter failure, latency, stale results, obligations, and revocation. | Consumer, purpose, policy decision, product version, access event, SLO state, obligation, and revocation result. |
| Data Sharing Service | Provisioning, delivery, recipient identity, package error, expiry, emergency suspension, revocation, and offboarding. | Recipient and purpose, agreement, package version, entitlement, delivery event, expiry, revocation, and deletion proof. |
| Platform Enablement Service | Provisioning, identity or policy binding, contract service, storage lifecycle, catalog drift, retention, deletion, rollback, and deprovisioning. | Resource, owner, identity, policy, contract and catalog bindings, lifecycle state, drift result, and deprovisioning proof. |
| Data Observability Service | Telemetry loss, collector or exporter failure, correlation gaps, alert storm, stale health, and sensitive telemetry. | Signal coverage, freshness, semantic-convention validation, correlation ids, alert state, and restoration result. |
| Data Foundation Operations Service | Support routing, incident command, communication, problem escalation, failed change, continuity, and recovery validation. | Ticket, incident, change or problem record; timeline; decision log; communication; recovery checks; and follow-up owner. |

## Required Service Delivery Record

Every adopting organization maintains one record per production service linking architecture direction to current delivery and operational evidence. This repository defines the required structure; the authoritative record is created and maintained in the adopter's service-management or engineering system.

| Field | Required Link or Evidence |
| --- | --- |
| Architecture direction | Current architecture and service guidance, boundaries, dependencies, interactions, and trust assumptions. |
| Service ownership | Service id, accountable owner, support tier, capabilities, interfaces, consumers, SLOs, and lifecycle state. |
| Delivery design | Increment, acceptance scenarios, dependencies, integration behavior, implementation owner, target release, and rollback design. |
| Constraints | Applicable standard, policy, data-contract, security, interoperability, and exception versions with enforcement points. |
| Playbooks and workflows | User and operator journeys, actors, actions, gates, approvals, workflow authority, and completion conditions. |
| Build and validation | Implementation and configuration versions, test results, conformance decisions, unresolved risks, and remediation owners. |
| Release and readiness | Approval, exact release, deployment receipt, go-live state where applicable, rollback target, communication, and catalog or registry state. |
| Operation and runbooks | Telemetry, SLOs, support, alerts, failure modes, versioned procedures, recovery objectives, escalation, and latest exercise. |
| Current evidence | Control, workflow, release, usage, cost, health, incident, recovery, exception, and improvement records with observation times. |
| Planning context | Current runway phase, next exit outcome, funded backlog, dependencies, and target evidence; never treated as readiness proof. |

Each link must resolve in both directions: from architecture direction to current evidence and from a release, incident, policy result, or operational outcome back to its owning service and applicable guidance.

## Runbook and Runway

| Concept | Purpose | Time Horizon | Completion Test |
| --- | --- | --- | --- |
| **Runbook** | Operate or recover one service, product, or known condition. | Minutes to hours during response; maintained throughout service life. | Authorized operators execute it and prove safe recovery. |
| **Runway** | Sequence foundation capabilities and investment across services and domains. | Quarters and maturity phases. | Phase exit evidence is demonstrated with real services, products, and consumers. |

The runway may fund creation and testing of runbooks. A runbook does not replace the runway, and a runway milestone does not prove operational readiness until the relevant controls and runbooks are exercised.

## Review Rule

A design or production-readiness review is incomplete when architecture direction has no accountable data service or when any required delivery link is absent or stale. Release evidence must prove the exact candidate; operational evidence must include observation time and current state; improvement work must trace back to the affected outcome, service, and guidance.

<div class="read-next"><strong>Next:</strong> choose one architecture outcome, assign its accountable data service, complete the service delivery record, and identify the next implementation increment and required evidence.</div>

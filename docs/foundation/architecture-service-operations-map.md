# Architecture to Operations Map

<div class="decision-brief"><div><small>Use when</small><strong>Tracing a design into delivery and operation.</strong></div><div><small>Decision</small><strong>Is every architecture concern governed, owned, executable, and evidenced?</strong></div><div><small>Owner</small><strong>Architect with service and operations owners.</strong></div><div><small>Output</small><strong>One linked traceability record.</strong></div></div>

This page connects architecture to operational evidence. Use it during design review, service onboarding, production readiness, and operational improvement.

## The Traceability Chain

<div class="model-strip">
  <div class="model-step"><strong>1 · Design</strong>Defines the required structure, boundaries, flows, and qualities.</div>
  <div class="model-step"><strong>2 · Decisions and standards</strong>Make important choices explicit and define enforceable rules.</div>
  <div class="model-step"><strong>3 · Service</strong>Owns the reusable capability, interface, controls, SLO, and support.</div>
  <div class="model-step"><strong>4 · Playbook</strong>Coordinates the actions and gates needed to achieve an outcome.</div>
  <div class="model-step"><strong>5 · Runbook</strong>Defines detection, containment, recovery, validation, and escalation.</div>
  <div class="model-step"><strong>6 · Evidence</strong>Proves the design, controls, actions, health, and recovery.</div>
</div>

| Link | Question | Authoritative Artifact |
| --- | --- | --- |
| Design | What structure, boundary, interaction, and quality are required? | Approved architecture view. |
| Decisions and standards | Which choices and rules constrain implementation? | Accepted ADRs and applicable standards or policies. |
| Service | Which reusable capability owns the outcome? | Versioned service contract and service registry record. |
| Playbook | Who performs which action, and what advances each gate? | Action playbook backed by authoritative workflow state. |
| Runbook | How is a known condition detected and safely recovered? | Versioned, exercised operational procedure. |
| Evidence | What proves conformance, health, action, and recovery now? | Authoritative control, workflow, telemetry, and operations records. |

The [Runway](../runway.md) schedules when capabilities in this chain are introduced and scaled. It is a planning overlay, not another traceability link and not evidence of operational readiness.

## Design to Delivery

Each service follows the same path from architecture to an executable user or operator journey.

| Outcome | Architecture | Owning Service | Primary Playbook |
| --- | --- | --- | --- |
| Discover, request, and track work | [Data Service Portal architecture](../services/data-service-portal.md#service-architecture) | [Data Service Portal](../services/data-service-portal.md) | [Choose an Action](../playbooks/index.md) |
| Receive governed AI guidance and action | [Data Service AI Assistant architecture](../services/data-service-ai-assistant.md#service-architecture) | [Data Service AI Assistant](../services/data-service-ai-assistant.md) | The selected foundation playbook; the assistant does not create a parallel process. |
| Onboard a source | [Data Ingestion Service architecture](../services/data-ingestion-service.md#service-architecture) | [Data Ingestion Service](../services/data-ingestion-service.md) | [Onboard a Source](../playbooks/onboard-source.md) |
| Create or change a product | [Data Product Creation Service architecture](../services/data-product-creation-service.md#service-architecture) | [Data Product Creation Service](../services/data-product-creation-service.md) | [Create or Change a Data Product](../playbooks/create-change-data-product.md) and [Approve Product Go-Live](../playbooks/approve-product-go-live.md) |
| Consume a product | [Data Consumption Service architecture](../services/data-consumption-service.md#service-architecture) | [Data Consumption Service](../services/data-consumption-service.md) | [Consume a Data Product](../playbooks/consume-data-product.md) |
| Share a product | [Data Sharing Service architecture](../services/data-sharing-service.md#service-architecture) | [Data Sharing Service](../services/data-sharing-service.md) | [Share a Data Product](../playbooks/share-data-product.md) |
| Provision common controls and resources | [Platform Enablement Service architecture](../services/platform-enablement-service.md#service-architecture) | [Platform Enablement Service](../services/platform-enablement-service.md) | Invoked by each applicable foundation playbook; it is not a separate user journey. |
| Observe service and product health | [Data Observability Service architecture](../services/data-observability-service.md#service-architecture) | [Data Observability Service](../services/data-observability-service.md) | [Operate a Service or Product](../playbooks/operate-service-product.md) |
| Coordinate support and recovery | [Data Foundation Operations architecture](../services/data-foundation-operations-service.md#service-architecture) | [Data Foundation Operations Service](../services/data-foundation-operations-service.md) | [Operate a Service or Product](../playbooks/operate-service-product.md) |

Use the [Standards Overview](../standards/index.md) to identify the standards that constrain each service. Record consequential implementation choices in the [Decision Register](../implementation/architecture-decisions.md).

When a row involves more than one service, add an [Integration Design](../architecture/integration-design.md) that names the outcome owner, interaction contracts, failure behavior, correlation identifiers, and end-to-end evidence.

## Operations and Evidence

Each service must map its material failure modes to an exercised runbook and authoritative evidence.

| Service | Runbook Focus | Minimum Evidence |
| --- | --- | --- |
| Data Service Portal | Availability, search projection freshness, workflow handoff, task recovery, and authority reconciliation. | Synthetic journey, projection lag, workflow status, failed-task recovery, and reconciliation result. |
| Data Service AI Assistant | Model or skill degradation, grounding failure, unsafe requests, interrupted approvals, cancellation, and fallback. | Evaluation result, policy decision, approval record, trace, fallback outcome, and retained audit event. |
| Data Ingestion Service | Connection failure, schema change, backlog, replay, duplicate or lost delivery, quarantine growth, and source recovery. | Source and contract ids, run status, checkpoint, counts, quarantine reason, lineage, and validated handoff. |
| Data Product Creation Service | Build or deployment failure, quality breach, incompatibility, drift, rollback, and product-health validation. | Contract and product versions, test result, release record, lineage, quality state, rollback result, and go-live decision. |
| Data Consumption Service | Resolution, policy or entitlement failure, adapter failure, latency, stale results, obligations, and revocation. | Consumer, purpose, policy decision, product version, access event, SLO state, obligation, and revocation result. |
| Data Sharing Service | Provisioning, delivery, recipient identity, package error, expiry, emergency suspension, revocation, and offboarding. | Recipient and purpose, agreement, package version, entitlement, delivery event, expiry, revocation, and deletion proof. |
| Platform Enablement Service | Provisioning, identity or policy binding, contract service, storage lifecycle, catalog drift, retention, deletion, rollback, and deprovisioning. | Resource, owner, identity, policy, contract and catalog bindings, lifecycle state, drift result, and deprovisioning proof. |
| Data Observability Service | Telemetry loss, collector or exporter failure, correlation gaps, alert storm, stale health, and sensitive telemetry. | Signal coverage, freshness, semantic-convention validation, correlation ids, alert state, and restoration result. |
| Data Foundation Operations Service | Support routing, incident command, communication, problem escalation, failed change, continuity, and recovery validation. | Ticket, incident, change or problem record; timeline; decision log; communication; recovery checks; and follow-up owner. |

## Required Traceability Record

Every production service maintains one record with the same six links:

| Field | Required Link or Evidence |
| --- | --- |
| Design | Approved architecture view, boundaries, dependencies, data flows, and trust assumptions. |
| Decisions and standards | Applicable ADRs, standards, policy versions, exceptions, and decision evidence. |
| Service | Service id, owner, support tier, capabilities, interfaces, consumers, SLOs, and lifecycle state. |
| Playbooks | User and operator journeys that invoke the service, including gate criteria and workflow authority. |
| Runbooks | Versioned procedures mapped to alerts, failure modes, changes, recovery objectives, and escalation routes. |
| Evidence | Current conformance, workflow, telemetry, health, recovery exercise, exception, and improvement records. |

Record the current runway phase and next phase exit separately as planning context. A runway phase never substitutes for any required field above.

## Runbook Contract

A runbook is an operational control, not a narrative troubleshooting page. Use the [Service Runbook Template](../delivery-templates/service-runbook-template.md). At minimum it must identify:

- Service, product, environment, owner, support tier, architecture decision, and affected dependencies.
- Trigger, observable symptoms, severity criteria, product and consumer impact, and safe diagnostic evidence.
- Preconditions, required authority, segregation of duties, step-up access, and prohibited actions.
- Containment, recovery, rollback, continuity, communication, and escalation steps.
- Separate **system recovery** and **data-product recovery** checks for quality, freshness, lineage, access, backlog, and consumers.
- Telemetry, incident, change, release, contract, and correlation identifiers retained as evidence.
- Test cadence, last exercise, known limitations, review owner, version, and expiry.

## Runbook and Runway

| Concept | Purpose | Time Horizon | Completion Test |
| --- | --- | --- | --- |
| **Runbook** | Operate or recover one service, product, or known condition. | Minutes to hours during response; maintained throughout service life. | Authorized operators execute it and prove safe recovery. |
| **Runway** | Sequence foundation capabilities and investment across services and domains. | Quarters and maturity phases. | Phase exit evidence is demonstrated with real services, products, and consumers. |

The runway may fund creation and testing of runbooks. A runbook does not replace the runway, and a runway milestone does not prove operational readiness until the relevant controls and runbooks are exercised.

## Review Rule

A production-readiness review is incomplete when any of the six links is absent or stale. The trace must resolve in both directions: from a design requirement to current evidence, and from an incident or control result back to the responsible service, rule, and design decision.

<div class="read-next"><strong>Next:</strong> choose one service, complete its six-link traceability record, and create or exercise a runbook for each material failure and recovery condition.</div>

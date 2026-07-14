# Architecture to Operations Map

<div class="decision-brief"><div><small>Use when</small><strong>Tracing a design into delivery and operation.</strong></div><div><small>Decision</small><strong>Is every architecture concern owned, executable, and recoverable?</strong></div><div><small>Owner</small><strong>Architect with service and operations owners.</strong></div><div><small>Output</small><strong>Linked design, service, playbook, runbook, and evidence.</strong></div></div>

This page is the correlation point between architecture, foundation services, action playbooks, operational runbooks, and the delivery runway. Use it during design review, service onboarding, production readiness, and operational improvement.

## The Traceability Chain

<div class="model-strip">
  <div class="model-step"><strong>1 · Architecture</strong>Defines structure, boundaries, decisions, and required qualities.</div>
  <div class="model-step"><strong>2 · Service</strong>Owns a reusable capability, interface, SLO, controls, and support.</div>
  <div class="model-step"><strong>3 · Playbook</strong>Coordinates people and services to complete a foundation task.</div>
  <div class="model-step"><strong>4 · Runbook</strong>Guides operators through detection, diagnosis, safe action, and recovery.</div>
  <div class="model-step"><strong>5 · Evidence</strong>Proves the design, action, control, and recovery worked.</div>
  <div class="model-step"><strong>6 · Runway</strong>Sequences when the enterprise capability is established and scaled.</div>
</div>

| Artifact | Primary Question | Authority |
| --- | --- | --- |
| Architecture design | What structure, boundary, interaction, and quality are required? | Architecture owner and decision record. |
| Service contract | Which reusable capability owns the outcome and interface? | Service owner and service registry. |
| Action playbook | Who performs which cross-service actions and what evidence advances the gate? | Journey owner and authoritative workflow. |
| Operational runbook | How is a known operating condition detected, contained, recovered, validated, and escalated? | Service or product owner with operations. |
| Evidence | What proves current conformance, health, decision, action, and recovery? | Source system for each evidence type. |
| Runway | When should the capability be introduced and what exit evidence proves maturity? | Foundation sponsor and capability owners. |

## Traceability by Service

=== "Engage"

    **Portal and marketplace**

    - **Architecture:** [Data Service Portal Design](../architecture/data-service-portal-model.md)
    - **Service:** [Data Service Portal](../services/data-service-portal.md)
    - **Playbook:** [Choose an Action](../playbooks/index.md)
    - **Runbook focus:** portal availability, search projection freshness, workflow handoff, task recovery, notification failure, and authority reconciliation.

    **Data Service AI Assistant**

    - **Architecture:** [Agentic Data Foundation](../architecture/agentic-data-foundation.md)
    - **Service:** [Data Service AI Assistant](../services/data-service-ai-assistant.md)
    - **Playbook:** the selected foundation playbook; the assistant does not create a parallel process.
    - **Runbook focus:** model or skill degradation, grounding failure, unsafe request, approval interruption, task cancellation, fallback, and audit preservation.

=== "Deliver"

    **Data ingestion**

    - **Architecture:** [Data Foundation Model](../architecture/data-foundation-model.md) and [Data Ingestion Design](../architecture/data-ingestion-design.md)
    - **Service:** [Data Ingestion Service](../services/data-ingestion-service.md)
    - **Playbook:** [Onboard a Source](../playbooks/onboard-source.md)
    - **Runbook focus:** connection failure, schema change, backlog, replay, duplicate or lost delivery, quarantine growth, source recovery, and validated handoff.

    **Data product creation**

    - **Architecture:** [Product Lifecycle](../architecture/data-product-lifecycle-design.md) and [Data Product Creation Design](../architecture/data-product-creation-design.md)
    - **Service:** [Data Product Creation Service](../services/data-product-creation-service.md)
    - **Playbook:** [Create or Change a Product](../playbooks/create-change-data-product.md) and [Approve Product Go-Live](../playbooks/approve-product-go-live.md)
    - **Runbook focus:** build or deployment failure, quality breach, contract incompatibility, rollback, drift, failed release, and product-health validation.

=== "Enable"

    **Platform enablement**

    - **Architecture:** [Target Architecture](../architecture/target-architecture.md), [Reference Architecture](../architecture/reference-architecture.md), and [Unified Access Design](../architecture/unified-access-design.md)
    - **Service:** [Platform Enablement Service](../services/platform-enablement-service.md)
    - **Playbook:** the selected foundation playbook invokes enablement; shared provisioning does not create a parallel user journey.
    - **Runbook focus:** provisioning failure, identity or policy binding error, contract service degradation, storage lifecycle failure, catalog drift, secret rotation, retention or deletion failure, integration outage, rollback, and deprovisioning proof.

=== "Use"

    **Data consumption**

    - **Architecture:** [Unified Access Design](../architecture/unified-access-design.md) and [Data Consumption Design](../architecture/data-consumption-design.md)
    - **Service:** [Data Consumption Service](../services/data-consumption-service.md)
    - **Playbook:** [Consume a Data Product](../playbooks/consume-data-product.md)
    - **Runbook focus:** resolution failure, policy or entitlement error, adapter failure, latency, stale result, obligation enforcement, revocation, and consumer impact.

    **Data sharing**

    - **Architecture:** [Data Sharing Design](../architecture/data-sharing-design.md)
    - **Service:** [Data Sharing Service](../services/data-sharing-service.md)
    - **Playbook:** [Share a Data Product](../playbooks/share-data-product.md)
    - **Runbook focus:** provisioning, delivery, recipient identity, package error, leakage risk, expiry, emergency suspension, revocation, and offboarding proof.

=== "Operate"

    **Data observability**

    - **Architecture:** [Observability Design](../architecture/observability-design.md)
    - **Service:** [Data Observability Service](../services/data-observability-service.md)
    - **Playbook:** [Operate a Service or Product](../playbooks/operate-service-product.md)
    - **Runbook focus:** telemetry loss, collector or exporter failure, correlation gaps, alert storm, stale health, sensitive telemetry, and evidence restoration.

    **Foundation operations**

    - **Architecture:** [Reference Architecture](../architecture/reference-architecture.md) and [Operating Model](../governance/operating-model.md)
    - **Service:** [Data Foundation Operations Service](../services/data-foundation-operations-service.md)
    - **Playbook:** [Operate a Service or Product](../playbooks/operate-service-product.md)
    - **Runbook focus:** support routing, incident command, major communication, problem escalation, change failure, continuity invocation, and recovery validation.

## Required Traceability Record

Every production service should maintain these links in its service record:

| Field | Required Link or Evidence |
| --- | --- |
| Architecture | Approved architecture view, decision records, boundaries, dependencies, and trust assumptions. |
| Service | Service id, owner, support tier, capabilities, interfaces, consumers, SLOs, and lifecycle state. |
| Standards | Applicable contract, access, product, workload, telemetry, interoperability, and AI controls. |
| Playbooks | Onboarding, change, access, sharing, product go-live, and operation journeys that invoke the service. |
| Runbooks | Versioned procedures mapped to alerts, failure modes, changes, recovery objectives, and escalation routes. |
| Telemetry | Dashboards, alerts, SLOs, product health, lineage, usage, cost, and correlation identifiers. |
| Recovery | Last exercise, result, gaps, owner, due date, rollback target, and system-plus-product validation. |
| Runway | Current adoption phase, required exit evidence, dependencies, and next maturity decision. |

## Runbook Contract

A runbook is an operational control, not a narrative troubleshooting page. Use the [Service Runbook Template](../delivery-templates/service-runbook-template.md). At minimum it must identify:

- Service, product, environment, owner, support tier, architecture decision, and affected dependencies.
- Trigger, observable symptoms, severity criteria, product and consumer impact, and safe diagnostic evidence.
- Preconditions, required authority, segregation of duties, step-up access, and actions that are prohibited.
- Containment, recovery, rollback, continuity, communication, and escalation steps.
- Separate **system recovery** and **data-product recovery** checks for quality, freshness, lineage, access, backlog, and consumers.
- Telemetry, incident, change, release, contract, and correlation identifiers retained as evidence.
- Test cadence, last exercise, known limitations, review owner, version, and expiry.

## Runbook and Runway

| Concept | Scope | Time Horizon | Completion Test |
| --- | --- | --- | --- |
| **Runbook** | One service, product, condition, or operational procedure. | Minutes to hours during response; reviewed throughout service life. | Operators can execute it and prove safe recovery. |
| **Runway** | Enterprise capability adoption across services and domains. | Quarters and maturity phases. | Phase exit evidence operates with real services, products, and consumers. |

The runway may fund creation and testing of runbooks. A runbook does not replace the runway, and a runway milestone does not prove operational readiness until the relevant runbooks are exercised.

## Review Rule

A production-readiness review is incomplete when any link in the chain is missing. Architecture without a service owner is aspirational; a service without a playbook is hard to adopt; a service without an exercised runbook is not operable; and a claimed runway phase without evidence is not mature.

<div class="read-next"><strong>Next:</strong> select a service above, verify its traceability record, and complete the Service Runbook Template for each material failure or recovery condition.</div>

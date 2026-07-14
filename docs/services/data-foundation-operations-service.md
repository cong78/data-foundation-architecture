# Data Foundation Operations Service

<div class="decision-brief"><div><small>Use when</small><strong>Designing support, response, change, or improvement across services.</strong></div><div><small>Decision</small><strong>Which operational workflow and authority applies?</strong></div><div><small>Owner</small><strong>Foundation operations and service owner.</strong></div><div><small>Output</small><strong>Owned response, recovery, communication, and learning.</strong></div></div>

## Definition

The Data Foundation Operations Service coordinates support, service management, incident response, problem elimination, change, release readiness, reliability, and operational improvement across all data foundation services.

It turns observable conditions and user-reported needs into accountable action. The [Data Observability Service](data-observability-service.md) detects and explains health; this service coordinates response, recovery, communication, and learning.

## Position in the Foundation

This is a **cross-cutting service**, not another stage in the source-to-product flow. It supports the portal, ingestion, product creation, consumption, sharing, Platform Enablement, observability, AI assistant, and their shared platform dependencies.

<div class="standards-map reference-map" role="img" aria-label="Data Foundation Operations Service connecting engagement and observability to coordinated response">
  <div class="standards-map-head" aria-hidden="true">
    <span>Operational trigger</span><i></i><span>Operations capability</span><i></i><span>Service outcome</span>
  </div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Engage</small><strong>Support and service request</strong><p>User need, question, operational request, complaint, or planned engagement.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Data Service Portal</strong><strong>Intake and routing</strong><strong>Status communication</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Owned response</strong><p>Correct service, priority, owner, target, status, and resolution path.</p></div>
  </section>
  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Respond</small><strong>Health and risk signal</strong><p>Alert, SLO breach, failed change, product impact, security event, or dependency failure.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Incident and problem</strong><strong>Change and release</strong><strong>Reliability and continuity</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Controlled recovery</strong><p>Restored service, validated product health, stakeholder communication, and retained evidence.</p></div>
  </section>
  <section class="standards-map-lane lane-access">
    <div class="standards-map-cell"><small>Improve</small><strong>Operational evidence</strong><p>Incidents, changes, support demand, SLOs, cost, risk, recurring failure, and feedback.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Post-incident learning</strong><strong>Problem backlog</strong><strong>Service improvement</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Operational excellence</strong><p>Less toil, safer change, faster recovery, stronger reliability, and better service experience.</p></div>
  </section>
</div>

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Service registry, ownership, support tiers, operational SLOs, escalation routes, and readiness reviews. | Replacing the Data Service Portal, observability platform, delivery pipelines, or enterprise service-management platform. |
| Support intake, engagement, triage, assignment, status, communication, knowledge, and service feedback. | Owning product semantics, quality acceptance, business priority, or domain product decisions. |
| Incident command, impact coordination, recovery validation, communication, and post-incident review. | Detecting and storing telemetry that belongs to the Data Observability Service. |
| Problem management, recurring-failure analysis, reliability backlog, and improvement tracking. | Performing engineering remediation on behalf of accountable service or product teams. |
| Risk-based change, release coordination, maintenance windows, dependency checks, rollback readiness, and change evidence. | Replacing product CI/CD, workload deployment, contract compatibility, security, or go-live controls. |
| Continuity, recovery exercises, capacity, error budgets, operational risk, and reliability reporting. | Replacing enterprise security incident response, business continuity governance, or risk acceptance authority. |

## Operating Objects and Authority

| Object | Authoritative owner | Operations-service responsibility |
| --- | --- | --- |
| Service record | Service owner and service-management registry | Ensure owner, support, SLO, dependencies, criticality, escalation, continuity, and lifecycle are complete. |
| Health signal | Observability platform | Correlate signal to service, product, release, change, dependency, and affected consumers. |
| Incident record | Operations workflow system | Own severity, commander, timeline, impact, communication, actions, recovery, and closure evidence. |
| Problem record | Operations workflow system | Track root cause, recurring patterns, known error, workaround, remediation owner, risk, and due date. |
| Change record | Operations workflow system | Record scope, risk, dependencies, approval, window, validation, rollback, outcome, and related release. |
| Product release | Product creation and deployment systems | Link release evidence and runtime state; do not duplicate artifact or deployment authority. |
| Product health | Observability and product-management systems | Validate recovery against contract, SLO, quality, freshness, and consumer-impact evidence. |
| Improvement item | Accountable service or product backlog | Track commitment and outcome without replacing team delivery ownership. |

The portal presents operational status and journeys but does not become the authoritative incident, change, telemetry, or release store.

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Service management | Service portfolio and readiness | Every production service has an owner, criticality, support tier, SLO, dependencies, consumers, continuity target, runbook, and readiness evidence. |
| Engagement | Support and service request | One intake path routes user needs by service, product, impact, and urgency and exposes owner, target, status, knowledge, and resolution. |
| Response | Incident management | Severity, command, product and consumer impact, containment, recovery, communication, validation, and timeline remain coordinated in one record. |
| Learning | Problem management | Recurring failure and systemic weakness become known errors, root-cause evidence, prioritized remediation, and measured recurrence reduction. |
| Change | Change management | Standard, normal, and emergency changes receive proportionate risk, dependency, approval, communication, validation, rollback, and outcome controls. |
| Release | Release coordination | Product and platform releases are linked to readiness, change, dependencies, maintenance windows, consumer impact, validation, and rollback. |
| Reliability | Reliability and continuity | SLOs, error budgets, capacity, resilience, recovery exercises, continuity, toil, automation, and operational risk guide investment. |
| Improvement | Operational excellence | Incident, change, support, reliability, cost, risk, and feedback evidence drives owned actions and verifies improved outcomes. |

## Incident Flow

| Stage | Required outcome | Minimum evidence |
| --- | --- | --- |
| Detect or report | One correlated operational record is created without duplicate alert storms. | Trigger, observation time, service, product, environment, correlation ids. |
| Triage | Severity, scope, affected products and consumers, owner, and communication route are established. | Impact assessment, commander, responders, target and escalation. |
| Contain | Harm and propagation are limited while evidence is preserved. | Decision log, access or release action, workaround and risk. |
| Recover | Service behavior and product trust are restored. | Runtime health, quality, freshness, access, backlog and dependency checks. |
| Communicate | Stakeholders receive audience-appropriate, time-stamped status. | Updates, current impact, next update, recovery confirmation. |
| Learn | Causes, contributing conditions, control gaps, and improvements are recorded without blame. | Review, problem record, owners, due dates and recurrence measures. |

An incident is not closed merely because a job is running. Recovery must be validated at both **system** and **data-product** levels, including affected consumer experience.

## Change and Release Control

| Change class | Default path | Required control |
| --- | --- | --- |
| Standard | Pre-authorized, repeatable, automated path. | Tested procedure, bounded scope, telemetry, validation, rollback, periodic review. |
| Normal | Risk-based review before execution. | Impact and dependency analysis, owner approval, window, communication, validation and rollback. |
| Emergency | Expedited authority during active risk or incident. | Named authority, minimum safe evidence, command linkage, enhanced monitoring and retrospective review. |

Change control must be proportional. It should automate low-risk repeatable change and concentrate human review on risk, dependencies, consumer impact, irreversibility, and uncertainty.

Data Product Creation Contract approval, product go-live, and operational change approval remain separate decisions. A release may require all three, but none substitutes for another.

## Integration Model

| Integration | Information exchanged |
| --- | --- |
| Data Service Portal | Support intake, incident status, planned change, maintenance, service health, knowledge, feedback, and task progress. |
| Data Observability Service | Alerts, SLO breaches, traces, logs, metrics, product health, impacted consumers, recovery evidence, and incident correlation ids. |
| Catalog and lineage | Service, product, owner, dependency, source, port, consumer, and impact relationships. |
| Product creation and CI/CD | Release identity, test evidence, deployment status, change reference, approval, rollback target, and outcome. |
| Identity and policy | Responder authority, emergency access, separation of duties, approval and audit evidence. |
| Enterprise service management | Incident, problem, change, request, knowledge, communication, service record, and enterprise escalation. |
| Security and continuity | Security-event handoff, crisis escalation, continuity invocation, recovery objectives, and retained assurance evidence. |
| Platform Enablement | Resource health, provisioning and change receipts, contract or policy drift, retention and expiry actions, recovery bindings, and deprovisioning evidence. |

## Measures

Measure outcomes by service criticality and support tier; avoid one target for every service.

- SLO attainment and error-budget consumption.
- Mean time to acknowledge, engage, contain, recover, and validate product health.
- Incident recurrence and percentage linked to a managed problem.
- Change success, failed-change recovery, emergency-change rate, and rollback effectiveness.
- Support response, resolution, reassignment, reopen, backlog age, knowledge use, and consumer satisfaction.
- Continuity and recovery exercise success against agreed objectives.
- Operational toil removed, automation coverage, action completion, and measured reliability improvement.

## Controls

- Every production service has an owner, support tier, operational SLO, escalation path, dependency map, runbook, continuity target, and telemetry coverage.
- Every incident, problem, change, and release uses stable service, product, contract, release, environment, identity, and correlation identifiers where applicable.
- Major incidents have one commander, one authoritative timeline, explicit communication ownership, and system-plus-product recovery validation.
- Emergency access and emergency change are time-bound, least-privilege, auditable, and reviewed after use.
- Changes cannot silently bypass contract, security, product go-live, deployment, or segregation-of-duties controls.
- Improvement actions have accountable owners, due dates, risk, status, and outcome measures.

## Done Criteria

- The service portfolio and ownership model cover every production foundation service.
- Portal support and operational journeys call authoritative workflow APIs and expose current status.
- Observability signals create or enrich operational records with deduplication and product-impact context.
- Incident, problem, change, release, support, continuity, and improvement workflows are documented and exercised.
- Service and product recovery can be proven end to end from telemetry through affected consumers.
- Operations evidence is retained, searchable, permission-filtered, and available for service reviews, audit, maturity assessment, and improvement planning.

<div class="read-next">
  <strong>Next:</strong> trace the service through the <a href="/foundation/architecture-service-operations-map/">Architecture to Operations Map</a>, then create and exercise the applicable <a href="/delivery-templates/service-runbook-template/">Service Runbook</a>.
</div>

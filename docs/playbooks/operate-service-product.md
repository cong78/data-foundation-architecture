# Operate a Service or Product

<div class="decision-brief"><div><small>Use when</small><strong>A live capability needs support, change, recovery, or improvement.</strong></div><div><small>Decision</small><strong>Respond, restore, change, improve, deprecate, or retire.</strong></div><div><small>Owner</small><strong>Service or product owner with operations.</strong></div><div><small>Output</small><strong>Current health and accountable operational evidence.</strong></div></div>

## Operating Loop

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Observability:** correlate service, runtime, product, contract, release, consumer, cost, and SLO signals. | Current system and product health. |
| 2 | **Operations:** receive alert or support request, deduplicate, assess impact and severity, assign owner, and communicate status. | Operational record and timeline. |
| 3 | **Service or product owner:** contain risk, restore service, validate quality and consumer experience, and preserve evidence. | Recovery and validation record. |
| 4 | **Problem owner:** analyze recurring or material failures and fund systemic remediation. | Problem record and improvement backlog. |
| 5 | **Change owner:** classify risk, check dependencies, approve, schedule, communicate, validate, and roll back when needed. | Change and release outcome. |
| 6 | **Service review:** assess SLOs, error budget, quality, usage, cost, support demand, incidents, change success, value, and risk. | Review decisions and actions. |
| 7 | **Owner:** improve, consolidate, deprecate, or retire with consumer migration and evidence retention. | Updated lifecycle and portfolio state. |

## Recovery Rule

An incident is not resolved because infrastructure is running. Closure requires system health, product quality, freshness, access, backlog, dependency, and affected-consumer validation appropriate to impact.

## Done Criteria

- Service and product status, owner, next action, and observation time are visible.
- Incidents, problems, changes, releases, support, and improvements use stable correlation identifiers.
- Recovery, rollback, continuity, expiry, revocation, deprecation, and retirement are exercised according to criticality.
- Reviews lead to funded actions with owners, dates, and measurable outcomes.

Authoritative inputs: [Architecture to Operations Map](../foundation/architecture-service-operations-map.md), [Data Foundation Operations Service](../services/data-foundation-operations-service.md), [Data Observability Service](../services/data-observability-service.md), [Operating Model](../governance/operating-model.md), [Service Runbook Template](../delivery-templates/service-runbook-template.md), and [Runway](../runway.md).

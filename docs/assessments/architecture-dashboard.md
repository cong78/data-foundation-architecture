# Architecture Dashboard

<div class="decision-brief"><div><small>Use when</small><strong>Reviewing current architecture and implementation evidence.</strong></div><div><small>Decision</small><strong>Which verified gap requires action next?</strong></div><div><small>Owner</small><strong>Foundation sponsor and capability owners.</strong></div><div><small>Output</small><strong>Prioritized improvement with owner, evidence, and review date.</strong></div></div>

This repository defines the dashboard structure but does not bundle organization-specific implementation results. A missing observation remains **Not assessed**; it is not converted into an illustrative score.

## Evidence View

| Area | Decision question | Minimum evidence | Status source |
| --- | --- | --- | --- |
| Direction and ownership | Are scope, service ownership, domain accountability, and decision rights current? | Approved scope, owners, ADRs, risks, exceptions, and review records. | Governance and architecture records. |
| Foundation services | Are service boundaries implemented, supported, measurable, and reusable? | Service records, interfaces, SLOs, support, dependencies, incidents, changes, and usage. | Service catalog and operations platform. |
| Products and contracts | Are live products owned, contracted, tested, observable, supported, and used? | Product records, three contract types, go-live results, health, consumers, changes, and lifecycle decisions. | Portal, contract registry, catalog, and product telemetry. |
| Access and security | Are named users, workloads, delegated actors, and recipients governed at service and data boundaries? | Identity bindings, policy decisions, entitlements, obligations, expiry, deny tests, and revocation. | Identity, policy, Unity Catalog, and audit authorities. |
| Observability and operations | Can owners detect, diagnose, recover, validate, and improve service and product behavior? | OTel signals, product telemetry, SLOs, alerts, incidents, runbooks, recovery exercises, and improvements. | Grafana Cloud, Databricks, Unity Catalog, and operations records. |
| Interoperability and AI | Are interfaces portable and AI uses purpose-bound, reproducible, evaluated, and traceable? | Conformance tests, export and import results, AI-use terms, context versions, evaluations, and traces. | CI, interoperability records, AI gateway, and telemetry authorities. |

## Review Record

Use one row per measured scope and evidence window:

| Scope | Area | Result | Evidence time | Confidence | Gap or decision | Owner | Review date |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Pass / Fail / Not assessed |  | Automated / Sampled / Attested / Missing |  |  |  |

## Interpretation Rules

- A pass requires authoritative evidence for the stated scope and observation time.
- A failed mandatory gate remains visible and cannot be averaged into a percentage.
- Stale, inaccessible, sampled without scope, or unsupported claims are marked `Not assessed`.
- Design evidence does not prove implementation or operational behavior.
- Drill-through retains the source record, accountable owner, exception, and remediation.
- Use trends to guide improvement; do not rank domains without comparable scope and evidence confidence.

## Apply the Assessment

Use the [Data Foundation Maturity Assessment](data-foundation-maturity-assessment.md) for the common dimensions and scoring interpretation. Use the [Architecture to Operations Map](../foundation/architecture-service-operations-map.md) to connect a gap to its owning service, standard, playbook, runbook, evidence source, and runway phase.

<div class="read-next"><strong>Next:</strong> define one bounded review scope, collect authoritative evidence, and record only verified results.</div>

# Service Runbook Template

<div class="decision-brief"><div><small>Use when</small><strong>Preparing a service or product for support and recovery.</strong></div><div><small>Decision</small><strong>Can an authorized operator diagnose and recover this condition safely?</strong></div><div><small>Owner</small><strong>Service or product owner with operations.</strong></div><div><small>Output</small><strong>Versioned, tested procedure with retained evidence.</strong></div></div>

Create one runbook per material operating condition. Keep commands and vendor-specific steps in controlled implementation attachments when needed; keep identity, authority, validation, evidence, and recovery logic portable.

## 1. Runbook Identity

| Field | Value |
| --- | --- |
| Runbook id and title |  |
| Service and product ids |  |
| Condition or failure mode |  |
| Environment and region |  |
| Owner and support team |  |
| Support tier and severity ceiling |  |
| Version, status, approval, and expiry |  |
| Last review and exercise |  |

## 2. Architecture and Service Traceability

| Trace | Reference |
| --- | --- |
| Architecture view and decisions |  |
| Service definition and capabilities |  |
| Product and contract versions |  |
| Applicable standards and controls |  |
| Dependencies and affected consumers |  |
| Related playbook and workflow |  |
| SLO, recovery objective, and continuity tier |  |

Use [Architecture to Delivery](../foundation/architecture-to-delivery.md) to complete this section.

## 3. Trigger and Impact

- **Trigger:** alert, support report, failed change, SLO breach, product-health condition, or security handoff.
- **Observable symptoms:** what is measured, where, and at which observation time.
- **Impact:** affected service operations, products, contracts, consumers, data quality, freshness, access, and regulatory obligations.
- **Severity:** objective criteria and who may change severity.
- **False-positive checks:** safe checks that do not alter evidence or state.

## 4. Authority and Safety

| Control | Requirement |
| --- | --- |
| Required role and identity |  |
| Approval or incident-command authority |  |
| Step-up or emergency access |  |
| Segregation of duties |  |
| Sensitive evidence handling |  |
| Prohibited or irreversible actions |  |
| Maximum action scope and timeout |  |

Stop and escalate when identity, authority, target, impact, evidence, or rollback state is uncertain.

## 5. Diagnose

| Step | Check | Expected Evidence | If Not Met |
| ---: | --- | --- | --- |
| 1 | Confirm service, product, environment, release, and correlation ids. |  |  |
| 2 | Inspect system health, dependencies, capacity, and recent changes. |  |  |
| 3 | Inspect product quality, freshness, lineage, backlog, and access. |  |  |
| 4 | Identify affected consumers, Data Product Consumption Contracts, and downstream products. |  |  |
| 5 | Establish likely condition, confidence, and next safe action. |  |  |

## 6. Contain and Recover

| Step | Authorized Action | Expected Result | Rollback or Escalation |
| ---: | --- | --- | --- |
| 1 | Limit impact while preserving evidence. |  |  |
| 2 | Stabilize dependencies and stop unsafe propagation. |  |  |
| 3 | Restore service or activate the approved continuity path. |  |  |
| 4 | Replay, reconcile, or remediate product data when approved. |  |  |
| 5 | Restore normal routing, access, schedules, and monitoring. |  |  |

## 7. Validate Recovery

Do not close because infrastructure is running. Record both validation groups.

| Validation | Required Proof | Result |
| --- | --- | --- |
| System | Availability, latency, errors, saturation, dependencies, jobs, queues, and telemetry are within target. |  |
| Data product | Contract, schema, quality, freshness, volume, lineage, access, backlog, and reconciliation pass. |  |
| Consumer | Representative access works and affected consumers confirm or observe recovery. |  |
| Control | Policy, masking, entitlement, audit, retention, and sharing obligations remain enforced. |  |
| Stability | Health remains within target for the defined observation window. |  |

## 8. Communicate and Escalate

| Audience or Authority | Trigger | Channel | Owner | Required Message |
| --- | --- | --- | --- | --- |
| Operations and responders |  |  |  |  |
| Service and product owners |  |  |  |  |
| Consumers and recipients |  |  |  |  |
| Security, privacy, legal, or continuity |  |  |  |  |
| Leadership or major-incident forum |  |  |  |  |

## 9. Evidence and Closure

- Incident, problem, change, release, and support record ids.
- Service, product, contract, workload, release, environment, consumer, and correlation ids.
- Dashboards, queries, traces, logs, metrics, lineage, product-health results, and decision records.
- Actions executed, actor, authority, timestamp, target, result, exception, and rollback evidence.
- Recovery validation, remaining risk, follow-up owner, due date, and consumer communication.

## 10. Exercise and Improve

| Review Item | Result |
| --- | --- |
| Scenario and exercise date |  |
| Participants and authority tested |  |
| Recovery objective achieved |  |
| System and product validation passed |  |
| Missing access, telemetry, dependency, or instruction |  |
| Manual toil and automation candidate |  |
| Improvement owner and due date |  |
| Next review or exercise |  |

**Done:** an authorized person who did not write the runbook can execute it in a controlled exercise, recover both service and product trust, communicate appropriately, and retrieve the evidence afterward.

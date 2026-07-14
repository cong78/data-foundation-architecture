# Access Control Standard

<div class="decision-brief"><div><small>Use when</small><strong>Authorizing a service operation or product-data use.</strong></div><div><small>Decision</small><strong>Who may do what, for which purpose, under which obligations?</strong></div><div><small>Owner</small><strong>Policy owner and enforcement owner.</strong></div><div><small>Output</small><strong>Enforceable decision, entitlement, obligations, and audit.</strong></div></div>

This standard defines mandatory identity, service authorization, data authorization, entitlement, and evidence requirements for the data foundation.

## Identity Requirements

- Named users authenticate through enterprise identity with MFA and step-up support.
- Every application, service, pipeline, job, agent, model, and external integration has a unique registered workload identity.
- Credentials are short-lived and issued at runtime; embedded keys and shared system accounts are prohibited.
- Delegated calls preserve both the named-user subject and the workload or agent actor.
- Identity attributes include owner, type, team, trust domain, environment, lifecycle state, and assurance level.

## Authorization Requirements

Every request must pass two independent checks:

| Check | Mandatory Inputs | Enforcement |
| --- | --- | --- |
| Service authorization | Actor, subject, operation, service, environment, delegated scope, risk, approval state. | Gateway, service, workflow, or skill boundary. |
| Data authorization | Actor, subject, data action, product, interface, purpose, classification, Data Product Consumption Contract, environment, policy context. | Query, API, event, file, feature, retrieval, semantic, or context boundary. |

The effective decision is the most restrictive result. A service permit cannot override a data deny.

## Mandatory Policy Model

Policies must support:

- Role-based capability assignment for basic service operations.
- Attribute-based restrictions for identity, team, product, classification, environment, region, and trust domain.
- Purpose-based controls for BI, operational use, sharing, training, retrieval, grounding, and evaluation.
- Relationship-based checks where ownership, stewardship, Data Product Consumption Contract, or consumer subscription matters.
- Explicit obligations including row filter, field mask, tokenization, aggregation, output limit, watermark, logging, retention, and expiry.

## Service Enforcement

- Every externally or internally callable operation has a stable authorization action id.
- Administrative, approval, deployment, sharing, revocation, and irreversible actions require explicit scopes and appropriate step-up or separation of duties.
- Rate, concurrency, budget, environment, and task limits are enforced for system and agent identities.
- Services validate authorization at execution time, not only when the request or workflow was created.
- Service-to-service calls authenticate each hop and do not inherit unrestricted upstream privileges.

## Data Enforcement

- Every product port declares supported actions, classifications, purposes, policy reference, and enforcement point.
- Unified access adapters preserve actor and subject, enforce both service and data decisions, apply obligations, and emit decision evidence before releasing results.
- Row, column, record, field, event, file, retrieval, and output obligations are enforced as close as possible to data release.
- Raw and source-aligned access is restricted to approved engineering and operational purposes.
- Export, bulk download, external sharing, AI training, and sensitive retrieval require explicit purpose and enhanced controls.
- Caches, semantic models, extracts, indexes, features, and embeddings preserve source policy and revocation behavior.

## Entitlement Requirements

Every entitlement records:

| Field | Requirement |
| --- | --- |
| Entitlement id | Stable identifier. |
| Subject and actor | Receiving identity and delegated actor where applicable. |
| Service and data scope | Exact operations, products, ports, fields, rows, or recipient package. |
| Purpose | Approved use with linked use case and Data Product Consumption Contract. |
| Environment | Development, test, production, or external trust domain. |
| Owner and approvers | Accountable grant owner and required decision records. |
| Validity | Start, expiry, review schedule, and maximum duration. |
| Policy | Policy id and version that authorized the grant. |
| Enforcement | Expected policy enforcement points and provisioning status. |
| Revocation | Trigger, method, target recovery time, and verification result. |

## Decision Evidence

Every allow, deny, step-up, or obligation decision records:

- Timestamp, decision id, policy id and version.
- Actor, subject, identity type, assurance, and delegated scope.
- Service, operation, product, interface, data action, and environment.
- Purpose, Data Product Consumption Contract, classification, and relevant attributes.
- Result and obligations without exposing sensitive policy internals.
- Enforcement point, request or task correlation id, and outcome.

## Minimum Tests

- Named-user allow and deny by role, attribute, purpose, and product.
- Workload allow and deny by identity, environment, purpose, and port.
- Delegated actor cannot exceed the named user's authority or its own registered scope.
- Service permit plus data deny results in no data release.
- Mask, row filter, aggregation, output limit, and expiry obligations are enforced.
- Policy change, role loss, product change, incident, and expiry trigger review or revocation.
- Revoked access fails at every declared enforcement point within the required recovery time.
- Audit evidence correlates decision, enforcement, service operation, data use, and outcome.

## Minimum Done Criteria

- No shared human or system identities.
- No long-lived embedded credentials.
- No service or product interface without an authorization action and enforcement point.
- No sensitive data grant without purpose, expiry, owner, and revocation.
- No delegated or agent action without actor and subject traceability.
- No authorization design is complete until allow, deny, obligation, expiry, and revocation paths are tested.

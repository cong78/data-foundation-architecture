# Platform Governance Design

<div class="decision-brief"><div><small>Use when</small><strong>Placing decision rights, controls, enforcement, and assurance across the data foundation.</strong></div><div><small>Decision</small><strong>Who decides, which rule applies, where is it enforced, and what proves the outcome?</strong></div><div><small>Owner</small><strong>Platform governance owner with product, domain, service, security, privacy, and architecture authorities.</strong></div><div><small>Output</small><strong>Authority map, control placement, decision flow, exception path, and evidence.</strong></div></div>

Platform governance is the architecture that makes foundation decisions accountable, enforceable, and observable. It is not a separate approval layer around delivery. It connects ownership and policy to the contracts, services, enforcement points, telemetry, and evidence used throughout the product and service lifecycle.

## Design Reasoning

<div class="design-reasoning"><div><small>Context</small><p>Ownership and control decisions are distributed across products, domains, services, and enterprise authorities.</p></div><div><small>Forces</small><p>Delivery speed and local accountability must coexist with consistent policy, assurance, and explainability.</p></div><div><small>Decision</small><p>Keep decision authority explicit, express rules as policy, enforce them at service boundaries, and retain evidence.</p></div><div><small>Consequences</small><p>Teams gain clear authority but must synchronize decisions, exceptions, policy versions, and control receipts.</p></div><div><small>Verification</small><p>Trace every material rule from owner and policy through enforcement to current assurance evidence.</p></div></div>

## Governance Model at a Glance

<div class="standards-map" role="img" aria-label="Platform governance from declared intent through enforcement to assurance">
  <div class="standards-map-head" aria-hidden="true"><span>Governance responsibility</span><i></i><span>Architecture mechanism</span><i></i><span>Outcome</span></div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Declare</small><strong>Ownership · Purpose · Meaning · Risk</strong><p>State who is accountable, what is intended, and which obligations apply.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../data-contract-design/"><strong>Contracts and product lifecycle</strong></a><a href="../../standards/"><strong>Standards and policy</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Unambiguous control intent</strong><p>Versioned owners, rules, decisions, conditions, and change obligations.</p></div>
  </section>
  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Enforce</small><strong>Identity · Access · Quality · Lifecycle</strong><p>Apply the decision where data, services, products, and agent actions cross a boundary.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../platform-enablement-design/"><strong>Platform enablement</strong></a><a href="../../services/"><strong>Foundation services</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Policy in execution</strong><p>Purpose-bound access, quality gates, retention, sharing, and bounded automation.</p></div>
  </section>
  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Assure</small><strong>Evidence · Health · Exceptions · Improvement</strong><p>Compare actual behavior with the published promise and resolve gaps.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../../services/data-observability-service/"><strong>Data Observability</strong></a><a href="../../services/data-foundation-operations-service/"><strong>Foundation Operations</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Observable accountability</strong><p>Current control state, incidents, decisions, remediation, and retained proof.</p></div>
  </section>
</div>

**Governance rule:** declare control intent once, enforce it through the owning service at the real boundary, and retain evidence from the authoritative decision and runtime. A committee, catalog entry, or dashboard alone does not enforce governance.

## Governance Responsibilities

| Responsibility | Architecture outcome | Primary mechanism | Minimum evidence |
| --- | --- | --- | --- |
| Ownership and accountability | Every domain, product, contract, service, policy, and exception has one active accountable owner. | Stable identifiers, ownership registry, lifecycle state, escalation, and review cadence. | Owner, decision rights, acceptance, review date, and escalation route. |
| Product and portfolio governance | Products have justified boundaries, measurable value, controlled duplication, support, and retirement. | [Data Product Design](data-product-design.md), portfolio views, go-live gates, usage and cost reviews. | Product decision, health, adoption, duplication check, value review, and retirement action. |
| Contract and change governance | Producer and consumer promises are explicit, compatible, versioned, and communicated. | [Data Contract Design](data-contract-design.md), compatibility policy, workflow, and impact analysis. | Approved version, validation result, affected consumers, migration, and release record. |
| Meaning, quality, and lineage | Data meaning and fitness remain attributable and understandable across product boundaries. | Semantic context, quality rules, lineage, stewardship, and product telemetry. | Context version, rule results, lineage, limitations, breach, and remediation owner. |
| Identity, access, and security | Human, workload, model, and agent access is purpose-bound, least-privileged, expiring, observable, and revocable. | [Unified Access Design](unified-access-design.md), classification, policy decisions, obligations, and enforcement points. | Actor and subject, purpose, policy result, entitlement, access event, and revocation. |
| Privacy, retention, and compliance | Sensitive data is minimized, protected, retained, located, shared, and deleted according to obligations. | Classification, masking, residency, retention schedules, sharing controls, and audit integration. | Approval, applied obligation, retention or deletion receipt, recipient evidence, and audit trail. |
| AI and agent governance | AI use and agent execution remain bounded by approved purpose, product versions, contracts, skills, models, evaluation, and autonomy. | [Agentic Data Service Design](agentic-data-foundation.md), declarative execution envelope, model and skill profiles, and step-up approval. | Delegation chain, contract versions, policy decision, evaluation, action receipt, cost, and suspension state. |
| Service reliability and change | Foundation services remain supported, observable, recoverable, and safely changeable. | Service definitions, SLOs, telemetry, change authority, runbooks, and operations workflows. | Health, incident, change, recovery, continuity exercise, and improvement decision. |

## Authority and Accountability

Governance separates **decision authority** from **execution responsibility**. The accountable owner approves the intent and accepts the outcome; foundation services execute and evidence the approved decision.

| Decision boundary | Accountable authority | Execution responsibility |
| --- | --- | --- |
| Foundation architecture and standards | Architecture and applicable policy authorities. | Service and capability owners implement conforming designs and controls. |
| Source delivery and change | Source-system owner. | Data Ingestion Service validates delivery and publishes the source-aligned output. |
| Source-aligned product | Data Foundation Platform Team. | Ingestion and Platform Enablement Services operate the centrally managed lifecycle. |
| Aggregate or consumer-aligned product | Owning domain product owner with steward and technical owner. | Domain team uses the Data Product Creation Service and shared controls. |
| Consumer purpose and correct use | Consumer owner; security, privacy, or data owner approval where policy requires it. | Data Consumption or Sharing Service authorizes, serves, records, and revokes access. |
| Service reliability and release | Foundation service owner. | Service team executes; Foundation Operations coordinates cross-service support, incidents, changes, and recovery. |
| Agent action | User or workload owner for intent; service owner for delegated service behavior. | Data Service AI Assistant coordinates; the specialist agent and deterministic service execute within contract and policy. |

The Data Service AI Assistant may interpret, plan, route, and summarize work. It cannot widen authority, approve its own exception, or replace the accountable service decision.

## Governance Decision Flow

Every governed action follows one traceable sequence.

| Step | Required action | Failure outcome |
| --- | --- | --- |
| 1. Declare intent | Identify actor, subject, purpose, target product or service, action, environment, and requested duration. | Reject incomplete or ambiguous intent. |
| 2. Resolve authority | Resolve owners, contract versions, lifecycle state, classification, policy, and applicable standards. | Stop when authority is missing, expired, inconsistent, or unverifiable. |
| 3. Decide | Evaluate the request and produce allow, deny, defer, or exception-required with obligations. | Deny by default when no authoritative decision can be produced. |
| 4. Enforce | The owning service applies the decision at the service, data, product-port, workflow, or agent-tool boundary. | Do not rely on documentation or downstream detection as enforcement. |
| 5. Evidence | Record decision id, inputs, obligations, enforcement result, actor, time, versions, and correlation ids. | Treat an unevidenced action as non-conformant. |
| 6. Assure | Observe health and use, detect drift or breach, manage incidents and exceptions, and verify remediation. | Suspend or narrow affected activity until trust is restored. |

## Placement in the Architecture Blueprint

Platform governance is cross-cutting; it is not a seventh architecture plane.

| Plane | Governance responsibility |
| --- | --- |
| Experience | Capture intent, ownership, purpose, approvals, status, explanations, and evidence through the portal and assistant. |
| Control | Maintain contracts, product state, semantic authority, policy, workflow, gates, decisions, lineage, and quality rules. |
| Data | Enforce data-product boundaries, quality, retention, residency, sharing, and governed product-port behavior. |
| AI | Bind agents, skills, models, retrieval, context, memory, budgets, evaluations, approval, and suspension to declared authority. |
| Observability | Correlate decisions with system and product behavior, control drift, incidents, use, cost, and remediation. |
| Security | Authenticate identities and enforce service and data authorization, masking, purpose, entitlement, audit, and revocation. |

The [Platform Enablement Service](../services/platform-enablement-service.md) provides reusable policy, identity, contract, catalog, storage-lifecycle, integration, and evidence capabilities. Each lifecycle service remains accountable for applying those capabilities correctly at its own boundary.

## Governance Through the Lifecycle

| Lifecycle moment | Governance decision | Evidence needed to proceed |
| --- | --- | --- |
| Frame | Is the outcome in scope, valuable, owned, and assigned to the correct domain and service? | Purpose, boundary, owner, consumers, classification, and decision path. |
| Design | Are product, contract, context, access, quality, SLO, retention, and agentic controls complete? | Reviewed design, contract draft, policy mapping, risks, and test plan. |
| Go live | Is the exact product or service version fit, supported, secure, observable, and recoverable? | Passing gates, approvals, release, active telemetry, support, and rollback. |
| Operate | Does actual behavior meet contracts, policy, quality, SLOs, and expected value? | Health, access, usage, incidents, cost, exceptions, and review decisions. |
| Change | Is the change compatible, communicated, authorized, tested, and reversible? | Impact, compatibility, migration, approval, tests, release, and rollback. |
| Retire | Have consumers migrated and access, data, resources, contracts, and evidence reached consistent final states? | Migration, revocation, retention or deletion, catalog state, and archived decisions. |

## Forums and Exceptions

Automated rules and named owners should resolve routine decisions. Use a forum when policy conflicts, cross-domain impact, material risk, or an exception requires collective judgment.

| Forum | Reserved decision scope |
| --- | --- |
| Architecture authority | Cross-service architecture, standards interpretation, major design direction, and architecture exceptions. |
| Domain and product portfolio authority | Domain boundaries, product priority, duplication, ownership gaps, value, health, and retirement. |
| Security, privacy, and compliance authority | Sensitive use, external sharing, residency, legal obligations, high-risk AI use, and compensating controls. |
| Agentic AI authority | Autonomy class, privileged skills, model profiles, evaluation thresholds, safety incidents, suspension, and retirement. |

Every exception must identify the violated rule, reason, accountable risk owner, affected scope, compensating controls, evidence, expiry, review date, and remediation path. An exception never silently changes the published standard or grants broader agent authority.

## Design Completion Criteria

Platform governance design is complete when:

- Every material decision has one authoritative owner and one published source of control intent.
- Controls are mapped to named service and data enforcement points across all affected planes.
- Central source-aligned and federated domain-product accountabilities are explicit.
- Named-user, workload, model, and agent authority can be resolved, narrowed, revoked, and explained.
- Contracts, catalog projections, policies, runtime bindings, telemetry, and evidence reconcile to stable identifiers and versions.
- Go-live, change, exception, incident, and retirement decisions produce durable evidence.
- Governance gaps have an owner, risk decision, expiry, and measurable remediation.

<div class="read-next"><strong>Next:</strong> use the <a href="../platform-enablement-design/">Platform Enablement Design</a> to place reusable control capabilities, then verify mandatory rules in <a href="../../standards/">Standards</a>.</div>

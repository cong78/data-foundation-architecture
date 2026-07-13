# Data Contract Design

Data contracts are the executable control chain that carries trust from a source into every published data product and governed use. They define what a producer promises, what the platform enforces, and what evidence is required before and after product go-live.

Use the [Data Contract Standard](../standards/data-contract-standard.md) for mandatory fields, states, approvals, versioning, and test rules. This page explains where each contract belongs in the architecture and lifecycle.

## Core Model

Do not create one oversized contract for the whole data flow. Each producer accepts versioned input contracts and publishes one versioned contract for its own output. Purpose-specific contracts and agreements narrow that output promise without replacing it.

<div class="standards-map reference-map" role="img" aria-label="Contract chain from source delivery through product layers to governed use">
  <div class="standards-map-head" aria-hidden="true">
    <span>Input promise</span><i></i><span>Enforcement boundary</span><i></i><span>Output promise</span>
  </div>

  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Receive</small><strong>Source contract</strong><p>Delivery, schema, source meaning, cadence, and change obligations.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Ingestion and raw landing</strong><p>Validate receipt, provenance, classification, and quarantine. Raw has no product port.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Validated source-aligned</strong><p>Source-preserving product contract and central-to-federated handoff.</p></div>
  </section>

  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Compose</small><strong>Accepted input contracts</strong><p>Exact upstream products, versions, ports, quality, and freshness.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Aggregate product</strong><strong>Consumer-aligned product</strong><p>Both are reusable by design and owned by an accountable data domain.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Product contract</strong><p>Output schema, semantics, grain, quality, SLO, policy, ports, and compatibility.</p></div>
  </section>

  <section class="standards-map-lane lane-access">
    <div class="standards-map-cell"><small>Use</small><strong>Live product contract</strong><p>One canonical promise for the published product version.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Consumption contract</strong><strong>Sharing contract</strong><strong>AI-use contract</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Purpose-bound outcome</strong><p>Governed use by people, systems, recipients, agents, and models.</p></div>
  </section>
</div>

The chain can branch. An aggregate product may consume several source-aligned or aggregate products, while a consumer-aligned product may project any live upstream product for a declared purpose. Every output contract records the exact upstream product and contract versions used to produce it.

## Contracts by Product Layer

| Layer or boundary | Governing contract | Promise and enforcement | Accountable owner |
| --- | --- | --- | --- |
| Source delivery | **Source contract** | Delivery channel, schema, keys, source semantics, cadence, change notice, replay, and source obligations are checked during onboarding and receipt. | Source system owner; foundation platform enforces ingestion. |
| Raw source-aligned state | **Source contract clauses** | Envelope, identity, checksum, schema version, provenance, classification, and receipt controls are enforced. Failed records are quarantined. Raw is restricted and has no consumer-facing product contract. | Data Foundation Platform Team. |
| Validated source-aligned product | **Source-aligned product contract** | A product-contract profile promises a stable, source-preserving schema, keys, freshness, basic quality, limitations, lineage, and support boundary. It is the central-to-federated handoff. | Data Foundation Platform Team, with source owner obligations retained. |
| Aggregate product | **Product contract with upstream references** | Domain semantics, entity or composition rules, grain, metrics where applicable, reconciliation, restatement, and lineage to input contract versions are enforced. | Owning domain data team, steward, and metric owner where applicable. |
| Consumer-aligned product or view | **Product contract with purpose constraints** | Consumer, purpose, projection, minimization, interface, upstream versions, SLO, compatibility, and expiry are explicit. Repeated shared logic should be promoted to an aggregate product. | Serving or consuming domain data team. |
| Unified access port | **Consumption contract projection** | The stable table, SQL, API, event, file, feature, retrieval, semantic, or context interface is generated from and traceable to the product contract. Request and response behavior, policy, and obligations are enforced at access time. | Product owner and consumption platform owner. |
| External package | **Sharing contract plus sharing agreement** | Recipient, minimized scope, legal or approved purpose, delivery, retention, expiry, and revocation narrow a specific product-contract version. | Sharing owner and recipient owner. |
| AI use | **AI usage contract or clause plus consume agreement** | Retrieval, grounding, feature, training, or evaluation purpose; model or agent identity; snapshot; prohibited use; and evidence requirements are checked at access time. | Product owner and AI use-case owner. |

**Product contract** is the common contract type for every publishable data-product layer. “Source-aligned,” “aggregate,” and “consumer-aligned” are profiles of that type, not separate incompatible standards. Reusability is enforced through the common product-quality and go-live requirements rather than represented as another layer.

## Contract Composition Rule

Every data product has two contract perspectives:

| Perspective | Required content |
| --- | --- |
| Inputs accepted | Upstream product id and contract version, accepted port, compatibility range, required quality and freshness, and failure behavior. |
| Output promised | Product schema, semantics, grain, quality, freshness, policy, ports, compatibility, observability, owner, and support commitments. |

A transformation may strengthen, reshape, aggregate, or narrow an upstream promise, but it cannot silently weaken it. Any loss of fields, freshness, quality, lineage, permitted use, or semantic precision must be explicit in the output contract and assessed for consumer impact.

## Control Architecture

<div class="standards-map reference-map" role="img" aria-label="Contract control architecture from authoring through continuous operation">
  <div class="standards-map-head" aria-hidden="true">
    <span>Trigger</span><i></i><span>Control capability</span><i></i><span>Authoritative result</span>
  </div>

  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Define</small><strong>Portal · API · CLI · repository</strong><p>Author, compare, review, approve, and propose change.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Canonical ODCS artifact</strong><strong>Workflow and approval</strong><strong>Contract registry</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Versioned contract truth</strong><p>Immutable version, state, owner, product binding, and subscriptions.</p></div>
  </section>

  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Prove</small><strong>Contract candidate</strong><p>Product change with exact input and output promises.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Contract compiler</strong><strong>CI and compatibility tests</strong><strong>Product go-live gate</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Approved release evidence</strong><p>Generated controls, passing tests, approvals, and matching runtime bindings.</p></div>
  </section>

  <section class="standards-map-lane lane-access">
    <div class="standards-map-cell"><small>Enforce</small><strong>Live product and access request</strong><p>Product, contract, actor, purpose, port, and environment.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Ingestion and product runtime</strong><strong>Unified access and sharing</strong><strong>AI-use enforcement</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Runtime decision</strong><p>Accept, quarantine, publish, deny, mask, degrade, or revoke.</p></div>
  </section>

  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Improve</small><strong>Runtime and lifecycle events</strong><p>Conformance, breach, usage, incident, and change signals.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Observability</strong><strong>Lineage and impact</strong><strong>Consumer notification</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Measured contract health</strong><p>Affected consumers, owner action, remediation, and next-version input.</p></div>
  </section>
</div>

| Component | Architectural responsibility |
| --- | --- |
| Canonical contract repository | Stores immutable, reviewable contract versions in a portable format. |
| Contract registry | Resolves current and historical versions, lifecycle state, owners, subscriptions, and product bindings. |
| Portal and workflow | Supports authoring, review, exceptions, approvals, notifications, and evidence without becoming a second contract authority. |
| Contract compiler | Generates platform schemas, validation rules, test packs, policy inputs, and interface definitions from the canonical artifact. |
| CI/CD gates | Test syntax, schema and semantic compatibility, quality rules, policy, lineage, and affected consumers before deployment. |
| Runtime enforcement | Applies compiled controls at ingestion, transformation, publication, unified access, sharing, and AI-use boundaries. |
| Catalog, lineage, and impact | Connect products, ports, contract versions, upstream dependencies, consumers, agreements, and affected changes. |
| Observability | Records conformance, freshness, quality, access, use, and breach evidence against product and contract versions. |

The catalog discovers and relates contracts; the contract registry owns contract versions and state. A technology may implement both capabilities, but their authority remains explicit.

## Lifecycle Enforcement

| Product lifecycle stage | Contract action | Automated enforcement | Required evidence |
| --- | --- | --- | --- |
| Discover | Identify producer, intended consumers, source dependencies, and likely contract profile. | Duplicate and dependency checks may advise but do not block exploration. | Product intent and accountable owner. |
| Design | Draft the output contract and pin expected input contracts. | Required fields, identifiers, classification, semantics, and policy linting. | Draft contract, input references, review route. |
| Build | Implement transformations and ports from the approved contract candidate. | Schema, semantic, quality, lineage, policy, compatibility, and interface tests run in CI. | Test results and generated artifact versions. |
| Approve go-live | Approve and publish an immutable contract version. | Go-live is blocked unless the contract is approved, all critical tests pass, runtime bindings match, and exceptions are valid. | Approval, compatibility decision, lineage, policy, quality, and observability evidence. |
| Operate | Continuously compare delivery and product behavior with the published contract. | Runtime validation, SLO evaluation, access enforcement, drift detection, and incident routing. | Time-stamped conformance and breach telemetry. |
| Evolve | Propose a new version and compare it with active upstream and downstream contracts. | Breaking changes are blocked until impact, approval, notification, migration, and coexistence requirements are satisfied. | Compatibility report, affected consumers, migration plan, release decision. |
| Retire | Deprecate the version and close its dependencies and agreements. | Retirement is blocked while active products, ports, consume agreements, shares, or AI uses still depend on the version without an approved migration. | Consumer migration, access removal, retention, and archive evidence. |

Product and contract states move together, but they are not identical. A contract can be approved before the product is ready; a product cannot become live until the approved contract is implemented, published, and proven by go-live evidence.

## Enforcement Outcomes

Every enforceable clause must declare its enforcement point, severity, and outcome. Avoid treating every failure as either a silent warning or a complete platform outage.

| Clause or failure | Default outcome |
| --- | --- |
| Unknown producer, invalid envelope, corrupt file, or incompatible source schema | Reject or quarantine before validated source-aligned publication. |
| Critical schema, key, semantic, classification, policy, or lineage test failure | Block build or product go-live. |
| Critical runtime data-quality failure | Stop publication of the affected version or mark it unavailable; preserve the last known good product when safe. |
| Non-critical quality threshold or freshness breach | Mark product health degraded, notify owner and subscribers, and open an incident according to the SLO. |
| Unauthorized service operation, data purpose, field, sharing recipient, or AI use | Deny access and record decision evidence. |
| Breaking contract change without approved migration | Block release and keep the compatible version available. |
| Contract-to-runtime drift | Mark deployment non-conformant, alert the owner, and block the next promotion; immediately deny only where security or policy is at risk. |

Exceptions are versioned, approved, time-bound, visible to consumers, and monitored to expiry. They never rewrite the canonical contract or bypass identity and policy enforcement.

## Minimum Architecture Rules

1. Every publishable data product has one canonical product contract version and one accountable owner.
2. Raw landing is a restricted internal state; it is governed by source clauses and is not presented as a live product.
3. Every product records accepted upstream contract versions and publishes its own output promise.
4. Edge contracts and agreements narrow a product contract; they do not duplicate or replace it.
5. Product go-live is impossible without an approved contract, passing critical tests, matching runtime bindings, and observable evidence.
6. Contract changes are assessed across lineage, active consumers, agreements, shares, AI uses, and product health before release.
7. The same canonical contract drives documentation, tests, policy inputs, interface definitions, and telemetry correlation.
8. Contract enforcement is technology-neutral and remains portable across product storage and runtime platforms.

<div class="read-next">
  <strong>Next:</strong> use Data Product Lifecycle Design to align product states and gates, then apply the Data Contract Standard to the canonical artifact.
</div>

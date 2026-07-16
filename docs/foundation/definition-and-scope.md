# Definition and Scope

## Definition

The **data foundation** is the shared organizational capability that turns data needed beyond its source boundary into trusted, governed, and reusable data products. It gives analytics, applications, platforms, AI agents, and AI models a consistent way to discover, understand, access, and rely on data.

The foundation is used when data requires an independent lifecycle, accountable product ownership, stable meaning, governed access, or reuse across consumers. It may provide replicated, projected, federated, event, API, feature, retrieval, or sharing interfaces. It does not require every use case or dataset to be copied into a central platform.

The data foundation is part of the broader **Data and AI Foundation**. It supplies trusted data and context to BI, business applications, AI platforms, agents, models, and internal or external data ecosystems without replacing their distinct responsibilities.

## In Scope

Bring a use case into the data foundation when at least one of these conditions is material and the expected value justifies its lifecycle and operating cost.

| Case | Why It Belongs in the Data Foundation |
| --- | --- |
| Reuse across teams or purposes | Multiple independent consumers need a stable product rather than source-specific integrations. |
| Historical or reproducible analysis | Decisions, reports, training, evaluation, or audits must be reproduced against known data versions. |
| Cross-source or cross-domain composition | Data must be reconciled and given durable meaning beyond one source system. |
| Decoupling from source operations | Consumer scale, query patterns, availability, retention, or change cadence should not burden or destabilize the source. |
| Governed data access | Classification, purpose, entitlement, minimization, lineage, retention, and evidence must be applied consistently. |
| AI-ready data and context | Agents or models need permission-filtered, semantically described, versioned, observable, and evaluable grounding data. |
| Internal or external data exchange | A governed product must cross team, platform, customer, supplier, partner, or organizational boundaries. |
| Long-lived organizational data | Data must remain usable, understandable, and supported beyond one application release or source implementation. |

In scope does not automatically mean replication. The foundation can govern a logical product that is served through a direct, federated, projected, or replicated interface.

## Out of Scope

Keep a use case outside the data foundation when the source or consuming application is the correct authority and no durable data-product responsibility is created.

| Case | Preferred Boundary |
| --- | --- |
| Transaction or command | Read or change current operational state through the source API, event interface, or approved MCP tool. |
| Source-authoritative lookup | Use a governed direct interface when correctness depends on the latest source state and source availability is acceptable. |
| Application-internal state | Keep transient workflow state, session data, and private implementation data within the owning application. |
| Single-use transfer | Use application integration when there is one bounded consumer, no durable reuse, and no independent product lifecycle. |
| Temporary computation | Keep ephemeral intermediate data with the workload unless retention, reuse, audit, or recovery creates a product obligation. |
| Duplicate without purpose | Do not ingest data without an accountable owner, declared consumers, measurable value, lifecycle, and operating commitment. |
| AI or application runtime design | Keep model architecture, prompt design, transaction processing, and application behavior in their owning platforms. The foundation governs only their data boundary. |

## Boundary Decisions

Choose the lightest pattern that preserves the required authority, trust, reuse, and evidence.

| Need | Default Direction | Move Further into the Foundation When... |
| --- | --- | --- |
| Current operational state or command | Direct source API, event, or MCP interface. | History, reproducibility, cross-source composition, source isolation, or independent SLOs are required. |
| Analytical query over source data | Federated access where source impact and semantics are acceptable. | Scale, stability, retention, performance, or source-change risk requires projection or replication. |
| Reusable business data | Governed data product through the foundation. | This is already a foundation case; select the least-coupled physical access pattern. |
| AI agent action | Governed source or service tool for bounded action. | The agent also needs reusable historical, semantic, retrieval, feature, or evaluation data. |
| AI model grounding or training | Versioned data product or governed retrieval, feature, or semantic port. | Always retain purpose, lineage, quality, snapshot or index version, and evaluation evidence. |
| External exchange | Governed product and sharing service. | Recipient identity, minimization, contract, expiry, revocation, and audit must be controlled independently of the source. |

Use the [Data Consumption Service decision guide](../services/data-consumption-service.md#direct-federated-or-replicated-access-decision) for direct, federated, projected, and replicated choices.

## Guidance Boundary

This repository defines the common architecture, service responsibilities, decision rules, standards, and operating expectations needed to establish the data foundation. It does not prescribe one mandatory technology stack, detailed vendor runbooks, every domain data model, application internals, or AI model and prompt architecture.

## Ownership Boundary

The Data Foundation Platform Team centrally owns source onboarding, ingestion, and the raw and validated source-aligned lifecycle. Source system teams remain accountable for source availability, source semantics, and change obligations. Domain data teams federate the creation and ownership of aggregate and consumer-aligned products using shared foundation services, standards, controls, and evidence.

### How Data Domains Fit

A data domain is a business-aligned accountability and product-portfolio boundary **inside** the shared data foundation. The foundation supplies shared services, centrally managed source-aligned inputs, standards, controls and evidence; each domain adopts them and owns its downstream product meaning, stewardship, priorities, consumer outcomes and quality decisions.

A domain is not defined by one workspace, catalog, schema, team or vendor platform. Its identity remains stable across implementation and organization changes. Every product has one accountable owning domain, and cross-domain use occurs through governed product ports and contracts. See [Data Domain Design](../architecture/data-domain-design.md).

## Scope Decision Flow

1. Define the business outcome, authoritative source, consumers, purpose, latency, history, reuse, and evidence needs.
2. Decide whether the need is a source-authoritative transaction or lookup, or a durable data-product responsibility.
3. Select direct, federated, projected, event-based, or replicated access using the lightest sufficient pattern.
4. When the foundation is in scope, assign the owning domain and data service, define the applicable data contract, and establish lifecycle and access controls.
5. Approve go-live only when the product or governed interface has measurable value, ownership, quality, observability, support, and retirement evidence.

# Data Service Portal

<div class="decision-brief"><div><small>Use when</small><strong>Designing a user entry point or foundation journey.</strong></div><div><small>Decision</small><strong>What belongs in the portal versus an authoritative service?</strong></div><div><small>Owner</small><strong>Portal owner with journey and service owners.</strong></div><div><small>Output</small><strong>Coherent journey, state boundary, and evidence view.</strong></div></div>

## Definition

The data service portal is the user entry point for the data foundation. It provides a single place for users to discover data products through its Data Product Marketplace capability, request access, onboard sources, create or manage data products, manage data contracts, track workflow status, and view product trust signals.

The portal is the experience layer over the foundation services. It should orchestrate workflows and expose consistent information without becoming a separate source of truth from the catalog, policy, lineage, observability, or contract systems.

The [Data Service Portal Design](../architecture/data-service-portal-model.md) defines the portal's intent-led journeys, object model, product detail standard, state ownership, and experience principles.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Data Product Marketplace discovery and comparison, access requests, onboarding workflows, data product lifecycle workflows, and data contract management. | Operating the marketplace as a separate portal, catalog, product registry, or commercial storefront. |
| User-facing views for product health, ownership, classification, lineage, quality, freshness, usage, and lifecycle status. | Owning the actual data pipelines, transformations, or consumption endpoints. |
| Request intake, support engagement, operational status, approvals, notifications, task tracking, and evidence presentation. | Bypassing governance, security, stewardship, or operational authority. |

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Experience | Portal navigation and journey entry | Users start from Explore, Ingest, Produce, Consume, Share, Operate, or My Work and retain context across the journey. |
| Marketplace | Product discovery and comparison | Ingestors, producers, and consumers find and compare products using purpose, semantics, trust, access, and interface evidence. |
| Marketplace | Product detail and engagement | One product view presents identity, contract, context, lineage, health, support, and role-relevant next actions. |
| Workflow | Request and task orchestration | Source onboarding, product creation, access, sharing, support, and operational requests have visible state, owner, evidence, and next action. |
| Contracts | Contract management experience | Teams author, review, approve, version, compare, and change contracts through governed workflows. |
| Product lifecycle | Product and portfolio management | Teams propose, bring live, change, deprecate, retire, consolidate, and review products with current evidence. |
| Access | Identity-aware agreement journeys | Named users, workloads, delegated applications, agents, models, and recipients request bounded access or sharing. |
| Trust | Health and impact views | Quality, freshness, SLOs, lineage, usage, incidents, cost, and affected consumers are visible with authority and observation time. |
| Engagement | Notifications and subscriptions | Consumers and owners receive relevant contract, release, incident, deprecation, approval, and task updates. |
| Operations | Support and service engagement | Users open support, inspect status and planned change, follow recovery, use knowledge, and provide feedback. |
| Intelligence | Data Service AI Assistant | Ask, Plan, and Act modes explain evidence, prepare artifacts, and execute approved typed skills in context. |
| Interoperability | Canonical artifact and channel parity | Product and contract artifacts can be imported or exported, and portal journeys remain available through governed APIs and automation. |

## Portal Experience Model

| View | User Decision |
| --- | --- |
| Journey catalog | What outcome am I trying to achieve? |
| Data Product Marketplace | Which existing product best fits my purpose, and what can I do with it? |
| Product detail | Is this product understandable, trustworthy, permitted, and fit for use? |
| Agreement workflow | Who will use or receive the product, why, for how long, and under which terms? |
| Portfolio | Which products need action, investment, consolidation, or retirement? |
| Product health | What changed, who is affected, and what should happen next? |
| AI assistant | What can be explained, drafted, or safely executed from this context? |

## Data Product Marketplace

The Data Product Marketplace is a capability within the Data Service Portal. It helps ingestors, producers, and consumers find, evaluate, and act on data products without creating another metadata or workflow authority.

| Role | Marketplace Need | Primary Actions |
| --- | --- | --- |
| Ingestor | Understand which products and consumers depend on a source and whether its source-aligned product is healthy. | Find source-aligned products, inspect contracts and downstream impact, open source onboarding, and respond to schema or quality issues. |
| Producer | Reuse existing products before creating another and manage products already owned by the team. | Search and compare input products, use a product as an input, open a product workspace, propose or change a contract, and submit product go-live. |
| Consumer | Select a product that is fit, permitted, understandable, and reliable for an intended use. | Compare products, inspect trust and semantics, request access, subscribe to change and incident notices, and open an approved product port. |

The marketplace experience should provide:

- Search and filters for domain, concept, product pattern, interface, classification, permitted purpose, lifecycle, and current health.
- Comparable product summaries that show owner, contract, context, quality, freshness, availability, policy, usage, and support.
- Product detail pages with stable actions: **Use as input**, **Request access**, **Request sharing**, **Manage product**, or **Report an issue**, shown only when relevant.
- Saved products, curated collections, recent activity, subscriptions, and role-aware recommendations with an explainable ranking basis.
- Direct continuation into ingestion, product creation, consumption, sharing, contract, and operations workflows without re-entering product or purpose context.

Marketplace listings are read projections. Product identity and lifecycle come from the product registry; searchable metadata from the catalog; contracts from the contract registry; semantics from context authorities; access from policy and entitlement services; and health from observability. The marketplace may rank and present this information, but it must show authority and observation time and must not approve access or product go-live itself.

## Data Contract Management

The portal should provide the governed interface for managing data contracts across source interfaces, data products, consumption APIs, and sharing packages.

| Contract Capability | Purpose |
| --- | --- |
| Contract registry | Maintain approved contracts with owner, version, status, schema, semantics, quality expectations, and lifecycle state. |
| Contract authoring | Allow product teams and source teams to propose new contracts using standard templates. |
| Review and approval | Route contract changes to owners, stewards, security, privacy, and impacted consumers where needed. |
| Compatibility checks | Detect breaking changes in schema, semantics, quality expectations, and access behavior. |
| Change communication | Notify subscribed consumers about new versions, deprecations, incidents, and migration deadlines. |
| Evidence capture | Store approval records, test results, exception decisions, and go-live evidence. |
| Portability | Validate the canonical contract, preserve extensions, and show the last round-trip conformance result. |

Use the [Data Contract Standard](../standards/data-contract-standard.md) as the minimum contract model.

## Support and Operations

The portal is the front door for operational engagement, while the [Data Foundation Operations Service](data-foundation-operations-service.md) owns routing, incident, problem, change, release, reliability, communication, and improvement workflows.

| Portal Experience | Required behavior |
| --- | --- |
| Get support | Select or infer service and product, capture impact and urgency, preserve context, and show owner and target. |
| Service status | Show current service and product health, incidents, affected capabilities, observation time, and next update. |
| Planned change | Show approved maintenance, expected impact, dependencies, consumer action, validation, and rollback status. |
| Incident engagement | Provide audience-appropriate updates, subscriptions, workarounds, recovery state, and closure evidence. |
| Knowledge and feedback | Surface runbooks or consumer guidance appropriate to the user and capture whether support resolved the need. |

The portal must not expose restricted responder notes, sensitive logs, security details, personal data, or emergency credentials. Views are filtered by identity, role, service, product, domain, and incident sensitivity.

## Data Domain Management

The portal must make domain onboarding and recurring maturity review evidence-driven.

| Domain Capability | Portal Behavior |
| --- | --- |
| Domain registry | Show stable id, boundary, owners, lifecycle, governance context and authoritative links. |
| Onboarding | Capture admission gates, decisions, conditions, service dependencies and provisioning status. |
| Capability adoption | Show selected foundation service profiles, conformance, support, quotas and cost allocation. |
| Maturity | Record six dimension scores, evidence, gaps, actions, exceptions and assessment history. |
| Domain portfolio | Show products, contracts, consumers, health, value, cost, duplication and lifecycle. |
| Cross-domain view | Show semantic overlap, lineage, contracts, dependencies and shared consumers. |

Use [Data Domain Design](../architecture/data-domain-design.md) and the [Data Domain Onboarding Record](../delivery-templates/data-domain-onboarding-template.md) as the minimum model.

## Data Product Management

The portal must also provide the user-facing control surface for data product management.

| Product Management Capability | Portal Behavior |
| --- | --- |
| Product registry | Show product id, owner, steward, lifecycle state, domain, contract, consumers, and support route. |
| Product creation | Guide teams through product proposal, design, contract, quality, classification, and go-live. |
| Go-live gates | Show gate status and prevent go-live when mandatory evidence is missing. |
| Portfolio view | Show products by domain, lifecycle state, health, usage, owner, cost, and exception status. |
| Consumer subscriptions | Allow consumers to subscribe to products and receive incident, change, and deprecation notifications. |
| Change management | Route product and contract changes through compatibility check, approval, and consumer impact workflow. |
| Retirement | Manage deprecation notices, migration plans, access removal, archive, and evidence retention. |

Use the [Data Product Management Standard](../standards/data-product-management-standard.md) as the minimum management model.

## Architecture Guidance

The portal should act as an orchestration and experience layer. It should integrate with authoritative systems instead of duplicating them:

- Catalog for product metadata and discovery.
- Policy and identity services for access decisions.
- Workflow engine for approvals and status.
- Lineage system for upstream and downstream impact.
- Observability service for product health and trust signals.
- Contract registry for schema, semantic, quality, and compatibility rules.

The user experience should use seven stable areas:

1. **Explore:** Data Product Marketplace, product comparison, collections, and innovation.
2. **Ingest:** source onboarding, source contracts, source-aligned products, and ingestion health.
3. **Produce:** product creation and change, workspaces, contracts, semantics, analytics, AI, and product go-live.
4. **Consume:** purpose-bound requests, subscriptions, entitlements, and product ports.
5. **Share:** recipient agreements, packages, activation, expiry, and revocation.
6. **Operate:** health, support, incidents, change, reliability, cost, improvement, and retirement.
7. **My Work:** owned products, approvals, contracts, subscriptions, notifications, and portfolio actions.

## Controls

- Portal permissions are based on identity, role, domain, and approved purpose.
- Contract changes require review, approval, versioning, and consumer notification.
- Product go-live requires all mandatory gates to pass.
- Product lifecycle changes require evidence and audit trail.
- Access requests are routed through policy and stewardship workflows.
- Product metadata shown in the portal is synchronized from authoritative systems.
- Marketplace search indexes and recommendations are rebuildable projections, expose freshness, and never override policy or product lifecycle state.
- Sensitive metadata and telemetry are masked or restricted where required.
- All portal actions are auditable.

## Done Criteria

- Users can discover data products and understand ownership, trust, classification, access, and usage guidance.
- Ingestors, producers, and consumers receive role-relevant marketplace actions without entering separate portals.
- Producers can compare and reuse existing input products before proposing another product.
- Users can request access and track approval status.
- Product teams can create and manage data contracts through a governed workflow.
- Contract changes trigger compatibility checks and consumer notifications.
- Product teams can bring products live, operate, deprecate, and retire them through governed workflows.
- Users can see separate service-operation and data-entitlement decisions, including purpose, scope, obligations, expiry, and revocation status.
- Product health, quality, freshness, and incidents are visible from the portal.
- Portal records link back to authoritative catalog, policy, lineage, observability, and workflow systems.
- Users can export canonical product and contract artifacts without requiring a platform-native format.
- Journey and product views clearly identify the authority and observation time for every trust signal.
- Assistant answers are grounded, actions are typed and approved, and every execution returns an auditable receipt.

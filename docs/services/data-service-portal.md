# Data Service Portal

## Definition

The data service portal is the user entry point for the data foundation. It provides a single place for users to discover data products, request access, onboard sources, create or manage data products, manage data contracts, track workflow status, and view product trust signals.

The portal is the experience layer over the foundation services. It should orchestrate workflows and expose consistent information without becoming a separate source of truth from the catalog, policy, lineage, observability, or contract systems.

The [Data Service Portal Design](../architecture/data-service-portal-model.md) defines the portal's intent-led journeys, object model, product detail standard, state ownership, and experience principles.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Data product discovery, access requests, onboarding workflows, data product lifecycle workflows, and data contract management. | Replacing backend systems for catalog, identity, policy, lineage, observability, or workflow execution. |
| User-facing views for product health, ownership, classification, lineage, quality, freshness, usage, and lifecycle status. | Owning the actual data pipelines, transformations, or consumption endpoints. |
| Request intake, approvals, notifications, status tracking, and evidence capture. | Bypassing governance, security, or stewardship approval processes. |

## Core Capabilities

- Data product discovery and catalog search.
- Data product detail pages with owner, steward, description, schema, classification, quality, freshness, lineage, and usage guidance.
- Access request and approval workflow.
- Named-user, workload, delegated application, and external-recipient access requests.
- Source onboarding request workflow.
- Data product creation and go-live workflow.
- Data contract creation, review, approval, versioning, and change management.
- Contract compatibility checks and schema change notifications.
- Consumer subscription and impact notification.
- Product health, SLO, incident, and usage dashboards.
- Integration with identity, catalog, policy, lineage, observability, and workflow systems.
- Import, export, and conformance status for canonical contract and product artifacts.
- Intent-led journey catalog for innovation, source connection, product creation, consumption, sharing, AI, observability, semantics, policy, and industrialization.
- Domain team, use-case, workspace, saved-product, portfolio, and notification views.
- Context-aware AI assistant with separate Ask, Plan and Act modes.

## Portal Experience Model

| View | User Decision |
| --- | --- |
| Journey catalog | What outcome am I trying to achieve? |
| Product discovery | Which existing product best fits my purpose? |
| Product detail | Is this product understandable, trustworthy, permitted, and fit for use? |
| Agreement workflow | Who will use or receive the product, why, for how long, and under which terms? |
| Portfolio | Which products need action, investment, consolidation, or retirement? |
| Product health | What changed, who is affected, and what should happen next? |
| AI assistant | What can be explained, drafted, or safely executed from this context? |

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

The user experience should be organized around common journeys:

1. Start an innovation idea.
2. Find and understand a data or AI product.
3. Connect a source system.
4. Produce, bring live, or evolve a data, analytics, or AI product.
5. Consume a product through a purpose-bound agreement.
6. Share a product with a customer, supplier, or partner.
7. Define semantics, apply policy, and manage contracts.
8. Evaluate AI products and industrialize approved products.
9. Track health, incidents, usage, cost, and consumer impact.
10. Review the portfolio for reuse, consolidation, investment, and retirement.

## Controls

- Portal permissions are based on identity, role, domain, and approved purpose.
- Contract changes require review, approval, versioning, and consumer notification.
- Product go-live requires all mandatory gates to pass.
- Product lifecycle changes require evidence and audit trail.
- Access requests are routed through policy and stewardship workflows.
- Product metadata shown in the portal is synchronized from authoritative systems.
- Sensitive metadata and telemetry are masked or restricted where required.
- All portal actions are auditable.

## Done Criteria

- Users can discover data products and understand ownership, trust, classification, access, and usage guidance.
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

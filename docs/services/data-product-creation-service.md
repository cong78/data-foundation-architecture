# Data Product Creation Service

## Definition

The data product creation service turns source-aligned data and existing products into trusted, reusable datasets or data interfaces. It applies data product principles so consumers can understand, access, and rely on the data.

Use the [Data Product Management Standard](../standards/data-product-management-standard.md), [Data Product Workload Standard](../standards/data-product-workload-standard.md), and [Data Contract Standard](../standards/data-contract-standard.md) as mandatory controls for product go-live.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Product design, transformation, validation, documentation, go-live approval, and publication. | Source system ownership or source application change management. |
| Declarative developer workspace, isolated environments, deployment promotion, and rollback. | Provider-specific infrastructure exposed as the product interface. |
| Data contracts, semantic definitions, lineage, quality rules, ownership, and lifecycle state. | Consumer dashboard, application, or model implementation. |
| Product workspaces, reusable templates, and product readiness evidence. | External sharing agreements, except product packaging needed for sharing. |

## Product Requirements

Each data product must be:

- Owned by a business or data domain.
- Documented with clear business meaning.
- Governed by a data contract.
- Validated against explicit quality rules.
- Classified for sensitivity and permitted use.
- Published through the catalog.
- Versioned and lifecycle-managed.
- Observable in production.
- Described by a portable product descriptor with open input and output port definitions.

## Product Management Capabilities

| Capability | Requirement |
| --- | --- |
| Product registry | Maintain product id, owner, steward, status, domain, contract, and support route. |
| Go-live workflow | Enforce required gates before a product can go live. |
| Developer workspace | Provide templates, workload specifications, API and CLI, isolated environments, preview, CI/CD, promotion, and rollback. |
| Resource orchestration | Resolve portable resource profiles into governed runtime plans and execution receipts. |
| Portfolio review | Identify duplicate, low-usage, unhealthy, ownerless, or high-cost products. |
| Consumer subscription | Track active consumers and notify them about incidents, contract changes, and deprecation. |
| Change management | Require impact analysis, compatibility check, migration plan, and release note for product changes. |
| Exception management | Track accepted deviations with owner, risk, compensating control, expiry, and remediation. |

## Core Capabilities

- Product workspace and template creation.
- Transformation and enrichment pipelines.
- Data quality rules and validation suites.
- Business glossary and semantic mapping.
- Semantic context package creation and validation.
- Product contract creation and testing.
- Product go-live workflow.
- Declarative workload validation, environment promotion, drift detection, and rollback.
- Lineage from source to product outputs.
- Publication to catalog and Data Service Portal.
- Versioning, deprecation, and retirement support.
- Product health telemetry for freshness, quality, usage, and incidents.

## Architecture Guidance

A trusted dataset should have clear boundaries. It should represent a reusable business concept such as customer, supplier, asset, product, order, event, transaction, or compliance record.

Trusted datasets should avoid hidden assumptions. Transformations, filters, joins, exclusions, and enrichment logic must be documented and testable. Product logic should be versioned and observable so consumers can understand changes and impact.

Each product should publish a [semantic context package](../architecture/semantic-context-design.md) that binds business meaning, grain, metrics, relationships, usage context, and limitations to exact product and contract versions.

## Controls

- Product owner and steward are assigned.
- Business purpose and intended consumers are defined.
- Source lineage is captured.
- Data contract is approved.
- Contract tests pass and compatibility status is known.
- Quality rules are implemented and passing.
- Sensitive fields are classified.
- Access policy is defined.
- Freshness and availability expectations are documented.
- Product lifecycle state is managed in the portal and catalog.

## Done Criteria

- Product is published in the catalog with owner, steward, contract, schema, classification, and lifecycle state.
- Quality checks and product SLOs are visible.
- Lineage is available from source to product output.
- Access pattern is approved.
- Consumer-facing documentation is published.
- Product health telemetry is available in the observability service.
- Active consumers are registered for impact analysis and notifications.
- Product and contract artifacts pass schema validation and round-trip portability tests.
- Semantic context is versioned, validated, policy-aware, and linked to authoritative terms, metrics, lineage, and health.
- Workload specification validates, produces a deterministic plan, and binds the deployed release to product and contract versions.
- Environment promotion, drift detection, and rollback have passing evidence.

# Data Product Management Standard

This standard defines how data products are created, governed, operated, changed, and retired. It makes data product management enforceable instead of informal.

## Portable Product Descriptor

Every live product must have an [Open Data Product Standard 1.0](https://bitol.io/announcing-odps-v1-0-0-building-the-language-of-data-products/) compatible descriptor. It is the portable product manifest; catalog records and platform-native product objects are projections of it.

The descriptor must reference the product id, owners, lifecycle state, input and output ports, contracts, SLOs, policies, support route, and authoritative metadata links. It must validate in CI and survive export and import without losing required meaning.

## Mandatory Product Model

Every live data product must have:

| Area | Mandatory Requirement |
| --- | --- |
| Ownership | Product owner, data steward, technical owner, support contact, and escalation path. |
| Purpose | Clear business purpose, intended consumers, approved use cases, and out-of-scope use. |
| Contract | Approved data contract with schema, semantics, quality rules, access policy, compatibility rules, and version. |
| Semantic context | Versioned product context with grain, concepts, metrics, relationships, valid uses, prohibited uses, limitations, and authoritative references. |
| Classification | Sensitivity, privacy, confidentiality, regulatory, residency, and AI usage classification. |
| Quality | Defined quality dimensions, thresholds, severity, owner, and remediation process. |
| Freshness | Freshness SLO, update frequency, expected availability, and breach handling. |
| Lineage | Source-to-product lineage and product-to-consumer lineage. |
| Access | Approved consumption patterns, access workflow, masking, and purpose restrictions. |
| Observability | Product health dashboard, SLO status, incidents, usage, cost, and consumer impact. |
| Lifecycle | Draft, review, go-live approved, active, deprecated, retired, or exception state. |

## Product Quality Model

The product must demonstrate eight qualities adapted from the [Data Developer Platform data-product attributes](https://datadeveloperplatform.org/why_ddp_for_data/#a-closer-look-at-the-solution-achieving-the-state-of-data-products). These qualities are acceptance outcomes, not marketing labels.

| Quality | Architecture Interpretation | Minimum Evidence |
| --- | --- | --- |
| Discoverable | Intended consumers can find the product through governed search using business language, domain, use case, concepts, and interfaces. | Indexed portal and catalog entry, owner, description, tags, semantic concepts, current lifecycle and health. |
| Addressable | The product and each input or output port have stable identifiers independent of physical paths and vendor-native names. | Product id, port ids, version, canonical descriptor, resolvable links, identifier round-trip test. |
| Understandable | Consumers can determine meaning, grain, time behavior, limitations, quality, examples, and correct usage without reverse-engineering implementation. | Contract, semantic context package, schema, metric definitions, sample-safe examples, limitations, consumer guidance. |
| Natively accessible | Consumers use the product through interfaces suited to their normal tools and workload while remaining behind unified access and policy controls. | Approved SQL, API, event, file, semantic, feature, retrieval, or context port tested by a representative consumer. |
| Trustworthy | The product proves authenticity, lineage, contract conformance, quality, freshness, availability, ownership, support and current operational health. | Passing tests, lineage, provenance, SLO status, product telemetry, incidents and support route. |
| Interoperable | The product composes with other products and consumers through open, machine-readable artifacts and interfaces. | ODPS and ODCS validation, open interface definition, canonical ids, independent-client or import/export conformance result. |
| Independent | The product has one clear purpose, accountable ownership, explicit dependencies, independently manageable lifecycle and value beyond one pipeline output. | Product brief, owner, ports, dependency inventory, workload, SLOs, support, usage and value measures. |
| Secure | Human and machine access is authenticated, purpose-bound, least-privilege, enforceable, observable, expiring and revocable. | Classification, service and data policy, entitlement, obligations, allow and deny tests, audit and revocation evidence. |

“Natively accessible” does not permit direct access to physical storage. It means that the [Unified Access Design](../architecture/unified-access-design.md) exposes a governed interface that fits the consumer's channel.

## Product Lifecycle States

| State | Meaning | Allowed Actions |
| --- | --- | --- |
| Draft | Product idea or early design exists. | Define owner, purpose, source, contract, classification, and target consumers. |
| Review | Product is ready for governance, architecture, and stewardship review. | Review contract, controls, lineage, quality, access, and observability. |
| Go-live approved | Product has passed all mandatory readiness gates. | Publish to catalog and portal for approved consumption. |
| Active | Product is being consumed and operated against SLOs. | Monitor, support, evolve, and manage incidents. |
| Deprecated | Product should no longer be used for new consumers. | Notify consumers, publish migration path, maintain limited support. |
| Retired | Product is no longer available for consumption. | Remove access, archive evidence, apply retention, update catalog. |
| Exception | Product violates a standard with accepted risk. | Track owner, risk, compensating control, expiry, and remediation plan. |

## Standard Delivery Path

The delivery path combines product thinking with self-service engineering. Each stage leaves reusable, machine-readable evidence.

| Stage | Team Outcome | Foundation Automation | Exit Evidence |
| --- | --- | --- | --- |
| 1. Frame | Agree the business outcome, product boundary, owner, consumers, value measure and non-goals. | Search existing products and duplication candidates; create stable product id and proposal. | Product brief, accountable owner, intended consumers, expected value, reuse decision. |
| 2. Design | Define ports, contract, semantic context, classification, access, SLOs and dependencies. | Generate standard descriptor, contract and workload skeletons; validate identifiers and required fields. | Reviewed design, contract draft, context package, access model, architecture mapping. |
| 3. Provision | Create an isolated workspace and approved runtime resources without a platform ticket. | Resolve resource profiles, identity, secrets, policies, environments, budgets and CI/CD. | Versioned workspace, workload plan, environment receipt, ownership and expiry. |
| 4. Build | Implement ingestion, transformation, quality, interfaces, lineage and telemetry. | Reusable patterns, local and CI validation, preview environments, test data controls and drift checks. | Immutable artifact, passing unit, contract, quality, security and lineage tests. |
| 5. Prove | Demonstrate all eight product qualities and mandatory go-live gates with representative consumers. | Run conformance, policy, reliability, rollback, performance and independent-client tests. | Gate record, consumer acceptance, known limitations, exception and remediation records. |
| 6. Go live | Publish the approved version and make access requestable through governed channels. | Promote the same artifact, register ports, publish metadata, provision entitlements and emit release evidence. | Release record, portal detail, active health, support route and rollback target. |
| 7. Operate | Meet SLOs, support consumers and measure quality, usage, value and cost. | Product health, alerts, incident workflow, usage and cost attribution, consumer-impact analysis. | Review decisions, incidents, improvements, adoption and value evidence. |
| 8. Evolve or retire | Change compatibly or remove the product without abandoning consumers. | Impact analysis, versioning, migration workflow, deprecation, access removal and evidence archive. | Migration completion, retired interfaces, revoked access and retained records. |

The developer should declare product intent once. The platform should generate or orchestrate provider-specific manifests, provisioning, tests and evidence from canonical product, contract and workload artifacts.

## Product Go-Live Gates

A product cannot go live unless all mandatory gates pass.

| Gate | Required Evidence |
| --- | --- |
| Ownership gate | Product owner, steward, technical owner, support route, escalation route. |
| Purpose gate | Business purpose, intended use, prohibited use, known consumers. |
| Contract gate | Approved contract, version, compatibility rules, test result. |
| Quality gate | Quality rules, thresholds, latest validation result, remediation owner. |
| Security gate | Classification, access policy, masking rules, privacy/security approval where needed. |
| Lineage gate | Source lineage and downstream dependency registration. |
| Observability gate | Freshness, quality, availability, usage, incident, and cost telemetry. |
| Documentation gate | Catalog entry, portal detail page, consumer guidance, change policy. |
| Portability gate | Valid product descriptor, canonical identifiers, open interface definitions, and successful export/import test. |
| Product qualities gate | Evidence that discoverable, addressable, understandable, natively accessible, trustworthy, interoperable, independent and secure outcomes are met. |

## Portfolio Management

Data products should be managed as a portfolio, not as isolated datasets.

| Portfolio Concern | Management Rule |
| --- | --- |
| Duplication | New products must be checked against existing live products before creation. |
| Ownership gaps | Products without an accountable owner or steward cannot remain live. |
| Low usage | Products with low or no usage should be reviewed for retirement or consolidation. |
| Poor health | Products with repeated SLO or quality breaches require remediation plan. |
| Contract drift | Products with implementation behavior different from contract must be blocked from go-live or moved to exception. |
| Consumer impact | Changes must identify impacted consumers before release. |
| Cost | High-cost products require usage and value review. |

## Product Review Cadence

| Review | Frequency | Participants | Purpose |
| --- | --- | --- | --- |
| Product health review | Monthly | Product owner, steward, technical owner, reliability team. | Review SLOs, incidents, usage, quality, and cost. |
| Portfolio review | Quarterly | Domain lead, governance, platform, product owners. | Review duplication, value, adoption, lifecycle, and retirement. |
| Contract review | On change and at least annually | Contract owner, steward, platform, consumers. | Validate schema, semantics, quality, compatibility, and consumer impact. |
| AI usage review | On approval and at least annually | Product owner, AI owner, privacy/security, governance. | Confirm AI purpose, data controls, evidence, and lineage. |

## Enforcement Rules

- No product go-live without an approved data contract.
- No external sharing from a product that has not passed go-live unless an explicit exception exists.
- No AI training, retrieval, evaluation, or feature use without approved AI usage classification.
- No breaking change without impact analysis, consumer notification, and migration path.
- No product remains active without observable freshness and quality status.
- No product remains live if ownership is missing or expired.
- No live product may depend on a vendor-native descriptor as its only machine-readable definition.

## Minimum Portal Views

The Data Service Portal must show:

- Product owner, steward, support contact, and lifecycle state.
- Contract id, version, status, and compatibility policy.
- Product description, business definitions, schema, and sample-safe usage guidance.
- Classification, permitted use, prohibited use, and access pattern.
- Quality score, freshness, availability, incidents, and known limitations.
- Source lineage and downstream consumers.
- Change history, deprecation notices, and migration guidance.
- Open interface types, conformance level, canonical descriptor, and latest portability test status.

Portal views should follow the [Data Service Portal product detail standard](../architecture/data-service-portal-model.md#product-detail-standard). Declared contract targets must be visually and semantically distinct from current measured product health.

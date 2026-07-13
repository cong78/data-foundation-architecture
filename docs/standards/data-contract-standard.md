# Data Contract Standard

<div class="decision-brief"><div><small>Use when</small><strong>Defining or changing a source, product, access, sharing, or AI promise.</strong></div><div><small>Decision</small><strong>Does the contract meet content, lifecycle, and compatibility rules?</strong></div><div><small>Owner</small><strong>Contract owner and approvers.</strong></div><div><small>Output</small><strong>Approved, testable, published contract version.</strong></div></div>

The data contract standard defines the minimum content and lifecycle rules for contracts across source interfaces, data products, consumption APIs, event streams, and sharing packages.

Contracts are enforceable platform assets. A contract is not complete when it is written; it must be reviewed, versioned, tested, published, monitored, and used by pipelines and consumers.

Use [Data Contract Design](../architecture/data-contract-design.md) to place these contract types across source-aligned, aggregate, consumer-aligned, consumption, sharing, and AI-use boundaries.

## Canonical Representation

The portable contract artifact must conform to the [Open Data Contract Standard 3.1](https://bitol-io.github.io/open-data-contract-standard/latest/). Enterprise requirements are added through its extension mechanism, without redefining standard fields.

- Store the canonical YAML artifact in version control and the contract registry.
- Pin and record the ODCS schema version and media type.
- Generate platform schemas and validation rules from the canonical contract.
- Preserve unknown extensions during import and export.
- Prove semantic equivalence after round-trip export and import.
- Use OpenAPI for API ports and AsyncAPI plus CloudEvents for event ports.

The field model below is the enterprise minimum. Its implementation must map to the canonical ODCS artifact rather than create a competing schema.

## Contract Types

| Type | Purpose | Typical Owner |
| --- | --- | --- |
| Source contract | Defines what a source system provides to the foundation. | Source system owner. |
| Product contract | Defines the live product promise and ports. Source-aligned, aggregate, and consumer-aligned products use profiles of this common type. | Data product owner. |
| Consumption contract | Narrows a product contract to API, semantic, event, feature, retrieval, or other access behavior; it does not replace the product contract. | Product owner and platform owner. |
| Sharing contract | Narrows a product contract to recipient-specific package, scope, usage, expiry, and revocation. | Sharing owner. |
| AI usage contract | Narrows a product contract to approved AI use such as retrieval, training, evaluation, grounding, or feature use. | Product owner and AI use-case owner. |

Consume agreements and sharing agreements are lifecycle records that reference a contract version; they are not replacements for the product contract. A consume agreement binds identity, team, use case, purpose, duration, and entitlement. A sharing agreement additionally binds recipient identity, legal basis, minimized scope, delivery channel, expiry, and revocation.

Raw landing is not a separate contract type or product. Source-contract clauses govern its technical receipt, provenance, quarantine, replay, retention, and restricted access. The validated source-aligned output is the first publishable layer and therefore has a product contract.

## Required Contract Fields

| Field | Description |
| --- | --- |
| Contract id | Stable unique identifier. |
| Name | Human-readable contract name. |
| Owner | Accountable person or team. |
| Domain | Business or data domain. |
| Version | Semantic version or approved enterprise versioning scheme. |
| Status | Draft, review, approved, published, deprecated, retired. |
| Purpose | Why the contract exists and what use cases it supports. |
| Consumers | Known or intended consumers. |
| Schema | Fields, types, nullability, keys, and structural rules. |
| Semantics | Business definitions and valid interpretation. |
| Semantic context | Versioned package reference for grain, concepts, metrics, relationships, valid uses, prohibited uses, and limitations. |
| Quality rules | Completeness, validity, consistency, timeliness, uniqueness, and domain rules. |
| Freshness | Expected update frequency and freshness SLO. |
| Classification | Sensitivity, privacy, confidentiality, and permitted use. |
| Access policy | Roles, attributes, purpose, masking, and approval requirements. |
| Compatibility rules | What counts as breaking, non-breaking, or compatible change. |
| Observability | Required metrics, traces, logs, events, and product health signals. |
| Logical access | Stable product port id, interface type, supported actions, identity types, policy, service levels, and provider-independent endpoint behavior. |
| Change process | Reviewers, approvals, notice period, and migration expectations. |

## Contract State Model

| State | Meaning | Entry Criteria | Exit Criteria |
| --- | --- | --- | --- |
| Draft | Contract is being authored. | Owner assigned. | Required fields complete. |
| In review | Contract is under review. | Draft complete. | Reviewers approve or request change. |
| Approved | Contract can be implemented. | Steward, platform, and required risk reviews complete. | Validation succeeds. |
| Published | Contract is visible and available for consumers. | Compatibility and validation checks pass. | Superseded, deprecated, or retired. |
| Deprecated | Contract should not be used for new consumers. | Replacement or retirement path exists. | Consumers migrated or exception granted. |
| Retired | Contract is no longer valid. | No active consumers or approved migration complete. | Archived as evidence. |
| Exception | Contract violates a rule under accepted risk. | Risk owner and expiry date recorded. | Remediated or escalated. |

## Ownership and RACI

| Activity | Product Owner | Contract Owner | Steward | Platform | Security/Privacy | Consumer |
| --- | --- | --- | --- | --- | --- | --- |
| Define business meaning | Accountable | Responsible | Consulted | Informed | Informed | Consulted |
| Define schema and semantics | Accountable | Responsible | Consulted | Consulted | Informed | Consulted |
| Define quality rules | Accountable | Responsible | Responsible | Consulted | Informed | Consulted |
| Define access and masking | Accountable | Consulted | Responsible | Responsible | Consulted | Informed |
| Approve sensitive data use | Consulted | Consulted | Consulted | Informed | Accountable | Informed |
| Test compatibility | Informed | Responsible | Consulted | Accountable | Informed | Informed |
| Communicate changes | Accountable | Responsible | Consulted | Informed | Informed | Consulted |
| Accept breaking change impact | Accountable | Responsible | Consulted | Consulted | Consulted | Accountable |

## Enforcement Points

Contracts must be used by the platform at these points:

| Enforcement Point | Required Behavior |
| --- | --- |
| Source onboarding | Source cannot be onboarded without approved source contract or exception. |
| Ingestion validation | Incoming data is validated against schema and required quality rules. |
| Product go-live | Product cannot go live without an approved product contract and passing tests. |
| Consumption approval | Consumers see contract terms and subscribe to contract changes. |
| CI/CD pipeline | Breaking schema or semantic changes fail validation unless approved. |
| Observability | Contract compatibility failures emit telemetry and create incident or workflow item. |
| Sharing | Shared packages must reference contract version and recipient scope. |
| AI usage | AI access must check permitted AI purposes in the contract. |

## Contract Example

```yaml
contract_id: customer_profile.v1
name: Customer Profile Data Product
domain: customer
owner: customer-data-product-team
status: approved
version: 1.0.0
purpose: Governed customer profile data for analytics, applications, and approved AI retrieval.
classification:
  sensitivity: confidential
  personal_data: true
  ai_use:
    retrieval: allowed_with_approval
    training: prohibited
schema:
  - name: customer_id
    type: string
    nullable: false
    description: Stable customer identifier.
  - name: customer_segment
    type: string
    nullable: false
    allowed_values: [enterprise, small_business, consumer]
quality_rules:
  - id: customer_id_not_null
    dimension: completeness
    rule: customer_id must not be null
    severity: critical
freshness:
  expected_frequency: daily
  slo: available_by_08_00_business_day
access_policy:
  default: restricted
  masking:
    email: masked_unless_approved
compatibility:
  breaking:
    - removing a field
    - changing field meaning
    - reducing freshness SLO
observability:
  required_metrics:
    - freshness_minutes
    - quality_pass_rate
    - consumer_query_count
```

## Breaking Change Rules

| Change | Default Classification |
| --- | --- |
| Add nullable field | Non-breaking |
| Add required field | Breaking |
| Remove field | Breaking |
| Rename field | Breaking |
| Change field type | Breaking |
| Change business meaning | Breaking |
| Tighten classification | Breaking for consumers without approval |
| Reduce freshness | Breaking |
| Add stricter quality rule | Potentially breaking |

## Versioning Rules

| Version Change | Use When | Consumer Impact |
| --- | --- | --- |
| Patch | Documentation clarification or non-behavioral metadata update. | No migration required. |
| Minor | Backward-compatible field or rule addition. | Consumers may opt in. |
| Major | Breaking schema, semantic, quality, access, or freshness change. | Migration plan required. |

## Contract Testing

Every contract should have automated or semi-automated tests for:

- Schema compatibility.
- Required fields and nullability.
- Primary key or uniqueness rules.
- Allowed values and reference integrity.
- Quality thresholds.
- Freshness expectations.
- Access and masking behavior.
- AI usage permission checks where applicable.
- Backward compatibility against subscribed consumers.

## Approval Rules

- Source contracts require source owner and steward approval.
- Product contracts require product owner, steward, and platform review.
- Sensitive contracts require security and privacy review.
- AI-enabled contracts require AI usage review.
- Breaking changes require impacted consumer notification and migration plan.

## Minimum Done Criteria

A contract is ready for publication when:

- Required fields are complete.
- Owner, steward, and support contacts are assigned.
- Schema, semantics, quality rules, access policy, and compatibility rules are defined.
- Contract tests pass.
- Required approvals are recorded.
- Consumers can subscribe to changes.
- Contract version is linked to catalog entry, product, pipeline, and observability signals.
- Canonical contract validates against the pinned ODCS schema and passes the portability round-trip test.

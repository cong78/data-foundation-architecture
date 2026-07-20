# Data Product Template

Use this template when proposing, designing, approving go-live, or publishing an aggregate or consumer-aligned data product. The product definition and delivery promise form one Data Product Creation Contract.

## Data Product Creation Contract

### Embedded Product Descriptor

This section is the ODPS-compatible product descriptor inside the contract. It shares the contract id, version, approval, lifecycle, and change history; do not publish it as a separately governed artifact.

| Field | Value |
| --- | --- |
| Product name |  |
| Product id |  |
| Domain |  |
| Product owner |  |
| Data steward |  |
| Technical owner |  |
| Support contact |  |
| Escalation path |  |
| Lifecycle state | Draft / Review / Go-live approved / Active / Deprecated / Retired |
| Intended consumers |  |
| Primary use cases |  |
| Prohibited use cases |  |

### Contract Identity

| Field | Value |
| --- | --- |
| Contract id |  |
| Contract version |  |
| Contract status | Draft / Review / Approved / Published / Deprecated / Retired / Exception |
| Compatibility rules |  |
| Breaking change process |  |
| Consumer notification period |  |

## Business Definition

Describe the business concept represented by the product. Include what the product is and what it is not.

## Product Outcome

| Field | Value |
| --- | --- |
| Consumer problem |  |
| Expected business or operational outcome |  |
| Value measure and baseline |  |
| Existing products considered |  |
| Why a new or changed product is required |  |
| Explicit non-goals |  |

## Product Quality Assessment

| Quality | Acceptance Statement | Status | Evidence |
| --- | --- | --- | --- |
| Discoverable | Intended consumers can find the product using their business language and use case. |  |  |
| Addressable | Product and ports have stable, provider-independent identifiers. |  |  |
| Understandable | Meaning, grain, metrics, limitations, quality and usage are clear. |  |  |
| Natively accessible | A representative consumer uses an approved interface through familiar tools. |  |  |
| Trustworthy | Contract, lineage, quality, freshness, availability and support are proven. |  |  |
| Interoperable | Artifacts and interfaces pass applicable independent conformance tests. |  |  |
| Independent | Purpose, ownership, ports, dependencies, lifecycle and value are explicit. |  |  |
| Secure | Named-user and workload access, obligations, expiry, audit and revocation are proven. |  |  |

## Semantic Context

| Field | Value |
| --- | --- |
| Context id and version |  |
| Product grain |  |
| Time meaning |  |
| Business concept references |  |
| Governed metric references |  |
| Key relationships |  |
| Valid uses |  |
| Prohibited uses |  |
| Known limitations |  |
| Lineage and health references |  |

## Source and Lineage

| Source | Owner | Ingestion Pattern | Contract | Classification |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Product Go-Live Gates

| Gate | Status | Evidence |
| --- | --- | --- |
| Ownership gate |  |  |
| Purpose gate |  |  |
| Contract gate |  |  |
| Quality gate |  |  |
| Security gate |  |  |
| Lineage gate |  |  |
| Observability gate |  |  |
| Documentation gate |  |  |
| Semantic context gate |  |  |
| Portability gate |  |  |
| Product qualities gate |  |  |

## Open Interfaces

| Port | Type | Open Specification | Contract | Endpoint or Artifact |
| --- | --- | --- | --- | --- |
|  | Input / Output |  |  |  |

## Quality Rules

| Rule | Dimension | Threshold | Severity | Owner |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Access and Usage

| Access-Control Field | Value |
| --- | --- |
| Service operations and action ids |  |
| Named-user access pattern |  |
| Workload identity access pattern |  |
| Delegated or agent access |  |
| Data enforcement points |  |
| Row, column, field, or output obligations |  |
| Purpose and Data Product Consumption Contract requirements |  |
| Default entitlement duration |  |
| Revocation target |  |

| Consumer Type | Access Pattern | Approval Needed | Notes |
| --- | --- | --- | --- |
| BI |  |  |  |
| Application |  |  |  |
| Platform |  |  |  |
| AI agent or model |  |  |  |

## AI Readiness Profile

Complete this section only when an AI use is proposed. Approval applies to the declared use, not to every possible AI workload.

| Field | Value |
| --- | --- |
| AI use-case owner |  |
| Outcome, user, decision or action |  |
| Pattern | Retrieval / Grounding / Feature / Training / Fine-tuning / Evaluation / Agent tool context |
| Product and contract versions |  |
| Live data or immutable snapshot |  |
| Selected scope and minimization rationale |  |
| Model, agent, skill and workload identities |  |
| Risk tier and harmful outcomes |  |
| Approved and prohibited uses |  |
| Projection ids and versions |  |
| Evaluation set, metrics and release thresholds |  |
| Approval status, conditions, expiry and review date |  |

| AI Readiness Gate | Status | Evidence | Owner |
| --- | --- | --- | --- |
| Purpose and product binding |  |  |  |
| Rights, classification and minimization |  |  |  |
| Meaning, lineage and reproducibility |  |  |  |
| Quality, representativeness and time behavior |  |  |  |
| Identity, policy and revocation |  |  |  |
| Projection integrity |  |  |  |
| Evaluation and runtime safeguards |  |  |  |
| Observability, change and lifecycle |  |  |  |

Use the [AI-Ready Data Product Checklist](../standards/ai-ready-data-standard.md#ai-ready-data-product-checklist) for pass criteria. A failed blocking gate means the product is not approved for the declared AI purpose, even when it remains approved for BI or analytics.

## Consumers and Subscriptions

| Consumer | Use Case | Access Pattern | Contact | Notification Required |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Observability

| Signal | Target |
| --- | --- |
| Freshness SLO |  |
| Quality pass rate |  |
| Availability SLO |  |
| Incident owner |  |
| Dashboard link |  |

## Go-Live Evidence

- Owner assigned.
- Steward assigned.
- Contract approved.
- Contract tests passing.
- Quality rules passing.
- Classification reviewed.
- Access policy approved.
- Lineage available.
- Product health dashboard available.
- Consumer documentation published.
- Active consumers registered.
- The publishing data contract and its embedded product descriptor validate against pinned open schemas.
- Required interoperability conformance record is approved.
- Exception status reviewed.

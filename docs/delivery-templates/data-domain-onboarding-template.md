# Data Domain Onboarding Record

Use this record to register a data domain, decide whether it can use foundation services, establish its maturity baseline, and manage its improvement plan. Store the completed record in the Data Service Portal and link every decision to authoritative evidence.

## Domain Identity

| Field | Value |
| --- | --- |
| Domain name |  |
| Stable domain id |  |
| Business purpose |  |
| Lifecycle state | Candidate / Registered / Enabled / Producing / Operating / Offboarding |
| Domain owner |  |
| Product portfolio owner |  |
| Lead data steward |  |
| Technical lead |  |
| Risk, privacy and security contact |  |
| Support and escalation route |  |
| Cost owner |  |
| Review forum and cadence |  |

## Boundary and Relationships

| Field | Value |
| --- | --- |
| Business capabilities and concepts in scope |  |
| Explicit exclusions |  |
| Key source systems and source owners |  |
| Existing and proposed products |  |
| Priority consumers and use cases |  |
| Upstream and downstream domains |  |
| Overlaps with existing domains |  |
| Authoritative products for shared concepts |  |
| Proposed boundary decision |  |

## Governance Context

| Field | Value |
| --- | --- |
| Classification baseline |  |
| Personal or sensitive data |  |
| Regulatory and legal obligations |  |
| Residency and regional constraints |  |
| Retention and deletion requirements |  |
| External-sharing constraints |  |
| Approved AI usage constraints |  |
| Required assurance or validation |  |

## Admission Gates

| Gate | Acceptance evidence | Status | Decision or gap |
| --- | --- | --- | --- |
| Identity | Stable domain id and non-duplicative name. |  |  |
| Boundary | In-scope concepts, exclusions, source relationships and overlaps reviewed. |  |  |
| Accountability | Domain owner, portfolio owner, steward, technical lead and escalation route accepted. |  |  |
| Value | First use case, consumers, expected outcome and value measure identified. |  |  |
| Governance | Classification, privacy, legal, residency, retention and sharing context reviewed. |  |  |
| Access | Named-user and workload identity model, policy boundary, expiry and revocation are enforceable. |  |  |
| Operations | Support tier, service levels, incident ownership, continuity and observability agreed. |  |  |
| Funding | Cost owner, allocation model, quotas and initial capacity accepted. |  |  |

An unresolved identity, boundary, accountability, governance, access, or operations gate blocks enablement. Record any conditional acceptance with an owner and expiry.

## Foundation Capability Profile

| Capability | Required profile | Owner | Provisioning evidence | Conformance status |
| --- | --- | --- | --- | --- |
| Data Service Portal |  |  |  |  |
| Data ingestion |  |  |  |  |
| Data product creation |  |  |  |  |
| Unified data access and consumption |  |  |  |  |
| Data sharing |  |  |  |  |
| Data observability |  |  |  |  |
| Catalog, semantics and context |  |  |  |  |
| Contract, policy and identity |  |  |  |  |

## Maturity Baseline

Complete the [Data Foundation Maturity Assessment](../assessments/data-foundation-maturity-assessment.md) using this domain as the assessment scope.

| Dimension | Score | Key evidence | Priority gap | Target |
| --- | --- | --- | --- | --- |
| Direction and ownership |  |  |  |  |
| Foundation services |  |  |  |  |
| Data products and contracts |  |  |  |  |
| Access, security and governance |  |  |  |  |
| Observability and operations |  |  |  |  |
| Interoperability and AI enablement |  |  |  |  |
| Overall |  | Assessment record: |  |  |

Do not use only the overall score. A critical gap in one dimension remains visible and may become an admission condition even when the average is high.

## First Product Proof

| Field | Value |
| --- | --- |
| Product and contract id |  |
| Source and ingestion pattern |  |
| Product creation profile |  |
| Consumption or sharing port |  |
| Representative consumer |  |
| Go-live evidence |  |
| Service and product telemetry |  |
| Support and incident route |  |
| Expected outcome and measure |  |

## Improvement Plan

| Improvement | Maturity dimension | Owner | Target evidence | Due date | Dependency | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Decision

| Field | Value |
| --- | --- |
| Decision | Register / Enable / Enable with conditions / Block / Offboard |
| Decision rationale |  |
| Conditions and expiries |  |
| Approved service profiles |  |
| Exceptions and risk acceptance |  |
| Decision owner and date |  |
| Next maturity review |  |

## Completion Checklist

- Domain identity and boundary are approved.
- Accountable roles and support are accepted.
- Admission gates have evidence and decisions.
- Foundation service profiles and cost allocation are agreed.
- Baseline maturity is scored by dimension.
- First product proof is selected or complete.
- Improvement actions have owners, target evidence and dates.
- Portal record, review cadence and next decision are active.

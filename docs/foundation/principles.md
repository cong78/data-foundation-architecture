# Principles

These principles guide architecture decisions across the data foundation. They apply to ingestion, product creation, consumption, sharing, observability, governance, and operations. Principles express direction; the [Architecture Policy Language](../standards/architecture-policy-language.md) translates that direction into enforceable rules and testable criteria.

## Principle Summary

| Principle | Decision Direction |
| --- | --- |
| Data is managed as a product | Trusted datasets are managed with accountable owners, intended consumers, quality expectations, documentation, access rules, and lifecycle states. |
| Governance is built in | Platform Enablement makes security, privacy, classification, lineage, retention, identity, and quality controls reusable; lifecycle services enforce them in context. |
| Standard patterns come first | Approved ingestion, product, consumption, sharing, and observability patterns are the default; deviations are explicit exceptions. |
| Metadata is a first-class asset | Business, technical, operational, and governance metadata is captured throughout the lifecycle. |
| Consumption is fit for purpose | BI, applications, platforms, AI agents, and models receive access through patterns designed for their needs. |
| Data contracts protect consumers | Interfaces are explicit, versioned, tested, and communicated before change. |
| Open by contract | Canonical product, contract, metadata, lineage, telemetry, API, and event artifacts use open specifications and tested export paths. |
| The portal is the front door | Users interact with foundation services through a consistent portal for discovery, requests, contracts, and workflow status. |
| Trust is observable | Freshness, quality, usage, incidents, lineage, and ownership are visible to owners and consumers. |
| Security follows the data | Access control, masking, purpose limitation, and audit logging travel with the data. |
| AI readiness is designed | Data is made usable for AI through semantics, lineage, quality, policy, and telemetry. |

## Applying Principles

Use principles in architecture reviews, product go-live decisions, platform design, and exception handling. For an enforceable decision, link the principle to an architecture policy containing atomic rules, executable criteria, named decisions, and evidence. When a design conflicts with an active rule, record the policy id and version with:

- Reason for the exception.
- Risk and compensating controls.
- Owner and expiry date.
- Migration path back to the standard pattern.

Use the [Open Interoperability Standard](../standards/open-interoperability-standard.md) when a decision introduces a product format, interface, platform dependency, or cross-company exchange.

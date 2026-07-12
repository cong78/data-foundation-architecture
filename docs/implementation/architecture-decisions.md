# Architecture Decisions

This page defines the key architecture decisions that should be made explicitly. Each decision should be captured as an architecture decision record when it affects platform direction, governance, security, or reuse.

## Decision Map

| Decision | Recommended Direction | Rationale |
| --- | --- | --- |
| User entry point | Use the Data Service Portal for discovery, requests, contracts, and workflow status. | Prevents fragmented access paths and creates consistent evidence. |
| Portal interaction model | Organize journeys by user intent and bind them to domain team, use case, workspace, product, purpose, and evidence. | Makes complex foundation services understandable and reusable. |
| Portal state | Limit portal-owned state to experience, drafts, preferences, tasks, and rebuildable read projections. | Prevents the experience layer from becoming a competing control plane. |
| Product detail | Present declared contract terms separately from measured quality, health, lineage, incidents, usage, and cost. | Prevents synthetic or stale trust claims. |
| Metadata authority | Use catalog and metadata services as the source of truth for product metadata. | Avoids duplicate product inventories. |
| Contract authority | Use a data contract registry as the source of truth for schemas, semantics, quality rules, compatibility, and lifecycle. | Enables automated validation and change management. |
| Canonical artifacts | Store contracts and products in open, machine-readable canonical formats; generate vendor objects from them. | Keeps meaning portable across tools and platforms. |
| Interface definitions | Use OpenAPI for synchronous APIs and AsyncAPI plus CloudEvents for event interfaces. | Makes interfaces discoverable, testable, and independently consumable. |
| Metadata and lineage exchange | Support DCAT catalog export and OpenLineage runtime events. | Enables catalog federation and replaceable lineage backends. |
| Identifier strategy | Use stable product, contract, dataset, source, consumer, purpose, run, and trace identifiers across every plane. | Preserves correlation through migration and sharing. |
| Extension strategy | Namespace enterprise extensions and preserve unknown fields during import and export. | Allows local controls without forking open semantics. |
| Ingestion patterns | Standardize file inbox push, connector pull, API extraction, CDC, and streaming. | Covers most integration needs while reducing custom pipelines. |
| Data product boundary | Publish products around reusable business concepts, not around pipeline outputs. | Improves discoverability, ownership, and reuse. |
| AI access | Route AI access through governed consumption patterns with service identity and purpose approval. | Keeps AI usage auditable and policy-controlled. |
| Agent boundary | Route assistant and agent execution through one policy-enforced Agent Gateway. | Centralizes identity, budgets, authorization, approval, audit and suspension. |
| Skill contract | Expose foundation actions as typed, versioned, least-privilege skills over stable service APIs. | Makes agent behavior testable and reusable. |
| LLM abstraction | Reference approved enterprise LLM profiles rather than provider model names in business logic. | Supports routing, portability, policy and rollback. |
| Agent autonomy | Default to read, recommend and draft; require explicit approval for consequential actions. | Limits excessive agency and preserves accountability. |
| Observability | Use OpenTelemetry-compatible telemetry for foundation services and data products. | Creates consistent operational and trust signals. |
| Sharing | Share from live products using recipient-specific packaging and revocable entitlements. | Reduces risk and improves auditability. |
| Technology selection | Select named products only after capability mapping, mandatory gates, weighted assessment, representative proof, TCO and exit review. | Prevents feature-led selection and makes vendor trade-offs evidence-based. |

## ADR Template

```md
# ADR-000: Decision Title

## Status

Proposed | Accepted | Deprecated | Replaced

## Context

What problem are we solving? What constraints matter?

## Decision

What decision was made?

## Consequences

What improves? What trade-offs or risks remain?

## Evidence

Which policies, product requirements, prototypes, or reviews support the decision?

## Review Date

When should this decision be revisited?
```

## High-Risk Decisions

These decisions require architecture and governance review:

- Allowing direct raw data access for consumers.
- Bypassing the Data Service Portal for access approval.
- Publishing a product without a contract or owner.
- Using AI training or retrieval data without approved purpose.
- Sharing data externally without expiry, revocation, and audit.
- Emitting sensitive data into traces, logs, metrics, or events.
- Creating a new ingestion or consumption pattern outside standard patterns.
- Selecting a platform feature without a canonical export or tested exit path.
- Selecting a vendor or technology without approved requirements, knockout gates, proof-of-capability, TCO, and an exit plan.
- Storing canonical product, contract, policy, entitlement, lineage, or observability state only in the portal.
- Presenting inferred or simulated health, usage, quality, or lineage as measured evidence.
- Giving an agent direct database, platform administrator, or unrestricted network access.
- Allowing retrieved content or tool output to change authorization, autonomy or approval requirements.

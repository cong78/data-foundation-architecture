# Architecture Decisions

This page defines the key architecture decisions that should be made explicitly. Each decision should be captured as an architecture decision record when it affects platform direction, governance, security, or reuse.

## Decision Register

| ADR | Decision | Status | Owner | Review date | Affected areas |
| --- | --- | --- | --- | --- | --- |
| [ADR-001](../decisions/adr-001-central-federated-ownership.md) | Centralize ingestion and source-aligned products; federate aggregate and consumer-aligned products. | Accepted | Data Foundation Architecture | 2027-07-15 | Ownership, ingestion, domains, product creation |
| [ADR-002](../decisions/adr-002-unity-catalog.md) | Use Unity Catalog as the technical catalog and unified authorization standard. | Accepted | Data Platform Architecture | 2027-07-15 | Catalog, access, lineage, products, AI assets |
| [ADR-003](../decisions/adr-003-delta-storage.md) | Use Delta as the default durable tabular storage format. | Accepted | Data Platform Architecture | 2027-07-15 | Storage, product workloads, recovery, interoperability |
| [ADR-004](../decisions/adr-004-unified-data-access.md) | Place governed product ports and a unified access layer above physical storage. | Accepted | Data Access Architecture | 2027-07-15 | Consumption, identity, policy, product ports |
| [ADR-005](../decisions/adr-005-observability-platforms.md) | Use Grafana Cloud for system observability and Databricks plus Unity Catalog for product observability, connected by OpenTelemetry. | Accepted | Observability Architecture | 2027-07-15 | Telemetry, operations, product trust, incidents |

An ADR records one consequential decision. The broader map below remains a decision backlog: create another ADR when a listed direction becomes adopted, changes a public interface, or requires migration and evidence.

## Decision Map

| Decision | Recommended Direction | Rationale |
| --- | --- | --- |
| Architecture policy | Express principles, rules, and criteria through the Architecture Policy Language; keep the YAML or JSON envelope canonical and use OPA and Rego as the default execution profile. | Makes architecture guidance readable, testable, portable, and enforceable without coupling its meaning to one evaluator. |
| User entry point | Use the Data Service Portal for discovery, requests, contracts, and workflow status. | Prevents fragmented access paths and creates consistent evidence. |
| Portal interaction model | Organize journeys by user intent and bind them to domain team, use case, workspace, product, purpose, and evidence. | Makes complex foundation services understandable and reusable. |
| Portal state | Limit portal-owned state to experience, drafts, preferences, tasks, and rebuildable read projections. | Prevents the experience layer from becoming a competing control plane. |
| Product detail | Present declared contract terms separately from measured quality, health, lineage, incidents, usage, and cost. | Prevents synthetic or stale trust claims. |
| Data catalog | Use Unity Catalog as the standard technical catalog for foundation-managed data and AI assets, including governed external or synchronized projections. | Creates one technical inventory, namespace, native policy surface, lineage context, and audit boundary. |
| Physical table storage | Use Unity Catalog managed Delta tables by default for new durable tabular data; approve exceptions for justified external, federated, operational, non-tabular, event, or Iceberg needs. | Standardizes reliability and operations while preserving fit-for-purpose interfaces and controlled interoperability. |
| Metadata authority | Keep product, contract, semantic, policy, and telemetry authorities portable and project their identifiers and selected state into Unity Catalog. | Prevents the technical catalog from becoming an unexportable duplicate control plane. |
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

## Applicable Policy Decisions

Which policy ids and versions apply, what decision did each return, and where is the evidence record?

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
- Creating a durable production table outside Delta or leaving a live asset unregistered in Unity Catalog without an approved exception.
- Storing canonical product, contract, policy, entitlement, lineage, or observability state only in the portal.
- Presenting inferred or simulated health, usage, quality, or lineage as measured evidence.
- Giving an agent direct database, platform administrator, or unrestricted network access.
- Allowing retrieved content or tool output to change authorization, autonomy or approval requirements.

# Data Consumption Service

## Definition

The data consumption service makes trusted data available to consumers through fit-for-purpose access patterns. It supports BI, applications, platforms, AI agents, and AI models without requiring every consumer to build custom extraction logic.

It implements the [Unified Access Design](../architecture/unified-access-design.md): one governed logical access contract above distributed physical data-product storage and runtimes.

For a selected implementation profile, see [Data Consumption Design](../architecture/data-consumption-design.md), which maps this service to Unity Catalog, SQL warehouses, open table and sharing interfaces, and conformant non-SQL adapters.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Governed SQL, API, file, event, semantic, feature, and retrieval access patterns. | Building the final BI dashboard, application feature, or AI model. |
| Access request, policy enforcement, masking, usage telemetry, and consumer experience signals. | Approving business purpose outside the governance workflow. |
| Named-user, workload, delegated, agent, and model access with separate service and data decisions. | Enterprise identity lifecycle or source-system account administration. |
| AI-ready data access for retrieval, grounding, training, evaluation, and agent use. | Model architecture, prompt design, or model deployment platforms. |

## Consumer Channels

| Channel | Typical Use | Architecture Needs |
| --- | --- | --- |
| BI and reporting | Dashboards, self-service analysis, management reporting. | SQL access, semantic layer, governed metrics, row-level security. |
| Applications | Operational or customer-facing experiences. | APIs, low-latency access, service-level objectives, change contracts. |
| Platforms | Reuse by internal company platforms. | Product APIs, bulk access, event subscriptions, tenancy controls. |
| AI agents and models | Retrieval, grounding, training, evaluation, feature use. | Metadata-rich access, policy enforcement, lineage, freshness, evaluation datasets. |

## Open Interface Profiles

| Channel | Interface Profile |
| --- | --- |
| API | OpenAPI definition with standard authentication and error semantics. |
| Event | AsyncAPI channel definition with CloudEvents envelope. |
| Table | Open table metadata and catalog interface where supported. |
| Query | SQL plus an open transport such as Arrow Flight SQL where high-speed portability is required. |
| File | Documented open format, schema, checksums, partitioning, and manifest. |
| AI | Governed context, feature, or retrieval API linked to product, contract, snapshot, identity, and purpose. |
| Semantic context | Context API exposing product meaning, grain, metrics, relationships, limitations, and evidence references with policy filtering. |

## Core Capabilities

- Data discovery and access request workflow.
- SQL, API, file, event, semantic, feature, and retrieval access patterns.
- Policy enforcement at query, API, and dataset levels.
- Separate service-operation and product-data authorization for every access path.
- Row-level and column-level security.
- Data masking and purpose-based access.
- Usage monitoring and cost visibility.
- Data freshness and quality indicators for consumers.
- AI-ready interfaces such as feature datasets, retrieval indexes, and governed context APIs.
- Versioned semantic context APIs linked to product and contract versions.
- Consumer telemetry for usage, latency, errors, access decisions, and downstream dependency impact.
- Stable product and port resolution independent of provider-native paths.
- Runtime adapter selection, policy pushdown, federated execution where required, and fail-closed obligation handling.

## Unified Access Responsibilities

| Logical Capability | Consumption Service Behavior |
| --- | --- |
| Entry | Offer consistent SQL, API, event, file, semantic, feature, retrieval, and context interfaces. |
| Resolve | Map product and port ids to approved contract, semantic context, policy, health, and runtime binding. |
| Authorize | Enforce service operation first, then data action, purpose, entitlement, and obligations. |
| Execute | Route to the approved physical runtime and push down safe query and policy operations. |
| Validate | Enforce request, response, schema, contract, output, and minimization rules. |
| Observe | Emit decision, adapter, physical execution, usage, cost, lineage, and consumer outcome evidence. |

## Architecture Guidance

Consumption should be based on live data products where possible. Direct access to raw or source-aligned data should be controlled and treated as an exception unless the consumer is building or operating a data product.

For AI workloads, consumption must be secure, traceable, and meaningful to models and agents. Access policies must apply to service accounts and agent identities, not only human users.

Use the [AI-Ready Data Standard](../standards/ai-ready-data-standard.md) when designing retrieval, training, evaluation, feature, or grounded answer patterns.

Use the [Semantic and Context Design](../architecture/semantic-context-design.md) to keep BI, application, platform, and AI interpretations consistent without introducing a duplicate metadata authority.

Use the [Unified Access Design](../architecture/unified-access-design.md) for named-user, workload, delegated, agent, and external access. A service permit never overrides a data deny.

## Controls

- Consumer has an approved access purpose.
- Data product classification permits the requested usage.
- Access is enforced through approved platform patterns.
- Sensitive fields are masked, tokenized, aggregated, or blocked as required.
- Usage telemetry is collected and linked to the product and consumer.
- AI use cases are checked for approved training, retrieval, grounding, or evaluation usage.

## Done Criteria

- Consumer can access data through an approved pattern.
- Access decision and policy enforcement are auditable.
- Named-user and system access preserve actor, subject, purpose, product, interface, policy version, obligations, and outcome.
- Freshness, quality, and product status are visible to the consumer.
- Usage is observable by product owner and platform team.
- Downstream dependency is recorded for impact analysis.
- An independent client can consume the declared open interface without a provider-specific SDK.
- The same logical product port can be rebound to another conformant physical runtime without changing the consumer contract.
- Every runtime adapter proves identity propagation, authorization obligations, contract enforcement, telemetry, and fail-closed behavior.

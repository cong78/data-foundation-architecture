# Architecture Design Map

<div class="decision-brief"><div><small>Use when</small><strong>Locating the design authority for a service or cross-service concern.</strong></div><div><small>Decision</small><strong>Is this a service, shared-capability, or integration design?</strong></div><div><small>Owner</small><strong>Architecture owner with service owners.</strong></div><div><small>Output</small><strong>Named design, target planes, interfaces, and evidence.</strong></div></div>

The architecture uses three complementary design classes. Every production change identifies one primary class and links any supporting designs. The [Architecture Blueprint](target-architecture.md) is the composition view that places all three classes into six planes.

## Three Design Classes

| Design Class | Defines | Primary Question | Completion Evidence |
| --- | --- | --- | --- |
| **Service-specific design** | One service boundary, owned capabilities, interfaces, controls, SLOs, failure modes, and evidence. | What does this service own and how does it behave? | Approved service design linked to the service contract, APIs or events, SLOs, controls, and runbooks. |
| **Shared capability design** | Reusable structures used by several services: product and contract models, catalog, storage, identity, policy, semantics, access, telemetry, and developer paths. | Which capability should be provided once rather than reimplemented by each service? | Stable shared model, authority map, reusable interfaces, policy decisions, and conformance tests. |
| **Integration design** | Cross-service interactions, handoffs, workflow authority, identifiers, failure behavior, and end-to-end evidence. | How do independently owned services complete one outcome safely? | Versioned interaction contract, sequence, correlation model, failure ownership, and end-to-end test. |

These classes are not architecture layers or delivery stages. A service-specific design may span several target planes; a shared capability supports several services; an integration design crosses both.

Every service-specific design includes an **Agentic Interaction** contract. It names the service specialist agent, applicable data contracts, typed skills, autonomy ceiling, mandatory deferral points, and deterministic fallback. The Data Service AI Assistant coordinates these agents but does not absorb their service ownership.

## Service to Design Map

| Foundation Service | Service-Specific Design and Reference Profile | Supporting Shared Capabilities | Primary Integration Flows | Target Planes |
| --- | --- | --- | --- | --- |
| [Data Service Portal](../services/data-service-portal.md) | Canonical technology-neutral service design on the service page. | Data contract, lifecycle, semantic context, identity, and workflow authority. | Discover and request; onboard; product go-live; support engagement. | Experience, Control, Security |
| [Data Service AI Assistant](../services/data-service-ai-assistant.md) | Canonical technology-neutral service design on the service page. | [Agentic Data Service Design](agentic-data-foundation.md), semantic context, unified access, identity, policy, skill registry, and approved model profiles. | Ask and explain; plan; approved typed action; evidence retrieval. | Experience, AI, Control, Security, Observability |
| [Data Ingestion Service](../services/data-ingestion-service.md) | Canonical service design; [Databricks reference profile](../reference-solutions/data-ingestion-design.md). | Data foundation model, ingestion contract, catalog and storage, identity, and telemetry. | Source onboarding; source change; validated source-aligned handoff. | Data, Control, Security, Observability |
| [Data Product Creation Service](../services/data-product-creation-service.md) | Canonical service design; [Databricks reference profile](../reference-solutions/data-product-creation-design.md). | Product lifecycle, creation contract, domain model, semantic context, developer experience, catalog, and storage. | Create or change product; compatibility review; product go-live; rollback. | Data, Control, Security, Observability |
| [Data Consumption Service](../services/data-consumption-service.md) | Canonical service design; [Databricks reference profile](../reference-solutions/data-consumption-design.md). | Unified access, semantic context, consumption contract, identity, policy, and catalog. | Discover and subscribe; authorize; resolve port; serve; revoke. | Data, Control, Security, AI, Observability |
| [Data Sharing Service](../services/data-sharing-service.md) | Canonical service design; [Databricks reference profile](../reference-solutions/data-sharing-design.md). | Consumption contract, classification, identity federation, policy, retention, and telemetry. | Approve recipient; package; deliver; monitor; revoke and offboard. | Data, Control, Security, Observability |
| [Platform Enablement Service](../services/platform-enablement-service.md) | Canonical technology-neutral service design on the service page. | [Shared Platform Capabilities](platform-foundation-design.md), including contract, catalog, storage, identity, security, integration, automation, and evidence capabilities. | Provision; bind controls; reconcile; rotate; retain; delete; deprovision. | Control, Data, Security, Observability |
| [Data Observability Service](../services/data-observability-service.md) | Canonical service design; [Databricks and Grafana reference profile](../reference-solutions/observability-design.md). | OpenTelemetry conventions, product identity, lineage, SLOs, catalog context, and evidence retention. | Emit and correlate; detect; assess product impact; restore evidence. | Observability across every plane |
| [Data Foundation Operations Service](../services/data-foundation-operations-service.md) | Canonical technology-neutral service design on the service page. | Service ownership, support model, telemetry, change authority, continuity, and runbooks. | Support; incident; problem; change; release; recovery; improvement. | Experience, Control, Observability, Security |

Each service page is authoritative for the definition, boundary, architecture, capabilities, contracts, integrations, controls, actions, and done criteria. A technology reference solution shows one conformant implementation and cannot redefine the service design.

## Shared Capability Designs

| Shared Design | Reused By | Stable Concern |
| --- | --- | --- |
| [Data Foundation Model](data-foundation-model.md) | Ingestion, creation, consumption, sharing, portal, observability. | Product patterns, ownership boundaries, states, and relationships. |
| [Data Contract Design](data-contract-design.md) | Every lifecycle service, portal, assistant, and control workflow. | Three contract types, lifecycle gates, compatibility, and enforcement. |
| [Data Domain Design](data-domain-design.md) | Portal, creation, governance, portfolio, and operations. | Business accountability, product portfolio, and federated ownership. |
| [Data Product Lifecycle Design](data-product-lifecycle-design.md) | Creation, portal, consumption, sharing, observability, and operations. | Product state, go-live, change, deprecation, and retirement. |
| [Semantic and Context Design](semantic-context-design.md) | Portal, consumption, AI assistant, creation, and observability. | Meaning, metrics, relationships, retrieval context, and authority. |
| [Unified Access Design](unified-access-design.md) | Consumption, sharing, AI, platform enablement, and security. | Logical product ports, identity, policy, runtime adapters, and receipts. |
| [Data Product Developer Experience](data-product-developer-experience.md) | Ingestion, creation, platform enablement, and portal. | Declarative workloads, environments, tests, promotion, and rollback. |
| [Shared Platform Capabilities](platform-foundation-design.md) | Every foundation service. | Reusable control and runtime capabilities with stable provider boundaries. |
| [Agentic Data Service Design](agentic-data-foundation.md) | Every foundation service and the Data Service AI Assistant. | Multi-agent coordination, service-agent ownership, contract-driven autonomy, typed skills, approvals, evaluation, and evidence. |

## Integration Design Scope

Use the [Integration Design](integration-design.md) whenever an outcome crosses service ownership. It defines:

- The initiating service and the service accountable for completion.
- Synchronous APIs, asynchronous events, workflow callbacks, and product ports.
- Contract, product, actor, purpose, workflow, run, trace, release, and incident identifiers.
- Timeout, retry, idempotency, compensation, reconciliation, and degraded-mode behavior.
- Control decisions and obligations at each trust boundary.
- Agent task delegation, contract references, autonomy ceiling, budgets, approval state, and completion ownership when agents collaborate.
- Evidence that proves the end-to-end outcome rather than only local success.

## Traceability Rule

Every architecture change records:

1. One primary service-specific, shared-capability, or integration design.
2. The affected service contracts and target planes.
3. Applicable published standards, policies, and architecture constraints.
4. Required playbook, runbook, and evidence updates.
5. An end-to-end acceptance test when more than one service is involved.

Use [Architecture to Delivery](../foundation/architecture-to-delivery.md) to assign this design trace to an owning data service and carry it into implementation and operation.

<div class="read-next"><strong>Next:</strong> select the service row that owns the outcome, then review its primary design, supporting shared capabilities, and integration flows.</div>

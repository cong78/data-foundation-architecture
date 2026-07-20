# Architecture Design Map

<div class="decision-brief"><div><small>Use when</small><strong>Locating the design authority for a service or cross-service concern.</strong></div><div><small>Decision</small><strong>Is this a service, shared-capability, or integration design?</strong></div><div><small>Owner</small><strong>Architecture owner with service owners.</strong></div><div><small>Output</small><strong>Named design, target planes, interfaces, and evidence.</strong></div></div>

The architecture uses three complementary design classes. Every production change identifies one primary class and links any supporting designs. The [Architecture Blueprint](target-architecture.md) is the composition view that places all three classes into six planes.

## Three Design Classes

| Design Class | Defines | Primary Question | Completion Evidence |
| --- | --- | --- | --- |
| **Service-specific design** | One service boundary, owned capabilities, interfaces, controls, SLOs, failure modes, and evidence. | What does this service own and how does it behave? | Approved service design linked to the service definition, APIs or events, SLOs, controls, and runbooks. |
| **Shared capability design** | Reusable structures used by several services: product and contract models, catalog, storage, identity, policy, semantics, access, telemetry, and developer paths. | Which capability should be provided once rather than reimplemented by each service? | Stable shared model, authority map, reusable interfaces, policy decisions, and conformance tests. |
| **Integration design** | Cross-service interactions, handoffs, workflow authority, identifiers, failure behavior, and end-to-end evidence. | How do independently owned services complete one outcome safely? | Versioned interface specification, sequence, correlation model, failure ownership, and end-to-end test. |

These classes are not architecture layers or delivery stages. A service-specific design may span several target planes; a shared capability supports several services; an integration design crosses both.

Every service-specific design includes an **Agentic Interaction** specification. It names the service specialist agent, applicable data contracts, typed skills, autonomy ceiling, mandatory deferral points, and deterministic fallback. The Data Service AI Assistant coordinates these agents but does not absorb their service ownership.

## Service to Design Map

Read each row from left to right: the **service architecture owns the service and its supporting-design dependencies**, the **integration design owns cross-service handoffs**, and the blueprint shows plane placement.

<div class="service-design-table" markdown>

| Foundation Service | Service Architecture | Primary Integration Flows | [Blueprint Placement](target-architecture.md#service-placement-in-the-target) |
| --- | --- | --- | --- |
| [Data Service Portal](../services/data-service-portal.md) | [Service architecture](../services/data-service-portal.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): discover and request; onboard; product go-live; support engagement. | **Primary:** Experience. **Supporting:** AI, Control, Security; Observability for health views. |
| [Data Service AI Assistant](../services/data-service-ai-assistant.md) | [Service architecture](../services/data-service-ai-assistant.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): ask and explain; plan; approved typed action; evidence retrieval. | **Primary:** Experience, AI. **Supporting:** Control, Security, Observability. |
| [Data Ingestion Service](../services/data-ingestion-service.md) | [Service architecture](../services/data-ingestion-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): source onboarding; source change; delivery and replay; validated source-aligned handoff. | **Primary:** Data. **Supporting:** AI, Control, Security, Observability. |
| [Data Product Creation Service](../services/data-product-creation-service.md) | [Service architecture](../services/data-product-creation-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): propose; provision; build and validate; compatibility review; go-live; rollback or retire. | **Primary:** Data, Control. **Supporting:** AI, Security, Observability. |
| [Data Consumption Service](../services/data-consumption-service.md) | [Service architecture](../services/data-consumption-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): discover and subscribe; authorize; resolve port; serve; renew or revoke. | **Primary:** Data. **Supporting:** Control, Security, AI, Observability. |
| [Data Sharing Service](../services/data-sharing-service.md) | [Service architecture](../services/data-sharing-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): approve recipient and purpose; package; deliver; monitor; revoke and offboard. | **Primary:** Data. **Supporting:** AI, Control, Security, Observability. |
| [Platform Enablement Service](../services/platform-enablement-service.md) | [Service architecture](../services/platform-enablement-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): provision; bind controls; reconcile; rotate; retain; recover; delete or deprovision. | **Primary:** Control, Data. **Supporting:** AI, Security, Observability. |
| [Data Observability Service](../services/data-observability-service.md) | [Service architecture](../services/data-observability-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): emit and correlate; detect; assess product impact; alert; recover and publish evidence. | **Primary:** Observability. **Supporting:** AI and every plane through common identity and telemetry. |
| [Data Foundation Operations Service](../services/data-foundation-operations-service.md) | [Service architecture](../services/data-foundation-operations-service.md#service-architecture). | [Integration Design](integration-design.md#critical-integration-flows): support; incident; problem; change; release; recovery; continuity and improvement. | **Primary:** Experience, Control. **Supporting:** AI, Observability, Security. |

</div>

Each service page is authoritative for the definition, boundary, architecture, capabilities, applicable data contracts, integrations, controls, actions, and target user experience.

## Shared Capability Designs

| Shared Design | Reused By | Stable Concern |
| --- | --- | --- |
| [Data Foundation Model](data-foundation-model.md) | Ingestion, creation, consumption, sharing, portal, observability. | Product patterns, ownership boundaries, states, and relationships. |
| [Data Contract Design](data-contract-design.md) | Every lifecycle service, portal, assistant, and control workflow. | Three contract types, lifecycle gates, compatibility, and enforcement. |
| [Data Domain Design](data-domain-design.md) | Portal, creation, governance, portfolio, and operations. | Business accountability, product portfolio, and federated ownership. |
| [Data Product Design](data-product-design.md) | Creation, portal, consumption, sharing, observability, and operations. | Product definition, boundary, design elements, ownership, lifecycle, and go-live. |
| [Platform Governance Design](platform-governance-design.md) | Every foundation service, product lifecycle, and target plane. | Decision rights, policy intent, enforcement placement, assurance, exceptions, and evidence. |
| [Semantic and Context Design](semantic-context-design.md) | Portal, consumption, AI assistant, creation, and observability. | Meaning, metrics, relationships, retrieval context, and authority. |
| [Unified Access Design](unified-access-design.md) | Consumption, sharing, AI, platform enablement, and security. | Logical product ports, identity, policy, runtime adapters, and receipts. |
| [Developer Experience Design](developer-experience-design.md) | Ingestion, creation, platform enablement, and portal. | Declarative workloads, environments, tests, promotion, and rollback. |
| [Platform Enablement Design](platform-enablement-design.md) | Every foundation service. | Reusable control and runtime capabilities with stable provider boundaries. |
| [Agentic Data Service Design](agentic-data-foundation.md) | Every foundation service and the Data Service AI Assistant. | Multi-agent coordination, service-agent ownership, data-contract-driven autonomy, typed skills, approvals, evaluation, and evidence. |

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
2. The affected service definitions and target planes.
3. Applicable published standards, policies, and architecture constraints.
4. Required playbook, runbook, and evidence updates.
5. An end-to-end acceptance test when more than one service is involved.

Use [Architecture to Delivery](../foundation/architecture-to-delivery.md) to assign this design trace to an owning data service and carry it into implementation and operation.

## Machine-Readable Traceability

The validated [`architecture-registry.yaml`](../assets/data/architecture-registry.yaml) records typed **implements**, **depends on**, **constrained by**, and **participates in** relationships. CI validates entity targets, anchors, duplicate relationships, core-design coverage, and minimum service traceability; the [Information Graph](../foundation/information-graph.md#architecture-information-graph) renders the same relationships.

<div class="read-next"><strong>Next:</strong> select the service row that owns the outcome, then review its primary design, supporting shared capabilities, and integration flows.</div>

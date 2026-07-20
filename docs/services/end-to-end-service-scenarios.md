# End-to-End Service Scenarios

<div class="decision-brief"><div><small>Use when</small><strong>Validating that the foundation works across service boundaries.</strong></div><div><small>Decision</small><strong>Can the complete user outcome be controlled, recovered, and proven?</strong></div><div><small>Owner</small><strong>Architecture owner with participating service and product owners.</strong></div><div><small>Output</small><strong>Accepted sequence, authority chain, failure behavior, and evidence.</strong></div></div>

These scenarios test how foundation services collaborate to complete user outcomes. They are not implementation runbooks or replacements for service-specific architecture. Each scenario must work through stable service interfaces, preserve authority, enforce the applicable contract and policy, and produce correlated evidence.

| Scenario | Starts With | Finishes With | Primary Contract |
| --- | --- | --- | --- |
| Source onboarding | Approved source need | Supported live source-aligned product | Source System Ingestion Contract |
| Domain product creation | Defined consumer outcome | Live aggregate or consumer-aligned product | Data Product Creation Contract |
| Governed consumption | Approved user or workload purpose | Authorized product-port result and receipt | Data Product Consumption Contract |
| AI-agent use and action | Authenticated user goal | Grounded answer or approved service action with trace | Data Product Consumption Contract plus applicable service interface |

Every scenario carries the same evidence envelope: `actor_id`, `purpose_id`, `domain_id`, `product_id`, `contract_id`, `workflow_id`, `policy_decision_id`, `trace_id`, timestamps, outcome, and accountable service.

## 1. Onboard a Source

**Outcome:** the foundation makes source data available as a supported, governed, and observable source-aligned product without taking transaction authority from the source.

| Step | Owning Service | Decision or Control | Required Evidence |
| --- | --- | --- | --- |
| Register intent | [Data Service Portal](data-service-portal.md) | Source, purpose, owner, consumers, classification, and expected value are complete. | Request and source-owner acknowledgement |
| Agree delivery | [Data Ingestion Service](data-ingestion-service.md) | Source System Ingestion Contract defines delivery, schema, change, quality, retention, and support obligations. | Approved contract version |
| Provision path | [Platform Enablement Service](platform-enablement-service.md) | Storage, identity, secrets, connectivity, policy, and telemetry bindings satisfy the approved pattern. | Provisioning plan and receipts |
| Ingest and validate | [Data Ingestion Service](data-ingestion-service.md) | Delivery is authenticated, idempotent, quarantinable, replayable, and contract-conformant. | Run, validation, lineage, and quarantine evidence |
| Bring live | [Data Ingestion Service](data-ingestion-service.md) | Source-aligned product has ownership, ports, SLOs, observability, support, and rollback. | Go-live decision and product-health baseline |

**Failure test:** a breaking source change must be detected before incompatible publication. The ingestion service pauses or quarantines delivery, identifies affected products and consumers, and resumes only after contract resolution and replay evidence.

## 2. Create a Domain Product

**Outcome:** a domain team turns live source-aligned inputs into an aggregate or consumer-aligned product with an independently managed promise.

| Step | Owning Service | Decision or Control | Required Evidence |
| --- | --- | --- | --- |
| Define outcome | [Data Product Creation Service](data-product-creation-service.md) | Consumer problem, owning domain, product type, grain, value, and lifecycle are explicit. | Product proposal and accountable owners |
| Agree product promise | [Data Product Creation Service](data-product-creation-service.md) | Data Product Creation Contract defines inputs, transformations, semantics, quality, ports, compatibility, and support. | Approved contract and product descriptor |
| Build through paved path | [Data Product Creation Service](data-product-creation-service.md) | Workload, environment, identity, storage, policy, and telemetry use approved shared capabilities. | Reproducible plan, build, test, and lineage records |
| Assess readiness | [Data Product Creation Service](data-product-creation-service.md) | Quality, security, compatibility, SLO, semantic context, observability, support, and rollback gates pass. | Go-live evidence set |
| Publish and operate | [Data Product Creation Service](data-product-creation-service.md) | Product, ports, contract, context, health, and support route become discoverable together. | Live lifecycle state and catalog projection |

**Failure test:** when a proposed release breaks a consumer obligation, publication is blocked. The prior product version remains available until the owner approves a compatible change, migration window, or explicit retirement path.

## 3. Consume a Data Product

**Outcome:** a named user or workload receives purpose-bound access through a stable product port without relying on physical storage details.

| Step | Owning Service | Decision or Control | Required Evidence |
| --- | --- | --- | --- |
| Discover product | [Data Service Portal](data-service-portal.md) | Product meaning, fitness, health, ports, terms, and owner are visible for the consumer context. | Product and context versions viewed |
| Declare use | [Data Consumption Service](data-consumption-service.md) | Consumer identity, purpose, requested port, duration, and obligations are complete. | Subscription or access request |
| Decide access | [Data Consumption Service](data-consumption-service.md) | Service authorization and data authorization both allow the request under current policy and contract. | Policy decision, entitlement, and obligations |
| Resolve and serve | [Data Consumption Service](data-consumption-service.md) | Logical port resolves to an approved runtime adapter; masking, minimization, and limits are applied. | Access receipt, runtime trace, and usage telemetry |
| Renew or revoke | [Data Consumption Service](data-consumption-service.md) | Expiry, purpose change, product change, or policy change updates access consistently. | Renewal or revocation evidence |

**Failure test:** a revoked entitlement must stop new access and invalidate active paths within the declared control objective. Denial and revocation evidence must identify the policy, actor, product, port, and enforcement point.

## 4. Use Data Through an AI Agent

**Outcome:** an AI agent uses governed product context and, when authorized, delegates a typed service action without gaining wider authority than the user or contract allows.

| Step | Owning Service | Decision or Control | Required Evidence |
| --- | --- | --- | --- |
| Capture goal | [Data Service AI Assistant](data-service-ai-assistant.md) | User identity, goal, purpose, channel, and requested outcome are explicit. | Conversation and purpose context |
| Ground the plan | [Data Service AI Assistant](data-service-ai-assistant.md) | Product, contract, semantic context, policy, health, and applicable skills are retrieved from authoritative sources. | Cited context versions and retrieval trace |
| Bound delegation | [Data Service AI Assistant](data-service-ai-assistant.md) | Specialist agent, typed skill, data scope, tool scope, budget, autonomy ceiling, and approval state are declared. | Signed task envelope and policy decision |
| Execute or defer | Owning Foundation Service | Deterministic service controls authorize and execute the action, or return a denial, clarification, or approval request. | Tool calls, approvals, service workflow, and control receipts |
| Consolidate result | [Data Service AI Assistant](data-service-ai-assistant.md) | The answer distinguishes facts, inference, decisions, actions, limitations, and remaining ownership. | End-to-end trace, citations, action result, and evaluation |

**Failure test:** prompt content, retrieved context, or another agent cannot widen identity, purpose, contract scope, tool permissions, or autonomy. The service rejects the action, preserves the reason, and offers a governed next step.

## Completion Rule

A scenario is complete only when the user outcome, authority decisions, service state, failure behavior, and evidence agree. Local API success, pipeline completion, model output, or catalog registration alone is insufficient.

Use the [Architecture Decision Process](../decisions/architecture-decision-process.md) to resolve decision ownership and record consequential choices, the [Integration Design](../architecture/integration-design.md) for handoff mechanics, and service pages for service-specific behavior.

<div class="read-next"><strong>Next:</strong> select one scenario and use it as an end-to-end acceptance case for the affected architecture and services.</div>

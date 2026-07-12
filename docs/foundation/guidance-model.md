# Guidance Model

This repository is both an architecture guide and a delivery reference. Follow the architecture path once; use services, standards, governance, and delivery artifacts by task.

## How to Use This Guidance

| Need | Start Here | Outcome |
| --- | --- | --- |
| Understand the foundation | [Definition and Scope](definition-and-scope.md) | Shared language and boundaries |
| Make an architecture decision | [Principles](principles.md) | A consistent decision basis |
| Design the target architecture | [Target Architecture](../architecture/target-architecture.md) and [Reference Architecture](../architecture/reference-architecture.md) | Six-plane model and capability map |
| Design product meaning and context | [Semantic and Context Design](../architecture/semantic-context-design.md) | Versioned semantics, relationships, usage context, and authoritative references |
| Design identity and access | [Access Control Design](../architecture/access-control-design.md) | Named-user and workload identity, service and data decisions, entitlements, and evidence |
| Design logical data access | [Unified Data Access Layer](../architecture/unified-data-access-layer.md) | Provider-independent product ports, policy enforcement, runtime routing, and access evidence |
| Design the portal experience | [Data Service Portal Model](../architecture/data-service-portal-model.md) | Journeys, product experience, agreements, and state boundaries |
| Design the developer experience | [Data Product Developer Experience](../architecture/data-product-developer-experience.md) | Declarative workloads, environments, deployment, rollback, and channel parity |
| Design agentic services | [Agentic Data Foundation](../architecture/agentic-data-foundation.md) and [Data Service AI Assistant](../services/data-service-ai-assistant.md) | Agent, skill, LLM, context, approval, and evaluation boundaries |
| Plan implementation | [Architecture Blueprint](../implementation/implementation-blueprint.md) | Platform components, delivery sequence, and backlog |
| Design a reusable service | [Services Overview](../services/index.md) | Capabilities, controls, integration, and done criteria |
| Apply mandatory rules | [Standards Overview](../standards/index.md) | Concrete contract, product, telemetry, interoperability, and AI rules |
| Prove readiness | [Architecture Dashboard](../assessments/architecture-dashboard.md) | Architecture, industry, and AI-readiness evidence |
| Start delivery | [Runway](../runway.md) and [Templates](../delivery-templates/data-product-template.md) | Sequenced adoption and reusable artifacts |

## Guidance Levels

| Level | Purpose | Examples |
| --- | --- | --- |
| Definition | Establish shared meaning. | What is a data product? What is in scope? |
| Principle | Set durable decision rules. | Governance is built in. Security follows the data. |
| Architecture | Describe logical structure and interaction. | Target planes, reference flow, capability map. |
| Architecture delivery | Translate the target state into components, patterns, and backlog. | Blueprint, patterns, decisions. |
| Service contract | Define reusable platform capabilities. | Portal, ingestion, product creation, consumption, sharing, observability. |
| Standard | Define mandatory details for implementation consistency. | Contract fields, telemetry attributes, AI-ready requirements. |
| Control | Define minimum expectations. | Quality gates, policy enforcement, telemetry hygiene. |
| Operating model | Define how teams work. | Roles, forums, SLOs, service ownership. |

## Standard Service Page Structure

Every service page follows the same pattern:

| Section | Purpose |
| --- | --- |
| Definition | What the service is and why it exists. |
| Scope | What the service owns and does not own. |
| Core capabilities | The reusable capabilities the service must provide. |
| Architecture guidance | How the service should be designed and integrated. |
| Controls | Minimum governance, security, quality, or operational controls. |
| Done criteria | Evidence that the service or product is ready for use. |

## Decision Rules

Use these rules when designs compete:

1. Prefer live, governed data products over direct access to raw or source-aligned data.
2. Prefer standard portal, ingestion, consumption, sharing, and observability patterns over custom workflows or pipelines.
3. Capture metadata, lineage, quality, and telemetry as part of delivery, not as aftercare.
4. Make access policy enforceable by platform services, not only by documentation.
5. Design for both human and machine consumers, including AI agents and models.
6. Keep product ownership close to the business domain, while keeping foundation patterns reusable.
7. Keep canonical artifacts and identifiers independent of platform-native names and paths.
8. Use agents for interpretation and adaptive planning; keep authorization, approval, lifecycle state and irreversible execution deterministic.

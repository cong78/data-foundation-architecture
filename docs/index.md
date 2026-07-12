# Data Foundation Architecture

<div class="brand-lockup">
  <img src="assets/images/data-foundation-logo.svg" alt="Data Foundation Architecture logo">
  <div>
    <strong>Data Foundation Architecture</strong>
    <span>Trusted data products for analytics, applications, platforms, sharing, agents, and models.</span>
  </div>
</div>

Architecture guidance for an **AI-ready data foundation**: open contracts, reusable products, unified access, observable trust, and governed automation.

## Choose Your Path

| I need to... | Start with | Then use |
| --- | --- | --- |
| Understand or review the architecture | [Architecture Overview](architecture/overview.md) | [Target Architecture](architecture/target-architecture.md) and [Reference Architecture](architecture/reference-architecture.md) |
| Design or implement a foundation service | [Services Overview](services/index.md) | The relevant service page, [architecture patterns](implementation/service-implementation-patterns.md), and standards |
| Build and deploy a data product | [Data Product Developer Experience](architecture/data-product-developer-experience.md) | [Data Product Workload Standard](standards/data-product-workload-standard.md) and [workload template](delivery-templates/data-product-workload-template.md) |
| Create and govern a data product | [Data Product Lifecycle](architecture/data-product-lifecycle.md) | [Data Contract Standard](standards/data-contract-standard.md) and [Data Product Template](delivery-templates/data-product-template.md) |
| Design access for users and systems | [Access Control Design](architecture/access-control-design.md) | [Unified Data Access Layer](architecture/unified-data-access-layer.md) and [Access Control Standard](standards/access-control-standard.md) |
| Enable agents, models, or the Data Service AI Assistant | [Agentic Data Foundation](architecture/agentic-data-foundation.md) | [Agent, Skill and LLM Standard](standards/agent-skill-llm-standard.md) and [AI Readiness Assessment](assessments/ai-readiness-assessment.md) |

## Architecture at a Glance

The Data Service Portal is the front door. Six foundation services turn source data into governed products for people, applications, partners, agents, and models.

<div class="foundation-grid">
  <a class="foundation-card" href="services/data-service-portal/"><strong>Portal</strong>Discovery, requests, contracts, workflows, access, and evidence.</a>
  <a class="foundation-card" href="services/data-ingestion-service/"><strong>Ingestion</strong>File, connector, API, CDC, and streaming onboarding.</a>
  <a class="foundation-card" href="services/data-product-creation-service/"><strong>Product creation</strong>Owned, contracted, quality-managed, live data products.</a>
  <a class="foundation-card" href="services/data-consumption-service/"><strong>Consumption</strong>Unified governed access for people, systems, agents, and models.</a>
  <a class="foundation-card" href="services/data-sharing-service/"><strong>Sharing</strong>Controlled internal and external exchange with revocation.</a>
  <a class="foundation-card" href="services/data-observability-service/"><strong>Observability</strong>OpenTelemetry-based system and product insights.</a>
</div>

## How the Guidance Fits Together

| Question | Guidance | Result |
| --- | --- | --- |
| Why and where? | [Definition and Scope](foundation/definition-and-scope.md) and [Principles](foundation/principles.md) | Shared boundaries and decision rules. |
| What is the target? | [Architecture](architecture/overview.md) | Target model, building blocks, flows, and decisions. |
| How is it provided? | [Services](services/index.md) | Reusable service contracts, controls, and done criteria. |
| What is mandatory? | [Standards](standards/index.md) and [Governance](governance/index.md) | Implementable rules, ownership, and evidence. |
| How do we adopt it? | [Delivery](delivery/index.md) | Sequenced delivery, assessments, templates, and examples. |

## Recommended Architecture Path

1. [Definition and Scope](foundation/definition-and-scope.md)
2. [Principles](foundation/principles.md)
3. [Architecture Overview](architecture/overview.md)
4. [Target Architecture](architecture/target-architecture.md)
5. [Reference Architecture](architecture/reference-architecture.md)
6. [Services Overview](services/index.md)
7. [Delivery Runway](runway.md)

Use standards, governance pages, templates, and examples as working references rather than reading them front to back.

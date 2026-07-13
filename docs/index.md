# Data Foundation Architecture

<div class="brand-lockup">
  <div>
    <span>Trusted data products for analytics, applications, platforms, sharing, agents, and models.</span>
  </div>
</div>

Architecture guidance for an **AI-ready data foundation**: open contracts, reusable products, unified access, observable trust, and governed automation.

## Foundation Journey

| Step | Journey stage | Core guidance | Outcome |
| ---: | --- | --- | --- |
| 1 | **Frame the foundation** | [Definition and Scope](foundation/definition-and-scope.md) · [Principles](foundation/principles.md) | Agreed boundaries, ownership model, decision rules, and non-goals. |
| 2 | **Design the target** | [Architecture Overview](architecture/overview.md) · [Target Architecture](architecture/target-architecture.md) · [Reference Architecture](architecture/reference-architecture.md) | Shared layers, planes, building blocks, flows, and control boundaries. |
| 3 | **Organize data domains** | [Data Domain Design](architecture/data-domain-design.md) · [Domain Onboarding Record](delivery-templates/data-domain-onboarding-template.md) · [Maturity Assessment](assessments/data-foundation-maturity-assessment.md) | Registered domains with admission decisions, central-to-federated handoffs, and improvement plans. |
| 4 | **Establish foundation services** | [Services Overview](services/index.md) · [Architecture Patterns](implementation/service-implementation-patterns.md) · [Reference Solutions](architecture/data-ingestion-design.md) | Reusable ingestion, creation, consumption, sharing, and observability capabilities. |
| 5 | **Deliver governed products** | [Product Lifecycle Design](architecture/data-product-lifecycle-design.md) · [Developer Experience](architecture/data-product-developer-experience.md) · [Data Product Management Standard](standards/data-product-management-standard.md) | Contracted, tested, observable products that pass product go-live. |
| 6 | **Enable governed use** | [Unified Access Design](architecture/unified-access-design.md) · [Consumption](services/data-consumption-service.md) · [Sharing](services/data-sharing-service.md) · [Agentic Foundation](architecture/agentic-data-foundation.md) | Purpose-bound access for people, systems, partners, agents, and models. |
| 7 | **Operate and improve** | [Observability Design](architecture/observability-design.md) · [Governance](governance/index.md) · [Delivery Runway](runway.md) | Measured health, accountable operations, prioritized gaps, and continuous improvement. |

Use the journey in order for a new foundation. For an existing capability, enter at the relevant stage and retain traceability to the framing and target decisions.

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

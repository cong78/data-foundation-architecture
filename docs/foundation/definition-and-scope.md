# Definition and Scope

## Definition

The **data foundation** is the enterprise capability that makes company data trusted, reusable, secure, observable, and ready for analytics, applications, platforms, and AI.

It combines:

- Reusable platform services.
- Architecture standards and integration patterns.
- Data product lifecycle guidance.
- Governance, security, and compliance controls.
- Operating model expectations for ownership, support, and reliability.

The data foundation is part of the broader **Data and AI Foundation**. It provides the trusted data layer that AI platforms, BI platforms, business applications, and internal or external data ecosystems can safely consume.

## Scope

The architecture guidance covers six foundation services:

| Service | Primary Responsibility |
| --- | --- |
| Data service portal | Provide the user entry point for data discovery, access requests, data product onboarding, workflow tracking, and data contract management. |
| Data ingestion service | Bring data from source systems into the foundation using governed push, pull, and streaming patterns. |
| Data product creation service | Create trusted, reusable datasets using data product principles. |
| Data consumption service | Make trusted data available through fit-for-purpose access patterns. |
| Data sharing service | Share governed data with internal platforms, customers, suppliers, and partners. |
| Data observability service | Observe data products end to end using system telemetry and data insight telemetry, with OpenTelemetry as the standard. |

## In Scope

- Source onboarding and ingestion patterns.
- Landing, raw, conformed, curated, and product-oriented data zones.
- Data product design, ownership, go-live, and lifecycle management.
- Data service portal experience for discovery, onboarding, access, workflow tracking, and data contract management.
- Metadata, catalog, lineage, classification, quality, and policy controls.
- Consumption patterns for BI, applications, platforms, AI agents, and AI models.
- Secure data sharing across internal and external boundaries.
- End-to-end data product observability using OpenTelemetry-compatible telemetry.
- Operating model, roles, decision forums, and service management.

## Out of Scope

This guidance does not define:

- A mandatory single technology stack.
- Detailed implementation runbooks for a specific cloud or vendor platform.
- Business domain data models for every company domain.
- Application architecture outside data integration and data consumption interfaces.
- AI model architecture, model training platforms, or prompt engineering standards except where they depend on governed data access.

## Design Boundary

The foundation owns the standard path from source data to trusted, governed consumption. Domain teams own the business meaning, quality rules, and product decisions for the datasets they publish.

When a use case needs data, the preferred path is:

1. Onboard the source using a standard ingestion pattern.
2. Create or reuse a live data product.
3. Expose it through a governed consumption or sharing pattern.
4. Manage data contracts, access, approvals, and lifecycle workflows through the portal.
5. Observe the product using common telemetry and SLOs.

# Operating Model

The foundation operating model defines how platform teams, domain teams, and consumers work together.

## Team Responsibilities

| Team | Owns |
| --- | --- |
| Foundation platform team | Shared services, Platform Enablement, source onboarding, ingestion operation, raw and validated source-aligned products, reference patterns, platform reliability, and automation |
| Domain data teams | Aggregate and consumer-aligned products; domain definitions, business quality rules, reuse, value, lifecycle, support, and consumer relationships |
| Source system teams | Source System Ingestion Contracts, source availability, change communication |
| Consumer teams | Responsible consumption, access requests, feedback, use-case controls |
| Governance and risk teams | Policies, exceptions, assurance, audit and compliance evidence |
| Data reliability team | Observability standards, data incident process, SLO reporting, telemetry quality |
| Foundation operations team | Service portfolio, support, incident command, problem, change, release coordination, continuity, communication, reliability practice, and improvement evidence |
| Portal owner | User experience, workflow entry points, portal integrations, and service request usability |

## Central and Federated Accountability

| Capability or product | Accountable owner | Required handoff |
| --- | --- | --- |
| Data Ingestion Service | Foundation platform team | Approved Source System Ingestion Contract and delivery obligations from the source system team. |
| Raw and validated source-aligned product | Foundation platform team | Stable validated-state contract, source limitations, lineage, quality, freshness, and support route for domain teams. |
| Data Product Creation Service and paved path | Foundation platform team | Governed workspace, templates, controls, release automation, policy integration, and service SLOs. |
| Platform Enablement Service | Foundation platform team with enterprise identity, security, privacy, and infrastructure authorities | Governed storage lifecycle, contract system, identity and security bindings, catalog synchronization, integration patterns, automation, and control evidence. |
| Aggregate product | Owning domain data team | Governed domain semantics, composition or calculation rules, explicit grain, lineage, product SLO, and metric ownership where applicable. |
| Consumer-aligned product or view | Serving or consuming domain data team | Purpose, Data Product Consumption Contract, upstream versions, expiry, and support ownership. |

The platform team may run distributed regional infrastructure, and domain teams may deploy workloads through self-service. Neither changes accountability: source-aligned management remains central and business-product ownership remains federated.

## Service Management

Each foundation service should have:

- A service owner.
- Published service description.
- Support model and escalation path.
- Service-level objectives.
- Onboarding process.
- Reusable templates and patterns.
- Portal workflow for requests, approvals, status, evidence, and contract changes.
- Operational dashboards.
- Cost and usage transparency.
- OpenTelemetry instrumentation guidance and service health reporting.

## Delivery Model

Data products and platform capabilities should be delivered iteratively. A typical delivery flow is:

1. Identify business or AI use case.
2. Confirm source availability and ownership.
3. Foundation platform team selects and operates the ingestion pattern and publishes the validated source-aligned contract.
4. Domain data team accepts the input contract and designs its Data Product Creation Contract and governance controls.
5. Domain data team builds and validates the aggregate or consumer-aligned product through the shared creation service.
6. Publish product for approved consumption.
7. Manage access, contract changes, and consumer subscriptions through the portal.
8. Monitor usage, quality, cost, and feedback.

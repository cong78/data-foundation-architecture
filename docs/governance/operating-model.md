# Operating Model

The foundation operating model defines how platform teams, domain teams, and consumers work together.

## Team Responsibilities

| Team | Owns |
| --- | --- |
| Foundation platform team | Shared services, source onboarding, ingestion operation, raw and validated source-aligned products, reference patterns, platform reliability, and automation |
| Domain data teams | Reusable domain, aggregate, and consumer-aligned products; domain definitions, business quality rules, value, lifecycle, support, and consumer relationships |
| Source system teams | Source contracts, source availability, change communication |
| Consumer teams | Responsible consumption, access requests, feedback, use-case controls |
| Governance and risk teams | Policies, exceptions, assurance, audit and compliance evidence |
| Data reliability team | Observability standards, data incident process, SLO reporting, telemetry quality |
| Portal owner | User experience, workflow entry points, portal integrations, and service request usability |

## Central and Federated Accountability

| Capability or product | Accountable owner | Required handoff |
| --- | --- | --- |
| Source onboarding and ingestion service | Foundation platform team | Approved source contract and delivery obligations from the source system team. |
| Raw and validated source-aligned product | Foundation platform team | Stable validated-state contract, source limitations, lineage, quality, freshness, and support route for domain teams. |
| Product creation service and paved road | Foundation platform team | Governed workspace, templates, controls, release automation, policy integration, and service SLOs. |
| Reusable domain product | Owning domain data team | Accepted source-aligned or product input contracts and a domain-owned output contract. |
| Aggregate product | Owning domain data team | Governed metrics, changed grain, lineage, product SLO, and metric ownership. |
| Consumer-aligned product or view | Serving or consuming domain data team | Purpose, consumer agreement, upstream versions, expiry, and support ownership. |

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
4. Domain data team accepts the input contract and designs its product contract and governance controls.
5. Domain data team builds and validates the domain, aggregate, or consumer-aligned product through the shared creation service.
6. Publish product for approved consumption.
7. Manage access, contract changes, and consumer subscriptions through the portal.
8. Monitor usage, quality, cost, and feedback.

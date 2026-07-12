# Operating Model

The foundation operating model defines how platform teams, domain teams, and consumers work together.

## Team Responsibilities

| Team | Owns |
| --- | --- |
| Foundation platform team | Shared services, reference patterns, platform reliability, automation |
| Domain data teams | Data products, domain definitions, quality rules, consumer relationships |
| Source system teams | Source contracts, source availability, change communication |
| Consumer teams | Responsible consumption, access requests, feedback, use-case controls |
| Governance and risk teams | Policies, exceptions, assurance, audit and compliance evidence |
| Data reliability team | Observability standards, data incident process, SLO reporting, telemetry quality |
| Portal owner | User experience, workflow entry points, portal integrations, and service request usability |

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
3. Select ingestion pattern.
4. Design data product contract and governance controls.
5. Build and validate product.
6. Publish product for approved consumption.
7. Manage access, contract changes, and consumer subscriptions through the portal.
8. Monitor usage, quality, cost, and feedback.

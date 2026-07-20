# Reference Solutions

<div class="decision-brief"><div><small>Use when</small><strong>Applying the guidance to a delivery increment.</strong></div><div><small>Decision</small><strong>Which proven profile and record should be adapted?</strong></div><div><small>Owner</small><strong>Delivery owner with architecture, service, and evidence owners.</strong></div><div><small>Output</small><strong>Adapted solution, recorded decisions, and adoption evidence.</strong></div></div>

Reference solutions connect technology-neutral guidance to delivery. They are optional starting points, not mandatory architecture: each adoption must preserve the relevant service boundary, standards, contracts, interoperability requirements, and exit path.

## How to Use Them

1. Confirm the required outcome in Architecture, Services, and Standards.
2. Select a technology profile only when it fits the published architecture, service definition, standards, and delivery context.
3. Complete the relevant reference records while adapting the profile.
4. Prove conformance, security, operability, cost, and portability before go-live.
5. Retain decisions and evidence with the delivered capability.

## Selected Technology Profiles

| Delivery concern | Reference profile | Adoption focus |
| --- | --- | --- |
| Source onboarding and source-aligned delivery | [Data Ingestion - Databricks](data-ingestion-design.md) | Lakeflow, Auto Loader, Unity Catalog, Delta, contract enforcement, and operational evidence. |
| Aggregate and consumer-aligned product creation | [Data Product Creation - Databricks](data-product-creation-design.md) | Workspaces, deployment automation, Unity Catalog, Delta, quality, and go-live controls. |
| Governed product access | [Data Consumption - Databricks](data-consumption-design.md) | Unified access, SQL and open interfaces, semantics, policy, and consumption evidence. |
| Internal and external exchange | [Data Sharing - Databricks](data-sharing-design.md) | Delta Sharing, recipient controls, contract flow, monitoring, expiry, and revocation. |
| System and data product observability | [Observability - Databricks and Grafana](observability-design.md) | Unity Catalog and Databricks product signals, Grafana system signals, OpenTelemetry correlation, and ownership. |

## Reusable Reference Records

| Delivery decision | Reference record | Evidence retained |
| --- | --- | --- |
| Define an executable architecture rule | [Architecture Decision Policy](architecture-policy-template.md) | Stable decision, enforcement points, tests, evidence, and lifecycle. |
| Onboard a data domain | [Data Domain Onboarding](data-domain-onboarding-template.md) | Boundary, ownership, maturity baseline, capabilities, and first-product proof. |
| Onboard a source | [Source Onboarding](source-onboarding-template.md) | Ingestion contract, delivery pattern, controls, support, and validated handoff. |
| Create or change a data product | [Data Product](data-product-template.md) | Publishing data contract, descriptor, semantics, quality, ports, controls, and go-live evidence. |
| Define executable product work | [Data Product Workload](data-product-workload-template.md) | Resources, environments, deployment, rollback, telemetry, and release decision. |
| Select a vendor or technology | [Technology Selection](technology-selection-template.md) | Knockout gates, weighted evidence, proof of capability, cost, risk, and exit. |
| Prove portability | [Interoperability Conformance](interoperability-conformance-template.md) | Profile, independent tests, exceptions, and decision. |
| Design an agentic capability | [Agent and Skill](agent-skill-template.md) | Agent boundary, skills, context, controls, evaluation, telemetry, and release status. |
| Operate or recover a capability | [Service Runbook](service-runbook-template.md) | Trigger, authority, diagnosis, recovery, validation, escalation, and exercise evidence. |

Complete only the records required by the selected profile and risk. A reference record supports delivery evidence; it does not replace an authoritative contract, policy decision, published design, or service state.

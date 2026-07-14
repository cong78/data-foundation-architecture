# Technology Selection Standard

<div class="decision-brief"><div><small>Use when</small><strong>Selecting or reassessing a vendor or technology.</strong></div><div><small>Decision</small><strong>Which option passes mandatory gates and best meets weighted outcomes?</strong></div><div><small>Owner</small><strong>Architecture decision owner.</strong></div><div><small>Output</small><strong>Evidence-based selection, ADR, risks, cost, and exit plan.</strong></div></div>

This standard defines how architects evaluate and select vendors, managed services, open-source products, and internally built technologies for the data foundation.

Technology is selected against an architecture capability and evidence-based use case. Vendor features do not redefine Data Product Creation Contracts, canonical metadata, policy intent, semantic context, telemetry, or service boundaries.

## Approved Data Platform Defaults

The [Data Catalog and Storage Standard](catalog-storage-standard.md) establishes Unity Catalog as the data catalog standard and Delta Lake as the default physical table storage format. These are approved defaults rather than options that every delivery team must rescore.

An alternative catalog, table format, operational store, serving store, or federated binding requires the same mandatory gates, proof, portability evidence, owner, review date, and exit plan defined by this standard. The assessment must show a material requirement that the default profile cannot satisfy.

## Selection Principles

1. Select for a defined capability and workload, not for the longest feature list.
2. Apply mandatory architecture and security gates before weighted scoring.
3. Compare the smallest viable combination of technologies, including the current platform and build option.
4. Validate critical claims through executable proof, not demonstrations or roadmap promises.
5. Score open interfaces, exportability, operational ownership, and exit cost explicitly.
6. Separate product quality from vendor viability and commercial terms.
7. Record assumptions, evidence, exceptions, dissent, and review date in an architecture decision record.

## Capability-to-Technology Mapping

Start with the architecture capability, then evaluate technologies in the applicable category.

| Architecture Capability | Technology Categories | Required Architecture Interfaces |
| --- | --- | --- |
| Data Service Portal | Portal framework, catalog experience, workflow, search, notification. | Stable service APIs, identity, catalog, contract, policy, workflow, health. |
| Ingestion | File transfer, connector framework, CDC, API ingestion, event streaming, schema registry. | Source System Ingestion Contracts, open schemas, replay, quarantine, lineage, OTLP. |
| Product Creation | Developer workspace, orchestration, transformation, quality, semantic tooling, CI/CD. | Product, contract and workload artifacts; open lineage; environment and release APIs. |
| Physical product storage | Object storage, open table format, lakehouse, warehouse, operational store, event log. | Portable data formats, catalog APIs, workload identity, retention, encryption, export. |
| Unified Data Access | SQL gateway, federation, semantic layer, API gateway, event access, feature service, retrieval gateway. | Stable product ports, policy decision and enforcement, OpenAPI, AsyncAPI, query and context contracts. |
| Data Sharing | Data exchange, sharing protocol, clean room, managed file or API delivery. | Recipient identity, Data Product Consumption Contract, minimization, expiry, revocation, and audit. |
| Data Observability | OpenTelemetry collector and backend, data quality, lineage, incident and product-health tooling. | OTLP, OpenTelemetry conventions, OpenLineage, stable product and decision identifiers. |
| Governance and Control | Catalog, glossary, contract registry, policy engine, entitlement, lineage, quality and workflow. | ODCS, ODPS, DCAT, policy APIs, identity federation, import and export. |
| Agentic and AI | Model gateway, agent runtime, skill registry, retrieval, vector index, evaluation and safety tooling. | Typed skills, model profiles, context APIs, delegated identity, approval, evaluation, telemetry. |

One product may cover several categories. Score each capability separately before accepting suite-level simplification benefits.

## Mandatory Knockout Gates

A candidate does not proceed to weighted scoring when a mandatory gate fails without an approved, time-bound exception.

| Gate | Required Evidence |
| --- | --- |
| Architecture fit | Clear ownership boundary, deployment model, integration path, and no duplicate system of record. |
| Identity and access | Named-user and workload identity, delegated access where required, service and data enforcement, audit and revocation. |
| Security and compliance | Encryption, key control, vulnerability management, isolation, residency, retention, audit, incident and assurance reports. |
| Contract and metadata | Stable APIs and machine-readable import/export for required product, contract, schema, semantic, policy and lineage context. |
| Observability | OTLP or approved adapter, health and audit export, stable correlation identifiers, cardinality and sensitive-data controls. |
| Availability and recovery | Measured availability, failure isolation, backup, restore, regional recovery, RTO and RPO evidence. |
| Data portability | Tested export in usable formats without loss of required meaning, controls, lineage or metadata. |
| Exit feasibility | Documented migration path, data and metadata extraction, configuration export, dependency inventory, time and cost estimate. |
| Legal and commercial | Acceptable data terms, intellectual property, support, liability, audit, termination and post-termination access. |

## Weighted Assessment

Score each dimension from **0 to 5** using evidence. The default weights total 100 and may be adjusted before candidates are scored.

| Dimension | Default Weight | Evaluation Focus |
| --- | ---: | --- |
| Architecture fit | 15 | Capability boundary, integration, deployment, tenancy, hybrid fit, architectural simplicity. |
| Functional fit | 15 | Required workflows, interfaces, scale patterns, administration and user outcomes. |
| Interoperability and portability | 15 | Open standards, APIs, artifact export, adapters, conformance, migration and lock-in. |
| Security and compliance | 15 | Identity, policy, encryption, isolation, audit, privacy, residency and assurance. |
| Reliability and operations | 10 | SLOs, scaling, failure modes, recovery, upgrades, supportability and observability. |
| Developer and operator experience | 10 | API, CLI, automation, IaC, testing, debugging, documentation and cognitive load. |
| Data and AI readiness | 8 | Semantics, lineage, quality, AI usage controls, retrieval, evaluation and traceability. |
| Commercial and TCO | 7 | License, consumption, infrastructure, people, support, migration and exit costs. |
| Vendor and ecosystem | 5 | Financial viability, product investment, skills market, partners, support and roadmap credibility. |

### Scoring Scale

| Score | Meaning | Evidence Standard |
| ---: | --- | --- |
| 0 | Not supported. | Confirmed absence. |
| 1 | Major gap. | Custom build or high-risk workaround required. |
| 2 | Partial. | Material configuration, adapter or operational limitation. |
| 3 | Meets requirement. | Demonstrated and documented for the target scenario. |
| 4 | Strong. | Proven beyond the minimum with low implementation risk. |
| 5 | Leading fit. | Independently proven, reusable and materially improves the target outcome. |

`weighted score = sum(score / 5 x weight)`

Do not use the total score to hide a critical weakness. Report knockout gates, dimension scores, confidence, risk and TCO separately.

## Evidence Confidence

Every score carries a confidence rating:

| Confidence | Evidence |
| --- | --- |
| High | Executed test in a representative environment with retained results. |
| Medium | Credible customer evidence, contract commitment or detailed technical documentation. |
| Low | Vendor statement, demonstration, roadmap item or untested assumption. |

A candidate cannot be selected with low confidence in a mandatory or top-weighted dimension unless the decision records a validation condition and deadline.

## Proof-of-Capability

The proof must exercise one thin architecture slice using representative scale, identity, policy and failure conditions.

| Test | Required Proof |
| --- | --- |
| Integrate | Connect identity, catalog, contract, policy, telemetry and one real runtime boundary. |
| Deliver | Build or expose one product port through the standard developer and go-live path. |
| Enforce | Prove named-user and workload service authorization, data authorization, masking or filtering, expiry and revocation. |
| Operate | Show deployment, scaling, upgrade, failure, debugging, alerting, recovery and support workflows. |
| Interoperate | Use an independent client or receiver for the selected open interface and export canonical artifacts. |
| Migrate | Export product data, metadata, configuration and evidence, then import or consume them independently. |
| Measure | Capture latency, throughput, reliability, product health, cost, operator effort and consumer experience. |

Vendor engineers may assist, but enterprise engineers must run or independently verify the critical tests.

## Total Cost of Ownership

Evaluate at least three years and include:

- License, subscription and consumption charges.
- Compute, storage, network, observability and backup costs.
- Platform engineering, product engineering, security and support effort.
- Integration, adapters, testing, training and change management.
- High availability, disaster recovery and non-production environments.
- Growth, contract uplifts and unfavorable consumption scenarios.
- Migration, dual-running, data egress, termination and exit costs.

Record unit economics relevant to the capability, such as cost per product, pipeline run, query, API call, terabyte, active consumer, agent task or telemetry volume.

## Decision Outcomes

| Outcome | Meaning |
| --- | --- |
| Select | Candidate passes gates and has sufficient evidence, fit, confidence and value. |
| Conditional select | Candidate is selected with explicit conditions, owners, deadlines and fallback. |
| Pilot only | Candidate may be used for bounded learning but not as an approved platform standard. |
| Reject | Candidate fails a mandatory gate or presents unacceptable risk or cost. |
| Defer | Evidence or requirements are insufficient for a responsible decision. |

## Required Decision Record

The final record includes capability scope, requirements, candidates, knockout results, weighted scores, confidence, PoC results, TCO, risks, exceptions, architecture mapping, selected option, rejected alternatives, implementation conditions, exit plan and review date.

Use the [Technology Selection Record](../delivery-templates/technology-selection-template.md) and link the result to an [Architecture Decision Record](../implementation/architecture-decisions.md).

## Minimum Done Criteria

- Requirements and weights were approved before candidate scoring.
- Current platform, build and vendor options were considered where credible.
- All mandatory gates have evidence or approved expiring exceptions.
- Critical claims were independently tested in a representative thin slice.
- Scores include evidence links and confidence ratings.
- TCO includes implementation, operation, growth, migration and exit.
- Product, contract, policy, metadata, telemetry and data portability were tested.
- The decision has accountable owners, conditions, exit plan and review date.

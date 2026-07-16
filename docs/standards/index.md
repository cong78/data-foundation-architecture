# Standards Overview

<div class="decision-brief"><div><small>Use when</small><strong>Determining what is mandatory at a boundary.</strong></div><div><small>Decision</small><strong>Which standards and enforcement points apply?</strong></div><div><small>Owner</small><strong>Control owner and implementation owner.</strong></div><div><small>Output</small><strong>Applicable rules, tests, and evidence.</strong></div></div>

The standards turn the architecture blueprint into enforceable design and delivery rules. They apply across planes and services; they are not isolated documents or technology-specific checklists. Use the [Architecture Decision Policy](../decisions/architecture-decision-policy.md) when a normative architecture decision needs stable rules, executable criteria, enforcement points, and evidence.

## How the Standards Fit

<div class="standards-map" role="img" aria-label="Standards mapped from architecture blueprint planes to foundation services in three lanes">
  <div class="standards-map-head" aria-hidden="true">
    <span>Target planes</span><i></i><span>Standards</span><i></i><span>Service outcomes</span>
  </div>

  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell">
      <small>Govern and describe</small>
      <strong>Experience · Control · Security</strong>
      <p>Define ownership, meaning, policy, lifecycle, and evidence.</p>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus">
      <a href="data-contract-standard/"><strong>Data Contract</strong></a>
      <a href="access-control-standard/"><strong>Access Control</strong></a>
      <a href="data-product-management-standard/"><strong>Data Product Management</strong></a>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell">
      <strong>Portal · Product Creation</strong>
      <p>Contract workflows, product state, go-live gates, and consumer trust.</p>
    </div>
  </section>

  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell">
      <small>Build and exchange</small>
      <strong>Control · Data · Security</strong>
      <p>Turn declared intent into portable, governed runtime behavior.</p>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus">
      <a href="data-product-workload-standard/"><strong>Data Product Workload</strong></a>
      <a href="catalog-storage-standard/"><strong>Data Catalog and Storage</strong></a>
      <a href="open-interoperability-standard/"><strong>Open Interoperability</strong></a>
      <a href="technology-selection-standard/"><strong>Technology Selection</strong></a>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell">
      <strong>Ingestion · Creation · Consumption · Sharing</strong>
      <p>Repeatable deployment and open product interfaces across platforms.</p>
    </div>
  </section>

  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell">
      <small>Observe and automate</small>
      <strong>AI · Observability · Security</strong>
      <p>Make data and automated actions measurable, bounded, and traceable.</p>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus">
      <a href="otel-telemetry-standard/"><strong>OpenTelemetry</strong></a>
      <a href="ai-ready-data-standard/"><strong>AI-Ready Data</strong></a>
      <a href="agent-skill-llm-standard/"><strong>Agent, Skill and LLM</strong></a>
    </div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell">
      <strong>Observability · AI Assistant · All Services</strong>
      <p>Correlated health, AI context, evaluation, policy, and action evidence.</p>
    </div>
  </section>
</div>

The lanes show the primary design outcomes. The matrices below capture supporting relationships and exact service coverage.

## Standards to Architecture Blueprint

**P** = primary control definition. **S** = supporting requirement or evidence.

| Standard | Experience | Control | Data | AI | Observability | Security |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| [Data Contract](data-contract-standard.md) | S | P | P | S | S | P |
| [Access Control](access-control-standard.md) | S | P | P | P | P | P |
| [Data Catalog and Storage](catalog-storage-standard.md) | S | P | P | S | S | P |
| [Data Product Management](data-product-management-standard.md) | P | P | P | S | P | S |
| [Data Product Workload](data-product-workload-standard.md) | P | P | P | S | P | P |
| [Open Interoperability](open-interoperability-standard.md) | S | P | P | P | S | S |
| [OpenTelemetry](otel-telemetry-standard.md) | S | S | S | S | P | S |
| [AI-Ready Data](ai-ready-data-standard.md) | S | S | P | P | P | P |
| [Agent, Skill and LLM](agent-skill-llm-standard.md) | P | P | S | P | P | P |
| [Technology Selection](technology-selection-standard.md) | S | P | P | P | P | P |

### Plane Interpretation

| Plane | Standards Outcome |
| --- | --- |
| Experience | The portal exposes product, contract, health, access, and agent evidence without becoming the system of record. |
| Control | Canonical contracts with embedded product descriptors, policies, lifecycle state, and conformance evidence drive workflow and automation. |
| Data | Ingestion, processing, serving, and sharing implement versioned interfaces and portable product artifacts. |
| AI | AI uses approved products, typed skills, governed context, bounded autonomy, evaluation, and traceable model access. |
| Observability | OpenTelemetry correlates platform, pipeline, product, contract, consumer, agent, quality, usage, and cost signals; operations uses that evidence for response and improvement. |
| Security | Identity, purpose, classification, masking, approval, retention, and audit are enforced at every access boundary. |

## Standards to Foundation Services

| Service | Primary Standards | What the Service Enforces |
| --- | --- | --- |
| [Data Service Portal](../services/data-service-portal.md) | Data Contract; Access Control; Data Product Management; Agent, Skill and LLM | Contract lifecycle and decisions, product state, go-live gates, identity-aware service journeys, evidence, and assistant approvals. |
| [Data Service AI Assistant](../services/data-service-ai-assistant.md) | Agent, Skill and LLM; Data Contract; AI-Ready Data; OpenTelemetry | Multi-agent coordination, grounded context, contract-bounded task scope, typed skills, delegated identity, approval classes, evaluations, traces, and service receipts. |
| [Data Ingestion](../services/data-ingestion-service.md) | Data Contract; Data Catalog and Storage; Open Interoperability; OpenTelemetry | Source schema, compatibility, provenance, validation, Unity Catalog registration, Delta landing, open ingestion interfaces, and runtime telemetry. |
| [Data Product Creation](../services/data-product-creation-service.md) | Data Product Management; Data Product Workload; Data Contract; Data Catalog and Storage; AI-Ready Data | Developer workspace, declarative runtime intent, publishing contract with embedded portable descriptor, Unity Catalog and Delta bindings, tests, lineage, semantics, deployment, rollback, go-live gates, and AI usage policy. |
| [Data Consumption](../services/data-consumption-service.md) | Data Contract; Access Control; Data Catalog and Storage; Open Interoperability; AI-Ready Data | Governed product ports over Unity Catalog, Delta, direct, federated, API, event, feature, and retrieval interfaces with separate service and data authorization. |
| [Data Sharing](../services/data-sharing-service.md) | Data Contract; Access Control; Data Catalog and Storage; Open Interoperability; Data Product Management | Recipient identity, purpose, minimized Unity Catalog packages, open exchange, expiry, revocation, and sharing evidence. |
| [Platform Enablement](../services/platform-enablement-service.md) | Data Contract; Access Control; Data Catalog and Storage; Open Interoperability; OpenTelemetry; Technology Selection | Storage lifecycle, contract services, identity and security bindings, catalog synchronization, integration interfaces, provisioning, reconciliation, deprovisioning, and control evidence. |
| [Data Observability](../services/data-observability-service.md) | OpenTelemetry; Data Product Management; AI-Ready Data | End-to-end traces, product SLOs, quality, freshness, lineage correlation, incidents, usage, cost, and AI access evidence. |
| [Data Foundation Operations](../services/data-foundation-operations-service.md) | OpenTelemetry; Data Product Management; Data Product Workload; Access Control | Service ownership, support, incident, problem, change, release, reliability, responder authority, recovery evidence, and improvement. |

## Enforcement and Evidence

| Standard | Key Enforcement Points | Minimum Evidence |
| --- | --- | --- |
| Data Contract | Source onboarding, CI, product go-live, consumption, sharing, agent task dispatch, autonomous execution, and change release. | Versioned contract, compiled execution envelope, validation results, compatibility and policy decisions, approvals, agent and service receipts, subscriber impact. |
| Access Control | Every portal, API, CLI, workflow, service, query, event, file, feature, retrieval, agent, and sharing boundary. | Identity, actor and subject, service decision, data decision, purpose, entitlement, obligations, policy version, outcome, revocation test. |
| Data Catalog and Storage | Source onboarding, product design, CI/CD, product go-live, runtime drift detection, and exception review. | Unity Catalog object or projection, Delta binding or exception, policy tests, lineage, retention, recovery, portability, and reconciliation evidence. |
| Data Product Management | Proposal, review, go-live, operation, change, deprecation, retirement. | Publishing contract with embedded descriptor, owners, gate results, SLO status, usage, incidents, lifecycle decisions. |
| Data Product Workload | Authoring, pull request, plan, environment creation, deployment, promotion, rollback, drift response. | Versioned specification, resolved plan, policy results, artifact identity, release and rollback receipts, telemetry. |
| Open Interoperability | Artifact validation, API and event publication, catalog exchange, platform migration, external sharing. | Conformance report, round-trip test, interface specification, adapter and exception records. |
| OpenTelemetry | Every service boundary, pipeline run, product update, access, agent action, and incident. | Correlated traces, metrics, logs, stable identifiers, retention and cardinality controls. |
| AI-Ready Data | AI-use approval, retrieval or feature publication, training and evaluation access, runtime grounding. | Data Product Consumption Contract with AI-use terms, lineage, snapshot or index version, quality and freshness, purpose decision, and evaluation result. |
| Agent, Skill and LLM | Service-agent and skill release, multi-agent task delegation, model routing, context retrieval, tool call, side effect, approval, suspension. | Agent and skill manifests, delegated task envelope, contract versions, schemas, policy decision, evaluation suite, action preview, service receipt, trace, audit event. |
| Technology Selection | Requirements, shortlist, knockout review, scoring, proof-of-capability, commercial review, decision and periodic reassessment. | Approved criteria and weights, gate evidence, scores, confidence, test results, TCO, risks, exit plan and selection record. |

## Apply the Standards in Order

Before applying standards, use the [Architecture Decision Policy](../decisions/architecture-decision-policy.md) to express any new or changed normative architecture decision.

1. Define the product and source interfaces with the **Data Contract Standard**.
2. Define named-user and workload identity, service and data decisions, entitlements, and enforcement with the **Access Control Standard**.
3. Register assets in Unity Catalog and bind durable tabular storage to Delta with the **Data Catalog and Storage Standard**.
4. Define ownership, lifecycle, go-live, health, and retirement with the **Data Product Management Standard**.
5. Define runtime intent, environments, deployment, and rollback with the **Data Product Workload Standard**.
6. Select portable artifacts and open interfaces with the **Open Interoperability Standard**.
7. Instrument services and products with the **OpenTelemetry Standard**.
8. Add AI permissions, semantics, lineage, and evaluation data with the **AI-Ready Data Standard**.
9. Add agents, skills, models, context, approvals, and evaluations with the **Agent, Skill and LLM Standard**.
10. Evaluate actual products and vendors against all applicable requirements with the **Technology Selection Standard**.

!!! tip "Design review rule"
    Review standards by architecture boundary, not by document. For each service interface, identify the applicable contract, policy, product state, telemetry, interoperability profile, and AI or agent controls before implementation.

# Service Implementation Patterns

This page gives practical implementation patterns for each foundation service. Use it to translate service guidance into platform components and delivery tasks.

## Data Service Portal Pattern

| Layer | Implementation Guidance |
| --- | --- |
| Experience | Product discovery, product detail pages, request forms, approval tasks, status timeline, contract editor, product health views. |
| Integration | Catalog, identity, policy engine, workflow engine, contract registry, lineage, observability, notification service. |
| Data | Store portal workflow state and user preferences; do not duplicate authoritative product metadata. |
| Controls | Audit all actions, enforce role-based views, mask restricted metadata, require approval for sensitive requests. |

Build portal capability as thin vertical journeys:

| Journey Slice | Minimum Integration |
| --- | --- |
| Discover | Catalog search, semantic concepts, current trust summary, saved products. |
| Produce | Team, use case, workspace, product descriptor, contract, go-live workflow. |
| Consume | Authenticated identity, purpose, policy decision, entitlement, subscription, audit. |
| Connect source | Source owner, ingestion pattern, source contract, onboarding workflow, status. |
| Share | Recipient identity, sharing agreement, minimization, delivery, expiry, revocation. |
| Observe | OTLP metrics and traces, quality results, OpenLineage, incidents, usage, cost. |
| Build AI | Product and data dependencies, agent or model identity, tool permissions, evaluation evidence. |

## Ingestion Pattern

| Layer | Implementation Guidance |
| --- | --- |
| Experience | Portal request captures source owner, data description, classification, pattern, frequency, and consumer need. |
| Runtime | Use reusable jobs, connectors, stream subscriptions, or CDC pipelines. |
| Validation | Apply schema validation, contract checks, quarantine, checksum, and source reconciliation. |
| Controls | Restrict raw access, capture source lineage, emit telemetry, maintain retry and replay strategy. |

## Data Product Factory Pattern

| Layer | Implementation Guidance |
| --- | --- |
| Workspace | Provide standard repo or workspace template with pipeline, tests, documentation, contract, and observability configuration. |
| Transformation | Use reusable batch or streaming transformation patterns with versioned logic. |
| Quality | Define completeness, validity, uniqueness, consistency, timeliness, and domain-specific rules. |
| Publication | Publish schema, contract, documentation, lifecycle state, access pattern, and health signals to the catalog and portal. |

## Data Product Developer Workspace Pattern

| Layer | Implementation Guidance |
| --- | --- |
| Workload specification | Declare product id, contract, code, inputs, outputs, resources, policies, SLOs, environment, deployment target, and dependencies in one versioned artifact. |
| Developer interfaces | Keep portal, API, CLI, and approved agent skills behaviorally equivalent and backed by the same service contracts. |
| Environment | Provide isolated development and test environments, controlled test data, configuration inheritance, expiry, and automatic de-provisioning. |
| Resource abstraction | Expose portable workload, connector, compute, storage, secret, policy, and service endpoint resources without leaking provider details into the product contract. |
| Delivery | Generate a plan, run contract and policy checks, preview changes, deploy progressively, capture evidence, and support deterministic rollback. |
| Operations | Detect configuration drift, correlate release and runtime telemetry, expose debugging context, and retain deployment receipts. |

The developer workspace is a channel over foundation services, not a parallel platform. Product metadata remains in the product registry, contracts in the contract registry, policies in the policy service, and runtime state in the responsible execution platform.

## Data Product Management Pattern

| Area | Implementation Guidance |
| --- | --- |
| Registry | Store product id, owner, steward, lifecycle state, contract, classification, consumers, and support route. |
| Gates | Implement go-live gates as workflow checkpoints with required evidence. |
| Portfolio | Provide views for duplicate products, low usage, poor health, missing ownership, cost, and retirement candidates. |
| Change | Link product changes to contract version, compatibility result, release note, consumer notification, and migration plan. |
| Subscription | Maintain active consumer list for impact analysis, incident notification, and deprecation management. |
| Evidence | Keep approvals, test results, quality reports, lineage, access decisions, and incident records linked to product version. |
| Portability | Validate ODPS and ODCS artifacts, preserve canonical ids, and test export/import in CI. |

## Consumption Pattern

| Channel | Implementation Guidance |
| --- | --- |
| SQL and semantic | Governed SQL endpoint, semantic layer, metric definitions, row and column access policies. |
| API | Product-backed API with versioning, throttling, contract, audit, and SLOs. |
| Event | Product event stream with schema registry, consumer subscription, replay, and dead-letter handling. |
| AI retrieval | Approved retrieval index or context API with lineage, freshness, access control, and evaluation evidence. |
| Feature access | Feature dataset or feature service linked to product contract, lineage, and model usage. |

## Sharing Pattern

| Pattern | Implementation Guidance |
| --- | --- |
| Outbound feed | Product-specific extract with recipient scope, encryption, delivery schedule, expiry, and audit. |
| Governed API | Recipient entitlement, token management, throttling, contract, usage logging, revocation. |
| Clean room | Controlled collaboration environment, minimized data, permitted joins, output controls. |
| Portal publication | Internal sharing package with approved consumer group and product owner support. |

For API ports use OpenAPI. For event ports use AsyncAPI plus CloudEvents. For runtime lineage use OpenLineage, and for telemetry use OpenTelemetry and OTLP. Platform-specific adapters must preserve canonical product, contract, dataset, run, consumer, and purpose identifiers.

## Observability Pattern

| Signal | Implementation Guidance |
| --- | --- |
| Trace | Propagate product, pipeline, source, contract, and consumer context across service calls and jobs. |
| Metric | Emit freshness, quality pass rate, record counts, latency, failure rate, cost, usage, and SLO status. |
| Log | Log operational decisions, validation failures, access decisions, and incident context without sensitive values. |
| Event | Emit schema change, contract version change, go-live approval, product publication, incident, and revocation events. |

## Interoperability Test Pattern

| Test | Evidence |
| --- | --- |
| Artifact | Public schema validation and semantic round-trip result. |
| Protocol | Independent client consumes API, event, table, query, or share. |
| Metadata | DCAT export can be indexed by a second catalog implementation. |
| Lineage and telemetry | Independent OpenLineage endpoint and OTLP collector accept signals. |
| Security | Federated identity, access expiry, and revocation behave as declared. |

## Agentic Service Pattern

| Layer | Implementation Guidance |
| --- | --- |
| Assistant | Separate Ask, Plan and Act; show evidence, assumptions, action preview and receipt. |
| Agent | Bind goal, autonomy, identity, purpose, skills, model profile, budgets and evaluation version. |
| Skill | Use typed schemas, least privilege, idempotency, timeout, compensation and audit. |
| Context | Retrieve through policy-filtered services and retain source, version and freshness. |
| Workflow | Own approvals, durable task state, retries, cancellation and compensation. |
| Observability | Correlate conversation, task, agent, model, retrieval, skill, tool, product, contract, purpose and outcome. |

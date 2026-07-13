# Runway

This runway describes a practical, sequenced path for maturing an enterprise data foundation.

## Phase 1: Foundation Baseline

- Define reference architecture and service ownership.
- Establish the Data Service Portal as the user entry point.
- Launch intent-led journeys for source onboarding, product creation, consumption, and product health.
- Establish source onboarding and ingestion patterns.
- Implement catalog, classification, lineage, and access workflows.
- Define OpenTelemetry conventions for foundation services and data products.
- Create initial data product templates.
- Create initial data contract templates and approval workflow.
- Establish mandatory product go-live gates.
- Define the Data Product Workload Standard and a portable resource profile.
- Adopt ODCS and ODPS canonical artifacts with stable enterprise identifiers.
- Bring the first governed data products live.

## Phase 2: Trusted Reuse

- Expand data product lifecycle management.
- Add contract registry, compatibility checks, and consumer subscription notifications.
- Add product portfolio review for duplicates, ownerless products, low usage, health breaches, and retirement.
- Add data quality dashboards and go-live gates.
- Launch a developer workspace with portal, API, and CLI parity, isolated environments, deployment preview, and rollback.
- Standardize semantic and API consumption patterns.
- Introduce cost and usage observability.
- Add product health dashboards for freshness, quality, reliability, and consumer usage.
- Build the Data Service Portal experience for product discovery and access.
- Add domain team, use-case, workspace, saved-product, agreement, and portfolio views.
- Standardize product detail around identity, ownership, contract, quality, interfaces, semantics, lineage, access, health, and change.
- Add DCAT, OpenLineage, OpenAPI, AsyncAPI, CloudEvents, and OTLP conformance adapters.
- Prove clean-room artifact export/import and independent-client consumption.

## Phase 3: AI-Ready Data Foundation

- Define AI data usage policies.
- Publish AI-ready datasets, feature sets, retrieval indexes, and evaluation datasets.
- Add model and agent lineage back to data products.
- Observe AI consumption using product-level telemetry, agent identity, and model usage signals.
- Strengthen controls for prompts, embeddings, and agent identities.
- Monitor AI consumption patterns and quality feedback.
- Prove end-to-end AI correlation across product, contract, snapshot, index, identity, purpose, evaluation, and source lineage.
- Add dedicated MCP product, AI agent, AI model, and AI evaluation journeys.
- Establish Agent Gateway, agent and skill registry, LLM gateway, context gateway and evaluation service.
- Launch the Data Service AI Assistant in grounded Ask and Plan modes.
- Add read-only discovery, contract, lineage, policy and health skills.
- Add bounded write skills with typed previews, explicit approval, durable tasks and receipts.
- Certify agent and skill versions through quality, policy, safety, reliability and cost evaluations.

## Phase 4: Ecosystem Sharing

- Standardize customer, supplier, and partner sharing patterns.
- Add sharing agreement automation and recipient entitlement management.
- Implement clean room or controlled collaboration patterns where needed.
- Improve external audit and revocation evidence.
- Validate at least one partner exchange with an open sharing interface and federated identity.
- Add separate customer, supplier, and partner sharing agreements with recipient identity, expiry, delivery status, and revocation.

## Success Measures

- Number of live data products reused by multiple consumers.
- Reduction in duplicated data pipelines.
- Time required to onboard a new source.
- Percentage of products with owner, contract, quality rules, and lineage.
- Consumer satisfaction and adoption.
- Number of AI systems using governed data products.
- External sharing agreements with auditable controls.
- Percentage of live products passing their required interoperability conformance level.
- Percentage of agent runs grounded in authoritative sources with complete trace and policy evidence.
- Agent task success, unsupported-claim rate, approval accuracy, safety evaluation pass rate and cost per completed task.

# Industry Alignment

Assessment date: **12 July 2026**.

The architecture is strong in scope, product governance, contract lifecycle, AI controls, and end-to-end observability intent. Its main industry gap was that openness and portability were implicit rather than testable.

## Cross-Check

| Area | Current Position | Industry-Aligned Improvement |
| --- | --- | --- |
| Service model | Strong | Keep the six services and six architecture planes. They form a clear capability model. |
| Data contracts | Strong intent | Use ODCS as the canonical artifact; generate platform schemas from it; test round-trip portability. |
| Data products | Strong lifecycle | Add an ODPS-compatible machine-readable descriptor and explicit input/output ports. |
| Catalog | Partial | Publish a DCAT 3 exchange profile so products remain discoverable across catalogs. |
| APIs and events | Partial | Require OpenAPI for synchronous APIs and AsyncAPI plus CloudEvents for event interfaces. |
| Lineage | Partial | Standardize runtime lineage on OpenLineage and map cross-company provenance to PROV-O when needed. |
| Observability | Strong foundation | Align with published OpenTelemetry conventions first; govern custom `data.*` attributes through a versioned registry. |
| Storage and query | Technology-neutral | Add open interface profiles such as Iceberg REST Catalog, Delta Sharing, and Arrow Flight SQL where applicable. |
| Identity and policy | Strong control intent | Separate authentication, policy decision, and enforcement; support federated workload identity for cross-platform use. |
| AI readiness | Strong governance | Make product, contract, snapshot, identity, purpose, retrieval index, evaluation set, and source lineage machine-correlatable. |
| Conformance | Gap | Add independent import/export, protocol, identity, revocation, lineage, and telemetry tests. |

## Data Developer Platform Benchmark

The [Data Developer Platform specification](https://datadeveloperplatform.org/) describes an internal developer platform for data engineers and data scientists. Its architecture separates a central control plane, developer-oriented workload management, and data activation. Its strongest contribution to this guidance is the explicit developer plane: declarative specifications, environment management, automated deployment, API and CLI access, reusable resources, and rollback.

This architecture is broader than the DDP specification because it also defines enterprise consumption, external sharing, product contracts, interoperability conformance, OpenTelemetry product insights, and governed agentic AI. The comparison should therefore be used to strengthen developer experience, not to replace the six-plane model.

| DDP Concern | Alignment | Current Architecture Position | Required Improvement |
| --- | --- | --- | --- |
| Data-product-first | Strong | Data products, contracts, ownership, go-live, operation, and retirement are first-class. | Keep product value and consumer outcomes visible in developer workflows. |
| Unified self-service platform | Strong | Portal journeys compose shared services and authoritative systems. | Ensure APIs and CLI offer the same capabilities as the portal. |
| Control and execution separation | Strong | Control and data planes are explicitly separated. | Define deployment contracts between control services and runtimes. |
| Developer plane | Partial | Product factory and workspace patterns exist, but are distributed across guidance. | Establish a named Data Product Developer Workspace capability. |
| Declarative workload specification | Gap | Contracts and product descriptors are declarative, but runtime intent is not unified. | Add one versioned workload specification linking product, contract, code, resources, policy, SLOs, and environments. |
| Configuration and environment management | Partial | Platform runtime is defined; environment lifecycle is not explicit. | Standardize ephemeral development, test, and production promotion with configuration inheritance. |
| Deployment and rollback | Partial | Go-live gates and release controls exist. | Define automated deployment, progressive delivery, rollback, and evidence capture. |
| API-first and CLI-first development | Partial | Stable service APIs are required; CLI parity is not explicit. | Require portal, API, CLI, and agent skills to invoke the same service contracts. |
| Composable resource abstractions | Partial | Reusable services and architecture building blocks exist. | Define a small portable resource model for workload, connector, compute, storage, secret, policy, and service endpoint. |
| Experimentation and fail-safe operation | Gap | Agent safety and service reliability are covered, but product sandboxes are weak. | Add isolated workspaces, preview environments, test data controls, failure recovery, and rollback drills. |
| Hybrid and multi-tenant activation | Partial | Portability and federated identity are covered. | Make tenant, region, environment, and execution target explicit in workload contracts. |
| Embedded governance and observability | Strong | Contracts, policy, lineage, quality, OpenTelemetry, and go-live gates are integrated. | Feed all developer and deployment events into product evidence and health. |
| AI-ready and agentic delivery | Stronger | Governed AI data use, agents, skills, models, context, approvals, evaluations, and traces are explicit. | Expose developer-plane actions as bounded, typed skills without bypassing deterministic controls. |

### Benchmark Verdict

The architecture aligns well with the DDP product, control-plane, composability, self-service, and embedded-governance principles. It is not yet equally strong as a **data developer platform specification** because its declarative workload, environment, deployment, rollback, and CLI contracts are not detailed enough.

Adopting the developer-workspace improvements below would make the architecture complementary to DDP while retaining stronger enterprise product governance, open interoperability, sharing, observability, and AI controls.

## What State of the Art Means Here

State of the art is not the number of platform components. It is the ability to change an engine, catalog, observability backend, sharing provider, or AI adapter without redefining the product or losing governance evidence.

The target architecture therefore separates four concerns:

| Layer | Stable Responsibility |
| --- | --- |
| Semantic layer | Product meaning, contract, policy intent, ownership, quality, and SLOs. |
| Interface layer | Open API, event, table, file, query, lineage, telemetry, and metadata protocols. |
| Runtime layer | Replaceable storage, compute, catalog, workflow, and observability implementations. |
| Adapter layer | Vendor integration and optimization without changing canonical semantics. |

## Priority Improvements

| Priority | Change | Acceptance Test |
| --- | --- | --- |
| Now | Adopt the Open Core Profile and canonical identifiers. | One product exports and imports without losing required meaning. |
| Now | Make ODCS and ODPS artifacts part of product go-live. | CI validates both artifacts and blocks incompatible changes. |
| Now | Define a declarative data-product workload specification. | One file links product, contract, code, resources, policies, SLOs, environments, and deployment target. |
| Now | Establish portal, API, CLI, and agent-skill parity. | The same product workflow can be executed through each channel using one service contract and policy path. |
| Next | Add developer workspaces and environment promotion. | A team creates an isolated workspace, previews changes, promotes a release, and destroys the environment without a platform ticket. |
| Next | Add deployment rollback and recovery evidence. | A failed product release rolls back product code, configuration, and affected runtime resources while preserving audit evidence. |
| Next | Add DCAT, OpenLineage, OpenAPI, AsyncAPI, CloudEvents, and OTLP adapters. | Independent reference consumers accept each exported interface. |
| Next | Create a versioned semantic-convention registry for `data.*` telemetry. | Two runtimes emit equivalent product health signals. |
| Next | Prove one platform migration and one partner-sharing scenario. | The consumer does not need a provider-specific SDK for the open path. |
| Later | Add portable policy bundles and cross-domain identity federation. | Authorization behavior remains equivalent across two enforcement points. |

## Architecture Verdict

With the open profile applied, this is a credible state-of-the-art **architecture guideline**: comprehensive, AI-aware, product-led, observable, and intentionally vendor-neutral.

It becomes a proven reference architecture only after at least one thin vertical slice passes Level 2 conformance and one external or cross-platform slice passes the relevant Level 3 tests.

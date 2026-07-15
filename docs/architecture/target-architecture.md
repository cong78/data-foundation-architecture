# Target Architecture

<div class="decision-brief"><div><small>Use when</small><strong>Checking logical completeness and control boundaries.</strong></div><div><small>Decision</small><strong>How do service, shared-capability, and integration designs compose across the six planes?</strong></div><div><small>Owner</small><strong>Architecture owner with service and capability owners.</strong></div><div><small>Output</small><strong>Six-plane target, design placement, and identified gaps.</strong></div></div>

The target architecture is organized into six planes. Each plane has a clear responsibility, but they operate together through shared metadata, contracts, policies, telemetry, and workflow.

!!! note "Completeness view, not delivery sequence"
    Use the six planes to test whether a design covers experience, control, data, AI, observability, and security. Navigate delivery through the five stages in [Foundation in One View](../foundation/foundation-in-one-view.md).

## Architecture Planes

<div class="architecture-native target-plane-map" role="img" aria-label="Six-plane target architecture">
  <a class="architecture-band band-experience" href="../../services/data-service-portal/"><small>Intent and interaction</small><strong>Experience Plane</strong><span>Portal journeys · marketplace · contracts · lifecycle · evidence</span></a>
  <span class="architecture-down" aria-hidden="true"></span>
  <a class="architecture-band band-control" href="../data-contract-design/"><small>Decisions and authority</small><strong>Control Plane</strong><span>Unity Catalog · products · semantics · contracts · policy · lineage · quality · go-live</span></a>
  <span class="architecture-down architecture-down--split" aria-hidden="true"></span>
  <div class="architecture-plane-pair">
    <a class="architecture-band band-data" href="../data-foundation-model/"><small>Products and execution</small><strong>Data Plane</strong><span>Ingestion · Delta storage · processing · product ports · serving · sharing</span></a>
    <a class="architecture-band band-ai" href="../agentic-data-foundation/"><small>Governed intelligence</small><strong>AI Plane</strong><span>Context · skills · agents · model access · evaluation · AI lineage</span></a>
  </div>
  <span class="architecture-down" aria-hidden="true"></span>
  <a class="architecture-band band-observe" href="../observability-design/"><small>Trust and impact</small><strong>Observability Plane</strong><span>OpenTelemetry · product telemetry · SLOs · usage · cost · incident correlation</span></a>
  <a class="architecture-band band-security" href="../../governance/security-compliance/"><small>Cross-cutting authority across every plane</small><strong>Security Plane</strong><span>Identity · service and data authorization · purpose · masking · retention · audit · sharing controls</span></a>
</div>

## How Designs Compose the Target

The target architecture is not a fourth design type. It is the composition and completeness view for the three design classes in the [Architecture Design Map](design-map.md).

| Design Class | Reflected in the Target As | Primary Plane Relationship | Review Test |
| --- | --- | --- | --- |
| **Service-specific design** | Named service capabilities, boundaries, interfaces, controls, SLOs, and owned evidence. | Places one service across every plane needed to deliver its outcome. | Does every service capability have one owner and explicit plane placement? |
| **Shared capability design** | Shared product, contract, catalog, storage, identity, policy, semantic, access, telemetry, and automation structures. | Establishes common Control, Data, Security, and Observability capabilities reused by services. | Are common controls provided once without taking accountability from services? |
| **Integration design** | Critical flows, service handoffs, workflow state, identifiers, trust boundaries, failure behavior, and end-to-end evidence. | Connects planes without creating a new integration plane or hidden control authority. | Can one trace prove the outcome across every participating plane and service? |

Each detailed design must state its affected planes. Each plane must be realized through named services, shared foundations, and tested integration flows; a plane containing only conceptual components is incomplete.

## Plane Responsibilities

| Plane | Owns | State-of-the-Art Expectation |
| --- | --- | --- |
| Experience | Intent-led portal journeys, product discovery, product detail, developer workspaces, API and CLI, the three contract types, portfolio, contract lifecycle, product health, support and service-status views. | One coherent experience with channel parity for users, developers, decisions, operational engagement, and evidence. |
| Control | Catalog, semantic registry, context packages, knowledge graph projections, contracts, policy, lineage, quality rules, workflow, go-live gates. | Metadata-driven governance and automation with clear authority boundaries. |
| Data | Source onboarding, source-aligned raw and validated states, products, unified logical access, serving, and sharing. | Standard product ports over custom pipelines and provider-native paths. |
| AI | Agent gateway, skill registry, LLM gateway, governed context, scoped memory, evaluation, retrieval and AI lineage. | Agents are bounded, governed, traceable and purpose-bound. |
| Observability | OpenTelemetry, SLOs, product health, incidents, usage, cost. | Trust is measured end to end. |
| Security | Named-user and workload identity, delegated authority, service authorization, data authorization, ABAC, purpose, masking, entitlement, audit, retention, sharing controls. | Every request passes separate service and data decisions; security follows data and identities. |

The [Platform Enablement Service](../services/platform-enablement-service.md) spans the Control, Data, Observability, and Security planes. It provides shared storage lifecycle, contract, identity and security integration, catalog synchronization, integration, and automation capabilities. The [Data Foundation Operations Service](../services/data-foundation-operations-service.md) spans the Experience, Control, Observability, and Security planes to coordinate support, incidents, problems, changes, releases, reliability, and improvement. Neither horizontal service creates another target plane.

## Service Placement in the Target

| Service | Primary Planes | Supporting Planes | Primary Architecture Design |
| --- | --- | --- | --- |
| Data Service Portal | Experience | Control, Security | [Canonical service design](../services/data-service-portal.md) |
| Data Service AI Assistant | Experience, AI | Control, Security, Observability | [Canonical service design](../services/data-service-ai-assistant.md) |
| Data Ingestion Service | Data | Control, Security, Observability | [Technology-neutral service design](../services/data-ingestion-service.md) |
| Data Product Creation Service | Data, Control | Security, Observability | [Technology-neutral service design](../services/data-product-creation-service.md) |
| Data Consumption Service | Data | Control, Security, AI, Observability | [Technology-neutral service design](../services/data-consumption-service.md) |
| Data Sharing Service | Data | Control, Security, Observability | [Technology-neutral service design](../services/data-sharing-service.md) |
| Platform Enablement Service | Control, Data | Security, Observability | [Canonical service design](../services/platform-enablement-service.md) |
| Data Observability Service | Observability | Every plane through common identity and telemetry | [Technology-neutral service design](../services/data-observability-service.md) |
| Data Foundation Operations Service | Experience, Control | Observability, Security | [Canonical service design](../services/data-foundation-operations-service.md) |

The primary plane owns the service outcome in the target view. A supporting plane supplies mandatory decisions, context, or evidence; it does not take service ownership.

## Core Design Moves by Plane

Use this table to turn each plane into a concrete architecture work package. A design move is complete only when its proof can be reviewed.

| Plane | Required Design Moves | Architecture Proof |
| --- | --- | --- |
| **Experience** | Make the Data Service Portal the entry point for discovery, onboarding, product creation, access, sharing, health, and support. Provide the same product and workflow capabilities through portal, API, and CLI. Organize journeys around domains, use cases, products, contracts, and decisions. | Journey map; portal/API/CLI capability matrix; product detail and health view; workflow state and action receipt. |
| **Control** | Make publishing contracts with embedded product descriptors, semantic context, policy, lineage, quality, and go-live state versioned control artifacts. Use Unity Catalog as the catalog standard without making canonical artifacts platform-dependent. Automate compatibility, impact, approval, and lifecycle gates. | Authority map; canonical schemas; contract tests; policy decisions; lineage graph; product go-live evidence; export and import conformance result. |
| **Data** | Centrally manage ingestion and source-aligned raw and validated states. Federate aggregate and consumer-aligned product creation to domain teams. Use Delta Lake as the default durable tabular format and place unified logical access above distributed product storage. | Ownership boundary; source-to-product lineage; storage and retention profile; stable product ports; adapter selection; execution and rollback evidence. |
| **AI** | Expose typed, agent-callable foundation skills while keeping policy, approval, and lifecycle transitions deterministic. Bind retrieval, features, context, models, and agent actions to product, contract, identity, purpose, and lineage. Evaluate quality and safety before increasing autonomy. | Skill contract; delegated authority; approved purpose; context manifest; model and product versions; evaluation result; tool receipt and AI trace. |
| **Observability** | Emit OpenTelemetry from every foundation service and lifecycle event. Correlate system telemetry with data product telemetry across source, pipeline, product, consumer, contract, and incident. Make health, SLO, usage, freshness, quality, and impact visible. | Common resource identifiers; OTLP traces, metrics, and logs; product health record; SLO and alert; impact graph; incident correlation and recovery evidence. |
| **Security** | Authenticate named users and workloads, then make separate service and data authorization decisions. Enforce purpose, entitlement, masking, retention, residency, sharing, and delegated-agent limits through policy as code. Preserve decisions and obligations as audit evidence. | Identity and delegation model; service decision; data decision; policy version; enforced obligations; access receipt; revocation test; auditable break-glass path. |

The [Platform Enablement Service](../services/platform-enablement-service.md) supplies shared contracts, storage lifecycle, identity bindings, catalog synchronization, integration, and automation across these work packages. The [Data Foundation Operations Service](../services/data-foundation-operations-service.md) turns their telemetry, changes, failures, and support needs into coordinated operational action.

## Critical Flows by Plane

No critical flow stays inside one plane. Each row is an integration-design scope. The **primary plane** owns completion; the handoff column makes the required cross-plane collaboration explicit. Use the [Integration Design](integration-design.md) to specify interaction contracts, failure behavior, correlation, and end-to-end tests.

| Primary Plane | Critical Flow | Required Plane Handoff | Completion Evidence |
| --- | --- | --- | --- |
| **Experience** | Product discovery and subscription | Experience captures intent; Control returns product, contract, policy, and lifecycle state; Security approves access; Data exposes the selected port; Observability returns current health. | Product selection, approved request, subscription, endpoint, obligations, and visible health timestamp. |
| **Experience** | Support and operational engagement | Experience captures the request; Observability adds affected products and consumers; Operations assigns severity and accountable owner. | Support record linked to product, service, telemetry, owner, status, and communications. |
| **Control** | Contract change | Control checks compatibility and impact; Experience notifies affected parties; Data and AI validate dependent interfaces; Security checks policy impact. | Approved contract version, test results, affected consumers, migration window, exception, and rollback plan. |
| **Control** | Product go-live | Control evaluates contract, owner, semantics, quality, lineage, security, SLO, and support readiness; Data publishes approved ports; Experience exposes lifecycle state. | Product version, passed gates, approval, live ports, owner, SLO, runbook, and go-live receipt. |
| **Data** | Source to product | Experience starts onboarding; Security approves connection and classification; Control validates the ingestion and creation contracts; Data lands, validates, transforms, and publishes; Observability records lineage and health. | Source System Ingestion Contract, source-aligned state, product version, lineage, quality result, and product go-live evidence. |
| **Data** | Governed product access | Experience captures consumer purpose; Control resolves product, contract, context, and policy; Security returns service and data decisions; Data selects an adapter and executes near approved storage. | Consumption contract, policy decisions, selected port and adapter, obligations, result status, and usage trace. |
| **Data** | External sharing | Control validates the sharing profile; Security resolves recipient, minimization, entitlement, expiry, and residency; Data publishes a revocable share; Observability tracks delivery and use. | Approved recipient scope, shared product version, delivery receipt, expiry, audit trail, and tested revocation. |
| **AI** | AI product access | AI declares purpose and required context; Security validates identity, delegation, and purpose; Control resolves approved products and context; Data serves retrieval or feature access; Observability records model-to-data use. | Approved purpose, product and context versions, access decisions, retrieval or feature trace, model version, and evaluation status. |
| **AI** | Agent action | Experience authenticates intent; AI creates a bounded plan; Security constrains authority; Control validates workflow state; the selected service executes the typed skill; Observability records the action. | Intent, plan, skill version, policy decision, approval where required, tool result, action receipt, and trace. |
| **Observability** | Product incident | Observability detects an SLO or product-health breach and correlates source, pipeline, product, and consumer impact; Operations coordinates response; Experience communicates status; owners restore service and data trust. | Alert, impact graph, incident owner, containment, recovery validation, communications, and improvement action. |
| **Security** | Access decision and revocation | Security authenticates actor and subject, authorizes service operation, then authorizes product data and purpose; Control supplies policy context; Data enforces obligations; Observability retains evidence. | Service decision, data decision, obligations, enforcement point, access receipt, expiry, and revocation result. |
| **Security** | Platform change | Control supplies dependencies, contract, and go-live state; Security classifies risk and approvals; Platform Enablement applies the change; Observability validates outcome; Operations coordinates release and rollback. | Approved change, release identity, dependency impact, validation, policy and drift result, rollback evidence, and retained receipt. |

## Minimum State-of-the-Art Bar

The architecture should not be called mature unless these are true:

- Products cannot go live without approved contracts and passing go-live gates.
- Consumers access products through governed serving or sharing patterns.
- Product health is visible in the portal.
- Contract changes are tested before release and communicated to subscribers.
- AI agents and models use governed identities and approved purposes.
- Observability connects source, pipeline, product, consumer, contract, and incident.
- Operational response connects support, service ownership, observable impact, change, recovery, communication, and improvement across all foundation services.
- Security policies are enforced by services, not only written in documentation.
- Canonical artifacts can be exported, validated, and imported without a platform-specific control plane.
- Agent actions cannot exceed the user's delegated authority, registered skill contract, approved autonomy or task budget.

## State-of-the-Art Checklist

| Question | Required Answer |
| --- | --- |
| Can users find, request, and subscribe through one portal? | Yes |
| Are contracts tested before data is published? | Yes |
| Can a product go live without quality, lineage, or an owner? | No |
| Can AI access bypass policy or purpose approval? | No |
| Can incidents show affected consumers and source impact? | Yes |
| Can products be retired safely with migration evidence? | Yes |
| Can a product move between platforms without losing contract, metadata, lineage, or policy intent? | Yes |

<div class="read-next">
  <strong>Next:</strong> use the Architecture Design Map to select the owning service design, supporting shared capabilities, and required integration flows.
</div>

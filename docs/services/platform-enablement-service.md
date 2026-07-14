# Platform Enablement Service

<div class="decision-brief"><div><small>Use when</small><strong>Designing shared controls, infrastructure, or automation used by multiple services.</strong></div><div><small>Decision</small><strong>Which common capability should be provided once and reused?</strong></div><div><small>Owner</small><strong>Foundation platform team with enterprise control owners.</strong></div><div><small>Output</small><strong>Governed platform capability, interface, policy, and evidence.</strong></div></div>

## Definition

The Platform Enablement Service provides shared storage, data contract, identity, security, integration, metadata, and automation capabilities used consistently across the data foundation.

It centralizes reusable controls and paved paths while leaving lifecycle services accountable for applying those controls in their own workflows and runtimes.

## Position in the Foundation

Platform Enablement is a **horizontal service**, not another stage in the source-to-product flow. The Data Service Portal exposes its request and status journeys; ingestion, product creation, consumption, sharing, observability, and operations consume its APIs, events, policies, and evidence.

<div class="standards-map reference-map" role="img" aria-label="Platform Enablement Service providing shared capabilities to foundation services">
  <div class="standards-map-head" aria-hidden="true">
    <span>Service need</span><i></i><span>Shared enablement</span><i></i><span>Reusable outcome</span>
  </div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Declare</small><strong>Product · Purpose · Environment</strong><p>A service requests a governed resource or control using stable identifiers and versioned intent.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Contracts and metadata</strong><strong>Identity and security</strong><strong>Policy validation</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Approved plan</strong><p>Resolved policy, ownership, obligations, dependencies, and evidence requirements.</p></div>
  </section>
  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Provision</small><strong>Storage · Access · Integration</strong><p>Approved runtime intent is applied through reusable platform APIs and automation.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Delta storage lifecycle</strong><strong>Identity and policy bindings</strong><strong>APIs, events and connectors</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Governed resource</strong><p>Provisioned, discoverable, secured, observable, recoverable, and lifecycle-managed capability.</p></div>
  </section>
  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Assure</small><strong>State · Drift · Evidence</strong><p>Runtime state is reconciled with contracts, policy, catalog metadata, and approved configuration.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><strong>Conformance checks</strong><strong>Drift detection</strong><strong>Audit and lifecycle evidence</strong></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Continuous control</strong><p>Exceptions, expiry, retention, revocation, and remediation remain visible and actionable.</p></div>
  </section>
</div>

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Storage provisioning, Delta defaults, retention, archival, recovery, legal hold, and deletion automation. | Owning domain data, product semantics, business retention decisions, or application-specific persistence. |
| Registration, validation, versioning, approval integration, publication, and distribution of the three data contract types. | Executing ingestion, transformation, consumption, or sharing workloads on behalf of lifecycle services. |
| Integration of named-user, group, workload, service-principal, delegated, and agent identities with platform controls. | Replacing enterprise identity providers or becoming the authority for employment and organization identities. |
| Reusable encryption, secret, classification, masking, policy-enforcement, audit, and evidence patterns. | Defining enterprise cybersecurity policy, accepting security risk, or replacing security incident response. |
| Shared APIs, events, connectors, metadata synchronization, service endpoints, and integration conformance. | Building one-off source or consumer integrations that do not become supported platform patterns. |
| Provisioning, policy-as-code, validation, drift detection, reconciliation, and lifecycle automation. | Owning service support, incident command, change governance, or reliability improvement. |

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Storage lifecycle | Governed storage management | Product storage is provisioned with owner, environment, classification, region, format, encryption, recovery, retention, cost, and deletion controls. |
| Contract enablement | Data contract system | Ingestion, creation, and consumption contracts are registered, validated, versioned, approved, distributed, and linked to enforcement evidence. |
| Identity integration | Human and machine identity binding | Named users, groups, workloads, applications, agents, and external subjects resolve to governed platform identities without local identity silos. |
| Security enablement | Reusable security controls | Classification, encryption, secrets, masking, row and column controls, purpose obligations, audit, and break-glass patterns are consistently implementable. |
| Integration enablement | Standard integration interfaces | Services exchange commands, events, metadata, contracts, and evidence through supported APIs, schemas, connectors, and interoperability profiles. |
| Catalog integration | Metadata and lineage synchronization | Unity Catalog remains aligned with product, contract, ownership, classification, policy, lineage, lifecycle, and runtime identifiers. |
| Platform automation | Provisioning and reconciliation | Approved intent becomes repeatable infrastructure and configuration with preview, policy checks, receipts, drift detection, rollback, and deprovisioning. |
| Assurance | Conformance and control evidence | Every shared resource can prove its approved state, policy version, runtime binding, exception, expiry, and latest validation result. |

## Authority Model

Platform Enablement coordinates authoritative systems; it does not duplicate them.

| Concern | Authoritative owner or system | Platform Enablement responsibility |
| --- | --- | --- |
| Enterprise identity | Enterprise identity provider and identity governance | Resolve and bind identities, groups, workload credentials, delegation, and lifecycle events to foundation controls. |
| Security policy and risk | Cybersecurity, privacy, legal, and risk authorities | Translate approved policy into reusable technical controls and return enforcement evidence. |
| Data contract | Data Contract System with accountable contract parties | Operate contract registration, validation, versioning, distribution, compatibility, and evidence interfaces. |
| Catalog and technical access | Unity Catalog | Provision and reconcile catalog objects, privileges, classifications, lineage references, and product identifiers. |
| Physical product storage | Accountable product or source owner using approved platform profiles | Provision and manage technical lifecycle controls; do not take ownership of data meaning or fitness. |
| Runtime execution | Ingestion, creation, consumption, or sharing service | Supply resources and controls; the consuming service executes and proves enforcement. |
| Operational workflow | Data Foundation Operations Service and enterprise service management | Emit resource health, drift, change, expiry, and failure evidence into the operational process. |

## Service Interaction

| Consumer | Uses Platform Enablement For | Remains Accountable For |
| --- | --- | --- |
| Data Service Portal | Provisioning requests, contract workflows, policy previews, status, exceptions, and evidence. | Coherent user journeys and workflow presentation. |
| Data Ingestion | Connections, secrets, source storage, ingestion contracts, identity bindings, and retention controls. | Source onboarding, delivery, validation, quarantine, replay, and source-aligned outcomes. |
| Data Product Creation | Workspaces, product storage, creation contracts, catalog bindings, policies, environments, and deployment automation. | Product engineering, quality, semantics, lineage, release, and product go-live evidence. |
| Data Consumption | Consumer identities, consumption contracts, entitlements, policy bindings, endpoints, and revocation. | Governed product resolution, query or delivery behavior, obligations, and consumer experience. |
| Data Sharing | Recipient identity bindings, packages, secure endpoints, retention, expiry, and revocation controls. | Minimized exchange, recipient delivery, sharing evidence, and offboarding. |
| Data Observability | Standard resource identifiers, telemetry endpoints, control state, drift events, and evidence links. | Collection, correlation, product health, SLOs, and observable insights. |
| Foundation Operations | Service dependencies, change receipts, resource health, expiry, recovery, and deprovisioning evidence. | Support, incident, problem, change, recovery coordination, communication, and improvement. |

## Provisioning Contract

Every enablement request should declare:

- Requesting service, accountable owner, product or source id, environment, region, and criticality.
- Required capability and interface, expected data classification, purpose, consumers, and workload identity.
- Contract, catalog, policy, retention, recovery, observability, cost, and interoperability profiles.
- Dependencies, approval class, exception, expiry, rollback, and deprovisioning requirements.

The response returns a resolved plan, policy decisions, provisioned resource identifiers, catalog and contract bindings, validation results, telemetry references, and an immutable action receipt.

## Controls

- All provisioning uses authenticated service interfaces and stable source, product, contract, identity, environment, and resource identifiers.
- Delta Lake is the default durable tabular storage format; exceptions require documented interoperability, lifecycle, recovery, and exit evidence.
- Unity Catalog is the catalog and technical access-governance standard; canonical contract and product artifacts remain independently portable.
- Retention, deletion, archival, legal hold, recovery, residency, encryption, and cost controls are declared before production provisioning.
- Enterprise identities are reused; local users, shared credentials, and untracked service accounts are prohibited.
- Services enforce both service authorization and data authorization and return decisions and obligations as evidence.
- Contract or policy changes trigger compatibility, impact, approval, rollout, and rollback checks before enforcement changes.
- Runtime state is reconciled against approved intent; drift creates an owned remediation or time-bound exception.
- Deprovisioning proves access revocation, retention or deletion outcome, catalog state, dependency handling, and audit preservation.

## Measures

- Provisioning lead time and self-service completion rate by capability.
- Percentage of resources linked to owner, product, contract, identity, policy, retention, recovery, and telemetry profiles.
- Policy, contract, catalog, storage, and identity reconciliation success.
- Drift age, expired exceptions, orphaned identities, unowned storage, and overdue deletion actions.
- Reuse of supported patterns versus one-off integrations.
- Failed provisioning, rollback effectiveness, deprovisioning completion, and control-evidence freshness.

## Done Criteria

- Every shared capability has a service owner, supported interface, SLO, lifecycle, support route, and runbook.
- At least one end-to-end product uses enablement APIs for storage, contracts, identity, security, integration, catalog, and evidence without manual control duplication.
- Lifecycle services can enforce shared controls independently and return correlated evidence.
- Unity Catalog, the contract system, enterprise identity, policy systems, and runtime resources reconcile through stable identifiers.
- Retention, recovery, revocation, deletion, drift, exception, and deprovisioning paths are tested.
- Platform Enablement failures are observable and recoverable through the Data Foundation Operations Service.

<div class="read-next">
  <strong>Next:</strong> map the service to applicable <a href="/standards/">Standards</a>, then define its operational controls with the <a href="/delivery-templates/service-runbook-template/">Service Runbook Template</a>.
</div>

# Data Sharing Service

<div class="decision-brief"><div><small>Use when</small><strong>Exchanging product data across a recipient boundary.</strong></div><div><small>Decision</small><strong>Which recipient contract, package, entitlement, and exit controls apply?</strong></div><div><small>Owner</small><strong>Sharing service owner with product, recipient, and policy owners.</strong></div><div><small>Output</small><strong>Controlled, monitored, revocable exchange.</strong></div></div>

## Definition

The Data Sharing Service exchanges live data products with internal platforms, customers, suppliers, partners, and other approved recipients. It creates a minimized recipient package, binds it to a Data Product Consumption Contract and entitlement, monitors delivery and use, and proves expiry, revocation, and offboarding.

## Scope and Boundaries

| Owns | Does Not Own |
| --- | --- |
| Recipient onboarding, package creation, technical binding, entitlement, delivery, monitoring, expiry, revocation, and offboarding evidence. | Product semantics, product ownership, legal contracting, identity authority, or the source product lifecycle. |
| Table, API, event, file, and approved clean-room exchange profiles. | Uncontrolled export, permanent recipient credentials, or unmanaged copies. |
| Sharing-specific minimization and disclosure controls. | Treating delivery success as proof of continued permitted use. |

## Architecture Alignment

| Concern | Alignment |
| --- | --- |
| Primary plane | Data |
| Supporting planes | Control, Security, and Observability |
| Shared capabilities | Data Product Consumption Contract, identity federation, classification, policy, entitlement, retention, product ports, and telemetry. |
| Integration flows | Request recipient, approve purpose, minimize package, provision identity and entitlement, deliver, monitor, renew, revoke, delete, and offboard. |

## Service Architecture

```mermaid
flowchart LR
    PRODUCT["Live data product"]
    REQUEST["Recipient request"]
    SHARE["Data Sharing Service"]
    CONTROL["Policy and entitlement"]
    DELIVERY["Delivery adapter"]
    RECIPIENT["Approved recipient"]
    EXIT["Renew or revoke"]

    PRODUCT --> SHARE
    REQUEST --> SHARE --> CONTROL --> SHARE --> DELIVERY --> RECIPIENT --> EXIT
```

The package and recipient binding are technical implementations; the product and consumption contracts remain the portable authority.

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Onboarding | Recipient and trust registration | Legal entity, identity domain, owner, purpose, risk, support, and exit responsibilities are explicit. |
| Contracts | Recipient-specific consumption terms | Product version, purpose, minimized scope, channel, SLO, permitted and prohibited use, retention, expiry, and revocation are approved. |
| Protection | Package minimization and disclosure control | Only approved fields, rows, aggregates, events, files, or outputs cross the boundary. |
| Delivery | Governed exchange | Recipient identity, package, interface, entitlement, encryption, SLO, and support are bound and tested. |
| Operations | Monitoring and incident response | Delivery, usage, failure, policy, recipient activity, and product impact are observable and actionable. |
| Exit | Renewal, revocation, and offboarding | Entitlements expire or are revoked; delivery stops; copies or credentials are handled as contracted; evidence is retained. |

## Contracts and Interfaces

| Interface | Purpose | Required Contract |
| --- | --- | --- |
| Sharing request API | Request exchange with a named recipient and purpose. | Product and port, recipient, legal entity, purpose, scope, channel, duration, geography, retention, and use-case owner. |
| Package definition | Declare the minimized recipient view. | Exact product version, fields or rows, aliases, transformations, classification, policy, watermarking, and output controls. |
| Recipient binding | Provision identity, entitlement, delivery endpoint, and credentials. | Approved consumption contract, identity profile, expiry, rotation, revocation, and support. |
| Delivery adapter | Exchange table, API, event, file, or controlled output. | Protocol profile, schema, authentication, encryption, SLO, errors, telemetry, and compatibility. |
| Exit API | Suspend, revoke, expire, delete, or offboard. | Authority, affected package and recipient, effective time, obligations, confirmation, and retained proof. |

## Integrations and Dependencies

| Dependency | Sharing Uses | Sharing Provides |
| --- | --- | --- |
| Product owner and recipient owner | Approved product, purpose, scope, use, support, change, retention, and exit obligations. | Package proposal, activation status, delivery evidence, incidents, usage, and offboarding proof. |
| Contract, policy, privacy, security, and legal authorities | Classification, legal basis, policy decisions, approvals, geography, prohibited use, and obligations. | Recipient, product, purpose, requested disclosure, technical plan, and enforcement evidence. |
| Platform Enablement Service | Identity federation, secrets, package resources, endpoints, entitlement, policy, retention, and automation. | Typed provisioning, renewal, revocation, deletion, and deprovisioning intent. |
| Data Consumption Service | Logical product-port resolution and common authorization model. | External-recipient lifecycle, package, delivery, and exit behavior. |
| Observability and Operations | Delivery telemetry, product impact, incidents, alerts, communication, and recovery. | Recipient, package, entitlement, delivery, usage, expiry, revocation, failure, and recovery signals. |

## Controls and Evidence

| Control | Required Evidence |
| --- | --- |
| Sharing starts only from a live approved product and recipient-specific contract. | Product and contract versions, recipient owner, purpose, approvals, and activation decision. |
| Scope is minimized before delivery. | Classification, selected fields or rows, transformation, policy result, disclosure review, and package hash. |
| Recipient identity and entitlement are federated, bounded, expiring, and revocable. | Identity profile, grant, scopes, expiry, rotation, access audit, and revocation test. |
| Delivery and downstream use are monitored to the supported boundary. | Delivery events, recipient activity, usage, SLO, errors, policy decisions, and incident links. |
| Exit is tested before activation. | Suspension, revocation, credential invalidation, delivery stop, deletion or retention obligation, and proof retrieval. |

## Action Checklist

| Engineer | Product Owner |
| --- | --- |
| Implement package generation, identity, entitlement, protocol adapter, encryption, telemetry, expiry, revocation, deletion, reconciliation, and incident controls; test provider and recipient clients. | Confirm recipient, purpose, legal basis, minimized scope, permitted and prohibited use, service level, change behavior, retention, geography, support, renewal, and exit obligations. |
| Test unauthorized recipient, excessive scope, schema change, delivery failure, credential rotation, token expiry, recipient outage, emergency suspension, revocation, offboarding, and evidence retrieval. | Approve the package and recipient terms; communicate changes; review continued need, usage, incidents, expiry, and offboarding completion. |

## Reference Solutions

[Data Sharing Design](../architecture/data-sharing-design.md) maps this service to Delta Sharing, Unity Catalog shares and recipients, and explicit contract workflows. It is a selected reference profile; recipient and package semantics remain portable.

## Done Criteria

- Every exchange links one live product version, one recipient, one purpose, one minimized package, one contract, and one entitlement.
- Provider and recipient identity, protocol, compatibility, SLO, monitoring, support, and incident paths are tested.
- Product changes trigger recipient impact and compatibility review.
- Expiry, emergency suspension, revocation, credential invalidation, offboarding, and deletion or retention obligations are proven.
- Recipient activity and product impact can be correlated without exposing sensitive payloads in telemetry.
- The exchange can migrate or terminate without reconstructing its meaning from provider configuration.

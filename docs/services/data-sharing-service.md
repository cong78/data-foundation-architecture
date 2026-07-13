# Data Sharing Service

<div class="decision-brief"><div><small>Use when</small><strong>Exchanging product data across a recipient boundary.</strong></div><div><small>Decision</small><strong>Which package, agreement, entitlement, and exit controls apply?</strong></div><div><small>Owner</small><strong>Sharing service and agreement owner.</strong></div><div><small>Output</small><strong>Controlled, monitored, revocable exchange.</strong></div></div>

## Definition

The data sharing service enables governed exchange of data with internal platforms, customers, suppliers, partners, and company ecosystems. Sharing is explicit, contract-based, monitored, and revocable.

For a selected implementation profile, see [Data Sharing Design](../architecture/data-sharing-design.md), which maps this service to Delta Sharing, Unity Catalog shares and recipients, and an explicit product-contract, sharing-contract, and agreement lifecycle.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| Sharing approval, packaging, recipient entitlement, delivery, audit, expiry, and revocation. | Negotiating commercial or legal terms outside data usage controls. |
| Internal platform sharing and external customer, supplier, or partner sharing. | Owning the recipient system after delivery. |
| Secure outbound feeds, APIs, event publication, clean room patterns, and portal publication. | Consumer-side analytics, application, or AI implementation. |

## Sharing Scenarios

| Scenario | Example | Key Concern |
| --- | --- | --- |
| Internal platform sharing | A company platform consumes live supplier data products. | Compatibility, access policy, availability. |
| Customer sharing | A customer receives operational or reporting data. | Consent, contractual terms, privacy, audit. |
| Supplier sharing | A supplier receives forecast, quality, or logistics data. | Scope control, timeliness, data minimization. |
| Partner sharing | A partner ecosystem exchanges joint process data. | Legal basis, interoperability, traceability. |

## Core Capabilities

| Category | Capability | Owned Outcome |
| --- | --- | --- |
| Agreement | Sharing request and approval | Recipient, purpose, legal basis, product, scope, duration, permitted use, obligations, and approvers are recorded before delivery. |
| Contracts | Recipient-specific sharing contract | Product promise is reduced to an explicit package, interface, SLO, change, retention, expiry, and revocation agreement. |
| Identity | Recipient identity and entitlement | Organization, user or workload identity, authentication profile, entitlement, activation, rotation, and expiry are governed. |
| Packaging | Data selection and minimization | Only approved products, fields, rows, history, semantics, and documentation enter the recipient package. |
| Protection | Purpose and disclosure controls | Masking, tokenization, aggregation, watermarking, clean-room restrictions, and output controls enforce the agreement. |
| Delivery | Controlled exchange channels | Open sharing, API, file, event, secure transfer, portal delivery, or clean room provides a versioned and testable interface. |
| Evidence | Sharing telemetry and audit | Provisioning, delivery, usage, errors, policy decisions, recipient activity, and external lineage are linked to the agreement. |
| Lifecycle | Change and consumer communication | Contract or product changes trigger compatibility assessment, approval, notification, migration, and coexistence where required. |
| Exit | Expiry, revocation, and offboarding | Access, credentials, packages, cached rights, and active delivery stop predictably with retained closure evidence. |

## Architecture Guidance

External sharing should start from a live data product whenever possible. The service should create a sharing-specific view or package that contains only what the recipient is allowed to use.

External recipients use federated named-user or workload identities from approved trust domains. Sharing service authorization and recipient data authorization are evaluated separately; every entitlement is purpose-bound, minimized, time-limited, and revocable.

The architecture must support revocation. Sharing is not complete when data is delivered; it must remain governable through audit, retention, access expiry, and contractual controls.

Prefer open exchange interfaces such as Delta Sharing for large table delivery, OpenAPI for governed APIs, and AsyncAPI plus CloudEvents for events. Proprietary sharing features require a tested export path and an exit decision record.

## Controls

- Sharing purpose, recipient, dataset, duration, and allowed use are approved.
- Data minimization is applied before delivery.
- Recipient identity and entitlement are validated.
- Sensitive fields are masked or excluded according to policy.
- Sharing activity is logged and auditable.
- Expiry and revocation are technically enforceable.

## Done Criteria

- Sharing package or interface is documented and versioned.
- Recipient access is active only for approved scope and duration.
- Delivery and usage telemetry are available.
- Audit evidence is linked to the sharing agreement.
- Offboarding and revocation process is tested.
- A recipient using an independent client can consume the open interface and observe expiry or revocation correctly.

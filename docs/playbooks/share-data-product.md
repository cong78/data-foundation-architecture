# Share a Data Product

<div class="decision-brief"><div><small>Use when</small><strong>Product data must cross a recipient boundary.</strong></div><div><small>Decision</small><strong>Approve recipient, purpose, minimum scope, delivery, and exit.</strong></div><div><small>Owner</small><strong>Sharing owner with product, risk, and recipient owners.</strong></div><div><small>Output</small><strong>Contracted, observable, expiring, revocable exchange.</strong></div></div>

## Actions

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Requester:** select a live product and declare recipient, purpose, legal basis, fields, history, cadence, duration, and use restrictions. | Sharing request. |
| 2 | **Product and risk owners:** validate product health, permitted use, classification, privacy, residency, retention, and minimum necessary scope. | Scope and risk decision. |
| 3 | **Sharing owner:** create a Data Product Consumption Contract with external-sharing terms referencing the exact product and creation-contract versions. | Approved Data Product Consumption Contract. |
| 4 | **Sharing service:** generate minimized package, aliases, recipient identity, delivery binding, entitlement, expiry, and revocation controls. | Provisioning plan. |
| 5 | **Provider and recipient:** test independent consumption, policy, quality, delivery SLO, audit, notification, suspension, and revocation. | Acceptance and revocation test. |
| 6 | **Operations:** activate delivery health, usage, incident, change, renewal, expiry, and offboarding workflows. | Operating evidence. |
| 7 | **Sharing owner:** publish and periodically reconcile the Data Product Consumption Contract, entitlement, package, recipient, and activity. | Live exchange record. |

## Stop Conditions

- Source product is not live, healthy, or contractually permitted for the purpose.
- Recipient identity, legal basis, minimization, retention, or revocation cannot be proven.
- Technical share is treated as the Data Product Consumption Contract or approval record.
- Provider cannot notify, suspend, expire, or revoke the exchange.

## Done Criteria

- Recipient receives only approved scope through the agreed interface.
- Product, creation contract, Data Product Consumption Contract, package, entitlement, recipient, usage, expiry, and revocation remain correlated.
- External copies and retention obligations are explicitly addressed.

Authoritative inputs: [Sharing Service](../services/data-sharing-service.md), [Sharing Design](../architecture/data-sharing-design.md), and [Data Contract Standard](../standards/data-contract-standard.md).

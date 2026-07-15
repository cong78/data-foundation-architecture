# Consume a Data Product

<div class="decision-brief"><div><small>Use when</small><strong>A human or workload needs governed product access.</strong></div><div><small>Decision</small><strong>Approve purpose, port, scope, obligations, and duration.</strong></div><div><small>Owner</small><strong>Consumer owner with product and policy owners.</strong></div><div><small>Output</small><strong>Working, observable, revocable entitlement.</strong></div></div>

## Actions

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Consumer:** discover a live product and review contract, context, quality, freshness, limitations, incidents, and change policy. | Selected product and port. |
| 2 | **Consumer owner:** declare identity, use case, purpose, fields, interface, environment, duration, and expected volume. | Consume request. |
| 3 | **Policy service:** decide service access and data access separately; calculate masking, filtering, rate, region, and expiry obligations. | Policy decisions and obligations. |
| 4 | **Product owner or approver:** review exceptional purpose, sensitive scope, capacity, SLO, or AI-use conditions. | Approval or rejection. |
| 5 | **Data Consumption Service:** create entitlement and bind the logical port to a conformant runtime adapter. | Provisioning receipt. |
| 6 | **Consumer:** test representative access, semantics, error behavior, and obligations. | Acceptance result. |
| 7 | **Operations and product owner:** observe usage, cost, experience, incidents, expiry, and contract change impact. | Usage and health evidence. |

## Stop Conditions

- Product is not live or current health makes the intended use unsafe.
- Purpose is prohibited, unclear, excessive, or unsupported by the contract.
- Runtime adapter cannot enforce identity, policy, obligations, telemetry, or revocation.
- Requested direct raw access is not justified by product development or recovery need.

## Done Criteria

- Consumer uses a stable logical product port rather than a physical storage path.
- Identity, purpose, contract version, policy, entitlement, obligations, usage, and outcome are traceable.
- Expiry and revocation are tested.

Authoritative inputs: [Unified Access Design](../architecture/unified-access-design.md), [Data Consumption Service](../services/data-consumption-service.md), and [Access Control Standard](../standards/access-control-standard.md).

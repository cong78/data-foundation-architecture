# Approve Product Go-Live

<div class="decision-brief"><div><small>Use when</small><strong>A candidate product requests publication.</strong></div><div><small>Decision</small><strong>Approve, reject, or grant an expiring exception.</strong></div><div><small>Owner</small><strong>Product owner with required control approvers.</strong></div><div><small>Output</small><strong>Signed gate record bound to one release.</strong></div></div>

## Gate Review

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Workflow service:** freeze candidate identities and resolve product, contract, context, workload, artifact, and release versions. | Immutable review scope. |
| 2 | **Product owner:** confirm purpose, consumers, value, ownership, support, and lifecycle. | Ownership and purpose gates. |
| 3 | **Steward and risk roles:** review semantics, quality, classification, privacy, security, access, and AI or sharing constraints. | Control decisions. |
| 4 | **Platform automation:** verify contract, compatibility, lineage, telemetry, reliability, portability, deployment, and rollback. | Machine-readable gate results. |
| 5 | **Consumer representative:** test a representative product port and operating guidance. | Acceptance evidence. |
| 6 | **Approvers:** record approve, reject, or exception with rationale, owner, expiry, and remediation. | Signed go-live record. |
| 7 | **Release service:** publish product, contract, ports, health, support, and release evidence atomically or roll back. | Live status and release receipt. |

## Decision Rules

- Any failed ownership, contract, security, policy, critical quality, lineage, or rollback gate blocks approval.
- An exception is explicit, risk-owned, time-bound, visible, monitored, and cannot bypass identity or policy.
- Approval applies only to the reviewed release; material changes require a new decision.

## Done Criteria

- Portal and catalog show the live version, current contract, ports, owner, support, health, limitations, and change policy.
- Observability and operations can detect impact, communicate, recover, and roll back.
- Consumers can subscribe to change and incident notifications.

Authoritative inputs: [Product Management Standard](../standards/data-product-management-standard.md), [Product Lifecycle](../architecture/data-product-lifecycle-design.md), and [Data Product Template](../delivery-templates/data-product-template.md).

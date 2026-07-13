# Evidence Rules

## Evidence States

Use one of these states for every assessed claim:

| State | Meaning |
| --- | --- |
| Verified | Current evidence directly demonstrates the claim. |
| Partial | Evidence covers only part of the scope or requirement. |
| Attested | An accountable person asserts the claim, but independent evidence is absent. |
| Stale | Evidence exists but is outside the accepted observation window. |
| Missing | No usable evidence was provided. |
| Not applicable | The requirement does not apply and the rationale is approved. |

Only **Verified** evidence satisfies a maturity check by default. Treat approved `Not applicable` items according to the assessment method and disclose their effect on the denominator.

## Evidence Quality

Prefer evidence in this order:

1. Automated control or conformance result with timestamp and scope.
2. Authoritative registry, policy, contract, catalog, lineage, or telemetry record.
3. Approved governance or architecture decision.
4. Reproducible test result.
5. Manual sample or accountable attestation.

Record the authority, scope, observation time, environment, version, and link or identifier.

## Decision Discipline

- Do not infer approval from the existence of a document.
- Do not infer enforcement from a declared policy.
- Do not infer product health from contract targets.
- Do not infer domain maturity from one successful product.
- Do not infer portability from a vendor export feature without round-trip or independent-client evidence.
- Do not infer AI approval from general data access.
- Do not infer operational readiness from the existence of a runbook; require a current controlled exercise and recovery evidence.
- Report uncertainty and evidence gaps explicitly.

## Gates

Evaluate mandatory gates separately from maturity:

- A failed or unassessed domain admission gate blocks enablement.
- A conditional gate requires an owner, compensating control, and expiry.
- A failed product go-live gate blocks product publication unless a governed exception explicitly permits it.
- An overall score never overrides a gate.

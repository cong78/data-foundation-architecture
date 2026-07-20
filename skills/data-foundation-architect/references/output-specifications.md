# Output Specifications

## Assessment

Return:

1. Scope, stable id, lifecycle, assessment version, date, and evidence window.
2. Admission-gate decision when applicable.
3. Six maturity dimension scores, overall score, lowest dimension, and evidence coverage.
4. Verified strengths.
5. Gaps and risks ordered by consequence.
6. Improvement actions with target evidence, owner, dependency, and due date when known.
7. Guidance used.

## Architecture Design

Return:

1. Problem, outcomes, scope, actors, assumptions, constraints, non-goals, and primary design class.
2. Owning service, supporting shared capability designs, integration scope, and affected target planes.
3. Logical architecture with readable diagram.
4. Component responsibilities and authoritative systems.
5. Main value flow, service handoffs, and failure behavior.
6. Identity, policy, contract, semantic, lineage, telemetry, and lifecycle controls.
7. Product ports and interoperability profile.
8. Decisions, alternatives, risks, and open questions.
9. Action playbook, runbook coverage, telemetry, recovery evidence, and runway phase for production scope.
10. Delivery increments and done criteria.

## Architecture Review

Lead with findings:

| Severity | Meaning |
| --- | --- |
| Critical | Unsafe, unlawful, or structurally invalid; blocks adoption or go-live. |
| High | Likely failure, material trust gap, or mandatory control missing. |
| Medium | Important inconsistency, operability gap, or avoidable coupling. |
| Low | Clarity, maintainability, or optimization opportunity. |

For each finding include the affected element, consequence, evidence, guidance reference, and correction. Treat a missing link between architecture, service ownership, playbook, runbook, and recovery evidence as an operability finding. Then provide assumptions, residual risks, and a short summary.

## Generated Artifact

- Preserve the owning template's structure.
- Mark unknown values `TBD` and list the evidence needed to resolve them.
- Include stable identifiers and versions where applicable.
- Keep contract targets separate from current measurements.
- Include decisions, exceptions, owners, expiry, and evidence links.
- For runbooks, preserve separate system, data-product, consumer, control, and stability recovery checks.

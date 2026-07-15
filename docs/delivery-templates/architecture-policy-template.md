# Architecture Policy Template

Use this template for every new or materially changed architecture principle, rule, or criterion. Keep the YAML readable and store executable Rego modules and tests under `policies/`.

## Policy Bundle

```yaml
apiVersion: architecture.foundation/v1alpha1
kind: ArchitecturePolicy
metadata:
  id: DF-SCOPE-RULE-000
  title: TBD
  version: 0.1.0
  status: draft
  owner: TBD
  reviewDate: YYYY-MM-DD
  tags: []
spec:
  principle:
    id: DF-SCOPE-PRINCIPLE-000
    statement: TBD enduring direction
    rationale: TBD why this matters
  rules:
    - id: DF-SCOPE-RULE-000
      level: MUST
      statement: Subject MUST perform one observable behavior under an explicit condition.
      scope:
        appliesTo: []
        environments: []
        conditions: []
      enforcement:
        outcome: block
        points: []
      criteria:
        - id: DF-SCOPE-CRITERION-000
          description: Pass when TBD is true, evidenced by named authorities.
          decisionRef: data.architecture.package_name.decision
          expectedResult: allow
          evidenceAuthorities: []
  exception:
    allowed: true
    approvers: []
    maximumDays: 90
    requiredFields: [rationale, risk, compensatingControls, owner, expiry, remediation]
implementation:
  engine: open-policy-agent
  language: rego.v1
  entrypoint: data.architecture.package_name.decision
  modules: [policies/rego/policy_name.rego]
  tests: [policies/rego/policy_name_test.rego]
```

## Rego Decision

```rego
package architecture.package_name

import rego.v1

default allow := false
default applicable := false

applicable if {
    # Evaluate the declared policy scope.
}

violations contains {
    "criterionId": "DF-SCOPE-CRITERION-000",
    "message": "Readable failure reason.",
} if {
    applicable
    # Evaluate structured input only.
}

allow if {
    applicable
    count(violations) == 0
}

allow if not applicable

decision := {
    "policyId": "DF-SCOPE-RULE-000",
    "policyVersion": "0.1.0",
    "applicable": applicable,
    "allow": allow,
    "violations": [violation | some violation in violations],
}
```

## Required Tests

| Test | Purpose | Expected result |
| --- | --- | --- |
| Valid case | Prove the intended architecture state passes. | `allow: true`, no violations. |
| Missing evidence | Prove absence does not silently pass. | `allow: false`, named criterion. |
| Prohibited state | Prove a known violation is blocked. | `allow: false`, readable reason. |
| Boundary case | Prove scope, lifecycle, environment, and version boundaries. | Explicit expected result. |
| Exception case | Prove only valid, unexpired, scoped exceptions alter enforcement. | Decision references exception evidence. |

## Review Record

| Field | Value |
| --- | --- |
| Principle is enduring and technology-neutral | Pass / Fail |
| Rule is atomic and uses one matching keyword | Pass / Fail |
| Scope and enforcement points are explicit | Pass / Fail |
| Criterion tests the rule without adding policy | Pass / Fail |
| Evidence authorities are named | Pass / Fail |
| Schema validation passes | Pass / Fail |
| Rego format, check, and tests pass | Pass / Fail |
| Compatibility and affected-object impact reviewed | Pass / Fail |
| Exception and lifecycle behavior approved | Pass / Fail |

Use the [Architecture Policy Language](../standards/architecture-policy-language.md) for grammar, lifecycle, decision shape, and enforcement rules.

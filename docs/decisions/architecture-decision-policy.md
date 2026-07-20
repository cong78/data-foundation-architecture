# Architecture Decision Policy

<div class="decision-brief"><div><small>Use when</small><strong>Writing a principle, architecture rule, or acceptance criterion.</strong></div><div><small>Decision</small><strong>Is this direction, obligation, or proof?</strong></div><div><small>Owner</small><strong>Architecture decision policy owner.</strong></div><div><small>Output</small><strong>Readable decision policy with executable criteria and evidence.</strong></div></div>

## Definition

The Architecture Decision Policy is the common way to express architecture intent as readable guidance and policy as code. It governs how architecture decisions become explicit, versioned, testable, enforceable, and evidenced. It separates three things that are often mixed together:

| Type | Purpose | Required form | Machine behavior |
| --- | --- | --- | --- |
| **Principle** | Explain enduring direction and why it matters. | `We favor [quality or outcome] because [rationale].` | Groups and explains rules; it does not produce a pass/fail result alone. |
| **Rule** | State one obligation, prohibition, recommendation, or permitted option. | `[Subject] MUST / MUST NOT / SHOULD / SHOULD NOT / MAY [behavior] [condition].` | Maps to an enforcement outcome at named control points. |
| **Criterion** | Prove whether one rule is met for one evaluated object. | `PASS when [observable condition], evidenced by [authority].` | Resolves a named policy decision from structured input. |

A complete policy bundle connects **principle → rule → criterion → decision → evidence**. A diagram, paragraph, checklist item, or technology default is not an enforceable architecture decision policy until that chain is explicit.

## Open Profile

No single open standard covers general architecture principles, rules, executable criteria, and operational evidence. This profile combines small, replaceable specifications:

| Concern | Open baseline | Use in this repository |
| --- | --- | --- |
| Normative wording | [IETF BCP 14: RFC 2119 and RFC 8174](https://www.rfc-editor.org/info/rfc8174/) | Uppercase `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` communicate requirement level without ambiguity. |
| Portable document | [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) | Validates the authoritative YAML or JSON policy envelope, identifiers, lifecycle, scope, rules, criteria, exceptions, and implementation references. |
| Executable decision | [Open Policy Agent and Rego](https://www.openpolicyagent.org/docs/policy-language) | Default open-source execution profile for evaluating structured JSON input and returning named decisions. |
| Policy testing | [OPA policy tests](https://www.openpolicyagent.org/docs/policy-testing) | Positive, negative, boundary, and exception tests run before policy publication. |
| Runtime integration | [OPA named policy decisions](https://www.openpolicyagent.org/docs/integration) | CI/CD, portals, APIs, provisioning, and go-live gates submit input and consume structured decisions. |
| Decision evidence | OpenTelemetry conventions and stable policy attributes | Correlates policy id, version, input, decision, violations, enforcement point, actor, and evidence time. |

The YAML or JSON envelope is authoritative. Rego is a replaceable implementation profile: another engine may be used only when it preserves the schema, identifiers, decision semantics, tests, and evidence requirements.

## Normative Keywords

| Keyword | Meaning | Default enforcement |
| --- | --- | --- |
| `MUST` | Mandatory behavior. | Block when false. |
| `MUST NOT` | Prohibited behavior. | Block when true. |
| `SHOULD` | Expected default with a documented reason for deviation. | Warn or require rationale. |
| `SHOULD NOT` | Discouraged behavior requiring justification. | Warn or require rationale. |
| `MAY` | Explicitly permitted option. | Inform; never interpreted as mandatory. |

Use uppercase only when the word has this normative meaning. Avoid `shall`, `normally`, `appropriate`, `where possible`, and unqualified lower-case `must` or `should` in policy statements.

## Authoring Grammar

### Principle

Write one stable direction and rationale:

> Data is managed as a product with an explicit and observable promise.

A principle remains technology-neutral. It can guide several rules and does not pretend to be directly executable.

### Rule

Write one subject, one normative keyword, one behavior, and an explicit condition:

> A go-live-approved or active data product **MUST** reference one approved or published contract containing its product descriptor.

Split statements containing independent obligations into separate rules. A rule always has a stable id, scope, owner, version, enforcement points, failure outcome, criteria, and exception behavior.

### Criterion

Write an observable pass condition and authoritative evidence:

> PASS when the product references a contract id with approved or published status and an embedded descriptor, evidenced by the contract registry and product go-live record.

A criterion cannot introduce a new obligation. It only evaluates its parent rule. Human approval may be evidence, but `approved by architecture` is not sufficient without the decision scope and record.

## Policy Source Document

The policy source document is YAML or equivalent JSON validated against `policies/schema/architecture-policy.schema.json`. It contains:

| Section | Required content |
| --- | --- |
| Metadata | Stable id, title, semantic version, lifecycle status, owner, review date, and tags. |
| Principle | Principle id, statement, and rationale. |
| Rules | Rule id, normative level, atomic statement, scope, enforcement outcome, enforcement points, and criteria. |
| Criteria | Criterion id, readable pass condition, named decision reference, expected result, and evidence authorities. |
| Exception | Whether exceptions are allowed, approvers, maximum duration, required risk fields, and remediation. |
| Implementation | Engine profile, language version, named entrypoint, modules, and tests. |

Stable identifiers use `<scope>-<type>-<number>`, for example `DF-DATA-RULE-001`. Versions change independently from implementation releases. A breaking semantic or input-contract change requires a major policy version.

## Decision Input and Result

Every executable policy receives a JSON input document and returns a deterministic JSON decision. The minimum result is:

```json
{
  "policyId": "DF-DATA-RULE-001",
  "policyVersion": "1.0.0",
  "applicable": true,
  "allow": false,
  "violations": [
    {
      "criterionId": "DF-DATA-CRITERION-001",
      "message": "Live product does not reference a publishing data contract id."
    }
  ]
}
```

`applicable: false` means the evaluated object is outside the declared scope and is not a pass claim. The enforcement service adds evaluation time, policy-bundle digest, input reference, actor, enforcement point, exception reference, and trace id to the evidence record. Policy code remains deterministic and must not depend on wall-clock time, network calls, or mutable hidden state.

## Enforcement Model

| Point | Typical input | Required behavior |
| --- | --- | --- |
| Authoring and pull request | Policy document, design artifact, contract, configuration, or infrastructure plan. | Validate schema, references, syntax, tests, and compatibility. |
| Architecture review | Design facts, decisions, exceptions, and evidence references. | Show applicable principles, rule outcomes, failed criteria, and accountable decisions. |
| Provisioning and deployment | Resolved resource plan, identity, environment, policy version, and release. | Block mandatory violations before mutation. |
| Product go-live | Product, contract, workload, lineage, controls, tests, and release evidence. | Evaluate all blocking criteria against one immutable candidate. |
| Runtime reconciliation | Actual runtime, catalog, policy, health, and lifecycle state. | Detect drift, deny unsafe behavior, or create an accountable remediation record. |

Policy evaluation and enforcement remain separate. The evaluator returns a decision; the responsible service blocks, warns, records an exception, or routes remediation.

## Exceptions and Lifecycle

- An exception never edits or disables the policy definition.
- Every exception records policy id and version, object scope, rationale, risk, compensating controls, owner, approval, expiry, and remediation.
- Mandatory identity, legal, or safety controls may declare `allowed: false`.
- Expired exceptions evaluate as violations.
- Policies use `draft → proposed → active → deprecated → retired`; active versions remain immutable.
- Every policy change runs schema validation, Rego tests, compatibility review, and affected-object analysis.

## Repository Example

The executable example under `policies/` demonstrates a product go-live rule:

```bash
python scripts/validate_architecture_policies.py
opa test policies/rego -v
opa eval \
  --data policies/rego/data_product_contract.rego \
  --input policies/inputs/compliant-product.json \
  data.architecture.data_product_contract.decision
```

Use the [Architecture Decision Policy Template](../reference-solutions/architecture-policy-template.md) to create another bundle.

## Minimum Done Criteria

- Principle, rules, and criteria are distinct and linked by stable ids.
- Every rule contains exactly one matching normative keyword.
- Every mandatory rule has a blocking enforcement outcome and at least one executable criterion.
- Authoritative YAML or JSON validates against the pinned JSON Schema.
- Named Rego decisions return the standard result shape from explicit JSON input.
- Positive, negative, boundary, and exception tests pass.
- Policy owner, version, review date, enforcement points, and exception behavior are explicit.
- Decisions emit correlated, time-stamped evidence without logging prohibited input data.
- A policy engine can be replaced without changing the policy identifiers or decision meaning.

<div class="read-next"><strong>Next:</strong> use the <a href="../architecture-decision-process/">Architecture Decision Process</a> to establish authority and rationale, then use this policy for enforceable rules and the policy template for a machine-executable bundle.</div>

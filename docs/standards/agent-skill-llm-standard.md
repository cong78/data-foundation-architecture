# Agent, Skill and LLM Standard

<div class="decision-brief"><div><small>Use when</small><strong>Designing or releasing an agent, skill, model route, or tool action.</strong></div><div><small>Decision</small><strong>Is autonomy bounded, evaluated, approved, and traceable?</strong></div><div><small>Owner</small><strong>Agent or skill owner with risk approvers.</strong></div><div><small>Output</small><strong>Versioned capability, evaluations, policy, and receipts.</strong></div></div>

This standard defines the minimum contract for agentic capabilities in the data foundation.

It applies the lifecycle and provenance expectations of the [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), the risk controls in the [OWASP AI Agent Security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), and the excessive-agency principle of minimizing tool functionality, permissions and autonomy.

## Agent Manifest

| Field | Requirement |
| --- | --- |
| Agent id and version | Stable identifier and immutable released version. |
| Owner and support | Accountable owner, technical owner and escalation route. |
| Goal and boundaries | Permitted goals, prohibited goals and target users. |
| Autonomy | Maximum autonomy level and actions that always require approval. |
| Identity | Workload identity, delegated-user model and allowed trust domains. |
| Skills | Exact approved skill ids and version constraints. |
| Context | Allowed products, metadata types, classifications and retrieval policy. |
| Memory | Allowed memory types, retention, deletion and isolation. |
| Model profile | Approved model capabilities, routing policy and data handling class. |
| Budgets | Turn, tool, token, time, concurrency and cost limits. |
| Evaluation | Required suites, thresholds, red-team evidence and latest result. |
| Telemetry | Required identifiers, spans, metrics, audit and content-capture policy. |

## Skill Manifest

| Field | Requirement |
| --- | --- |
| Skill id and version | Stable, namespaced identifier and semantic version. |
| Description | One bounded capability written for discovery without hidden behavior. |
| Input and output | Machine-readable schemas with examples and validation. |
| Side effects | Read, draft, reversible write, irreversible write, external action. |
| Authorization | Required roles, attributes, purpose, scopes and step-up rules. |
| Data policy | Allowed classifications, fields, masking and residency. |
| Idempotency | Idempotency key and duplicate execution behavior. |
| Reliability | Timeout, retry, rate limit, circuit breaker and compensation. |
| Approval | Approval rule and independently generated action preview. |
| Observability | Trace attributes, audit event, outcome and cost metrics. |
| Tests | Contract, policy, safety, failure, replay and conformance tests. |

Skills call stable foundation APIs. Prompt text may guide skill selection, but it cannot redefine authorization, validation, or side effects.

## LLM Profile

| Field | Requirement |
| --- | --- |
| Profile id | Stable enterprise model profile independent of provider deployment name. |
| Supported tasks | Reasoning, extraction, classification, generation, embeddings, vision or tool use. |
| Data handling | Permitted classification, region, retention, training use and logging. |
| Model routing | Approved providers, fallback order and availability requirements. |
| Output contract | Structured output schema, citation and uncertainty requirements. |
| Safety | Content controls, prompt-injection handling and prohibited use. |
| Performance | Quality threshold, latency target, context limit and cost budget. |
| Lifecycle | Evaluation evidence, release status, deprecation and rollback. |

The agent references an LLM profile. It does not hard-code a single vendor model throughout business logic.

## Protocol Rules

| Boundary | Standard Direction |
| --- | --- |
| Foundation service | OpenAPI or AsyncAPI is canonical. |
| Assistant to tools | Typed internal tool API; MCP adapter may expose approved resources, prompts and tools. |
| Agent to remote agent | A2A may expose agent identity, skills, tasks and artifacts. |
| Telemetry | OpenTelemetry GenAI conventions plus foundation identifiers. |
| Artifacts | Canonical product, contract and evidence formats remain authoritative. |

MCP and A2A are interoperability adapters. Neither protocol grants authorization by itself or replaces policy checks at the target service.

## Approval Classes

| Class | Examples | Rule |
| --- | --- | --- |
| Read | Search catalog, inspect health, compare contracts. | Policy check; no confirmation unless sensitive. |
| Draft | Draft contract, onboarding plan, incident summary. | User reviews before publication. |
| Reversible write | Create request, submit review, retry validation. | Explicit confirmation or pre-approved bounded automation. |
| High impact | Publish, share externally, grant or revoke access, delete or retire. | Step-up authorization and named approver. |

## Evaluation Gates

An agent or skill cannot be certified without evidence for:

- Task completion and structured-output validity.
- Grounding, citation correctness and unsupported-claim rate.
- Correct skill selection and parameter generation.
- Identity, policy, purpose and approval enforcement.
- Prompt injection, indirect injection and tool-output isolation.
- Excessive agency, privilege escalation and data exfiltration resistance.
- Memory isolation, poisoning resistance and deletion.
- Timeout, retry, cancellation, idempotency and compensation.
- Latency, token use, tool use and cost budgets.
- Human escalation and safe failure behavior.

## Lifecycle

Agents, skills, prompts, retrieval configurations, model profiles and evaluation suites are versioned independently. A release records the exact dependency set. Breaking skill changes require a new major version and consumer impact analysis. A failing safety or policy evaluation blocks promotion and may trigger automatic suspension of the affected version.

## Minimum Done Criteria

- The agent, every enabled skill, and every LLM profile have stable ids, immutable versions, accountable owners, support routes, and approved manifests.
- Skill inputs, outputs, side effects, authorization, data policy, reliability, approval, and telemetry are machine-readable and tested.
- Read, draft, reversible-write, and high-impact actions enforce the correct policy, confirmation, step-up, and named-approval behavior.
- Evaluation evidence covers task quality, grounding, injection resistance, excessive agency, privilege, data handling, memory, failure, recovery, and cost thresholds.
- A release records exact agent, skill, prompt, retrieval, model-profile, policy, and evaluation versions and supports rollback or suspension.
- Traces and audit records connect actor, delegated user, agent, skill, model profile, product, contract, purpose, policy decision, approval, action, outcome, and cost without leaking sensitive payloads.

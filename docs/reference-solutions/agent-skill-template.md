# Agent and Skill Template

Use this template to propose, review and certify an agentic capability.

## Agent Summary

| Field | Value |
| --- | --- |
| Agent id and version |  |
| Owning foundation service |  |
| Multi-agent role | Assistant orchestrator / Service specialist / Contract specialist |
| Goal |  |
| Owner and support |  |
| Intended users |  |
| Prohibited goals |  |
| Maximum autonomy | A0 / A1 / A2 / A3 / A4 |
| Workload identity |  |
| Delegated-user model |  |
| Applicable data contract types |  |
| Behavior when contract is missing, expired, suspended or incompatible |  |
| Deterministic service fallback |  |
| LLM profile |  |
| Data classification limit |  |
| Turn, tool, time and cost budgets |  |

## Delegated Task Contract

| Field | Value |
| --- | --- |
| Accepted parent agents |  |
| Task input and output schemas |  |
| Required actor, purpose and contract references |  |
| Scope-narrowing and rejection rules |  |
| Maximum delegated autonomy |  |
| Budget and deadline behavior |  |
| Approval-state propagation |  |
| Completion owner and status authority |  |

## Skills

| Skill id and version | Purpose | Side Effect | Permission | Approval |
| --- | --- | --- | --- | --- |
|  |  | Read / Draft / Write / High impact |  |  |

## Context and Memory

| Type | Source | Policy Filter | Retention | Deletion |
| --- | --- | --- | --- | --- |
| Product context |  |  |  |  |
| Contract and policy |  |  |  |  |
| Conversation |  |  |  |  |
| Working memory |  |  |  |  |
| User preference |  |  |  |  |

## Action Controls

| Action | Target | Risk | Reversible | Approval | Compensation |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Contract-Driven Execution

| Contract Declaration | Compiled Control | Agent Behavior | Service Enforcement | Evidence |
| --- | --- | --- | --- | --- |
| Identity and purpose |  |  |  |  |
| Product, source, consumer, recipient and port scope |  |  |  |  |
| Allowed skills and parameter limits |  |  |  |  |
| Lifecycle, effective time, expiry and revocation |  |  |  |  |
| SLO, validation, telemetry and recovery obligations |  |  |  |  |

## Evaluation Evidence

| Gate | Suite | Threshold | Result | Evidence |
| --- | --- | --- | --- | --- |
| Task success |  |  |  |  |
| Grounding and citations |  |  |  |  |
| Tool selection |  |  |  |  |
| Policy enforcement |  |  |  |  |
| Prompt injection |  |  |  |  |
| Excessive agency |  |  |  |  |
| Multi-agent delegation and scope preservation |  |  |  |  |
| Contract expiry, suspension and revocation |  |  |  |  |
| Memory isolation |  |  |  |  |
| Reliability and cancellation |  |  |  |  |
| Latency and cost |  |  |  |  |

## Telemetry

Record conversation, task, agent, agent version, model profile, skill, tool, user, product, contract, purpose, policy decision, approval, trace, cost and outcome identifiers. Define which prompt or response content may be retained.

## Decision

**Status:** Draft / Review / Certified / Active / Suspended / Deprecated / Retired / Exception

**Approver:**

**Conditions and review date:**

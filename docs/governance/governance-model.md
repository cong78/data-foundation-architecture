# Governance Model

The data foundation requires governance that is practical, embedded, and accountable. Governance should guide delivery teams without becoming a separate manual process disconnected from the platform.

## Governance Roles

| Role | Responsibility |
| --- | --- |
| Data product owner | Owns product purpose, value, consumer fit, and lifecycle direction. |
| Data domain owner | Owns the domain boundary, portfolio direction, foundation adoption, funding, risks and maturity improvement. |
| Data steward | Owns definitions, quality rules, classification, and usage guidance. |
| Data engineer | Builds and operates ingestion, transformation, and publication pipelines. |
| Platform owner | Owns foundation service reliability, patterns, and platform runway. |
| Security and privacy officer | Defines and validates controls for sensitive or regulated data. |
| Consumer owner | Owns correct use of data within BI, applications, platforms, or AI systems. |
| Contract owner | Owns data contract accuracy, versioning, compatibility decisions, and change communication. |
| Product portfolio owner | Owns portfolio health across a domain, including duplication, adoption, lifecycle, cost, and retirement decisions. |
| Service agent owner | Owns a service agent's goal, delegated actions, autonomy limits, evaluation, lifecycle, deterministic fallback, and business outcome. This is normally the service owner or an accountable delegate. |
| AI Assistant owner | Owns multi-agent coordination, task routing, user interaction, delegation integrity, and end-to-end task status; does not assume accountability for specialist service decisions. |
| Skill owner | Owns the skill contract, authorization, reliability, tests and compatibility. |
| Model platform owner | Owns approved LLM profiles, routing, provider controls, availability and cost. |

## Governance Domains

- Ownership and accountability.
- Data classification and sensitivity.
- Data quality and product go-live.
- Access control and usage purpose.
- Lineage and impact analysis.
- Data retention and deletion.
- External sharing approval.
- AI data usage and model lineage.
- Data contract approval, compatibility, versioning, and exception handling.
- Data product go-live, portfolio health, duplication management, and retirement.
- Agent, skill, prompt, model profile, context, memory and evaluation governance.

## Multi-Agent Decision Rights

- The user or accountable owner approves the intent, purpose, contract, and autonomy class.
- The contract owner approves the declarative execution envelope and its lifecycle.
- The AI Assistant may interpret, plan, route, and coordinate work, but cannot widen authority or approve its own exception.
- Each service owner remains accountable for its specialist agent, typed skills, deterministic APIs, evidence, and recovery path.
- A receiving service agent may narrow, reject, or escalate a delegated task; it cannot add purpose, scope, tools, data, budget, or autonomy.
- Contract suspension, expiry, or revocation removes the associated execution authority at the next policy decision.

## Decision Forums

| Forum | Decisions |
| --- | --- |
| Data foundation architecture board | Architecture patterns, service direction, exceptions |
| Data governance council | Policy, ownership, classification, quality standards |
| Domain data forum | Domain boundary, product priorities, stewardship, consumer feedback, maturity gaps and improvement plan |
| Security and privacy review | Sensitive data access, external sharing, AI usage risks |
| Data contract review | Contract approval, breaking changes, consumer impact, migration timelines |
| Data product portfolio review | Product adoption, duplicate products, ownerless products, health breaches, cost, retirement |
| Agentic AI review | Agent autonomy, skills, model profiles, evaluations, safety evidence, incidents, suspension and retirement |

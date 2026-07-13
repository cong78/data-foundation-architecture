# AI-Ready Data Standard

<div class="decision-brief"><div><small>Use when</small><strong>Publishing or approving data for AI use.</strong></div><div><small>Decision</small><strong>Is the data fit, permitted, traceable, and reproducible for the AI purpose?</strong></div><div><small>Owner</small><strong>Product owner and AI use-case owner.</strong></div><div><small>Output</small><strong>Approved AI-use profile and evidence.</strong></div></div>

AI-ready data is data that can be safely and effectively used by AI agents, models, retrieval systems, feature pipelines, and evaluation workflows.

Agentic use must also follow the [Agent, Skill and LLM Standard](agent-skill-llm-standard.md).

## AI-Ready Requirements

| Requirement | Why It Matters |
| --- | --- |
| Clear business meaning | Models and agents need unambiguous context. |
| Source lineage | AI output must be traceable back to trusted data. |
| Quality evidence | Poor data quality becomes poor model behavior. |
| Freshness signal | AI systems need to know whether context is current. |
| Access policy | AI agents and service accounts must follow the same rules as humans. |
| Usage approval | Training, retrieval, grounding, and evaluation have different risk profiles. |
| Observability | AI usage must be traceable to product, consumer, and purpose. |
| Evaluation data | AI systems need trusted datasets for regression and quality checks. |
| Portable identifiers | AI traces must correlate the product, contract, snapshot, index, evaluation set, identity, purpose, and source across tools. |
| Semantic context | AI access must bind product meaning, grain, relationships, usage context, limitations, and evidence to exact product and contract versions. |

## AI Consumption Patterns

| Pattern | Description | Required Controls |
| --- | --- | --- |
| Retrieval | Product data is indexed or served as context for agents or applications. | Freshness, lineage, access control, sensitive data filtering, retrieval evaluation. |
| Training | Product data is used to train or fine-tune a model. | Explicit approval, privacy review, retention rules, model lineage, data snapshot. |
| Evaluation | Product data is used to test model or agent quality. | Representative dataset, expected outputs, versioning, bias and coverage review. |
| Feature use | Product data becomes model features. | Feature contract, drift monitoring, lineage, model dependency tracking. |
| Grounded answer API | Agent retrieves governed context at runtime. | Agent identity, purpose policy, response audit, source citation capability. |

## AI-Ready Data Product Checklist

- Product has a contract with AI usage permissions.
- Product classification permits the AI purpose.
- Product has clear business definitions and semantic descriptions.
- Product has quality rules and current quality status.
- Product has freshness SLO and current freshness value.
- Product lineage reaches back to source systems.
- Product access is enforced for agent or model identities.
- Product usage by AI systems is logged and observable.
- Retrieval or feature indexes are linked to product version and contract version.
- Evaluation datasets are versioned and linked to expected behavior.
- Retrieval indexes and feature views have independent lifecycle, version, freshness, and lineage records linked to their source product.
- Agent adapters expose approved capabilities without becoming the product, policy, or metadata authority.
- Agent context is filtered by authenticated identity, purpose, product contract and current policy before model invocation.
- Semantic context uses authoritative references and records the exact context version used for retrieval, grounding, or agent decisions.

## AI Evidence Model

| Evidence | Example |
| --- | --- |
| Usage approval | Approval record for retrieval, training, evaluation, or feature use. |
| Data snapshot | Product version and extraction timestamp used by model or index. |
| Lineage | Source systems, pipelines, product version, index or feature version. |
| Quality status | Quality score and failed checks at time of AI use. |
| Access record | Agent, model, application, user, and approved purpose. |
| Observability | Retrieval volume, latency, errors, freshness, and consumer usage. |
| Evaluation linkage | Evaluation set id, version, expected behavior, result, and product snapshot. |

## AI Interoperability Test

An AI access pattern is portable when a request can be traced across two independent components using the same product, contract, dataset snapshot, identity, purpose, and trace identifiers. The test must also prove that access policy, source attribution, and revocation remain effective when the AI adapter changes.

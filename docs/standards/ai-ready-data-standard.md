# AI-Ready Data Standard

<div class="decision-brief"><div><small>Use when</small><strong>Publishing or approving data for AI use.</strong></div><div><small>Decision</small><strong>Is the data fit, permitted, traceable, and reproducible for the AI purpose?</strong></div><div><small>Owner</small><strong>Product owner and AI use-case owner.</strong></div><div><small>Output</small><strong>Approved AI-use profile and evidence.</strong></div></div>

AI-ready data is data that can be safely and effectively used by AI agents, models, retrieval systems, feature pipelines, and evaluation workflows.

AI readiness is not a permanent label on a dataset. It is an evidence-backed decision for a specific combination of **product version, AI purpose, consumption pattern, identity, model or agent, and operating context**. A product may be ready for BI, approved for retrieval, and prohibited for training at the same time.

Agentic use must also follow the [Agent, Skill and LLM Standard](agent-skill-llm-standard.md).

## Start with the AI Context

Complete this context before evaluating readiness. An unknown answer is a gap, not an assumed pass.

| Context question | Required input |
| --- | --- |
| What outcome is supported? | Business outcome, user, decision or action, value measure, and accountable AI use-case owner. |
| How will data be used? | Retrieval, grounding, feature use, training, fine-tuning, evaluation, agent tool input, or another declared pattern. |
| What can go wrong? | Harmful answer or action, privacy exposure, unfair treatment, stale decision, unsupported claim, data leakage, or operational disruption. |
| Which exact data is needed? | Product id, contract version, fields, rows, time range, geography, classification, semantic context, and minimization rationale. |
| Is the use live or reproducible? | Live product and freshness target, or immutable snapshot, index, feature, and evaluation-set versions. |
| Who accesses it? | Application, model, agent, skill, workload identity, delegated user, team, environment, and approved purpose. |
| What behavior must be proven? | Grounding, retrieval relevance, coverage, prediction quality, bias, safety, refusal, citation, latency, cost, and fallback thresholds. |
| What is prohibited? | Disallowed purposes, models, regions, fields, outputs, actions, retention, onward use, and training. |

## Traditional Analytics and AI-Facing Products

An AI-facing product extends the same product disciplines used for analytics and BI. It does not justify a parallel ungoverned copy.

| Design concern | Traditional analytics or BI-facing product | AI-facing extension |
| --- | --- | --- |
| Primary outcome | Repeatable measures, trends, reports, exploration, and human decisions. | Predictions, generated answers, retrieval context, automated recommendations, features, evaluations, or bounded agent actions. |
| Main interface | SQL, table, semantic model, metric view, dashboard extract, or file. | Retrieval or context API, feature view, snapshot, evaluation set, vector or search index, bounded query, tool resource, plus suitable table or API ports. |
| Meaning | Business definitions, grain, dimensions, measures, filters, and time semantics. | The same meaning plus valid prompts or tasks, examples, relationships, limitations, ambiguity, citation units, and machine-usable context. |
| Quality focus | Accuracy, completeness, freshness, uniqueness, consistency, and reconciliation. | The same controls plus representativeness, coverage, label quality, leakage, retrieval relevance, chunk or feature integrity, bias, drift, and harmful-content risk. |
| Time behavior | Current reporting period, refresh schedule, and restatement rules. | Exact snapshot or index version, training cut-off, event time, freshness at inference, reproducibility, and temporal leakage prevention. |
| Access | Named users and BI workloads with row, column, purpose, export, and subscription controls. | Model, agent, skill, application, delegated user, and workload identities with purpose-specific training, retrieval, output, retention, and tool-action controls. |
| Lineage | Source-to-report or source-to-metric traceability. | Source-to-product-to-snapshot, feature, index, model, prompt or retrieval, evaluation, output, and action traceability. |
| Validation | Metric reconciliation, user acceptance, query performance, and dashboard checks. | Offline and online evaluations, baseline comparison, grounding and citation checks, safety tests, drift tests, human review, and fallback validation. |
| Observability | Refresh, quality, query usage, availability, incidents, and cost. | The same signals plus retrieval, feature, prompt or context version, model or agent identity, evaluation outcome, refusal, unsafe output, latency, token or compute cost, and downstream action. |
| Change impact | Schema, metric, semantic, refresh, and dashboard compatibility. | The same impact plus re-indexing, retraining, re-evaluation, prompt or tool behavior, model drift, and approval renewal. |

### Reuse, Project, or Create

| Decision | Use when | Architecture action |
| --- | --- | --- |
| Reuse the analytics product | Grain, semantics, fields, freshness, quality, policy, and interface already satisfy the AI purpose. | Add an AI-use profile to the Data Product Consumption Contract, plus workload identity, purpose decision, AI evaluation, and telemetry without copying the product. |
| Add an AI projection | The authoritative product is suitable but AI needs chunks, embeddings, features, labels, a bounded snapshot, or an evaluation set. | Create a versioned derivative projection linked to the source product and contract; give it independent freshness, rebuild, evaluation, retention, and retirement evidence. |
| Create or change a data product | The AI need requires materially different semantics, ownership, quality, SLO, lifecycle, or reusable output. | Use the normal product proposal and go-live process. Do not call a private model-preparation table a product by default. |
| Reject or redesign the use | Purpose, rights, representativeness, quality, safety, identity, or control obligations cannot be satisfied. | Minimize or anonymize data, constrain the AI behavior, select another product or interface, or stop the use case. |

## AI Consumption Patterns

| Pattern | Required product evidence | Not ready when |
| --- | --- | --- |
| Retrieval or grounding | Chunk or document identity, semantic context, permission filtering before retrieval, source citations, index version, freshness, deletion propagation, relevance and grounding evaluation. | Access is filtered only after retrieval, citations cannot resolve to a source version, deleted data remains indexed, or relevance and unsupported-claim thresholds are absent. |
| Training or fine-tuning | Approved immutable snapshot, collection basis, rights, representativeness, label provenance, leakage tests, retention, model lineage, and reproducible preparation. | Data rights are unclear, the dataset contains prohibited populations or fields, a moving live table is used without snapshotting, or leakage and bias are untested. |
| Evaluation | Versioned cases, expected behavior or scoring rubric, coverage by segment and risk, independence from training data, evaluator method, baseline, and release threshold. | The set is sampled only from successful examples, overlaps training data without control, lacks high-risk cases, or has no release decision threshold. |
| Feature use | Feature definition, entity and event-time semantics, offline and online parity, point-in-time correctness, freshness, null behavior, drift, and model dependency. | Feature leakage, training-serving skew, unstable entity keys, or unowned transformations remain. |
| Agent or tool context | Registered agent and skill, bounded resource or tool schema, delegated identity, contract and policy check, output minimization, approval class, receipt, and kill switch. | The agent receives broad credentials, can bypass product policy, treats tool output as authorization, or consequential actions lack approval and recovery. |

## AI-Ready Data Product Checklist

Use this checklist as a gate. Record **Pass, Conditional, Fail, or Not applicable**, an accountable owner, evidence link, and review date for every row. Any failed blocking row prevents approval for the declared AI purpose.

| Gate | Required action | Passing evidence | Primary owner | Blocking |
| --- | --- | --- | --- | :---: |
| Purpose | Declare one AI pattern, outcome, user, decision or action, value measure, prohibited uses, and risk tier. | Approved AI use-case and purpose record linked to the product. | AI use-case owner | Yes |
| Product and contract | Resolve exact product, port, contract, semantic-context, and lifecycle versions; declare whether the use reuses, projects, or changes the product. | Versioned dependency record and approved Data Product Consumption Contract with AI-use terms. | Product owner | Yes |
| Rights and classification | Confirm collection basis, classification, privacy, intellectual property, residency, retention, onward use, and training or retrieval permission. | Governance and legal decision with conditions and expiry. | Data steward and control owner | Yes |
| Minimization | Select only required records, fields, time ranges, context, features, or documents; justify each sensitive element. | Approved scope and enforced row, column, field, retrieval, and output rules. | Product owner and AI engineer | Yes |
| Meaning and context | Publish grain, time meaning, concepts, relationships, labels, metrics, examples, limitations, ambiguity, and valid or invalid uses. | Versioned semantic context package tested with representative AI tasks. | Data steward | Yes |
| Lineage and reproducibility | Trace sources and transformations to the exact live version, snapshot, feature, index, evaluation set, model or agent release, and output. | Machine-resolvable lineage and a reproducible build or retrieval record. | Technical owner | Yes |
| Data quality | Define thresholds for conventional quality and AI-specific coverage, representativeness, label, leakage, chunk, feature, retrieval, or bias risks. | Current results by relevant segment, exception decisions, and remediation owner. | Product owner and AI evaluator | Yes |
| Freshness and time | Define live freshness, snapshot cut-off, event-time behavior, restatement, deletion propagation, and temporal leakage controls. | SLO result and a test proving time behavior for the selected pattern. | Technical owner | Yes |
| Identity and policy | Register application, model, agent, skill, workload, delegated user, environment, and purpose; enforce service and data decisions independently. | Allow, deny, expiry, revocation, delegation, and purpose tests at the real access boundary. | Access owner | Yes |
| Projection integrity | Version indexes, embeddings, features, labels, caches, and evaluation sets independently and link them to source product and contract versions. | Build manifest, reconciliation result, freshness, deletion, rebuild, rollback, and retirement tests. | AI platform owner | When used |
| Evaluation | Define baseline, representative and high-risk cases, metrics, thresholds, evaluator, release rule, and regression cadence before go-live. | Retained evaluation report tied to data, projection, model or agent, and configuration versions. | AI use-case owner | Yes |
| Runtime safeguards | Define output filtering, citation, uncertainty or refusal, human review, fallback, rate and budget limits, action approval, suspension, and recovery. | Executed safety, failure, fallback, and kill-switch tests. | AI application owner | Yes |
| Observability | Emit product, contract, snapshot or index, identity, purpose, model or agent, evaluation, latency, cost, outcome, and trace identifiers without sensitive payload leakage. | Correlated trace and dashboard plus alert and incident route. | Observability owner | Yes |
| Change and lifecycle | Define which product, contract, policy, projection, model, or semantic changes trigger re-indexing, retraining, re-evaluation, reapproval, notification, or shutdown. | Tested change matrix, dependency subscriptions, deprecation plan, and review date. | Product and AI owners | Yes |
| Consumer validation | Test the real AI application with representative users and production-like controls, not only a notebook or model benchmark. | Acceptance evidence, known limitations, operating owner, support route, and go-live decision. | AI use-case owner | Yes |

### Readiness Outcome

| Outcome | Meaning | Next action |
| --- | --- | --- |
| Approved | All applicable blocking gates pass for the declared product version, AI purpose, pattern, identity, and environment. | Publish the approved AI-use profile and monitor it. |
| Conditional | No unacceptable risk remains, but named evidence or controls have an owner and expiry. | Restrict scope and close conditions before expiry. |
| Projection required | The source product is trusted, but the AI-specific derivative needs its own lifecycle and evidence. | Build and approve the projection without duplicating product ownership. |
| Not approved | One or more blocking gates fail or required evidence is unknown. | Redesign, select another product, reduce scope, or stop the use. |

## AI Evidence Model

| Evidence | Minimum context |
| --- | --- |
| AI-use decision | Product and contract versions, pattern, purpose, scope, conditions, prohibited use, owner, approver, decision, expiry, and review date. |
| Data binding | Live product release or immutable snapshot plus selected fields, time range, location, classification, and checksum or equivalent identity. |
| Projection manifest | Source product and contract, transformation, chunking or feature configuration, index or feature version, build time, freshness, deletion and rebuild state. |
| Lineage | Sources, transformations, product, snapshot, projection, model or agent release, evaluation, output, and action identifiers. |
| Quality and evaluation | Segment-level data results, AI task results, thresholds, baseline, exceptions, evaluator, configuration, and observation time. |
| Access record | Application, model, agent, skill, workload, delegated user, purpose, policy version, obligations, decision, result, and revocation state. |
| Runtime evidence | Retrieval, context, feature, citation, refusal, safety, latency, cost, outcome, incident, and trace identifiers. |

## AI Interoperability Test

An AI access pattern is portable when a request can be traced across two independent components using the same product, contract, dataset snapshot, identity, purpose, and trace identifiers. The test must also prove that access policy, source attribution, and revocation remain effective when the AI adapter changes.

## Minimum Done Criteria

- The AI context names the exact outcome, pattern, product and contract versions, purpose, identity, model or agent, environment, risks, prohibited uses, and accountable owner.
- Every applicable blocking checklist gate passes, or a conditional decision restricts scope with named evidence, owner, expiry, and review date.
- Rights, classification, minimization, semantic context, lineage, quality, freshness, identity, policy, evaluation, safeguards, and consumer validation are proven at the real access path.
- Snapshots, indexes, embeddings, features, labels, and evaluation sets are independently versioned, reproducible, rebuildable, deletable, and traceable when used.
- Runtime evidence correlates the product, contract, projection, model or agent, identity, purpose, policy decision, evaluation, output or action, and trace.
- Change, re-evaluation, reapproval, suspension, fallback, recovery, deprecation, and retirement triggers are tested and operationally owned.

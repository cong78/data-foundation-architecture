# Definition and Principles

<div class="decision-brief"><div><small>Use when</small><strong>Deciding whether a need belongs in the data foundation.</strong></div><div><small>Decision</small><strong>Does this need create a durable data-product responsibility?</strong></div><div><small>Owner</small><strong>Source, foundation, and domain owners.</strong></div><div><small>Output</small><strong>Agreed boundary, accountability, and design direction.</strong></div></div>

## Definition

The **data foundation** is the shared organizational capability that turns data needed beyond its source boundary into trusted, governed, and reusable data products. It gives people, applications, platforms, AI agents, and models a consistent way to discover, understand, access, and rely on data.

<div class="foundation-definition-model" role="img" aria-label="The data foundation turns data beyond source boundaries into governed data products for people, systems, models, and AI agents">
  <div class="foundation-definition-model__title"><small>Definition model</small><strong>From source-owned data to trusted, governed, reusable data products</strong></div>
  <div class="foundation-definition-model__flow">
    <div>
      <small>Source authority</small>
      <strong>Operational systems and external sources</strong>
      <span>Own transactions, source meaning, availability, and change obligations.</span>
    </div>
    <i aria-hidden="true">→</i>
    <div class="foundation-definition-model__focus">
      <small>Shared data foundation</small>
      <strong>Turn data into managed products</strong>
      <span>Ingest or connect · contract · contextualize · govern · observe · operate</span>
      <b>Trusted, governed, reusable data products</b>
    </div>
    <i aria-hidden="true">→</i>
    <div>
      <small>Purpose-bound use</small>
      <strong>People, applications, platforms, models, and AI agents</strong>
      <span>Discover and use dependable data through governed product ports.</span>
    </div>
  </div>
  <div class="foundation-definition-model__rule"><strong>Boundary rule</strong><span>The foundation owns the durable data-product responsibility beyond the source boundary; it does not replace source transactions or consumer decisions and actions.</span></div>
</div>

A durable data-product responsibility exists when data needs its own owner, meaning, quality expectations, access rules, service level, evidence, and lifecycle beyond one source application or one consumer implementation.

## Foundation Boundary

This boundary answers one practical question: **when should data become a foundation-managed data product, and when should a consumer continue to use the source system directly?**

“Bring data into the foundation” means the foundation accepts a durable product responsibility: ownership, meaning, quality, access, service levels, lineage, evidence, support, and lifecycle. It does **not** automatically mean copying data into one central store. Physical access can remain direct or federated when that is the lightest valid design.

### Choose One Boundary Outcome

| Outcome | Choose when | Resulting design |
| --- | --- | --- |
| **Keep the interaction at the source** | The need is a transaction, command, operational workflow, or current-state lookup; the source must remain the runtime authority; and no independently managed data product is required. | Consumer uses a governed source API, event interface, or MCP tool. The source owns availability, meaning, change, and operational behavior. |
| **Manage access through the foundation without replication** | Data should be discoverable and governed as a product, but residency, freshness, volume, latency, or source policy favors leaving it in place. The source can meet identity, policy, performance, telemetry, and support obligations. | Foundation exposes a direct, federated, event-based, or selectively projected product port with stable identity, policy, semantics, health, and evidence. |
| **Ingest and persist a foundation-managed product** | Consumers need reusable history, source isolation, cross-source composition, stable semantics, reproducibility, independent scale, governed sharing, contractual SLOs, or durable AI grounding, retrieval, training, or evaluation data. | Data Ingestion creates a managed source-aligned product; domain teams may build aggregate or consumer-aligned products from its published ports. |

### Bring Data Into the Foundation When

- More than one team, purpose, platform, model, or AI agent needs the same dependable data.
- History, point-in-time reproducibility, audit, replay, training, evaluation, or investigation must survive source change.
- Data must be combined across sources or domains under stable business meaning.
- Consumers need isolation from source outages, schema changes, load limits, retention, or operational release cycles.
- Quality, freshness, lineage, access, retention, sharing, and support require an independently owned service promise.

### Do Not Replicate Data When

- The consumer is executing a command, transaction, approval, or other source-owned action.
- Only the latest operational state is needed and the source API or MCP interface is the correct authority.
- The need is temporary, application-internal, or limited to one bounded integration with no independent owner or lifecycle.
- Federation can satisfy policy, latency, availability, semantic, source-capacity, telemetry, and support requirements.
- A copy would add cost, staleness, security exposure, or reconciliation work without creating a reusable product outcome.

An AI-agent use case does not by itself justify replication. Use source APIs or MCP for current state and actions; use a governed data product when the agent needs reusable context, history, semantic grounding, retrieval, training, evaluation, or reproducible evidence.

After selecting the boundary outcome, use the [Data Consumption Service decision guide](../services/data-consumption-service.md#direct-federated-or-replicated-access-decision) to choose the lightest valid access mode: direct, federated, selectively projected, event-based, or replicated.

Accountability remains clear across the boundary:

- **Source teams** own source transactions, meaning, availability, and change obligations.
- **Data Foundation Platform Team** owns source onboarding, ingestion, source-aligned products, and shared foundation capabilities.
- **Domain data teams** own the meaning, fitness, lifecycle, and outcomes of aggregate and consumer-aligned products.

See [Data Domain Design](../architecture/data-domain-design.md) and the [Data Foundation Model](../architecture/data-foundation-model.md) for the detailed ownership model.

## Design Principles

These principles guide every foundation architecture, service, product, and delivery decision.

| Principle | What It Means |
| --- | --- |
| Product outcomes come first | Design for a trusted, reusable consumer outcome, not merely a table, pipeline, workspace, or tool. |
| Ownership is explicit | Every source, service, contract, product, control, and lifecycle decision has one accountable authority. |
| Contracts define promises | Material data boundaries have versioned, testable obligations for meaning, structure, quality, use, change, and support. |
| Governance and security are built in | Identity, policy, classification, lineage, quality, retention, and evidence are applied through reusable services at real enforcement points. |
| Standard patterns precede exceptions | Approved ingestion, creation, consumption, sharing, observability, and operational patterns are the default. |
| One service portal is the front door | People use one coherent entry point for discovery, requests, contracts, access, workflow status, and evidence. |
| Trust is observable | Current quality, freshness, lineage, usage, reliability, ownership, and incident evidence are visible to owners and consumers. |
| Products remain open and usable | Stable interfaces, open formats, portable metadata, and tested export paths reduce unnecessary technology dependence. |
| AI readiness is embedded | Products include the semantics, policy, quality, lineage, telemetry, and purpose context needed for safe model and AI-agent use. |

Principles express direction. Enforceable rules and evidence criteria belong in [Standards](../standards/index.md) and the [Architecture Decision Policy](../decisions/architecture-decision-policy.md).

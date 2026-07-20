# Information Graph

<div class="decision-brief"><div><small>Use when</small><strong>You need a page, relationship, or definition.</strong></div><div><small>Choose</small><strong>Search for a known phrase, explore the architecture information graph, or look up a term.</strong></div><div><small>Owner</small><strong>The reader making or supporting a decision.</strong></div><div><small>Output</small><strong>The shortest path to authoritative guidance.</strong></div></div>

Use the site search when you know the words, the architecture information graph when you need to understand relationships, and the glossary when a term needs a precise definition.

<div class="information-paths" markdown>

| Need | Best route | Result |
| --- | --- | --- |
| Find a known topic | Use the search field in the top navigation. | Matching pages and highlighted terms. |
| Understand how guidance connects | Filter or search the interactive architecture information graph below. | Related services, designs, standards, scenarios, and references. |
| Confirm terminology | Use the glossary on this page or browser find. | The approved meaning used throughout the guide. |

</div>

## Architecture Information Graph

Use **Structure** for the menu hierarchy, **References** for links between pages, **Architecture** for typed design relationships, and **Combined** to inspect them together. Select a node to see its purpose and connected guidance.

<div class="guidance-graph" data-guidance-graph data-src="../../assets/data/guidance-graph.json" data-base="../..">
  <div class="guidance-graph-toolbar">
    <div class="guidance-graph-modes" role="group" aria-label="Graph view">
      <button type="button" data-graph-mode="structure" aria-pressed="true">Structure</button>
      <button type="button" data-graph-mode="references" aria-pressed="false">References</button>
      <button type="button" data-graph-mode="architecture" aria-pressed="false">Architecture</button>
      <button type="button" data-graph-mode="combined" aria-pressed="false">Combined</button>
    </div>
    <label><span>Section</span><select data-graph-group><option value="All">All sections</option></select></label>
    <label class="guidance-graph-search"><span>Find</span><input type="search" data-graph-search placeholder="Page or topic" autocomplete="off"></label>
    <button class="guidance-graph-reset" type="button" data-graph-reset title="Reset graph" aria-label="Reset graph">↺</button>
  </div>
  <div class="guidance-graph-summary" aria-label="Documentation graph metrics">
    <div><strong data-metric-pages>–</strong><span>Pages</span></div>
    <div><strong data-metric-links>–</strong><span>References</span></div>
    <div><strong data-metric-sections>–</strong><span>Top sections</span></div>
    <div><strong data-metric-architecture>–</strong><span>Architecture links</span></div>
  </div>
  <div class="guidance-graph-legend" aria-label="Graph legend">
    <span><i class="legend-structure"></i>Navigation relationship</span>
    <span><i class="legend-reference"></i>Page reference</span>
    <span><i class="legend-architecture"></i>Typed architecture relationship</span>
    <span><b class="legend-group"></b>Section</span>
    <span><b class="legend-page"></b>Page</span>
  </div>
  <div class="guidance-graph-canvas" data-graph-canvas>
    <svg role="img" aria-label="Interactive graph of guidance structure and architecture relationships"></svg>
    <div class="guidance-graph-tooltip" data-graph-tooltip hidden></div>
  </div>
  <div class="guidance-graph-detail" data-graph-detail aria-live="polite"></div>
</div>

## Glossary

| Term | Definition |
| --- | --- |
| Aggregate data product | A federated data product that combines one or more published input products into a reusable business outcome, measure, entity, or analytical structure without exposing its internal pipelines. |
| AI-ready data | Data that has clear meaning, lineage, quality, access policy, freshness, and metadata so it can safely support AI models, agents, retrieval, training, evaluation, or grounding. |
| Agentic by design | A service property in which typed skills, a specialist-agent boundary, applicable data contracts, autonomy limits, deferral points, evidence, and a deterministic fallback are defined from the start. |
| Architecture decision policy | A versioned, machine-readable architecture decision with stable rules, criteria, input, outcome, enforcement points, evidence requirements, owner, and lifecycle. |
| Consumer-aligned data product | A federated data product or governed view optimized for a defined consumption pattern or outcome while retaining stable ownership, data contract, ports, lifecycle, and reuse by approved consumers. |
| Data contract | A versioned, machine-readable, and enforceable promise between accountable parties at a source-ingestion, product-creation, or product-consumption boundary. It defines purpose, binding, meaning, service levels, controls, change, and evidence. |
| Declarative execution envelope | The machine-enforceable scope compiled from a published data contract into policy inputs, allowed skills and parameters, workflow gates, validation, telemetry obligations, expiry, and revocation behavior. |
| Data Product Consumption Contract | The data contract from one exact live product version to one approved consumer or recipient purpose, defining identity, port, channel, scope, controls, SLO, expiry, and revocation. |
| Data Product Creation Contract | The data contract from accepted input-product versions to an aggregate or consumer-aligned product, defining transformation, semantics, quality, ports, SLOs, change, support, and go-live evidence. |
| Data domain | A stable business-aligned accountability and product-portfolio boundary within the shared data foundation; it owns meaning, stewardship, and product outcomes while adopting shared foundation services and controls. |
| Data catalog | The control-plane registry for discoverable products, assets, ports, owners, classifications, lifecycle state, and links to data contracts, semantics, lineage, quality, and policy. |
| Data foundation | The shared capability that makes organizational data trusted, reusable, secure, observable, and ready for analytics, applications, platforms, and AI. |
| Data product go-live | The accountable decision that a specific product and data-contract version has passed mandatory ownership, purpose, quality, security, lineage, observability, documentation, portability, support, and rollback gates and may be consumed. |
| Data product telemetry | Observability signals that describe product quality, freshness, volume, distribution, business-rule changes, usage, cost, and anomalies. |
| Data product | An owned, data-contract-governed, and independently manageable data offering that provides trustworthy data through stable product ports for defined consumer outcomes. It includes the meaning, controls, service levels, support, evidence, and lifecycle needed to use it without understanding internal pipelines or storage. |
| Data product descriptor | The machine-readable product-definition section embedded in the publishing data contract, containing stable identity, purpose, domain, owners, lifecycle, ports, SLOs, support, and authoritative metadata links. |
| Data product health | A product-level view of trust based on freshness, quality, reliability, usage, incidents, data-contract compatibility, and cost. |
| Data product lifecycle | The governed progression of a product through proposal, design, build, go-live, operation, change, deprecation, and retirement with explicit gates and evidence. |
| Data product port | A stable, governed interface through which a product is published or consumed, such as SQL, API, event, file, feature, retrieval, or sharing, independent of its internal pipeline and physical location. |
| Data Service AI Assistant | The user-facing multi-agent coordinator that interprets intent, delegates bounded tasks to service specialist agents, consolidates evidence, and presents approvals and outcomes without becoming a service authority. |
| Data Service Portal | The user entry point for discovering data products, requesting access, managing workflows, viewing trust signals, and managing data contracts. |
| Evidence | A durable, attributable record that proves a decision, control, test, runtime outcome, exception, or recovery result for a named version, authority, and observation time. |
| Foundation service | A reusable platform capability that implements a standard part of the data foundation, such as ingestion, product creation, consumption, sharing, or observability. |
| Knowledge graph | A rebuildable relationship projection across catalog assets, concepts, products, data contracts, lineage, policies, consumers, and use cases for discovery, impact analysis, and governed AI grounding. |
| Multi-agent system | A governed collaboration model in which the Data Service AI Assistant coordinates service-owned specialist agents through typed tasks while identity, data contracts, policy, budgets, approvals, and deterministic services bound execution. |
| OpenTelemetry | The standard telemetry model used by the foundation for traces, metrics, logs, and events across data services and data products. |
| Platform Enablement Service | The horizontal foundation service that provides reusable storage lifecycle, data contract, identity, security, integration, catalog, automation, and control-evidence capabilities to lifecycle services. |
| Raw landing state | The restricted, faithful receipt state inside source-aligned data, used for replay, audit, recovery, and investigation. It is not a separate product layer. |
| Reference solution | A technology-specific implementation profile that maps products and services to the technology-neutral architecture without redefining its data contracts, boundaries, or mandatory outcomes. |
| Semantic context | A versioned package that explains a product's meaning, grain, metrics, relationships, valid uses, prohibited uses, limitations, and authoritative trust references. |
| Shared capability | A reusable control or runtime capability provided once for several foundation services through a stable interface and replaceable provider boundary. |
| Service specialist agent | A service-owned agent that plans and executes bounded work through registered skills and deterministic interfaces under the service's data contracts, policy, autonomy ceiling, and operational controls. |
| Source-aligned data product | A centrally managed, validated product that preserves source meaning and provenance while adding a stable data contract, product descriptor, quality evidence, lineage, support, and governed ports. |
| Source System Ingestion Contract | The data contract from a source system to the Data Ingestion Service, defining delivery, schema, provenance, reconciliation, replay, quarantine, source obligations, and the published source-aligned output. |
| System telemetry | Traces, metrics, logs, and runtime events that describe the availability, latency, errors, saturation, execution, and dependencies of foundation services and platform components. |
| Unified access design | The identity, policy, logical product-port, routing, enforcement, and evidence model above distributed physical data-product runtimes. |
| Trusted dataset | A dataset that has passed defined quality, ownership, documentation, security, and lifecycle controls for approved consumption. |

The architecture information graph is generated from navigation, page references, and the validated architecture registry. It supports discovery and impact analysis; the linked design, service, or standard remains authoritative.

<div class="read-next"><strong>Next:</strong> use <a href="../guidance-model/">How to Use This Guide</a> to choose a reading path, or open a result directly from the architecture information graph.</div>

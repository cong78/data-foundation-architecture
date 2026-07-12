# AI Readiness Assessment

Use this page as a lightweight self-assessment for the data foundation. It is intentionally practical: each checked item should have evidence in the portal, catalog, observability dashboards, governance records, or delivery artifacts.

For deeper architecture guidance, use the [Architecture Blueprint](../implementation/implementation-blueprint.md), [AI-Ready Data Standard](../standards/ai-ready-data-standard.md), and [OpenTelemetry Telemetry Standard](../standards/otel-telemetry-standard.md).

<div class="assessment-panel" data-assessment>
  <div class="assessment-score">
    <strong data-score>0%</strong>
    <span data-status>Early maturity</span>
  </div>
  <div class="maturity-meter"><span data-meter></span></div>

  <div class="assessment-checklist">
    <h2>Foundation</h2>
    <label><input type="checkbox"> The data foundation has clear definition, scope, principles, and service ownership.</label>
    <label><input type="checkbox"> The Data Service Portal is the standard entry point for discovery, requests, workflows, and contracts.</label>
    <label><input type="checkbox"> Data products have owners, stewards, lifecycle states, and support expectations.</label>

    <h2>Contracts and Trust</h2>
    <label><input type="checkbox"> Data contracts define schema, semantics, quality expectations, compatibility, and change rules.</label>
    <label><input type="checkbox"> Contracts have state, owner, approvals, tests, versioning, and consumer subscriptions.</label>
    <label><input type="checkbox"> Contract changes are reviewed, versioned, tested, and communicated to impacted consumers.</label>
    <label><input type="checkbox"> Live data products expose quality, freshness, lineage, classification, and usage guidance.</label>
    <label><input type="checkbox"> Data products cannot go live unless all go-live gates pass.</label>
    <label><input type="checkbox"> Product portfolio reviews identify duplicate, low-usage, unhealthy, ownerless, high-cost, and retirement candidates.</label>

    <h2>AI Consumption</h2>
    <label><input type="checkbox"> AI agents and models use governed identities and approved access patterns.</label>
    <label><input type="checkbox"> Datasets are approved for specific AI purposes such as retrieval, grounding, training, or evaluation.</label>
    <label><input type="checkbox"> Retrieval indexes, feature datasets, and evaluation datasets are linked back to source data products.</label>

    <h2>Observability</h2>
    <label><input type="checkbox"> Foundation services emit OpenTelemetry-compatible traces, metrics, logs, and events.</label>
    <label><input type="checkbox"> Product health dashboards show freshness, quality, reliability, usage, incidents, and cost.</label>
    <label><input type="checkbox"> AI usage can be traced from model, agent, or application back to data product and source lineage.</label>
  </div>
</div>

## How to Interpret the Score

| Score | Meaning | Recommended Action |
| --- | --- | --- |
| 0-39% | Early maturity | Focus on foundation definition, ownership, portal workflows, and basic product controls. |
| 40-64% | Emerging foundation | Standardize contracts, product go-live, quality, and access policy enforcement. |
| 65-84% | Strong foundation, targeted gaps | Deepen AI consumption, lineage, observability, and evidence capture. |
| 85-100% | AI-ready foundation | Use the foundation for governed AI scale and continuous improvement. |

!!! tip "Evidence-based use"
    Treat this as a working review tool. For each checked item, link to the real evidence: portal workflow, contract record, catalog entry, quality report, telemetry dashboard, or governance approval.

# Data Foundation Maturity Assessment

Use this assessment to evaluate whether the data foundation is defined, implemented, adopted, and operated as an enterprise capability. Check an item only when objective evidence exists in the Data Service Portal, contract registry, catalog, policy engine, observability platform, governance records, or delivery artifacts.

Assess the foundation at a defined scope, such as one domain, business unit, platform, or enterprise. Record the scope, assessment date, accountable reviewer, evidence links, exceptions, and next review date outside this page.

For implementation guidance, use the [Architecture Blueprint](../implementation/implementation-blueprint.md), [Data Product Management Standard](../standards/data-product-management-standard.md), [Open Interoperability Standard](../standards/open-interoperability-standard.md), and [OpenTelemetry Standard](../standards/otel-telemetry-standard.md).

<div class="assessment-panel" data-assessment>
  <div class="assessment-score">
    <strong data-score>0%</strong>
    <span data-status>Foundational</span>
  </div>
  <div class="maturity-meter"><span data-meter></span></div>

  <div class="assessment-checklist">
    <h2>Direction and Ownership</h2>
    <label><input type="checkbox"> The foundation has an approved definition, scope, principles, target architecture, and decision ownership.</label>
    <label><input type="checkbox"> Each foundation service has an accountable owner, service contract, support model, service levels, and lifecycle.</label>
    <label><input type="checkbox"> Domains have clear product ownership, stewardship, funding, and escalation responsibilities.</label>
    <label><input type="checkbox"> Architecture decisions, exceptions, risks, dependencies, and maturity improvements are reviewed with evidence.</label>

    <h2>Foundation Services</h2>
    <label><input type="checkbox"> The Data Service Portal provides one entry point for discovery, requests, contracts, access, workflows, and evidence.</label>
    <label><input type="checkbox"> Ingestion supports governed file, connector, API, CDC, and streaming patterns with repeatable onboarding.</label>
    <label><input type="checkbox"> Product creation provides reusable workload patterns, automated controls, and promotion across environments.</label>
    <label><input type="checkbox"> Consumption and sharing provide governed, observable delivery for people, systems, platforms, partners, agents, and models.</label>

    <h2>Data Products and Contracts</h2>
    <label><input type="checkbox"> Products have owners, purpose, consumers, lifecycle state, support expectations, costs, and measurable value.</label>
    <label><input type="checkbox"> Versioned contracts define schema, semantics, quality, service levels, classification, compatibility, and change rules.</label>
    <label><input type="checkbox"> Product go-live requires passing ownership, contract, quality, security, lineage, observability, documentation, and portability gates.</label>
    <label><input type="checkbox"> Portfolio reviews govern reuse, duplication, health, adoption, cost, deprecation, and retirement.</label>

    <h2>Access, Security and Governance</h2>
    <label><input type="checkbox"> Named users and workloads use governed identities with least-privilege, purpose-aware, time-bound access.</label>
    <label><input type="checkbox"> The unified data access layer enforces consistent discovery, policy, audit, and revocation across physical product stores.</label>
    <label><input type="checkbox"> Classification, privacy, retention, residency, legal, and external-sharing obligations are policy-enforced and evidenced.</label>
    <label><input type="checkbox"> Access decisions, entitlements, exceptions, incidents, and revocations are traceable to accountable owners and contracts.</label>

    <h2>Observability and Operations</h2>
    <label><input type="checkbox"> Foundation services emit OpenTelemetry-compatible traces, metrics, logs, and events with shared correlation identifiers.</label>
    <label><input type="checkbox"> Product telemetry covers freshness, quality, lineage, volume, usage, reliability, incidents, and cost against contract targets.</label>
    <label><input type="checkbox"> Service and product health are connected from source through ingestion, product creation, access, consumption, and sharing.</label>
    <label><input type="checkbox"> Teams rehearse incident response, continuity, recovery, expiry, revocation, and product retirement with retained evidence.</label>

    <h2>Interoperability and AI Enablement</h2>
    <label><input type="checkbox"> Contracts, metadata, lineage, telemetry, identity, policy, and product interfaces use open or portable profiles with conformance tests.</label>
    <label><input type="checkbox"> Semantic and context assets connect business meaning, metrics, ontology or knowledge graph references, and source lineage.</label>
    <label><input type="checkbox"> Agents and models use governed identities and products approved for declared retrieval, grounding, training, or evaluation purposes.</label>
    <label><input type="checkbox"> AI usage is traceable from application, agent, model, prompt or retrieval action to product, contract, policy, and source evidence.</label>
  </div>
</div>

## Maturity Levels

| Score | Level | Interpretation | Priority |
| --- | --- | --- | --- |
| 0-39% | Foundational | Direction or core capabilities are incomplete, inconsistent, or dependent on manual coordination. | Establish ownership, service boundaries, portal workflows, contracts, access controls, and minimum evidence. |
| 40-64% | Emerging | Repeatable patterns exist, but adoption and enforcement vary by domain or technology. | Standardize paved paths, automate gates, close service gaps, and measure adoption. |
| 65-84% | Established | The foundation is broadly governed and reusable, with targeted gaps in scale, interoperability, or operations. | Improve cross-platform conformance, product outcomes, end-to-end telemetry, and lifecycle automation. |
| 85-100% | Optimized | Capabilities are evidence-driven, interoperable, continuously improved, and ready for governed AI use at scale. | Optimize value, cost, resilience, portability, and policy automation while preventing local divergence. |

## Use the Result

1. Capture evidence and gaps for every item, not only the resulting percentage.
2. Score each dimension separately so strength in one area cannot hide a critical weakness in another.
3. Select a small number of improvements with owners, target evidence, dependencies, and review dates.
4. Reassess after each delivery increment and compare changes within the same scope.

!!! tip "Evidence over opinion"
    The score is a navigation aid, not certification. A checked item needs a durable evidence link; an unverified claim remains unchecked.

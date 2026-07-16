# Data Foundation Maturity Assessment

<div class="decision-brief"><div><small>Use when</small><strong>Baselining or reviewing a foundation or domain.</strong></div><div><small>Decision</small><strong>Which evidence-backed gaps require improvement?</strong></div><div><small>Owner</small><strong>Accountable scope owner and assessor.</strong></div><div><small>Output</small><strong>Scores, evidence gaps, owners, and review date.</strong></div></div>

Use this assessment to evaluate whether the data foundation is defined, implemented, adopted, and operated as a shared capability. Check an item only when objective evidence exists in the Data Service Portal, contract registry, catalog, policy engine, observability platform, governance records, or delivery artifacts.

Assess the foundation at a defined scope, such as one domain, business unit, platform, or enterprise. Record the scope, assessment date, accountable reviewer, evidence links, exceptions, and next review date outside this page.

For implementation guidance, use [Data Domain Design](../architecture/data-domain-design.md), the [Implementation Blueprint](../implementation/implementation-blueprint.md), [Data Product Management Standard](../standards/data-product-management-standard.md), [Open Interoperability Standard](../standards/open-interoperability-standard.md), and [OpenTelemetry Standard](../standards/otel-telemetry-standard.md).

## Assess a Data Domain

Create one assessment record per domain and assessment date. Use the stable domain id as the scope, complete the [Data Domain Onboarding Record](../reference-solutions/data-domain-onboarding-template.md), and interpret each dimension as domain adoption of the shared foundation:

| Dimension | Domain-level question |
| --- | --- |
| Direction and ownership | Is the boundary clear, accountability accepted, and portfolio improvement funded? |
| Foundation services | Does the domain consume centrally managed source-aligned inputs and use approved creation, access, consumption, sharing, platform enablement, observability, and operations profiles without duplicating controls, ingestion, or support paths? |
| Data products and contracts | Is the domain portfolio owned, contracted, reusable, governed through go-live and actively managed? |
| Access, security and governance | Are domain identities, policies, obligations, entitlements, exceptions and revocations enforceable and evidenced? |
| Observability and operations | Can the domain operate services and products end to end against SLOs, incidents, cost and lifecycle expectations? |
| Interoperability and AI enablement | Are domain artifacts portable and semantic, and are AI uses purpose-approved and traceable? |

Check a foundation-owned capability only when the domain has adopted it and can provide domain-specific evidence. Score all six dimensions separately before calculating the overall percentage.

!!! warning "Maturity is not an admission shortcut"
    Domain onboarding also has hard gates for identity, boundary, accountability, governance, access and operations. A high average cannot compensate for a failed hard gate. A low baseline can be accepted with a funded improvement plan when all hard gates pass.

<div class="assessment-panel" data-assessment>
  <div class="assessment-score">
    <strong data-score>0%</strong>
    <span data-status>Foundational</span>
  </div>
  <div class="maturity-meter"><span data-meter></span></div>

  <div class="assessment-checklist">
    <h2>Direction and Ownership</h2>
    <label><input type="checkbox"> The foundation has an approved definition, scope, principles, architecture blueprint, and decision ownership.</label>
    <label><input type="checkbox"> Each foundation service has an accountable owner, service contract, support model, service levels, and lifecycle.</label>
    <label><input type="checkbox"> Domains have clear product ownership, stewardship, funding, and escalation responsibilities.</label>
    <label><input type="checkbox"> Architecture decisions, exceptions, risks, dependencies, and maturity improvements are reviewed with evidence.</label>

    <h2>Foundation Services</h2>
    <label><input type="checkbox"> The Data Service Portal provides one entry point for discovery, requests, contracts, access, workflows, and evidence.</label>
    <label><input type="checkbox"> The foundation platform team centrally operates source onboarding, ingestion, and raw and validated source-aligned products across approved file, connector, API, CDC, and streaming patterns.</label>
    <label><input type="checkbox"> Shared product-creation capabilities provide reusable workload patterns and controls while domain teams own aggregate and consumer-aligned products.</label>
    <label><input type="checkbox"> Consumption and sharing provide governed, observable delivery for people, systems, platforms, partners, agents, and models.</label>
    <label><input type="checkbox"> Platform Enablement provides reusable storage lifecycle, contract, identity, security, integration, catalog, and automation capabilities with conformance and deprovisioning evidence.</label>
    <label><input type="checkbox"> The Data Foundation Operations Service provides one governed support, incident, problem, change, release, reliability, continuity, communication, and improvement model across services.</label>

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
    <label><input type="checkbox"> Service records, support tiers, SLOs, escalation, runbooks, dependencies, changes, releases, problems, improvement actions, and recovery evidence are current and linked.</label>

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

## Compare Data Domains

The portal may show a cross-domain maturity view, but it should support investment and risk decisions rather than create an unqualified ranking.

| Comparison rule | Required treatment |
| --- | --- |
| Common model | Use the same assessment version, scoring thresholds and evidence requirements. |
| Comparable scope | Record domain boundary, lifecycle, portfolio size, criticality, regulatory context and assessment date. |
| Dimension visibility | Show all six dimension scores and the lowest dimension beside the overall score. |
| Gate visibility | Show failed or conditional admission gates separately; never average them into maturity. |
| Evidence confidence | Mark whether evidence is automated, sampled, manually attested, stale or missing. |
| Trend over rank | Prioritize improvement against each domain's baseline, target and risk before comparing absolute position. |

Use the completed onboarding records as the source for a domain maturity heatmap and improvement portfolio. Keep drill-through links to evidence, conditions, exceptions and accountable owners.

!!! tip "Evidence over opinion"
    The score is a navigation aid, not certification. A checked item needs a durable evidence link; an unverified claim remains unchecked.

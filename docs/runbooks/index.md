# Runbooks

<div class="decision-brief"><div><small>Use when</small><strong>Turning guidance into an owned, testable action.</strong></div><div><small>Decision</small><strong>Which execution path should be followed next?</strong></div><div><small>Owner</small><strong>Accountable work owner with capability and evidence owners.</strong></div><div><small>Output</small><strong>Sequenced actions, reusable artifacts, and acceptance evidence.</strong></div></div>

Runbooks are the execution layer of this guide. They connect architecture intent to repeatable actions, implementation guidance, assessments, reference solutions, and measurable evidence.

## How Runbooks Fit

<div class="standards-map" role="img" aria-label="Runbooks mapped from planning through evidence to repeatable implementation">
  <div class="standards-map-head" aria-hidden="true">
    <span>Execution need</span><i></i><span>Runbook path</span><i></i><span>Outcome</span>
  </div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Sequence</small><strong>Priorities · Dependencies · Increments</strong><p>Build thin vertical slices instead of a large platform program.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../runway/"><strong>Runway</strong></a><a href="../implementation/implementation-blueprint/"><strong>Implementation Blueprint</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Adoption path</strong><p>Ordered capabilities, acceptance tests, dependencies, and measurable outcomes.</p></div>
  </section>
  <section class="standards-map-lane lane-build">
    <div class="standards-map-cell"><small>Prove</small><strong>Readiness · Conformance · Risk</strong><p>Make architecture claims testable before scaling adoption.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../assessments/architecture-dashboard/"><strong>Architecture Dashboard</strong></a><a href="../assessments/industry-alignment/"><strong>Industry Alignment</strong></a><a href="../assessments/data-foundation-maturity-assessment/"><strong>Foundation Maturity</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Decision evidence</strong><p>Visible maturity, gaps, conformance results, risks, and remediation priorities.</p></div>
  </section>
  <section class="standards-map-lane lane-intelligence">
    <div class="standards-map-cell"><small>Apply and reuse</small><strong>Solutions · Records · Evidence</strong><p>Adapt a reference profile and retain the decisions and proof needed for adoption.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../playbooks/"><strong>Action Playbooks</strong></a><a href="../reference-solutions/"><strong>Reference Solutions</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Repeatable execution</strong><p>Consistent contracts, workloads, controls, telemetry, and go-live evidence.</p></div>
  </section>
</div>

## Runbook Rules

1. Deliver one real source-to-consumer slice before expanding platform breadth.
2. Express enforceable rules with the [Architecture Decision Policy](../decisions/architecture-decision-policy.md) and automate them in templates, CI, workflows, and runtime services.
3. Treat conformance reports, telemetry, approvals, and release receipts as architecture evidence.
4. Reuse patterns when they fit; record an expiring exception when they do not.
5. Measure lead time, reuse, reliability, consumer value, and operating cost.

## Reference Solutions

[Reference Solutions](../reference-solutions/index.md) bring selected technology profiles and reusable records into the runbook path. Start with the technology-neutral architecture and service definition, adapt only the relevant profile, complete its reference record, and retain the resulting decisions, tests, approvals, and operational evidence.

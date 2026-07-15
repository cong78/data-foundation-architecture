# Delivery Overview

<div class="decision-brief"><div><small>Use when</small><strong>Turning guidance into a funded, testable increment.</strong></div><div><small>Decision</small><strong>What outcome should be delivered or proven next?</strong></div><div><small>Owner</small><strong>Delivery lead with capability and evidence owners.</strong></div><div><small>Output</small><strong>Sequenced work, reusable artifacts, and acceptance evidence.</strong></div></div>

Delivery turns architecture guidance into small, testable increments with reusable artifacts and measurable evidence.

## How Delivery Fits

<div class="standards-map" role="img" aria-label="Delivery guidance mapped from sequencing through evidence to reusable implementation">
  <div class="standards-map-head" aria-hidden="true">
    <span>Delivery need</span><i></i><span>Guidance</span><i></i><span>Outcome</span>
  </div>
  <section class="standards-map-lane lane-govern">
    <div class="standards-map-cell"><small>Sequence</small><strong>Priorities · Dependencies · Increments</strong><p>Build thin vertical slices instead of a large platform program.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../runway/"><strong>Runway</strong></a><a href="../implementation/implementation-blueprint/"><strong>Architecture Blueprint</strong></a></div>
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
    <div class="standards-map-cell"><small>Apply and reuse</small><strong>Templates · Examples · Receipts</strong><p>Start from approved artifacts and learn from completed slices.</p></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell standards-map-focus"><a href="../playbooks/"><strong>Action Playbooks</strong></a><a href="../delivery-templates/data-product-template/"><strong>Templates</strong></a><a href="../examples/customer-profile-example/"><strong>Worked Examples</strong></a></div>
    <span class="standards-map-arrow" aria-hidden="true"></span>
    <div class="standards-map-cell"><strong>Repeatable delivery</strong><p>Consistent contracts, workloads, controls, telemetry, and go-live evidence.</p></div>
  </section>
</div>

## Delivery Rules

1. Deliver one real source-to-consumer slice before expanding platform breadth.
2. Express enforceable rules with the [Architecture Policy Language](../standards/architecture-policy-language.md) and automate them in templates, CI, workflows, and runtime services.
3. Treat conformance reports, telemetry, approvals, and release receipts as architecture evidence.
4. Reuse patterns when they fit; record an expiring exception when they do not.
5. Measure lead time, reuse, reliability, consumer value, and operating cost.

Start policy-as-code work from the [Architecture Policy Template](../delivery-templates/architecture-policy-template.md).

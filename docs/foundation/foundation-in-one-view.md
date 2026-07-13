# Foundation in One View

<div class="decision-brief">
  <div><small>Use when</small><strong>Orienting a team or locating the next action.</strong></div>
  <div><small>Primary decision</small><strong>Which journey stage owns the current outcome?</strong></div>
  <div><small>Accountable owner</small><strong>Foundation, domain, product, consumer, or service owner.</strong></div>
  <div><small>Output</small><strong>One action path with required evidence and next gate.</strong></div>
</div>

The foundation has one primary story: **Frame → Establish → Deliver → Use → Operate**. Every architecture view, service, standard, template, and reference solution supports one or more stages of this journey.

## The Five-Stage Journey

<div class="standards-map reference-map" role="img" aria-label="Five-stage data foundation journey">
  <div class="standards-map-head" aria-hidden="true"><span>Intent</span><i></i><span>Primary work</span><i></i><span>Evidence</span></div>
  <section class="standards-map-lane lane-govern"><div class="standards-map-cell"><small>1 · Frame</small><strong>Agree the boundary</strong><p>Purpose, scope, principles, domains, ownership, and non-goals.</p></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell standards-map-focus"><strong>Definition and Scope</strong><strong>Principles</strong><strong>Domain Design</strong></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell"><strong>Decision basis</strong><p>Approved boundary, accountable owners, and architecture principles.</p></div></section>
  <section class="standards-map-lane lane-build"><div class="standards-map-cell"><small>2 · Establish</small><strong>Build the shared path</strong><p>Target structure, services, standards, controls, portal, and operating ownership.</p></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell standards-map-focus"><strong>Target and Reference Architecture</strong><strong>Service Portfolio</strong><strong>Standards</strong></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell"><strong>Foundation ready</strong><p>Reusable services with owners, interfaces, controls, SLOs, and evidence.</p></div></section>
  <section class="standards-map-lane lane-intelligence"><div class="standards-map-cell"><small>3 · Deliver</small><strong>Create trusted products</strong><p>Onboard sources, design contracts, build products, and pass product go-live.</p></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell standards-map-focus"><strong>Ingestion</strong><strong>Product Creation</strong><strong>Contract and Lifecycle</strong></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell"><strong>Live product</strong><p>Owned, contracted, tested, observable, supported, and requestable.</p></div></section>
  <section class="standards-map-lane lane-access"><div class="standards-map-cell"><small>4 · Use</small><strong>Enable governed outcomes</strong><p>Discover, request, consume, share, and enable approved AI use.</p></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell standards-map-focus"><strong>Unified Access</strong><strong>Consumption and Sharing</strong><strong>AI and Semantic Context</strong></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell"><strong>Purpose-bound use</strong><p>Identity, policy, contract, context, entitlement, and usage evidence.</p></div></section>
  <section class="standards-map-lane lane-govern"><div class="standards-map-cell"><small>5 · Operate</small><strong>Keep trust current</strong><p>Observe, support, change, recover, learn, improve, and retire safely.</p></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell standards-map-focus"><strong>Observability</strong><strong>Foundation Operations</strong><strong>Governance and Maturity</strong></div><span class="standards-map-arrow" aria-hidden="true"></span><div class="standards-map-cell"><strong>Measured improvement</strong><p>SLOs, incidents, changes, health, value, cost, and improvement decisions.</p></div></section>
</div>

## Action and Evidence Map

| Stage | Decision and accountable owner | Exit evidence |
| --- | --- | --- |
| **Frame** | Foundation sponsor approves scope; domain owners accept boundaries and accountability. | Scope, principles, domain records, decision rights, risks, and non-goals. |
| **Establish** | Service owners establish shared capabilities; governance owners make controls enforceable. | Service contracts, standards, APIs, policies, SLOs, support, portal journeys, and conformance evidence. |
| **Deliver** | Source owners accept delivery obligations; product owners accept the output promise. | Source contract, product contract, lineage, tests, workload, go-live record, ports, and support route. |
| **Use** | Consumer or use-case owner declares purpose; policy owner authorizes bounded access. | Consume or sharing agreement, entitlement, obligations, interface, context, and usage trace. |
| **Operate** | Service and product owners accept operational health, change, recovery, and improvement decisions. | Health, SLOs, incidents, changes, recovery validation, reviews, migrations, and retirement evidence. |

## Choose an Action

| I need to... | Use this playbook | Completion outcome |
| --- | --- | --- |
| Establish a domain boundary | [Onboard a Data Domain](../playbooks/onboard-data-domain.md) | Registered, accountable, enabled domain. |
| Bring in a source | [Onboard a Source](../playbooks/onboard-source.md) | Validated source-aligned product and handoff. |
| Build or change a product | [Create or Change a Data Product](../playbooks/create-change-data-product.md) | Tested candidate with complete evidence. |
| Decide whether a product may launch | [Approve Product Go-Live](../playbooks/approve-product-go-live.md) | Explicit approve, reject, or expiring exception decision. |
| Use a product | [Consume a Data Product](../playbooks/consume-data-product.md) | Purpose-bound access through a governed port. |
| Exchange data externally | [Share a Data Product](../playbooks/share-data-product.md) | Minimized, expiring, observable, revocable exchange. |
| Support or improve a live capability | [Operate a Service or Product](../playbooks/operate-service-product.md) | Restored or improved service with retained evidence. |

## How the Supporting Models Fit

| Model | What it answers | Rule |
| --- | --- | --- |
| Five journey stages | What outcome and action comes next? | **Primary navigation model.** |
| Five architecture layers | Where does a responsibility sit in the solution stack? | Use for placement, not sequence. |
| Six target planes | Which cross-cutting concern governs the design? | Use for architecture completeness. |
| Seven foundation services | Which reusable capability performs the work? | Use for service ownership and interfaces. |
| Three product patterns | What promise does the product make? | Source-aligned, aggregate, or consumer-aligned. |
| Four runway phases | How does the enterprise mature the capability? | Use for adoption planning, not an individual product lifecycle. |

## Where Authority Lives

| Question | Authoritative guidance |
| --- | --- |
| What is in scope and who owns the boundary? | [Definition and Scope](definition-and-scope.md) |
| What is the architecture structure? | [Data Foundation Model](../architecture/data-foundation-model.md) |
| How does a product move through states? | [Data Product Lifecycle Design](../architecture/data-product-lifecycle-design.md) |
| Which contract applies and where is it enforced? | [Data Contract Design](../architecture/data-contract-design.md) |
| What is mandatory? | [Standards](../standards/index.md) |
| What capability does the platform provide? | [Services](../services/index.md) |
| What must a team do now? | [Playbooks](../playbooks/index.md) |
| How is a selected technology applied? | Reference Solutions under Architecture. |
| How should adoption be sequenced? | [Runway](../runway.md) |

<div class="read-next"><strong>Next:</strong> choose the playbook that matches the intended outcome; use architecture and standards as decision inputs rather than reading every page in sequence.</div>

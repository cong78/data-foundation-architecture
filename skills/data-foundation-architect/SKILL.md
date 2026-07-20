---
name: data-foundation-architect
description: Assess, design, review, and generate governed data foundation architecture using this repository. Use for data domain onboarding or maturity, data products and contracts, foundation services, Data Service Portal marketplace journeys, unified access, observability, operational runbooks, semantic context, AI enablement, technology selection, architecture conformance, and delivery artifacts.
---

# Data Foundation Architect

Use the repository as the authority and this skill as the execution workflow. Load only the guidance required for the task; do not copy the complete documentation into context.

Read `manifest.json` before execution. Treat its capability, side-effect, authorization, data-policy, approval, reliability, and observability declarations as the portable runtime contract. The host agent runtime must enforce them outside prompt text.

## Locate the Guidance

1. Walk upward from the working directory until both `mkdocs.yml` and `docs/` exist.
2. Treat that directory as the repository root.
3. Read `references/guidance-map.md` and load only the listed pages needed for the selected workflow.
4. If the repository root cannot be found, state that the authoritative guidance is unavailable. Use bundled references for process only and label architecture conclusions as provisional.

Do not treat generated `site/` HTML as the source. Prefer Markdown under `docs/`.

## Select a Workflow

| User intent | Workflow | Primary result |
| --- | --- | --- |
| Assess, score, compare, onboard, identify gaps | Assess | Evidence-based maturity and admission decision |
| Design, architect, map, integrate, propose | Design | Layered architecture and decisions |
| Review, validate, challenge, check completeness | Review | Findings ordered by severity with remediation |
| Create, generate, fill, scaffold | Generate | Completed repository template or new governed artifact |

When intent spans workflows, run them in this order: **Assess → Design → Generate → Review**. Skip any stage that adds no value.

## Apply Core Integrity Rules

- Separate data foundation platform responsibilities, domain accountability, data product ownership, and runtime implementation.
- Separate principles, rules, and criteria. Use the Architecture Decision Policy for new or changed normative guidance, with an authoritative policy document, named decision, tests, enforcement points, and evidence.
- Use **Frame → Establish → Deliver → Use → Operate** as the primary journey; treat layers, planes, services, product patterns, and runway phases as supporting views.
- Use the nine foundation services as reusable capability boundaries. Keep the Data Product Marketplace inside the Data Service Portal rather than creating a separate catalog or platform.
- Keep source onboarding, ingestion, and raw and validated source-aligned products under central foundation platform accountability; keep domain, aggregate, and consumer-aligned product ownership federated to domain data teams.
- Treat a data product as the unit of trust and reuse; do not equate a table or pipeline with a product.
- Require explicit contracts, semantic context, policy, lineage, telemetry, lifecycle, and accountable ownership.
- Use only three contract types: Source System Ingestion Contract, Data Product Creation Contract, and Data Product Consumption Contract. Treat sharing and AI use as consumption profiles.
- Keep service authorization separate from data entitlement and evaluate named-user, workload, delegated, and external-recipient identities.
- Keep physical storage behind governed product ports and unified access.
- Apply Unity Catalog as the data catalog standard and Delta Lake as the default durable tabular storage format; require an approved exception and portable exit for alternatives.
- Distinguish declared contract targets from measured health and timestamp evidence.
- Treat Unity Catalog and Delta Lake as approved platform defaults; treat other vendor products as selected implementation profiles and preserve open interfaces, conformance, and exit paths for every binding.
- Preserve domain hard gates and product go-live gates. Never average a failed mandatory gate into a maturity score.
- Trace production designs through architecture decision, service definition, action playbook, operational runbook, evidence, and runway phase.
- Do not invent evidence, approvals, owners, measurements, or conformance results. Mark unknowns explicitly.

Read `references/evidence-rules.md` before scoring, certifying, or making a go-live or onboarding recommendation.

## Assess

1. Define the assessment object: data foundation, data domain, service, product, or implementation profile.
2. Record stable id, boundary, lifecycle, evidence window, accountable reviewer, and assessment version.
3. For domain onboarding, read:
   - `docs/architecture/data-domain-design.md`
   - `docs/assessments/data-foundation-maturity-assessment.md`
   - `docs/reference-solutions/data-domain-onboarding-template.md`
4. Evaluate admission gates independently from the six maturity dimensions.
5. Capture an evidence link or an explicit gap for every claim.
6. Use `scripts/assess_maturity.py` for deterministic scoring when a JSON assessment is available.
7. Report dimension scores, lowest dimension, evidence coverage, failed or conditional gates, risks, and a prioritized improvement plan.

Run:

```bash
python skills/data-foundation-architect/scripts/assess_maturity.py assessment.json --format markdown
```

Use `assets/domain-assessment.example.json` as the input shape. Do not interpret the overall percentage as certification.

## Design

1. State the problem, scope, actors, consumers, constraints, assumptions, and non-goals.
2. Classify the work as one primary **service-specific**, **shared capability**, or **integration** design using `docs/architecture/design-map.md`.
3. Identify the owning service, supporting designs, and affected target planes before adding a component.
4. Define logical responsibilities before mapping technologies; label vendor mappings as reference profiles.
5. Show the main value flow and keep cross-cutting identity, policy, contract, lineage, semantic, and telemetry controls explicit.
6. Define product ports, interface specifications, control authorities, enforcement points, evidence, failure behavior, and lifecycle.
7. For cross-service scope, name the outcome owner, handoff owners, correlation identifiers, compensation, reconciliation, and end-to-end test.
8. Record consequential alternatives and decisions.
9. Map the design to standards, owning services, target user experiences, action playbooks, operational runbooks, evidence, runway phase, and applicable done criteria.

Prefer one readable layered diagram plus focused flows. Avoid one diagram containing every control and interaction.

## Review

1. Determine the claimed scope and intended outcomes.
2. Check boundaries, service ownership, contracts, product lifecycle, access, observability, interoperability, operability, runbook coverage, and AI usage as applicable.
3. Distinguish missing design from missing evidence and implementation risk.
4. Lead with findings ordered by severity.
5. For each finding, provide affected area, consequence, supporting guidance, and a concrete correction.
6. End with assumptions, residual risks, and the smallest useful next actions.

Use the review output specification in `references/output-specifications.md`. Do not give a maturity label when the evidence set is materially incomplete.

## Generate

Start from the repository template that owns the requested artifact:

| Artifact | Template |
| --- | --- |
| Architecture decision policy | `docs/reference-solutions/architecture-policy-template.md` |
| Data domain onboarding | `docs/reference-solutions/data-domain-onboarding-template.md` |
| Data product | `docs/reference-solutions/data-product-template.md` |
| Data product workload | `docs/reference-solutions/data-product-workload-template.md` |
| Source onboarding | `docs/reference-solutions/source-onboarding-template.md` |
| Technology selection | `docs/reference-solutions/technology-selection-template.md` |
| Interoperability conformance | `docs/reference-solutions/interoperability-conformance-template.md` |
| Agent or skill | `docs/reference-solutions/agent-skill-template.md` |
| Service runbook | `docs/reference-solutions/service-runbook-template.md` |

Preserve template sections unless they are explicitly out of scope. Replace blank fields with supplied facts, `TBD`, `Not applicable` plus rationale, or an evidence request. Never silently remove a mandatory gate.

## Return Useful Results

Follow `references/output-specifications.md`. Keep outputs concise but decision-ready:

- Scope and outcome.
- Architecture or assessment result.
- Decisions and mandatory gates.
- Evidence and gaps.
- Risks and trade-offs.
- Prioritized next actions with owners when known.
- Architecture-to-service-to-runbook traceability for production scope.
- Exact repository guidance used.

When editing this repository, run all manifest tests, the strict MkDocs build, and the internal link checker before completion.

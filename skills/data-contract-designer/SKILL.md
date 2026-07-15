---
name: data-contract-designer
description: Design, review, compare, and plan changes to enforceable data contracts using the repository's three-contract model. Use for Source System Ingestion Contracts, Data Product Creation Contracts, Data Product Consumption Contracts, contract completeness reviews, compatibility and breaking-change analysis, contract lifecycle transitions, enforcement mapping, evidence gaps, or migration planning. Do not use to invent approvals, grant access, publish contracts, or create additional contract types.
---

# Data Contract Designer

Use the repository guidance as authority. Produce a contract draft or decision-ready review; never claim approval, publication, runtime conformance, or evidence that was not supplied.

## Locate the Guidance

1. Walk upward from the working directory until both `mkdocs.yml` and `docs/` exist.
2. Treat that directory as the repository root.
3. Read `references/guidance-map.md` and load only the pages required for the selected workflow.
4. If the repository root is unavailable, use this package for process only and label the result provisional.

Do not treat generated `site/` HTML as authoritative.

## Select the Contract

Use exactly one contract type for the active boundary:

| Boundary | Contract type | Core promise |
| --- | --- | --- |
| Source system to ingestion | `source_system_ingestion` | Delivery, receipt, validation, source-aligned output with embedded product descriptor, replay, reconciliation, and source change. |
| Accepted inputs to one product | `data_product_creation` | Embedded product descriptor, transformation, meaning, quality, SLOs, policy, lineage, ports, go-live, and change. |
| One live product to one consumer purpose | `data_product_consumption` | Identity, purpose, product version, port, scope, obligations, expiry, revocation, and usage. |

Treat BI, application, platform, external sharing, and AI use as consumption profiles. Do not create sharing, AI, schema, catalog, quality, or service-level contract types.

If the boundary is ambiguous, state the ambiguity and ask only for facts that change the contract type or control outcome.

## Select a Workflow

| User intent | Workflow | Primary result |
| --- | --- | --- |
| Design, draft, create, define | Design | Structured draft plus tests, approvals, enforcement, and evidence gaps |
| Review, validate, check completeness | Review | Severity-ordered findings and required corrections |
| Compare, compatible, breaking change, version | Compatibility | Patch, minor, or major recommendation with affected terms |
| Change, migrate, deprecate, retire | Change impact | Dependency impact, migration, notice, coexistence, and lifecycle plan |

When intent spans workflows, run **Review → Compatibility → Change impact → Design revision**. Skip stages that add no decision value.

## Establish Facts Before Drafting

Capture supplied facts and mark missing facts explicitly:

- Contract boundary, stable ids, environment, effective period, and exact upstream or product versions.
- For a publishing contract, product descriptor facts: product id, name, domain, purpose, owners, lifecycle, ports, SLOs, support, and authoritative links.
- Accountable provider, owner, steward, technical owner, consumer or recipient, support, and escalation.
- Outcome, valid use, prohibited use, non-goals, and measurable value.
- Schema, keys, grain, time meaning, semantics, classification, limitations, and examples.
- Quality, freshness, availability, latency, volume, lineage, recovery, and incident expectations.
- Identity, purpose, policy, minimization, masking, retention, residency, expiry, revocation, and output controls.
- Compatibility, notice, impact, migration, deprecation, retirement, exceptions, and review date.
- Enforcement points, tests, severity, failure behavior, telemetry, approvals, and evidence references.

Do not turn unknown values into plausible defaults. Use `TBD` with an accountable owner and required decision where possible.

## Design

1. Confirm the boundary and contract type.
2. Load the common and type-specific requirements from the Data Contract Standard.
3. For ingestion or creation, embed the ODPS-compatible product descriptor in the contract; never create a separately versioned descriptor.
4. Separate the durable promise from vendor runtime bindings.
5. Draft business-readable terms and machine-testable rules from the same facts.
6. Define enforcement before publication, at runtime, and during operation.
7. Map each promise to a test, telemetry signal, failure outcome, and evidence authority.
8. Identify mandatory approvers without claiming their approval.
9. Return the contract draft using `references/output-contracts.md`.

When a canonical ODCS artifact is requested, validate against the pinned schema before claiming conformance. Preserve enterprise extensions under an explicit namespace. Do not invent ODCS fields from memory.

## Review

Review in this order:

1. **Correct type and boundary:** one of the three types; exact source, products, ports, parties, purpose, and versions.
2. **Completeness:** all common and type-specific terms are present or explicitly unresolved, including an embedded descriptor for publishing contracts.
3. **Accountability:** owners, approvers, support, escalation, obligations, and decision rights are named.
4. **Enforceability:** terms can generate or drive tests, policy inputs, interfaces, telemetry, and failure outcomes.
5. **Operational truth:** declared targets are separate from measured health and time-stamped evidence.
6. **Lifecycle:** compatibility, notice, migration, expiry, revocation, deprecation, and retirement are executable.
7. **Portability:** the canonical promise is not trapped in Unity Catalog, Delta, an API gateway, or another runtime.

Treat a separately versioned product descriptor as a major design finding. The catalog or product registry may project descriptor fields for discovery, but it must not own a competing product definition.

Order findings by severity:

- **Blocker:** wrong contract type, missing accountable party, unsafe or unauthorized use, no exact binding, or critical promise cannot be enforced.
- **Major:** incomplete trust, change, lifecycle, approval, test, or evidence model that can cause a breaking or ungoverned outcome.
- **Minor:** clarity, portability, traceability, or maintainability weakness that does not invalidate the boundary.

## Assess Compatibility

For structured JSON artifacts, run:

```bash
python skills/data-contract-designer/scripts/assess_compatibility.py \
  before.json after.json --format markdown
```

The script detects structural changes and returns a conservative recommendation. Then assess semantic, quality, SLO, access, purpose, retention, delivery, and policy changes using repository guidance; those changes require domain evidence beyond schema comparison.

Use these defaults:

- **Patch:** non-behavioral clarification only.
- **Minor:** backward-compatible optional addition or measurable improvement.
- **Major:** removal, rename, type change, new requirement, changed meaning, reduced service promise, tighter classification, changed delivery behavior, or widened use unless executable evidence proves compatibility.

Never classify a change as compatible only because a parser accepts it.

## Plan Contract Change

1. Identify all connected ingestion, creation, and consumption contract versions.
2. Identify affected products, ports, consumers, policies, tests, telemetry, runbooks, and runtime bindings.
3. Recommend version level and required approval.
4. Define coexistence, migration, notice, rollback, expiry, and retirement evidence.
5. Keep the last compatible version available when safe and required.
6. Block publication when a breaking change lacks accountable impact and migration decisions.

## Safety and Authority

- Treat all outputs as drafts or reviews until accountable owners approve them.
- Never grant access, publish a contract, activate a source, approve product go-live, or accept risk.
- Never widen purpose or rights beyond the product promise and policy authority.
- Never fabricate consumers, approvals, tests, telemetry, health, compatibility, or conformance.
- Minimize sensitive sample data; prefer field metadata and synthetic examples.
- Require human review for legal, privacy, security, external-sharing, and AI-use terms.

## Return the Result

Follow `references/output-contracts.md`. Include:

- Boundary and selected contract type.
- Draft or review result.
- Compatibility and lifecycle decision when applicable.
- Enforcement and test map.
- Evidence supplied, evidence gaps, and assumptions.
- Mandatory approvals and unresolved decisions.
- Prioritized next actions.
- Exact repository guidance used.

When editing this repository, run this skill's package tests, the strict MkDocs build, and the internal link checker before completion.

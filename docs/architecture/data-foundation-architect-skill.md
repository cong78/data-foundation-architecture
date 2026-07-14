# Data Foundation Architect Skill

The repository includes a project-native AI skill that turns this guidance into repeatable architecture work without making the skill a second source of truth.

Current package version: **1.2.0**.

## What It Does

| Mode | Typical request | Result |
| --- | --- | --- |
| Assess | Assess a data domain for onboarding or maturity. | Admission decision, dimension scores, evidence gaps and improvement plan. |
| Design | Design a foundation capability or reference solution. | Layered architecture, flows, controls, decisions and done criteria. |
| Review | Validate an architecture, product, contract or technology choice. | Severity-ordered findings and remediation. |
| Generate | Create a governed delivery or operations artifact. | Completed domain, product, contract, technology, conformance, agent, or service-runbook template. |

## Package

The skill is stored at:

```text
skills/data-foundation-architect/
├── SKILL.md
├── manifest.json
├── schemas/
├── references/
├── scripts/
└── assets/
```

`SKILL.md` contains the runtime-neutral operating workflow. `manifest.json` defines capabilities, side effects, authorization, data policy, reliability, approvals, telemetry, and tests. JSON schemas define assessment and task contracts. The guidance map points to authoritative pages under `docs/`, including the five-stage journey, eight services, portal marketplace, and architecture-to-operations traceability.

## Integrate with an Agent Runtime

An agent platform integrates the skill through a small adapter:

1. Register the stable skill id and version from `manifest.json`.
2. Load `SKILL.md` when the request matches Assess, Design, Review, or Generate.
3. Expose repository guidance as read-only context and load pages through `references/guidance-map.md`.
4. Execute bundled scripts in an isolated runtime with explicit input and output schemas.
5. Apply platform identity, policy, approval, budget, and telemetry controls outside prompt text.

The package does not require a specific model provider, agent framework, tool protocol, or prompt syntax. MCP, A2A, HTTP APIs, function tools, or native runtime adapters may expose it without changing the skill contract.

## Example Invocations

```text
Use the Data Foundation Architect skill to assess the Customer domain for onboarding.

Use the Data Foundation Architect skill to review this data product against the product go-live gates.

Use the Data Foundation Architect skill to design governed supplier sharing with Delta Sharing.

Use the Data Foundation Architect skill to generate a technology selection record for data observability.

Use the Data Foundation Architect skill to create a service runbook linked to architecture, service ownership, telemetry, recovery evidence, and the runway.
```

## Maturity Scoring

The bundled scorer evaluates admission gates independently from maturity:

```bash
python skills/data-foundation-architect/scripts/assess_maturity.py \
  skills/data-foundation-architect/assets/domain-assessment.example.json \
  --format markdown
```

It reports all six maturity dimensions, evidence coverage and the lowest dimension. A failed mandatory gate blocks enablement regardless of the percentage.

## Governance Boundary

- The MkDocs guidance remains authoritative.
- The skill loads only task-relevant pages through progressive disclosure.
- The skill does not fabricate evidence, approvals, ownership or measurements.
- Generated designs remain proposals until accountable owners approve them.
- Unity Catalog and Delta Lake are approved catalog and storage defaults; other vendor mappings remain implementation profiles rather than enterprise contracts.
- Production designs trace architecture to service, playbook, runbook, evidence, and runway phase.
- Changes to source guidance require skill-map validation before release.

## Validation

Run:

```bash
python skills/data-foundation-architect/scripts/validate_package.py
python skills/data-foundation-architect/scripts/validate_examples.py
python skills/data-foundation-architect/scripts/verify_guidance_map.py
```

The example validator checks assessment input, scorer output, task request, and task result against local JSON Schemas without an external schema package. The repository CI should run all manifest tests together with the strict MkDocs build and internal-link validation.

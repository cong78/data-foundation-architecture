# Data Foundation Architect Skill

The repository includes a project-native AI skill that turns this guidance into repeatable architecture work without making the skill a second source of truth.

## What It Does

| Mode | Typical request | Result |
| --- | --- | --- |
| Assess | Assess a data domain for onboarding or maturity. | Admission decision, dimension scores, evidence gaps and improvement plan. |
| Design | Design a foundation capability or reference solution. | Layered architecture, flows, controls, decisions and done criteria. |
| Review | Validate an architecture, product, contract or technology choice. | Severity-ordered findings and remediation. |
| Generate | Create a governed delivery artifact. | Completed domain, product, contract, technology or conformance template. |

## Package

The skill is stored at:

```text
skills/data-foundation-architect/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/
└── assets/
```

`SKILL.md` contains the operating workflow. The guidance map points to authoritative pages under `docs/`. Evidence and output references keep decisions consistent. Scripts provide deterministic checks where model judgment should not calculate or validate silently.

## Activate in Codex

Keep the skill source in this repository and link it into the Codex skill directory so repository updates remain visible:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$PWD/skills/data-foundation-architect" \
  "${CODEX_HOME:-$HOME/.codex}/skills/data-foundation-architect"
```

Run this from the repository root. If the destination already exists, inspect it before replacing it. Start a new Codex session after activation so the skill metadata is discovered.

## Example Invocations

```text
Use $data-foundation-architect to assess the Customer domain for onboarding.

Use $data-foundation-architect to review this data product against the product go-live gates.

Use $data-foundation-architect to design governed supplier sharing with Delta Sharing.

Use $data-foundation-architect to generate a technology selection record for data observability.
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
- Vendor mappings remain implementation profiles rather than enterprise contracts.
- Changes to source guidance require skill-map validation before release.

## Validation

Run:

```bash
python /path/to/skill-creator/scripts/quick_validate.py skills/data-foundation-architect
python skills/data-foundation-architect/scripts/verify_guidance_map.py
```

The repository CI should run these checks together with the strict MkDocs build and internal-link validation.

# Data Contract Designer Skill

<div class="decision-brief"><div><small>Use when</small><strong>Designing, reviewing, or changing a data contract.</strong></div><div><small>Decision</small><strong>Which contract governs the boundary and is it enforceable?</strong></div><div><small>Owner</small><strong>Contract parties and accountable control owners.</strong></div><div><small>Output</small><strong>Draft, findings, compatibility decision, and evidence gaps.</strong></div></div>

The repository includes a portable Data Contract Designer skill that turns the three-contract model into a focused workflow without giving an AI authority to approve, publish, or enforce a contract.

Current package version: **1.0.0**.

## What It Does

| Mode | Typical request | Result |
| --- | --- | --- |
| Design | Draft the contract for a source, product, or consumer boundary. | Structured draft, enforcement tests, approvers, and evidence gaps. |
| Review | Check whether a contract is complete and enforceable. | Blocker, major, and minor findings with corrections. |
| Compatibility | Compare two versions and identify breaking changes. | Patch, minor, or major recommendation with affected terms. |
| Change impact | Plan migration, deprecation, or retirement. | Dependency, coexistence, notice, rollback, migration, and retirement plan. |

The skill uses only:

- **Source System Ingestion Contract**
- **Data Product Creation Contract**
- **Data Product Consumption Contract**

BI, applications, platforms, sharing, and AI remain consumption profiles rather than additional contract types.

## Package

```text
skills/data-contract-designer/
├── SKILL.md
├── manifest.json
├── agents/
├── references/
├── schemas/
├── scripts/
└── assets/
```

The package includes typed request and result schemas, evidence and output rules, representative examples, package validators, and a deterministic compatibility checker. The MkDocs [Data Contract Standard](../standards/data-contract-standard.md) remains authoritative.

## Install

Run one installation from the repository root. Symbolic links keep the packaged skill and installed skill synchronized.

=== "OpenAI Codex"

    ```bash
    mkdir -p .agents/skills
    ln -sfn ../../skills/data-contract-designer \
      .agents/skills/data-contract-designer
    ```

    Invoke with `$data-contract-designer` or select it through `/skills`.

=== "Claude Code"

    ```bash
    mkdir -p .claude/skills
    ln -sfn ../../skills/data-contract-designer \
      .claude/skills/data-contract-designer
    ```

    Invoke with `/data-contract-designer`.

=== "GitHub Copilot CLI"

    ```bash
    mkdir -p .github/skills
    ln -sfn ../../skills/data-contract-designer \
      .github/skills/data-contract-designer
    ```

    Run `/skills reload`, inspect it with `/skills info data-contract-designer`, and invoke `/data-contract-designer`.

For personal installation, copy or link the complete package to `~/.agents/skills/`, `~/.claude/skills/`, or `~/.copilot/skills/`. Invoke it from this repository so it can resolve the authoritative MkDocs guidance. See [Data Foundation Architect Skill](data-foundation-architect-skill.md#install-the-skill) for installation behavior and trust guidance.

## Example Invocations

```text
Use the Data Contract Designer skill to draft the Source System Ingestion Contract for SAP customer events.

Review this Data Product Creation Contract and identify blockers before product go-live.

Compare versions 1.4.0 and 2.0.0 of this contract and produce the migration impact.

Design a Data Product Consumption Contract for an AI retrieval use case with expiry and revocation.
```

## Compatibility Check

For structured JSON artifacts:

```bash
python skills/data-contract-designer/scripts/assess_compatibility.py \
  before.json after.json --format markdown
```

The checker detects field removal, field-type changes, optional-to-required changes, required additions, classification tightening, widened valid uses, and changed trust or control terms. Its result is deliberately conservative: semantics and runtime behavior still require accountable evidence.

## Authority Boundary

- The skill produces drafts and reviews; it does not approve or publish contracts.
- The Data Contract System remains authoritative for registered versions and lifecycle state.
- Lifecycle services enforce contracts at ingestion, creation, consumption, and operation boundaries.
- The skill does not grant access, activate sources, approve product go-live, accept risk, or invent evidence.
- ODCS conformance is claimed only after validation against the pinned canonical schema and portability profile.

## Validate

```bash
python skills/data-contract-designer/scripts/validate_package.py
python skills/data-contract-designer/scripts/validate_examples.py
python skills/data-contract-designer/scripts/verify_guidance_map.py
python skills/data-contract-designer/scripts/assess_compatibility.py \
  skills/data-contract-designer/assets/compatibility-before.example.json \
  skills/data-contract-designer/assets/compatibility-after.example.json \
  --format markdown
```

<div class="read-next"><strong>Next:</strong> use the <a href="/standards/data-contract-standard/">Data Contract Standard</a> to understand mandatory terms, then invoke the skill for a real boundary.</div>

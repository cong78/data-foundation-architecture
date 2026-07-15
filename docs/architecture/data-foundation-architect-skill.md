# Data Foundation Architect Skill

The repository includes a project-native AI skill that turns this guidance into repeatable architecture work without making the skill a second source of truth.

For focused contract authoring, review, compatibility, and migration work, use the companion [Data Contract Designer Skill](data-contract-designer-skill.md).

Current package version: **1.4.0**.

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
├── agents/
├── schemas/
├── references/
├── scripts/
└── assets/
```

`SKILL.md` contains the runtime-neutral operating workflow. `agents/openai.yaml` provides Skill Creator-compatible UI metadata. `manifest.json` defines capabilities, side effects, authorization, data policy, reliability, approvals, telemetry, and tests. JSON schemas define assessment and task contracts. The guidance map points to authoritative pages under `docs/`, including the five-stage journey, nine services, portal marketplace, and architecture-to-operations traceability.

## Install the Skill

Install the complete `skills/data-foundation-architect/` directory, not only `SKILL.md`; its manifest, references, schemas, scripts, and assets are part of the package.

Repository-scoped installation is recommended because the skill resolves its authoritative guidance from this MkDocs repository. Run the commands below from the repository root. A symbolic link keeps one canonical package, so updates under `skills/` are immediately available to the agent tool.

=== "OpenAI Codex"

    Codex discovers repository skills under `.agents/skills/`.

    ```bash
    mkdir -p .agents/skills
    ln -sfn ../../skills/data-foundation-architect \
      .agents/skills/data-foundation-architect
    ```

    Start Codex from this repository, run `/skills` to verify discovery, then invoke the skill explicitly:

    ```text
    $data-foundation-architect Review this architecture against the foundation guidance.
    ```

    Codex may also select the skill automatically when the request matches its description. If a newly installed skill does not appear, restart Codex. See the [Codex skills documentation](https://developers.openai.com/codex/skills).

=== "Claude Code"

    Claude Code discovers project skills under `.claude/skills/`.

    ```bash
    mkdir -p .claude/skills
    ln -sfn ../../skills/data-foundation-architect \
      .claude/skills/data-foundation-architect
    ```

    Start `claude` from this repository and invoke:

    ```text
    /data-foundation-architect Review this architecture against the foundation guidance.
    ```

    Claude Code can also load the skill automatically from its description. Skill changes are detected live when the skills directory was present at session start; otherwise restart the session. See the [Claude Code skills documentation](https://code.claude.com/docs/en/slash-commands).

=== "GitHub Copilot CLI"

    GitHub Copilot CLI discovers project skills under `.github/skills/`, `.agents/skills/`, or `.claude/skills/`. Use its native project location when installing it independently:

    ```bash
    mkdir -p .github/skills
    ln -sfn ../../skills/data-foundation-architect \
      .github/skills/data-foundation-architect
    ```

    Start `copilot`. In an existing session, reload and inspect the skill:

    ```text
    /skills reload
    /skills info data-foundation-architect
    /data-foundation-architect Review this architecture against the foundation guidance.
    ```

    The non-interactive CLI also supports `copilot skill list`. See the [GitHub Copilot CLI skills documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

!!! tip "One shared project location"
    OpenAI Codex and GitHub Copilot CLI both discover `.agents/skills/`. If only those two tools are used, the Codex installation is sufficient for both. Claude Code should use the additional `.claude/skills/` link.

### Install Without Symbolic Links

When symbolic links are unavailable, copy the package into the tool-specific directory. Repeat the copy after every skill update.

```bash
# Choose one destination: .agents/skills, .claude/skills, or .github/skills
mkdir -p .agents/skills
cp -R skills/data-foundation-architect .agents/skills/
```

Before trusting or invoking the skill, review `SKILL.md`, `manifest.json`, and bundled scripts. Installation makes the workflow discoverable; the host tool still controls filesystem, shell, network, approval, and identity permissions.

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

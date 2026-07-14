# Data Foundation Architecture

MkDocs repository for consolidated enterprise architecture guidance on building an AI-ready data foundation as part of a company Data and AI foundation.

## Scope

The guidance defines:

- Foundation definition and scope.
- Architecture principles and decision rules.
- Reference architecture and data product lifecycle.
- Nine foundation services.
- Architecture blueprint and service implementation patterns.
- Data contract, data product management, OpenTelemetry, and AI-ready data standards.
- Templates and examples for real delivery.
- Governance, security, compliance, operating model, and implementation runway.

The nine foundation services are:

- Data service portal
- Data Service AI Assistant
- Data ingestion service
- Data product creation service
- Data consumption service
- Data sharing service
- Platform enablement service
- Data observability service
- Data foundation operations service

## AI Skills

The repository includes a platform-neutral AI skill at `skills/data-foundation-architect/`. It supports evidence-based assessment, architecture design, review, and governed artifact generation while treating the MkDocs pages as the authoritative guidance.

See [Data Foundation Architect Skill](docs/architecture/data-foundation-architect-skill.md) for OpenAI Codex, Claude Code, and GitHub Copilot CLI installation, activation, examples, scoring, and validation.

The focused `skills/data-contract-designer/` package designs, reviews, compares, and plans changes to the three approved data contract types. See [Data Contract Designer Skill](docs/architecture/data-contract-designer-skill.md) for installation, examples, authority boundaries, and compatibility checking.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Build

```bash
mkdocs build
```

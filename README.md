# Data Foundation Architecture

MkDocs repository for consolidated architecture guidance on building an AI-ready data foundation as part of a company Data and AI foundation.

Version `0.1.0` is the first published, incubating release for controlled pilots. Publication of the guidance does not imply that an implementation is conformant or operationally ready.

## Scope

The guidance defines:

- Foundation definition and scope.
- Architecture principles and decision rules.
- Reference architecture and data product lifecycle.
- Nine foundation services.
- Architecture blueprint and service implementation patterns.
- Data contract, data product management, OpenTelemetry, and AI-ready data standards.
- Runbooks, templates, and examples for repeatable execution.
- Machine-readable architecture policies.
- Governance, security, compliance, operating model, and implementation runway.

The nine foundation services are:

- Data Service Portal
- Data Service AI Assistant
- Data Ingestion Service
- Data Product Creation Service
- Data Consumption Service
- Data Sharing Service
- Platform Enablement Service
- Data Observability Service
- Data Foundation Operations Service

## Architecture Assistance

Optional skills and the read-only agent help teams apply the guidance consistently. They are execution aids, not part of the logical foundation architecture or a replacement for accountable decisions.

The repository includes a platform-neutral AI skill at `skills/data-foundation-architect/`. It supports evidence-based assessment, architecture design, review, and governed artifact generation while treating the MkDocs pages as the authoritative guidance.

See [Data Foundation Architect Skill](docs/architecture/data-foundation-architect-skill.md) for OpenAI Codex, Claude Code, and GitHub Copilot CLI installation, activation, examples, scoring, and validation.

The focused `skills/data-contract-designer/` package designs, reviews, compares, and plans changes to the three approved data contract types. See [Data Contract Designer Skill](docs/architecture/data-contract-designer-skill.md) for installation, examples, authority boundaries, and compatibility checking.

The read-only `agent/` package begins a model-neutral Data Foundation Architecture Agent that can integrate behind a company AI assistant. It provides typed requests and results, repository-grounded citations, deterministic architecture tools, and an OpenAPI adapter contract. See [Data Foundation Architecture Agent](docs/architecture/data-foundation-architecture-agent.md).

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Build and Validate

```bash
mkdocs build --strict
python scripts/check_internal_links.py site
python scripts/check_navigation.py
python scripts/check_release_readiness.py
```

## Validate Architecture Policies

```bash
python scripts/validate_architecture_policies.py
```

See `GOVERNANCE.md`, `COMPATIBILITY.md`, `CONTRIBUTING.md`, `SUPPORT.md`, and `CHANGELOG.md` before adopting or changing a public guidance interface.

## License

Licensed under the [Apache License 2.0](LICENSE).

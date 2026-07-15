# Data Foundation Architecture Agent

Read-only, model-neutral architecture tools intended to run behind a company AI assistant and the Data Service AI Assistant.

## Run the Example

From the repository root:

```bash
PYTHONPATH=agent python -m data_foundation_architecture_agent.cli \
  agent/examples/search-request.json \
  --repository-root .
```

The result is JSON validated against `schemas/result.schema.json`. Every citation points to source Markdown under `docs/`; generated `site/` content is never indexed.

## Integration Boundary

Use `openapi.yaml` for an HTTP adapter. MCP or native company-assistant tools may use the same schemas, but must preserve:

- Authenticated actor and declared purpose.
- Read-only side-effect class.
- Exact operation and task identifiers.
- Repository paths, headings, excerpts, authority classes, and scores.
- Explicit evidence gaps and proposed actions.
- Agent version, guidance revision, operation, actor, purpose, source count, and outcome telemetry.

The MVP contains no model-provider dependency and performs no writes or external actions.

## Validate

```bash
PYTHONPATH=agent python agent/scripts/validate_agent.py
PYTHONPATH=agent python agent/scripts/evaluate_agent.py
PYTHONPATH=agent python -m unittest discover -s agent/tests -v
```

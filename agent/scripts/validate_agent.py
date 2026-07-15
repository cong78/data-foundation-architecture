#!/usr/bin/env python3
"""Validate the architecture-agent package and exercise every operation."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


AGENT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = AGENT_ROOT.parent
sys.path.insert(0, str(AGENT_ROOT))

from data_foundation_architecture_agent import ArchitectureAgent  # noqa: E402


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    manifest = load_json(AGENT_ROOT / "manifest.json")
    request_schema = load_json(AGENT_ROOT / "schemas" / "request.schema.json")
    result_schema = load_json(AGENT_ROOT / "schemas" / "result.schema.json")
    request_validator = Draft202012Validator(request_schema)
    result_validator = Draft202012Validator(result_schema)

    required_files = [
        AGENT_ROOT / "README.md",
        AGENT_ROOT / "openapi.yaml",
        AGENT_ROOT / "examples" / "search-request.json",
        AGENT_ROOT / "data_foundation_architecture_agent" / "runtime.py",
        AGENT_ROOT / "data_foundation_architecture_agent" / "guidance.py",
    ]
    missing = [str(path.relative_to(REPOSITORY_ROOT)) for path in required_files if not path.exists()]
    if missing:
        raise SystemExit("Missing architecture-agent files: " + ", ".join(missing))

    if manifest["side_effects"] != {"class": "read", "writes": False, "external_actions": False}:
        raise SystemExit("Architecture-agent MVP must remain read-only.")

    openapi = yaml.safe_load((AGENT_ROOT / "openapi.yaml").read_text(encoding="utf-8"))
    if openapi.get("openapi") != "3.1.0" or "/v1/architecture-agent/tasks" not in openapi.get("paths", {}):
        raise SystemExit("OpenAPI adapter contract is incomplete.")

    base_request = load_json(AGENT_ROOT / "examples" / "search-request.json")
    request_validator.validate(base_request)
    agent = ArchitectureAgent(REPOSITORY_ROOT)
    operation_queries = {
        "search_guidance": "data product go-live gates",
        "resolve_definition": "Data contract",
        "classify_design": "Cross-service handoff between ingestion and product creation",
        "trace_architecture": base_request["query"],
        "prepare_context_pack": "Design an observable data product consumption capability",
    }

    for operation in manifest["operations"]:
        request = copy.deepcopy(base_request)
        request["operation"] = operation
        request["query"] = operation_queries[operation]
        result = agent.run(request)
        result_validator.validate(result)
        if result["approval"]["side_effect_class"] != "read" or result["approval"]["required"]:
            raise SystemExit(f"Operation {operation} violated the read-only approval contract.")
        if not result["telemetry"]["guidance_revision"]:
            raise SystemExit(f"Operation {operation} omitted the guidance revision.")
        for citation in result["citations"]:
            if not (REPOSITORY_ROOT / citation["path"]).exists():
                raise SystemExit(f"Operation {operation} returned a missing citation: {citation['path']}")

    print(
        f"Validated {manifest['id']} v{manifest['version']} with "
        f"{len(manifest['operations'])} read-only operations and OpenAPI integration contract."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

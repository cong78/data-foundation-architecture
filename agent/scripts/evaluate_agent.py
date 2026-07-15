#!/usr/bin/env python3
"""Run deterministic golden cases against the read-only architecture agent."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


AGENT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = AGENT_ROOT.parent
sys.path.insert(0, str(AGENT_ROOT))

from data_foundation_architecture_agent import ArchitectureAgent  # noqa: E402


def main() -> int:
    agent = ArchitectureAgent(REPOSITORY_ROOT)
    base_request = json.loads(
        (AGENT_ROOT / "examples" / "search-request.json").read_text(encoding="utf-8")
    )
    cases = json.loads(
        (AGENT_ROOT / "evals" / "golden-cases.json").read_text(encoding="utf-8")
    )
    failures: list[str] = []

    for case in cases:
        request = copy.deepcopy(base_request)
        request.update(
            {
                "task_id": f"eval-{case['id']}",
                "operation": case["operation"],
                "query": case["query"],
                "purpose": "Run deterministic architecture-agent evaluation",
            }
        )
        result = agent.run(request)
        authorities = {citation["authority"] for citation in result["citations"]}
        required = set(case.get("required_authorities", []))

        if result["status"] != case["expected_status"]:
            failures.append(
                f"{case['id']}: status {result['status']} != {case['expected_status']}"
            )
        if result["classification"]["kind"] != case["expected_kind"]:
            failures.append(
                f"{case['id']}: kind {result['classification']['kind']} != {case['expected_kind']}"
            )
        if not required.issubset(authorities):
            failures.append(
                f"{case['id']}: missing authorities {sorted(required - authorities)}"
            )
        if len(result["citations"]) < case.get("minimum_citations", 1):
            failures.append(f"{case['id']}: insufficient citations")
        if result["approval"] != {
            "required": False,
            "side_effect_class": "read",
            "reason": "The MVP retrieves and classifies guidance without changing authoritative state.",
        }:
            failures.append(f"{case['id']}: read-only approval contract changed")

    if failures:
        raise SystemExit("Architecture-agent evaluation failed:\n- " + "\n- ".join(failures))

    print(f"Passed {len(cases)} architecture-agent golden cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

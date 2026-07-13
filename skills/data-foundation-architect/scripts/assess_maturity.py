#!/usr/bin/env python3
"""Score a data-domain maturity assessment without overriding admission gates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DIMENSIONS = (
    "direction-and-ownership",
    "foundation-services",
    "data-products-and-contracts",
    "access-security-and-governance",
    "observability-and-operations",
    "interoperability-and-ai-enablement",
)

ADMISSION_GATES = (
    "identity",
    "boundary",
    "accountability",
    "governance",
    "access",
    "operations",
)

GATE_STATUSES = {"pass", "conditional", "fail", "not_assessed"}


class AssessmentError(ValueError):
    pass


def maturity_level(score: int) -> str:
    if score >= 85:
        return "Optimized"
    if score >= 65:
        return "Established"
    if score >= 40:
        return "Emerging"
    return "Foundational"


def has_evidence(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return any(isinstance(item, str) and item.strip() for item in value)
    return False


def load_assessment(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise AssessmentError(f"Assessment file does not exist: {path}") from error
    except json.JSONDecodeError as error:
        raise AssessmentError(f"Invalid JSON at line {error.lineno}: {error.msg}") from error
    if not isinstance(data, dict):
        raise AssessmentError("Assessment root must be a JSON object")
    return data


def score_assessment(data: dict[str, Any]) -> dict[str, Any]:
    scope = data.get("scope")
    if not isinstance(scope, dict) or not scope.get("id") or not scope.get("name"):
        raise AssessmentError("scope.id and scope.name are required")

    gates = data.get("admission_gates")
    if not isinstance(gates, dict):
        raise AssessmentError("admission_gates must be an object")

    gate_results: dict[str, dict[str, Any]] = {}
    blocking_gates: list[str] = []
    conditional_gates: list[str] = []
    for gate in ADMISSION_GATES:
        item = gates.get(gate)
        if not isinstance(item, dict):
            raise AssessmentError(f"admission_gates.{gate} must be an object")
        status = item.get("status", "not_assessed")
        if status not in GATE_STATUSES:
            raise AssessmentError(
                f"admission_gates.{gate}.status must be one of {sorted(GATE_STATUSES)}"
            )
        evidence = item.get("evidence", [])
        gate_results[gate] = {
            "status": status,
            "has_evidence": has_evidence(evidence),
            "note": item.get("note", ""),
        }
        if status in {"fail", "not_assessed"}:
            blocking_gates.append(gate)
        elif status == "conditional":
            conditional_gates.append(gate)

    dimensions = data.get("dimensions")
    if not isinstance(dimensions, dict):
        raise AssessmentError("dimensions must be an object")

    dimension_results: dict[str, dict[str, Any]] = {}
    total_checks = 0
    total_passed = 0
    total_evidenced = 0

    for dimension in DIMENSIONS:
        checks = dimensions.get(dimension)
        if not isinstance(checks, list) or not checks:
            raise AssessmentError(f"dimensions.{dimension} must be a non-empty array")

        passed = 0
        evidenced = 0
        gaps: list[str] = []
        for index, check in enumerate(checks):
            if not isinstance(check, dict):
                raise AssessmentError(f"dimensions.{dimension}[{index}] must be an object")
            check_id = check.get("id")
            if not isinstance(check_id, str) or not check_id.strip():
                raise AssessmentError(f"dimensions.{dimension}[{index}].id is required")
            is_passed = check.get("passed")
            if not isinstance(is_passed, bool):
                raise AssessmentError(
                    f"dimensions.{dimension}[{index}].passed must be true or false"
                )
            evidence_present = has_evidence(check.get("evidence", []))
            if evidence_present:
                evidenced += 1
            if is_passed and evidence_present:
                passed += 1
            else:
                gaps.append(check_id)

        count = len(checks)
        score = round((passed / count) * 100)
        dimension_results[dimension] = {
            "score": score,
            "level": maturity_level(score),
            "passed": passed,
            "checks": count,
            "evidence_coverage": round((evidenced / count) * 100),
            "gaps": gaps,
        }
        total_checks += count
        total_passed += passed
        total_evidenced += evidenced

    overall_score = round((total_passed / total_checks) * 100)
    lowest_dimension = min(
        dimension_results,
        key=lambda name: dimension_results[name]["score"],
    )

    if blocking_gates:
        admission_decision = "Blocked"
    elif conditional_gates:
        admission_decision = "Enable with conditions"
    else:
        admission_decision = "Eligible for enablement"

    return {
        "scope": scope,
        "assessment_version": data.get("assessment_version", "unspecified"),
        "assessment_date": data.get("assessment_date", "unspecified"),
        "admission": {
            "decision": admission_decision,
            "blocking_gates": blocking_gates,
            "conditional_gates": conditional_gates,
            "gates": gate_results,
        },
        "maturity": {
            "score": overall_score,
            "level": maturity_level(overall_score),
            "evidence_coverage": round((total_evidenced / total_checks) * 100),
            "lowest_dimension": lowest_dimension,
            "dimensions": dimension_results,
        },
    }


def markdown_report(result: dict[str, Any]) -> str:
    scope = result["scope"]
    admission = result["admission"]
    maturity = result["maturity"]
    lines = [
        f"# Data Foundation Maturity Assessment: {scope['name']}",
        "",
        f"- **Scope:** `{scope['id']}`",
        f"- **Assessment version:** {result['assessment_version']}",
        f"- **Assessment date:** {result['assessment_date']}",
        f"- **Admission decision:** {admission['decision']}",
        f"- **Maturity:** {maturity['score']}% ({maturity['level']})",
        f"- **Evidence coverage:** {maturity['evidence_coverage']}%",
        f"- **Lowest dimension:** {maturity['lowest_dimension']}",
        "",
        "## Dimension Scores",
        "",
        "| Dimension | Score | Level | Evidence | Gaps |",
        "| --- | ---: | --- | ---: | --- |",
    ]
    for name, dimension in maturity["dimensions"].items():
        gaps = ", ".join(dimension["gaps"]) or "None"
        lines.append(
            f"| {name} | {dimension['score']}% | {dimension['level']} | "
            f"{dimension['evidence_coverage']}% | {gaps} |"
        )

    lines.extend(["", "## Admission Gates", ""])
    if admission["blocking_gates"]:
        lines.append(f"- **Blocking:** {', '.join(admission['blocking_gates'])}")
    if admission["conditional_gates"]:
        lines.append(f"- **Conditional:** {', '.join(admission['conditional_gates'])}")
    if not admission["blocking_gates"] and not admission["conditional_gates"]:
        lines.append("- All mandatory gates passed.")
    lines.extend(
        [
            "",
            "> The maturity score is an improvement signal, not certification, and does not override admission gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assessment", type=Path, help="Assessment JSON file")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()

    try:
        result = score_assessment(load_assessment(args.assessment))
    except AssessmentError as error:
        print(f"Assessment error: {error}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(markdown_report(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

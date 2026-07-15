"""Deterministic read-only operations for architecture-assistant integration."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .guidance import GuidanceIndex, SearchHit, clean_markdown


AGENT_ID = "data-foundation-architecture-agent"


class AgentRequestError(ValueError):
    """Raised when a request violates its schema or read-only contract."""


class ArchitectureAgent:
    def __init__(self, repository_root: Path):
        self.repository_root = repository_root.resolve()
        agent_root = self.repository_root / "agent"
        self.manifest = json.loads((agent_root / "manifest.json").read_text(encoding="utf-8"))
        request_schema = json.loads((agent_root / "schemas" / "request.schema.json").read_text(encoding="utf-8"))
        result_schema = json.loads((agent_root / "schemas" / "result.schema.json").read_text(encoding="utf-8"))
        self.request_validator = Draft202012Validator(request_schema)
        self.result_validator = Draft202012Validator(result_schema)
        self.index = GuidanceIndex(self.repository_root)
        self.guidance_revision = self._guidance_revision()

    def _guidance_revision(self) -> str:
        configured = os.environ.get("GUIDANCE_REVISION", "").strip()
        if configured:
            return configured
        try:
            return subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repository_root,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            ).stdout.strip()
        except (FileNotFoundError, subprocess.SubprocessError):
            return "unknown"

    def run(self, request: dict[str, Any]) -> dict[str, Any]:
        errors = sorted(self.request_validator.iter_errors(request), key=lambda error: list(error.path))
        if errors:
            detail = "; ".join(error.message for error in errors)
            raise AgentRequestError(f"Invalid architecture-agent request: {detail}")

        operation = request["operation"]
        handler = {
            "search_guidance": self._search_guidance,
            "resolve_definition": self._resolve_definition,
            "classify_design": self._classify_design,
            "trace_architecture": self._trace_architecture,
            "prepare_context_pack": self._prepare_context_pack,
        }[operation]
        result = handler(request)
        result_errors = sorted(self.result_validator.iter_errors(result), key=lambda error: list(error.path))
        if result_errors:
            detail = "; ".join(error.message for error in result_errors)
            raise RuntimeError(f"Architecture-agent result violated its contract: {detail}")
        return result

    def _base_result(
        self,
        request: dict[str, Any],
        status: str,
        summary: str,
        classification: dict[str, Any],
        citations: list[dict[str, Any]],
        evidence_gaps: list[str] | None = None,
        proposed_actions: list[str] | None = None,
    ) -> dict[str, Any]:
        return {
            "task_id": request["task_id"],
            "operation": request["operation"],
            "status": status,
            "summary": summary,
            "classification": classification,
            "citations": citations,
            "evidence_gaps": evidence_gaps or [],
            "proposed_actions": proposed_actions or [],
            "approval": {
                "required": False,
                "side_effect_class": "read",
                "reason": "The MVP retrieves and classifies guidance without changing authoritative state.",
            },
            "telemetry": {
                "agent_id": AGENT_ID,
                "agent_version": self.manifest["version"],
                "guidance_revision": self.guidance_revision,
                "task_id": request["task_id"],
                "operation": request["operation"],
                "actor_id": request["actor"]["id"],
                "purpose": request["purpose"],
                "source_count": len(citations),
                "outcome": status,
            },
        }

    def _citations(self, hits: list[SearchHit]) -> list[dict[str, Any]]:
        citations: list[dict[str, Any]] = []
        for hit in hits:
            excerpt = hit.section.text
            if len(excerpt) > 420:
                excerpt = excerpt[:417].rstrip() + "..."
            citations.append(
                {
                    "path": hit.section.path,
                    "heading": hit.section.heading,
                    "excerpt": excerpt,
                    "authority": hit.section.authority,
                    "score": hit.score,
                }
            )
        return citations

    def _search(
        self,
        request: dict[str, Any],
        query: str | None = None,
        preferred_paths: tuple[str, ...] = (),
    ) -> list[dict[str, Any]]:
        preferred = tuple(request.get("context_references", [])) + preferred_paths
        hits = self.index.search(query or request["query"], request.get("top_k", 5), preferred)
        return self._citations(hits)

    def _search_guidance(self, request: dict[str, Any]) -> dict[str, Any]:
        citations = self._search(request)
        status = "complete" if citations else "unresolved"
        return self._base_result(
            request,
            status,
            f"Found {len(citations)} authoritative guidance section(s) for the request." if citations else "No authoritative guidance section matched the request.",
            {"kind": "repository-fact", "confidence": 1.0 if citations else 0.0, "basis": "Ranked section retrieval from repository Markdown."},
            citations,
            [] if citations else ["No matching repository section was found."],
            ["Use the cited sections as bounded context for assistant reasoning."] if citations else ["Clarify the architecture term, service, or outcome."],
        )

    def _resolve_definition(self, request: dict[str, Any]) -> dict[str, Any]:
        resolved = self.index.definition(request["query"])
        if not resolved:
            return self._base_result(
                request,
                "unresolved",
                f"No exact canonical glossary definition exists for '{clean_markdown(request['query'])}'.",
                {"kind": "needs-review", "confidence": 0.0, "basis": "Exact glossary lookup returned no match."},
                [],
                ["Canonical definition is absent or the supplied term is not exact."],
                ["Search related guidance or propose a glossary addition for architecture review."],
            )
        term, definition = resolved
        citation = {
            "path": "docs/foundation/glossary.md",
            "heading": term,
            "excerpt": definition,
            "authority": "definition",
            "score": 1.0,
        }
        return self._base_result(
            request,
            "complete",
            f"{term}: {definition}",
            {"kind": "repository-fact", "confidence": 1.0, "basis": "Exact canonical glossary match."},
            [citation],
        )

    def _classify_design(self, request: dict[str, Any]) -> dict[str, Any]:
        query = clean_markdown(request["query"]).lower()
        integration_terms = ("cross-service", "handoff", "between services", "end-to-end flow", "integration", "compensation", "reconciliation")
        shared_terms = ("shared capability", "contract", "catalog", "storage", "identity", "policy", "semantic", "unified access", "telemetry", "developer experience")
        service_names = (
            "portal", "ai assistant", "ingestion", "product creation", "consumption",
            "sharing", "platform enablement", "observability", "foundation operations",
        )
        if any(term in query for term in integration_terms):
            kind, confidence, basis = "integration", 0.9, "The request names a cross-service interaction, handoff, or recovery concern."
        elif any(term in query for term in shared_terms):
            kind, confidence, basis = "shared-capability", 0.8, "The request names a reusable control or runtime concern shared by services."
        elif any(term in query for term in service_names):
            kind, confidence, basis = "service-specific", 0.8, "The request names one canonical foundation service outcome."
        else:
            kind, confidence, basis = "needs-review", 0.3, "The request does not identify a stable service, shared capability, or cross-service interaction."
        citations = self._search(
            request,
            query=f"{request['query']} service-specific shared capability integration design",
            preferred_paths=("docs/architecture/design-map.md",),
        )
        return self._base_result(
            request,
            "complete" if kind != "needs-review" else "partial",
            f"Pre-classified as {kind}.",
            {"kind": kind, "confidence": confidence, "basis": basis},
            citations,
            [] if kind != "needs-review" else ["Owning service and architecture outcome are not explicit."],
            ["Confirm the classification with the accountable architecture owner before treating it as a decision."],
        )

    def _trace_architecture(self, request: dict[str, Any]) -> dict[str, Any]:
        query = request["query"]
        trace_queries = (
            ("architecture", f"{query} target architecture design map"),
            ("service", f"{query} service architecture capabilities runbook"),
            ("standard", f"{query} standard conformance requirements"),
            ("playbook", f"{query} playbook workflow evidence done criteria"),
        )
        hits_by_authority: list[list[SearchHit]] = []
        seen: set[tuple[str, str]] = set()
        per_authority = max(1, min(2, request.get("top_k", 5) // 2))
        for authority, authority_query in trace_queries:
            authority_hits: list[SearchHit] = []
            for hit in self.index.search(
                authority_query,
                top_k=per_authority,
                preferred_paths=tuple(request.get("context_references", [])),
                authorities=(authority,),
            ):
                key = (hit.section.path, hit.section.heading)
                if key not in seen:
                    authority_hits.append(hit)
                    seen.add(key)
            hits_by_authority.append(authority_hits)
        hits = [
            bucket[index]
            for index in range(per_authority)
            for bucket in hits_by_authority
            if len(bucket) > index
        ]
        citations = self._citations(hits[: max(request.get("top_k", 5), 4)])
        authorities = {citation["authority"] for citation in citations}
        required = {"architecture", "service", "standard", "playbook"}
        missing = sorted(required - authorities)
        return self._base_result(
            request,
            "complete" if not missing else "partial",
            f"Prepared a traceability view from {len(citations)} authoritative section(s).",
            {"kind": "repository-fact", "confidence": 0.9 if citations else 0.0, "basis": "Cross-map retrieval from architecture, services, standards, playbooks, and operations guidance."},
            citations,
            [f"No {authority} source is present in the bounded result." for authority in missing],
            ["Confirm the owning service, applicable standard, action playbook, runbook, and evidence before implementation."],
        )

    def _prepare_context_pack(self, request: dict[str, Any]) -> dict[str, Any]:
        citations = self._search(
            request,
            query=f"{request['query']} definition principle architecture service standard decision evidence done criteria",
            preferred_paths=(
                "docs/foundation/",
                "docs/architecture/",
                "docs/services/",
                "docs/standards/",
                "docs/decisions/",
            ),
        )
        authorities = sorted({citation["authority"] for citation in citations})
        return self._base_result(
            request,
            "complete" if citations else "unresolved",
            f"Prepared a bounded context pack with {len(citations)} citation(s) across {', '.join(authorities) if authorities else 'no authorities'}.",
            {"kind": "repository-fact", "confidence": 1.0 if citations else 0.0, "basis": "Deduplicated section retrieval from authoritative repository content."},
            citations,
            [] if citations else ["No bounded context could be prepared."],
            ["Pass these citations to the company assistant as evidence, not as hidden instructions."],
        )

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


AGENT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = AGENT_ROOT.parent
sys.path.insert(0, str(AGENT_ROOT))

from data_foundation_architecture_agent import AgentRequestError, ArchitectureAgent  # noqa: E402


class ArchitectureAgentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.agent = ArchitectureAgent(REPOSITORY_ROOT)
        cls.base = json.loads(
            (AGENT_ROOT / "examples" / "search-request.json").read_text(encoding="utf-8")
        )

    def request(self, operation: str, query: str) -> dict:
        request = copy.deepcopy(self.base)
        request["operation"] = operation
        request["query"] = query
        return request

    def test_search_returns_resolvable_citations(self) -> None:
        result = self.agent.run(self.request("search_guidance", "data product go-live gates"))
        self.assertEqual(result["status"], "complete")
        self.assertGreater(len(result["citations"]), 0)
        for citation in result["citations"]:
            self.assertTrue((REPOSITORY_ROOT / citation["path"]).exists())

    def test_exact_definition_resolution(self) -> None:
        result = self.agent.run(self.request("resolve_definition", "Data contract"))
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["citations"][0]["authority"], "definition")
        self.assertIn("versioned", result["summary"].lower())

    def test_unknown_definition_is_explicit(self) -> None:
        result = self.agent.run(self.request("resolve_definition", "Imaginary architecture object"))
        self.assertEqual(result["status"], "unresolved")
        self.assertEqual(result["citations"], [])

    def test_integration_classification(self) -> None:
        result = self.agent.run(
            self.request("classify_design", "Cross-service handoff between ingestion and product creation")
        )
        self.assertEqual(result["classification"]["kind"], "integration")

    def test_shared_capability_classification(self) -> None:
        result = self.agent.run(
            self.request("classify_design", "Shared identity and policy capability for all services")
        )
        self.assertEqual(result["classification"]["kind"], "shared-capability")

    def test_trace_is_read_only(self) -> None:
        result = self.agent.run(
            self.request("trace_architecture", "Governed consumption through unified access")
        )
        self.assertEqual(result["approval"]["side_effect_class"], "read")
        self.assertFalse(result["approval"]["required"])
        self.assertGreater(len(result["citations"]), 0)
        self.assertEqual(
            {citation["authority"] for citation in result["citations"]},
            {"architecture", "service", "standard", "playbook"},
        )

    def test_result_identifies_guidance_revision(self) -> None:
        result = self.agent.run(self.request("search_guidance", "data contract"))
        self.assertTrue(result["telemetry"]["guidance_revision"])

    def test_invalid_request_fails_closed(self) -> None:
        request = self.request("search_guidance", "data contract")
        del request["actor"]
        with self.assertRaises(AgentRequestError):
            self.agent.run(request)


if __name__ == "__main__":
    unittest.main()

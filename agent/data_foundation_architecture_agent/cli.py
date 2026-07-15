"""Command-line adapter for the read-only architecture agent."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .runtime import AgentRequestError, ArchitectureAgent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", type=Path, help="JSON request file")
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        request = json.loads(args.request.read_text(encoding="utf-8"))
        result = ArchitectureAgent(args.repository_root).run(request)
    except (OSError, json.JSONDecodeError, AgentRequestError, RuntimeError) as error:
        print(json.dumps({"status": "rejected", "error": str(error)}, indent=2))
        return 2

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

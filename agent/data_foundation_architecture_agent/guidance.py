"""Index and retrieve authoritative Markdown guidance by section."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


TOKEN = re.compile(r"[a-z0-9][a-z0-9_-]+")
HEADING = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "how", "in", "is", "it", "of", "on", "or", "that", "the", "this",
    "to", "use", "what", "when", "which", "with",
}


@dataclass(frozen=True)
class GuidanceSection:
    path: str
    heading: str
    text: str
    authority: str
    tokens: Counter[str]


@dataclass(frozen=True)
class SearchHit:
    section: GuidanceSection
    score: float


def tokenize(value: str) -> list[str]:
    return [token for token in TOKEN.findall(value.lower()) if token not in STOP_WORDS]


def clean_markdown(value: str) -> str:
    value = re.sub(r"```.*?```", " ", value, flags=re.DOTALL)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_~]", "", value)
    value = value.replace("|", " ")
    return re.sub(r"\s+", " ", value).strip()


def authority_for(path: str) -> str:
    prefix = path.split("/", 2)[1] if path.startswith("docs/") and "/" in path else ""
    return {
        "foundation": "definition",
        "architecture": "architecture",
        "services": "service",
        "standards": "standard",
        "decisions": "decision",
        "playbooks": "playbook",
        "delivery-templates": "template",
        "assessments": "assessment",
    }.get(prefix, "other")


class GuidanceIndex:
    def __init__(self, repository_root: Path):
        self.repository_root = repository_root.resolve()
        self.sections = self._load_sections()
        self.document_frequency = self._document_frequency()

    def _load_sections(self) -> list[GuidanceSection]:
        sections: list[GuidanceSection] = []
        for path in sorted((self.repository_root / "docs").rglob("*.md")):
            relative = path.relative_to(self.repository_root).as_posix()
            sections.extend(self._parse_page(relative, path.read_text(encoding="utf-8")))
        return sections

    def _parse_page(self, relative: str, content: str) -> list[GuidanceSection]:
        page_title = Path(relative).stem.replace("-", " ").title()
        current_heading = page_title
        lines: list[str] = []
        parsed: list[GuidanceSection] = []
        in_fence = False

        def append_section() -> None:
            text = clean_markdown("\n".join(lines))
            if text:
                combined = f"{current_heading} {text}"
                parsed.append(
                    GuidanceSection(
                        path=relative,
                        heading=clean_markdown(current_heading),
                        text=text,
                        authority=authority_for(relative),
                        tokens=Counter(tokenize(combined)),
                    )
                )

        for line in content.splitlines():
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = HEADING.match(line)
            if match:
                append_section()
                current_heading = match.group(2)
                lines = []
            else:
                lines.append(line)
        append_section()
        return parsed

    def _document_frequency(self) -> Counter[str]:
        frequency: Counter[str] = Counter()
        for section in self.sections:
            frequency.update(section.tokens.keys())
        return frequency

    def search(
        self,
        query: str,
        top_k: int = 5,
        preferred_paths: tuple[str, ...] = (),
        authorities: tuple[str, ...] = (),
    ) -> list[SearchHit]:
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        total = max(len(self.sections), 1)
        phrase = clean_markdown(query).lower()
        hits: list[SearchHit] = []
        for section in self.sections:
            if authorities and section.authority not in authorities:
                continue
            score = 0.0
            heading_tokens = set(tokenize(section.heading))
            for token in query_tokens:
                count = section.tokens.get(token, 0)
                if not count:
                    continue
                inverse_frequency = math.log((total + 1) / (self.document_frequency[token] + 1)) + 1
                score += (1 + math.log(count)) * inverse_frequency
                if token in heading_tokens:
                    score += 1.5
            searchable = f"{section.heading} {section.text}".lower()
            if len(phrase) > 3 and phrase in searchable:
                score += 4.0
            if any(section.path.startswith(path) or path in section.path for path in preferred_paths):
                score += 2.0
            if score > 0:
                hits.append(SearchHit(section=section, score=round(score, 4)))

        hits.sort(key=lambda hit: (-hit.score, hit.section.path, hit.section.heading))
        return hits[:top_k]

    def definition(self, term: str) -> tuple[str, str] | None:
        glossary = self.repository_root / "docs" / "foundation" / "glossary.md"
        requested = clean_markdown(term).casefold()
        for line in glossary.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [clean_markdown(cell) for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0].casefold() == requested:
                return cells[0], cells[1]
        return None

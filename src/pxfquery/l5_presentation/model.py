from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from pxfquery.version import __version__


@dataclass
class PxFQueryAnswer:
    """Human-facing answer object built only from L4 evidence."""

    question: str
    interpreted_question: str
    headline: str
    summary: str
    summary_source: str = ""
    biological_results: list[dict[str, Any]] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)
    limitations: list[str] = field(default_factory=list)
    tables: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    figures: list[dict[str, Any]] = field(default_factory=list)
    html: str | None = None
    mcp: dict[str, Any] | None = None
    rendering_contract: dict[str, Any] = field(default_factory=dict)
    structured_result: dict[str, Any] = field(default_factory=dict)
    engineering: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def trace(self) -> list[dict[str, Any]]:
        return self.engineering.get("trace", [])

    def __getitem__(self, key: str) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        return self.structured_result[key]

    def __str__(self) -> str:
        return self._llm_answer_text()

    def _llm_answer_text(self) -> str:
        if self.summary_source != "l4.llm_synthesis.biological_summary" or not str(self.summary or "").strip():
            raise RuntimeError("L5 default answer requires L4 LLM biological_summary.")
        return "\n".join(
            [
                "Answer",
                str(self.summary).strip(),
                "",
                "=======",
                f"Analysis source: pxfquery {__version__}",
                'Evidence: inspect `answer.tables["route_summary"]` and `answer.tables["route_function_results"]`.',
                "Figures: call `pxf.tl.figures(qdata, output_dir=...)` after `pxf.tl.answer(qdata)`.",
            ]
        )

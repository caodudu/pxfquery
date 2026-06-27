from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class PxFQueryAnswer:
    """Human-facing query answer with structured evidence kept secondary."""

    question: str
    interpreted_question: str
    biological_results: list[dict[str, Any]] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)
    biological_interpretation: str = ""
    limitations: list[str] = field(default_factory=list)
    structured_result: dict[str, Any] = field(default_factory=dict)
    engineering: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def diagnostics(self) -> dict[str, Any]:
        return self.engineering.get("diagnostics", {})

    @property
    def trace(self) -> list[dict[str, Any]]:
        return self.engineering.get("trace", [])

    def __getitem__(self, key: str) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        return self.structured_result[key]

    def __str__(self) -> str:
        lines = [
            "PxFquery answer",
            "",
            f"Question understood as: {self.interpreted_question}",
            "",
            "Biological results:",
        ]
        if self.biological_results:
            for item in self.biological_results[:5]:
                label = item.get("label") or item.get("name") or item.get("id") or "result"
                score = item.get("score")
                rank = item.get("rank")
                prefix = f"{rank}. " if rank is not None else "- "
                suffix = f" (score={score})" if score is not None else ""
                lines.append(f"{prefix}{label}{suffix}")
        else:
            lines.append("- No biological result is claimed yet.")
        if self.evidence:
            lines.extend(["", "Evidence:"])
            for key, value in self.evidence.items():
                lines.append(f"- {key}: {value}")
        if self.biological_interpretation:
            lines.extend(["", "Interpretation:", self.biological_interpretation])
        if self.limitations:
            lines.extend(["", "Limitations:"])
            lines.extend(f"- {item}" for item in self.limitations)
        return "\n".join(lines)

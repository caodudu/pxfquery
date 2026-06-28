from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class QueryIntent:
    """Structured biomedical intent produced by the intent parser."""

    raw_query: str
    normalized_query: str
    query_type: str
    bio_context: str | None = None
    pert_desc: str | None = None
    pert_class: str | None = None
    genetic_modality: str | None = None
    function_desc: str | None = None
    activate: list[str] = field(default_factory=list)
    suppress: list[str] = field(default_factory=list)
    constraints: list[dict[str, Any]] = field(default_factory=list)
    forward_result_scope: str = "open"
    top_n: int | None = None
    extracted_phrases: dict[str, Any] = field(default_factory=dict)
    ambiguity_flags: list[str] = field(default_factory=list)
    missing_fields: list[str] = field(default_factory=list)
    parse_confidence: float = 0.0
    parse_method: str = "llm"
    parser_notes: list[str] = field(default_factory=list)
    provider_evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_resolver_intent(self) -> dict[str, Any]:
        return {
            "query_type": self.query_type,
            "bio_context": self.bio_context,
            "pert_desc": self.pert_desc,
            "pert_class": self.pert_class,
            "function_desc": self.function_desc,
            "activate": list(self.activate),
            "suppress": list(self.suppress),
            "constraints": list(self.constraints),
            "forward_result_scope": self.forward_result_scope,
            "top_n": self.top_n,
        }

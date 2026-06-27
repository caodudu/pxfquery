from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class QueryIntent:
    """Structured biomedical intent produced by the natural-language layer."""

    raw_query: str
    direction: str
    perturbation_type: str
    perturbation_identity: str | None = None
    biological_context: str | None = None
    function_target: str | None = None
    ambiguity_flags: list[str] = field(default_factory=list)
    missing_fields: list[str] = field(default_factory=list)
    parse_confidence: float = 0.0
    parse_method: str = "generic_biomedical_surface_parse"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

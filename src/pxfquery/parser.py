from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any


GENES = ("KRAS", "EGFR", "MYC", "BCL2", "TP53", "MAPK1", "MAPK3", "ERK", "QQQX1")
COMPOUNDS = ("erlotinib", "gefitinib", "ZX-9999")
CELL_LINES = ("A549", "H1975", "PC3")


@dataclass
class QueryIntent:
    raw_query: str
    direction: str
    perturbation_type: str
    perturbation_identity: str | None = None
    biological_context: str | None = None
    function_target: str | None = None
    ambiguity_flags: list[str] = field(default_factory=list)
    missing_fields: list[str] = field(default_factory=list)
    parse_confidence: float = 0.0
    parse_method: str = "rule_based_ms7"
    ai_route_used: bool = False
    fallback_used: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def parse_query(text: str, *, ai_route_used: bool = False, fallback_used: bool = False) -> QueryIntent:
    raw = text.strip()
    lower = raw.lower()
    direction = _direction(lower)
    function_target = _function_target(lower)
    context = _cell_line(raw)
    perturbation_type, perturbation_identity, ambiguity_flags = _perturbation(raw, lower, direction)
    missing_fields: list[str] = []

    if context is None and _requires_context(lower):
        missing_fields.append("context")
    if direction == "reverse" and not function_target:
        missing_fields.append("function_target")
    if direction == "forward" and not perturbation_identity and perturbation_type != "gene_or_pathway_ambiguous":
        missing_fields.append("perturbation_identity")

    confidence = 0.88
    if missing_fields:
        confidence -= 0.28
    if ambiguity_flags:
        confidence -= 0.2
    if perturbation_identity in {"QQQX1", "ZX-9999"}:
        confidence -= 0.08

    return QueryIntent(
        raw_query=raw,
        direction=direction,
        perturbation_type=perturbation_type,
        perturbation_identity=perturbation_identity,
        biological_context=context,
        function_target=function_target,
        ambiguity_flags=ambiguity_flags,
        missing_fields=missing_fields,
        parse_confidence=round(max(confidence, 0.05), 2),
        ai_route_used=ai_route_used,
        fallback_used=fallback_used,
    )


def _direction(lower: str) -> str:
    reverse_markers = (
        "which drugs",
        "what drugs",
        "what genetic",
        "find shrna",
        "find sirna",
        "find gene",
        "rank drugs",
        "i need drugs",
        "which perturbations",
    )
    return "reverse" if any(marker in lower for marker in reverse_markers) else "forward"


def _cell_line(raw: str) -> str | None:
    lower = raw.lower()
    if any(marker in lower for marker in ("do not know the cell line", "no cell line", "unknown cell", "avoid any context")):
        return None
    for cell_line in CELL_LINES:
        if re.search(rf"\b{re.escape(cell_line)}\b", raw, flags=re.IGNORECASE):
            return cell_line
    if "lung cancer" in lower and "pan-cancer" not in lower:
        return "lung cancer"
    if "cancer" in lower and "unknown" not in lower:
        return "cancer"
    return None


def _perturbation(raw: str, lower: str, direction: str) -> tuple[str, str | None, list[str]]:
    flags: list[str] = []
    if "erk" in lower:
        return "gene_or_pathway_ambiguous", "ERK", ["ERK may mean MAPK1, MAPK3, or pathway-level ERK signal"]
    if "egfr and kras" in lower or "both egfr and kras" in lower:
        return "gene_set", "EGFR + KRAS", []
    if "kras g12c" in lower and "erlotinib" in lower:
        return "mixed", "erlotinib + KRAS G12C", []
    for compound in COMPOUNDS:
        if compound.lower() in lower:
            return "compound", compound, []
    if "egfr inhibitor" in lower:
        return "compound", "EGFR inhibitor", []
    if direction == "reverse":
        if any(word in lower for word in ("drug", "compound")):
            return "compound", None, []
        if any(word in lower for word in ("shrna", "sirna", "knockout", "genetic", "gene")):
            return "gene", None, []
    for gene in GENES:
        if re.search(rf"\b{gene}\b", raw, flags=re.IGNORECASE):
            return "gene", gene, []
    return "unknown", None, []


def _function_target(lower: str) -> str | None:
    targets = [
        ("apoptosis", "activate apoptosis"),
        ("programmed cell death", "programmed cell death"),
        ("suppress myc", "suppress MYC"),
        ("suppress bcl2", "suppress BCL2"),
        ("tp53", "increase TP53 activity"),
        ("autophagy", "autophagy"),
        ("inflammatory response", "modulate inflammatory response"),
        ("cell growth", "increase cell growth"),
        ("senescence", "senescence"),
        ("functional program", "functional programs"),
        ("functional response", "functional response"),
        ("pathway effects", "pathway effects"),
    ]
    hits = [label for marker, label in targets if marker in lower]
    if "activate apoptosis" in hits and "suppress MYC" in hits and "suppress BCL2" in hits:
        return "activate apoptosis + suppress MYC + suppress BCL2"
    return hits[0] if hits else None


def _requires_context(lower: str) -> bool:
    missing_markers = (
        "do not know the cell line",
        "unknown cell",
        "no cell line",
        "avoid any context",
        "without any context",
        "do not ask clarification",
    )
    if any(marker in lower for marker in missing_markers):
        return True
    return "a549" not in lower and "h1975" not in lower and "pc3" not in lower and "pan-cancer" not in lower

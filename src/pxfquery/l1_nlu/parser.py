import re

from pxfquery.l1_nlu.schema import QueryIntent


def parse_query(text: str) -> QueryIntent:
    raw = text.strip()
    lower = raw.lower()
    direction = _direction(lower)
    perturbation_type = _perturbation_type(lower, direction)
    perturbation_identity = _perturbation_phrase(raw, lower, direction)
    biological_context = _context_phrase(raw, lower)
    function_target = _function_phrase(raw, lower, direction)
    missing_fields = _missing_fields(direction, perturbation_type, perturbation_identity, function_target)
    confidence = 0.72 - 0.12 * len(missing_fields)
    return QueryIntent(
        raw_query=raw,
        direction=direction,
        perturbation_type=perturbation_type,
        perturbation_identity=perturbation_identity,
        biological_context=biological_context,
        function_target=function_target,
        ambiguity_flags=[],
        missing_fields=missing_fields,
        parse_confidence=round(max(confidence, 0.1), 2),
        parse_method="generic_biomedical_surface_parse",
    )


def _direction(lower: str) -> str:
    reverse_cues = (
        "which ",
        "what ",
        "find ",
        "rank ",
        "identify ",
        "search for ",
        "i need ",
        "give me ",
    )
    effect_cues = (
        "what happens",
        "how does",
        "effect of",
        "response to",
        "after ",
        "when ",
    )
    if any(cue in lower for cue in effect_cues):
        return "forward"
    if any(cue in lower for cue in reverse_cues):
        return "reverse"
    return "unknown"


def _perturbation_type(lower: str, direction: str) -> str:
    drug_cues = ("drug", "compound", "small molecule", "inhibitor", "agonist", "antagonist", "treatment", "treating")
    genetic_cues = ("gene", "genetic", "knockdown", "knockout", "crispr", "sirna", "shrna", "overexpression", "orf")
    has_drug = any(cue in lower for cue in drug_cues)
    has_genetic = any(cue in lower for cue in genetic_cues)
    if has_drug and has_genetic:
        return "mixed"
    if has_drug:
        return "compound"
    if has_genetic:
        return "gene"
    if direction == "reverse":
        return "perturbation"
    return "unknown"


def _perturbation_phrase(raw: str, lower: str, direction: str) -> str | None:
    if direction == "reverse":
        return None
    patterns = (
        r"\bif\s+(?:I\s+)?(?:knock\s+down|knockdown|knock\s+out|knockout|overexpress|perturb)\s+(.+?)\s+in\b",
        r"\b(?:knock\s+down|knockdown|knock\s+out|knockout|overexpress|perturb)\s+(.+?)\s+in\b",
        r"\bafter\s+(.+?)\s+in\b",
        r"\bafter\s+(.+?)$",
        r"\bwhen\s+(.+?)\s+in\b",
        r"\bwith\s+(.+?)\s+in\b",
        r"\bresponse\s+to\s+(.+?)\s+in\b",
        r"\beffect\s+of\s+(.+?)\s+in\b",
        r"\bto\s+(.+?)\s+in\b",
        r"\bhow does\s+(.+?)\s+(?:change|affect|alter)\b",
    )
    for pattern in patterns:
        match = re.search(pattern, raw, flags=re.IGNORECASE)
        if match:
            return _clean_phrase(match.group(1))
    return None


def _context_phrase(raw: str, lower: str) -> str | None:
    patterns = (
        r"\bin\s+(.+?)\s+cells?\b",
        r"\bin\s+(.+?)\s+models?\b",
        r"\bin\s+(.+?)\s+cancer\b",
        r"\bfor\s+(.+?)\s+models?\b",
        r"\bfor\s+(.+?)\s+cancer\b",
    )
    for pattern in patterns:
        match = re.search(pattern, raw, flags=re.IGNORECASE)
        if match:
            phrase = _clean_phrase(match.group(1))
            suffix = " cancer" if pattern.endswith(r"\s+cancer\b") and not phrase.lower().endswith("cancer") else ""
            return f"{phrase}{suffix}"
    return None


def _function_phrase(raw: str, lower: str, direction: str) -> str | None:
    patterns = (
        r"\b(?:activate|activates|induce|induces|increase|increases|suppress|suppresses|decrease|decreases|inhibit|inhibits|modulate|modulates)\s+(.+?)\s+in\b",
        r"\b(?:activate|activates|induce|induces|increase|increases|suppress|suppresses|decrease|decreases|inhibit|inhibits|modulate|modulates)\s+(.+?)$",
        r"\bfunctional\s+(?:programs?|response|effects?)\b",
    )
    for pattern in patterns:
        match = re.search(pattern, raw, flags=re.IGNORECASE)
        if match and match.groups():
            verb = raw[match.start() : match.end()].split()[0]
            return _clean_phrase(f"{verb} {match.group(1)}")
        if match:
            return "functional programs"
    return None


def _missing_fields(direction: str, perturbation_type: str, perturbation_identity: str | None, function_target: str | None) -> list[str]:
    missing: list[str] = []
    if direction == "unknown":
        missing.append("direction")
    if direction == "forward" and perturbation_identity is None:
        missing.append("perturbation")
    if direction == "reverse" and function_target is None:
        missing.append("function")
    if perturbation_type == "unknown":
        missing.append("perturbation_type")
    return missing


def _clean_phrase(value: str) -> str:
    cleaned = " ".join(value.strip(" ?.,;:").split())
    stop_prefixes = ("the ", "a ", "an ")
    for prefix in stop_prefixes:
        if cleaned.lower().startswith(prefix):
            return cleaned[len(prefix) :]
    return cleaned

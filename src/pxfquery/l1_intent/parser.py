from __future__ import annotations

from typing import Any

from pxfquery.l1_intent.schema import QueryIntent


class IntentBackendNotConfigured(RuntimeError):
    """Raised when intent parsing is called without a registered LLM provider."""


class IntentBackendError(RuntimeError):
    """Raised when provider output cannot be accepted as a valid intent."""


GENETIC_MODALITIES = {
    "rnai",
    "shrna",
    "crispr",
    "knockdown",
    "knockout",
    "overexpression",
    "lof",
    "gof",
    "unknown",
    None,
}

FORWARD_RESULT_SCOPES = {"activated_only", "suppressed_only", "both", "open"}
CONSTRAINT_DIRECTIONS = {"activate", "suppress"}

FORBIDDEN_L1_OUTPUT_KEYS = {
    "answer",
    "biological_answer",
    "candidates",
    "candidate_perturbations",
    "drugs",
    "genes",
    "scores",
    "score",
    "evidence",
    "citations",
    "route_plan",
    "matrix_hits",
    "used_cell",
    "used_perturbation",
}

BIO_CONTEXT_HINT_WORDS = {
    "cell",
    "cells",
    "cell line",
    "cancer",
    "tumor",
    "tumour",
    "carcinoma",
    "melanoma",
    "leukemia",
    "lymphoma",
    "sarcoma",
    "models",
    "model",
    "tissue",
    "organ",
    "disease",
    "patient",
    "primary",
}

def parse_intent(text: str, *, provider: Any | None = None) -> QueryIntent:
    if provider is None:
        raise IntentBackendNotConfigured(
            "Intent parsing requires a registered LLM provider. "
            "Configure pxf.settings.use_diygateway(...) or pxf.settings.use_deepseek(...) before pxf.pp.parse(qdata)."
        )
    if not hasattr(provider, "parse_intent"):
        raise TypeError("Intent provider must expose parse_intent(text, schema=...)")
    payload, evidence = provider.parse_intent(
        text,
        schema=intent_schema(),
        validator=lambda candidate: validate_intent_payload(text, candidate),
    )
    return validate_intent_payload(text, payload, provider_evidence=evidence)


def intent_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "required": [
            "query_type",
            "bio_context",
            "pert_desc",
            "pert_class",
            "genetic_modality",
            "function_desc",
            "activate",
            "suppress",
            "constraints",
            "forward_result_scope",
            "top_n",
        ],
        "properties": {
            "query_type": {"enum": ["forward", "reverse"]},
            "bio_context": {"type": ["string", "null"]},
            "pert_desc": {"type": ["string", "null"]},
            "pert_class": {"enum": ["genetic", "drug", None]},
            "genetic_modality": {
                "enum": [
                    "rnai",
                    "shrna",
                    "crispr",
                    "knockdown",
                    "knockout",
                    "overexpression",
                    "lof",
                    "gof",
                    "unknown",
                    None,
                ]
            },
            "function_desc": {"type": ["string", "null"]},
            "activate": {"type": "array", "items": {"type": "string"}},
            "suppress": {"type": "array", "items": {"type": "string"}},
            "constraints": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["term", "avoid_direction"],
                    "properties": {
                        "term": {"type": "string"},
                        "avoid_direction": {"enum": ["activate", "suppress"]},
                    },
                },
            },
            "forward_result_scope": {"enum": ["activated_only", "suppressed_only", "both", "open"]},
            "top_n": {"type": ["integer", "null"]},
            "normalized_query": {"type": "string"},
            "extracted_phrases": {"type": "object"},
            "ambiguity_flags": {"type": "array", "items": {"type": "string"}},
            "missing_fields": {"type": "array", "items": {"type": "string"}},
            "parse_confidence": {"type": "number"},
            "parse_method": {"type": "string"},
            "parser_notes": {"type": "array", "items": {"type": "string"}},
        },
    }


def validate_intent_payload(
    raw_query: str,
    payload: Any,
    *,
    provider_evidence: dict[str, Any] | None = None,
) -> QueryIntent:
    if not isinstance(payload, dict):
        raise IntentBackendError("Intent provider returned a non-object payload")

    forbidden = sorted(key for key in payload if key in FORBIDDEN_L1_OUTPUT_KEYS)
    if forbidden:
        raise IntentBackendError(f"Intent provider included non-L1 output keys: {forbidden}")

    required = intent_schema()["required"]
    missing_keys = [key for key in required if key not in payload]
    if missing_keys:
        raise IntentBackendError(f"Intent provider payload is missing required keys: {missing_keys}")

    query_type = payload["query_type"]
    if query_type not in {"forward", "reverse"}:
        raise IntentBackendError(f"Intent provider field query_type has invalid value: {query_type!r}")

    pert_class = payload["pert_class"]
    if pert_class not in {"genetic", "drug", None}:
        raise IntentBackendError(f"Intent provider field pert_class has invalid value: {pert_class!r}")

    genetic_modality = payload["genetic_modality"]
    if genetic_modality not in GENETIC_MODALITIES:
        raise IntentBackendError(
            f"Intent provider field genetic_modality has invalid value: {genetic_modality!r}"
        )

    _validate_nullable_string(payload, "bio_context")
    _validate_nullable_string(payload, "pert_desc")
    _validate_nullable_string(payload, "function_desc")
    _validate_string_list(payload, "activate")
    _validate_string_list(payload, "suppress")
    _validate_constraints(payload, "constraints")
    if payload["forward_result_scope"] not in FORWARD_RESULT_SCOPES:
        raise IntentBackendError(
            f"Intent provider field forward_result_scope has invalid value: {payload['forward_result_scope']!r}"
        )
    if payload["top_n"] is not None and not isinstance(payload["top_n"], int):
        raise IntentBackendError("Intent provider field top_n must be an integer or null")

    _validate_intent_consistency(raw_query, payload)

    extracted_phrases = payload.get("extracted_phrases") or {}
    if not isinstance(extracted_phrases, dict):
        raise IntentBackendError("Intent provider field extracted_phrases must be an object when provided")

    ambiguity_flags = _optional_string_list(payload, "ambiguity_flags")
    missing_fields = _optional_string_list(payload, "missing_fields")
    parser_notes = _optional_string_list(payload, "parser_notes")

    parse_confidence = payload.get("parse_confidence", 0.0)
    if not isinstance(parse_confidence, (int, float)):
        raise IntentBackendError("Intent provider field parse_confidence must be numeric when provided")

    return QueryIntent(
        raw_query=raw_query.strip(),
        normalized_query=str(payload.get("normalized_query") or raw_query.strip()),
        query_type=query_type,
        bio_context=payload["bio_context"],
        pert_desc=payload["pert_desc"],
        pert_class=pert_class,
        genetic_modality=genetic_modality,
        function_desc=payload["function_desc"],
        activate=list(payload["activate"]),
        suppress=list(payload["suppress"]),
        constraints=list(payload["constraints"]),
        forward_result_scope=payload["forward_result_scope"],
        top_n=payload["top_n"],
        extracted_phrases=extracted_phrases,
        ambiguity_flags=ambiguity_flags,
        missing_fields=missing_fields,
        parse_confidence=float(parse_confidence),
        parse_method=str(payload.get("parse_method") or "llm"),
        parser_notes=parser_notes,
        provider_evidence=provider_evidence or {},
    )


def _validate_nullable_string(payload: dict[str, Any], key: str) -> None:
    value = payload[key]
    if value is not None and not isinstance(value, str):
        raise IntentBackendError(f"Intent provider field {key} must be a string or null")


def _validate_string_list(payload: dict[str, Any], key: str) -> None:
    value = payload[key]
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise IntentBackendError(f"Intent provider field {key} must be a string list")


def _optional_string_list(payload: dict[str, Any], key: str) -> list[str]:
    value = payload.get(key) or []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise IntentBackendError(f"Intent provider field {key} must be a string list when provided")
    return value


def _validate_constraints(payload: dict[str, Any], key: str) -> None:
    value = payload[key]
    if not isinstance(value, list):
        raise IntentBackendError(f"Intent provider field {key} must be a list")
    for item in value:
        if not isinstance(item, dict):
            raise IntentBackendError(f"Intent provider field {key} items must be objects")
        term = item.get("term")
        avoid_direction = item.get("avoid_direction")
        if not isinstance(term, str) or not term.strip():
            raise IntentBackendError(f"Intent provider field {key}.term must be a non-empty string")
        if avoid_direction not in CONSTRAINT_DIRECTIONS:
            raise IntentBackendError(
                f"Intent provider field {key}.avoid_direction has invalid value: {avoid_direction!r}"
            )


def _validate_intent_consistency(raw_query: str, payload: dict[str, Any]) -> None:
    del raw_query
    query_type = payload["query_type"]
    pert_desc = _clean(payload.get("pert_desc"))
    pert_class = payload["pert_class"]
    genetic_modality = payload["genetic_modality"]
    function_desc = _clean(payload.get("function_desc"))
    activate = payload.get("activate") or []
    suppress = payload.get("suppress") or []

    if payload.get("bio_context") and _bio_context_is_only_function_target(payload):
        raise IntentBackendError(
            "Intent consistency conflict: bio_context contains only functional target wording. "
            "Do not put pathway/function/cell-state targets in bio_context unless the user also gave a real cell, "
            "tissue, disease, organ, or model context."
        )

    if pert_class != "genetic" and genetic_modality not in {None, "unknown"}:
        raise IntentBackendError(
            "Intent consistency conflict: genetic_modality is set but pert_class is not genetic. "
            "Re-evaluate pert_class and genetic_modality."
        )

    if query_type == "reverse" and pert_desc and not (function_desc or activate or suppress):
        raise IntentBackendError(
            "Intent consistency conflict: query_type is reverse, but the payload contains a concrete perturbation "
            "description and no functional target. If the user asks for functional effects of a named perturbation, "
            "the corrected query_type should usually be forward."
        )

    if query_type == "reverse" and not (function_desc or activate or suppress):
        raise IntentBackendError(
            "Intent consistency conflict: reverse queries must include at least one functional target in "
            "function_desc, activate, or suppress. Do not rely on raw_query for downstream functional routing."
        )

    if query_type == "forward" and not pert_desc:
        raise IntentBackendError(
            "Intent consistency conflict: query_type is forward but pert_desc is empty. "
            "Forward queries need the perturbation described by the user, or missing_fields must explain why it is absent."
        )

    if query_type == "forward" and pert_desc:
        operation_terms = [
            term
            for term in [*activate, *suppress]
            if _forward_term_describes_perturbation(pert_desc, term)
        ]
        if operation_terms:
            raise IntentBackendError(
                "Intent consistency conflict: activate/suppress fields are only for functional targets. "
                f"These terms describe the named perturbation operation instead: {operation_terms}. "
                "Encode perturbation operation using genetic_modality and forward_result_scope, and leave "
                "activate/suppress empty unless the user named functional targets."
            )


def _clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _bio_context_is_only_function_target(payload: dict[str, Any]) -> bool:
    bio = _normalize(payload.get("bio_context"))
    if not bio or any(word in bio for word in BIO_CONTEXT_HINT_WORDS):
        return False
    terms = [
        payload.get("function_desc"),
        *(payload.get("activate") or []),
        *(payload.get("suppress") or []),
        *[
            item.get("term")
            for item in (payload.get("constraints") or [])
            if isinstance(item, dict)
        ],
    ]
    return any(_overlaps(str(term or ""), bio) for term in terms)


def _overlaps(term: str, haystack: str) -> bool:
    term_norm = _normalize(term)
    if not term_norm or not haystack:
        return False
    return term_norm in haystack or haystack in term_norm


def _forward_term_describes_perturbation(pert_desc: str, term: str) -> bool:
    term_norm = _normalize(term)
    pert_norm = _normalize(pert_desc)
    if not term_norm or not pert_norm:
        return False
    if term_norm == pert_norm or pert_norm in term_norm or term_norm in pert_norm:
        return True
    term_tokens = set(term_norm.split())
    pert_tokens = set(pert_norm.split())
    return bool(pert_tokens and pert_tokens <= term_tokens)


def _normalize(value: Any) -> str:
    return " ".join(str(value or "").lower().replace("_", " ").replace("-", " ").split())

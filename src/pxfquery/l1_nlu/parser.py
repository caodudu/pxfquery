from __future__ import annotations

from typing import Any

from pxfquery.l1_nlu.schema import QueryIntent


class NLUBackendNotConfigured(RuntimeError):
    """Raised when L1 is called without a real natural-language backend."""


class NLUBackendError(RuntimeError):
    """Raised when a backend response cannot be accepted as a valid L1 intent."""


def parse_query(text: str, *, backend: Any | None = None) -> QueryIntent:
    if backend is None:
        raise NLUBackendNotConfigured(
            "L1 natural-language parsing requires a configured LLM backend. "
            "Configure pxf.settings.use_diygateway(...) before pxf.pp.parse(qdata)."
        )
    if not hasattr(backend, "parse"):
        raise TypeError("L1 backend must expose parse(text, schema=...)")
    payload = backend.parse(text, schema=intent_schema())
    return validate_intent_payload(text, payload)


def intent_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "required": [
            "query_type",
            "bio_context",
            "pert_desc",
            "pert_class",
            "function_desc",
            "activate",
            "suppress",
            "top_n",
        ],
        "properties": {
            "query_type": {"enum": ["forward", "reverse"]},
            "bio_context": {"type": ["string", "null"]},
            "pert_desc": {"type": ["string", "null"]},
            "pert_class": {"enum": ["genetic", "drug", None]},
            "function_desc": {"type": ["string", "null"]},
            "activate": {"type": "array", "items": {"type": "string"}},
            "suppress": {"type": "array", "items": {"type": "string"}},
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


def validate_intent_payload(raw_query: str, payload: Any) -> QueryIntent:
    if not isinstance(payload, dict):
        raise NLUBackendError("L1 backend returned a non-object payload")
    required = intent_schema()["required"]
    missing_keys = [key for key in required if key not in payload]
    if missing_keys:
        raise NLUBackendError(f"L1 backend payload is missing required keys: {missing_keys}")

    query_type = payload["query_type"]
    if query_type not in {"forward", "reverse"}:
        raise NLUBackendError(f"L1 backend field query_type has invalid value: {query_type!r}")
    pert_class = payload["pert_class"]
    if pert_class not in {"genetic", "drug", None}:
        raise NLUBackendError(f"L1 backend field pert_class has invalid value: {pert_class!r}")

    _validate_nullable_string(payload, "bio_context")
    _validate_nullable_string(payload, "pert_desc")
    _validate_nullable_string(payload, "function_desc")
    _validate_string_list(payload, "activate")
    _validate_string_list(payload, "suppress")
    if payload["top_n"] is not None and not isinstance(payload["top_n"], int):
        raise NLUBackendError("L1 backend field top_n must be an integer or null")

    extracted_phrases = payload.get("extracted_phrases") or {}
    if not isinstance(extracted_phrases, dict):
        raise NLUBackendError("L1 backend field extracted_phrases must be an object when provided")
    ambiguity_flags = payload.get("ambiguity_flags") or []
    missing_fields = payload.get("missing_fields") or []
    parser_notes = payload.get("parser_notes") or []
    if not isinstance(ambiguity_flags, list) or not all(isinstance(item, str) for item in ambiguity_flags):
        raise NLUBackendError("L1 backend field ambiguity_flags must be a string list")
    if not isinstance(missing_fields, list) or not all(isinstance(item, str) for item in missing_fields):
        raise NLUBackendError("L1 backend field missing_fields must be a string list")
    if not isinstance(parser_notes, list) or not all(isinstance(item, str) for item in parser_notes):
        raise NLUBackendError("L1 backend field parser_notes must be a string list")

    parse_confidence = payload.get("parse_confidence", 0.0)
    if not isinstance(parse_confidence, (int, float)):
        raise NLUBackendError("L1 backend field parse_confidence must be numeric when provided")

    return QueryIntent(
        raw_query=raw_query.strip(),
        normalized_query=str(payload.get("normalized_query") or raw_query.strip()),
        query_type=query_type,
        bio_context=payload["bio_context"],
        pert_desc=payload["pert_desc"],
        pert_class=pert_class,
        function_desc=payload["function_desc"],
        activate=list(payload["activate"]),
        suppress=list(payload["suppress"]),
        top_n=payload["top_n"],
        extracted_phrases=extracted_phrases,
        ambiguity_flags=ambiguity_flags,
        missing_fields=missing_fields,
        parse_confidence=float(parse_confidence),
        parse_method=str(payload.get("parse_method") or "llm"),
        parser_notes=parser_notes,
    )


def _validate_nullable_string(payload: dict[str, Any], key: str) -> None:
    value = payload[key]
    if value is not None and not isinstance(value, str):
        raise NLUBackendError(f"L1 backend field {key} must be a string or null")


def _validate_string_list(payload: dict[str, Any], key: str) -> None:
    value = payload[key]
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise NLUBackendError(f"L1 backend field {key} must be a string list")

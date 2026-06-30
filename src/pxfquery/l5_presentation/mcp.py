from __future__ import annotations

import json
from typing import Any

from pxfquery.l5_presentation.model import PxFQueryAnswer


DEFAULT_MCP_RESULT_LIMIT = 8
DEFAULT_MCP_ROUTE_LIMIT = 8


def build_mcp_payload(answer: PxFQueryAnswer, *, detail: str = "compact", result_limit: int = DEFAULT_MCP_RESULT_LIMIT) -> dict:
    """Build an AI-product friendly MCP payload.

    Compact mode is intentionally small enough for tool-call responses. Full L4
    evidence remains available through detail="full".
    """

    full = detail == "full"
    payload = {
        "schema_version": "pxfquery-l5-mcp/v2",
        "detail": "full" if full else "compact",
        "question": answer.question,
        "answer": {
            "headline": answer.headline,
            "summary": answer.summary,
            "summary_source": answer.summary_source,
            "limitations": answer.limitations,
        },
        "ranked_results": _limit_rows(answer.tables.get("ranked_results"), result_limit),
        "route_summary": _limit_rows(answer.tables.get("route_summary"), DEFAULT_MCP_ROUTE_LIMIT),
        "evidence_contract": _evidence_contract(answer),
        "evidence_index": build_evidence_index(answer),
        "assistant_instruction": (
            "Use the supplied biological answer and compact evidence. Do not add candidates, "
            "change scores, invent citations, or upgrade weak/proxy/no-hit evidence."
        ),
    }
    if full:
        payload["tables"] = answer.tables
        payload["figure_specs"] = answer.figures
        payload["l4_evidence"] = answer.structured_result
        payload["assistant_instruction"] = (
            "Use the supplied L4 evidence and L5 rendering contract. Do not add candidates, "
            "change scores, invent citations, or upgrade weak/proxy/no-hit evidence."
        )
    return payload


def build_evidence_index(answer: PxFQueryAnswer) -> dict[str, Any]:
    tables = answer.tables or {}
    available_tables = [name for name, rows in tables.items() if rows]
    expected_tables = [
        "ranked_results",
        "route_summary",
        "route_function_results",
        "route_target_functions",
        "matrix_context",
        "claim_rules",
    ]
    available_layers = []
    dossier = answer.structured_result or {}
    for key, value in (dossier.get("evidence_layer") or {}).items():
        if value:
            available_layers.append(key)
    return {
        "available_tables": available_tables,
        "missing_tables": [name for name in expected_tables if name not in available_tables],
        "available_evidence_layers": available_layers,
        "ranked_result_count": len(tables.get("ranked_results") or []),
        "route_count": len(tables.get("route_summary") or []),
        "route_function_result_count": len(tables.get("route_function_results") or []),
        "route_target_function_count": len(tables.get("route_target_functions") or []),
        "full_evidence_available_with": 'detail="full"',
    }


def check_evidence_terms(answer: PxFQueryAnswer, terms: list[str] | tuple[str, ...], *, max_hits_per_term: int = 12) -> dict[str, Any]:
    searchable = _searchable_records(answer)
    results = []
    for term in terms:
        text = str(term or "").strip()
        needle = text.lower()
        hits = []
        if needle:
            for record in searchable:
                haystack = record["text"].lower()
                if needle in haystack:
                    hits.append({key: record[key] for key in ("source", "field", "label", "route_id", "cell", "direction") if record.get(key) is not None})
                    if len(hits) >= max_hits_per_term:
                        break
        results.append({"term": text, "present": bool(hits), "hits": hits})
    return {
        "schema_version": "pxfquery-mcp-evidence-terms/v1",
        "question": answer.question,
        "terms": results,
        "evidence_index": build_evidence_index(answer),
    }


def _evidence_contract(answer: PxFQueryAnswer) -> dict[str, Any]:
    contract = dict(answer.rendering_contract or {})
    contract["evidence"] = answer.evidence
    return contract


def _limit_rows(rows: list[dict[str, Any]] | None, limit: int) -> list[dict[str, Any]]:
    return list(rows or [])[: max(0, int(limit))]


def _searchable_records(answer: PxFQueryAnswer) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = [
        {
            "source": "answer",
            "field": "summary",
            "label": "answer.summary",
            "text": answer.summary or "",
        }
    ]
    for table_name in ("ranked_results", "route_summary", "route_function_results", "route_target_functions", "matrix_context", "claim_rules"):
        for row in answer.tables.get(table_name) or []:
            label = row.get("label") or row.get("function") or row.get("perturbation") or row.get("cell") or row.get("text") or table_name
            records.append(
                {
                    "source": table_name,
                    "field": "row",
                    "label": label,
                    "route_id": row.get("route_id"),
                    "cell": row.get("cell"),
                    "direction": row.get("direction"),
                    "text": json.dumps(row, ensure_ascii=False, sort_keys=True),
                }
            )
    return records

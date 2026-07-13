from __future__ import annotations

import copy
from typing import Any

from pxfquery.l5_presentation.figures import build_figure_specs
from pxfquery.l5_presentation.mcp import build_mcp_payload
from pxfquery.l5_presentation.model import PxFQueryAnswer
from pxfquery.l5_presentation.report import render_html_answer
from pxfquery.l5_presentation.tables import build_tables


def build_answer(question: str, structured: dict[str, Any], *, mode: str = "python") -> PxFQueryAnswer:
    dossier = _as_dossier(structured)
    if dossier.get("schema_version") != "l4-evidence-dossier/v1":
        raise ValueError("L5 expects an L4 evidence dossier; call pxf.tl.assemble(qdata) before pxf.tl.answer(qdata)")

    basis = dossier.get("claim_basis") or {}
    evidence_layer = dossier.get("evidence_layer") or {}
    intent = evidence_layer.get("intent_evidence") or {}
    route = evidence_layer.get("route_evidence") or {}
    matrix = evidence_layer.get("matrix_evidence") or {}
    synthesis = evidence_layer.get("llm_synthesis") or {}
    uncertainty = dossier.get("uncertainty_layer") or {}
    tables = build_tables(dossier)
    summary = _resolve_unnamed_compound_summary(_summary(basis, synthesis), tables)
    structured_result = _resolve_unnamed_compound_structured_result(dossier, tables)
    figures = build_figure_specs(dossier)
    limitations = _limitations(dossier)
    contract = _rendering_contract(dossier, mode)

    answer = PxFQueryAnswer(
        question=question,
        interpreted_question=_interpreted_question(intent, matrix),
        headline=_headline(basis),
        summary=summary,
        summary_source=_summary_source(basis, synthesis),
        biological_results=tables["ranked_results"],
        evidence=_evidence(dossier, route, matrix, synthesis),
        limitations=limitations,
        tables=tables,
        figures=figures,
        rendering_contract=contract,
        structured_result=structured_result,
        engineering={
            "dossier_status": dossier.get("dossier_status"),
            "confidence": uncertainty.get("confidence"),
            "trace": _trace(dossier),
        },
    )
    if mode == "html":
        answer.html = render_html_answer(answer)
    if mode == "mcp":
        answer.mcp = build_mcp_payload(answer)
    return answer


def _as_dossier(structured: dict[str, Any]) -> dict[str, Any]:
    if structured.get("schema_version") == "l4-evidence-dossier/v1":
        return structured
    nested = structured.get("evidence_dossier")
    return nested if isinstance(nested, dict) else structured


def _headline(basis: dict[str, Any]) -> str:
    return "Biological answer"


def _summary(basis: dict[str, Any], synthesis: dict[str, Any]) -> str:
    biological_summary = synthesis.get("biological_summary") or synthesis.get("summary")
    if biological_summary:
        return str(biological_summary)
    return ""


def _resolve_unnamed_compound_summary(summary: str, tables: dict[str, list[dict[str, Any]]]) -> str:
    if not summary or "unnamed compound" not in summary.lower():
        return summary
    ranked = tables.get("ranked_results") or []
    top_label = ""
    for row in ranked:
        label = str(row.get("label") or "").strip()
        if label and label != "Unnamed compound":
            top_label = label
            break
    if not top_label:
        return summary.replace("unnamed compound candidate", "BRD-labeled compound candidate").replace("Unnamed compound candidate", "BRD-labeled compound candidate")
    replacements = {
        "The unnamed compound candidate (rank 1)": top_label,
        "the unnamed compound candidate (rank 1)": top_label,
        "The unnamed compound candidate": top_label,
        "the unnamed compound candidate": top_label,
        "An unnamed compound candidate": top_label,
        "an unnamed compound candidate": top_label,
        "Unnamed compound candidate": top_label,
        "unnamed compound candidate": top_label,
    }
    text = summary
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _resolve_unnamed_compound_structured_result(dossier: dict[str, Any], tables: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    top_label = _top_resolved_candidate_label(tables)
    replacement = top_label or "BRD-labeled compound candidate"
    return _replace_unnamed_compound_strings(copy.deepcopy(dossier), replacement)


def _top_resolved_candidate_label(tables: dict[str, list[dict[str, Any]]]) -> str:
    for row in tables.get("ranked_results") or []:
        label = str(row.get("label") or "").strip()
        if label and label != "Unnamed compound":
            return label
    return ""


def _replace_unnamed_compound_strings(value: Any, replacement: str) -> Any:
    if isinstance(value, dict):
        return {key: _replace_unnamed_compound_strings(item, replacement) for key, item in value.items()}
    if isinstance(value, list):
        return [_replace_unnamed_compound_strings(item, replacement) for item in value]
    if not isinstance(value, str) or "unnamed compound" not in value.lower():
        return value
    text = value
    replacements = {
        "The unnamed compound candidate (rank 1)": replacement,
        "the unnamed compound candidate (rank 1)": replacement,
        "The unnamed compound candidate": replacement,
        "the unnamed compound candidate": replacement,
        "An unnamed compound candidate": replacement,
        "an unnamed compound candidate": replacement,
        "Unnamed compound candidate": replacement,
        "unnamed compound candidate": replacement,
        "Unnamed compound": replacement,
        "unnamed compound": replacement,
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _summary_source(basis: dict[str, Any], synthesis: dict[str, Any]) -> str:
    if synthesis.get("biological_summary"):
        return "l4.llm_synthesis.biological_summary"
    if synthesis.get("summary"):
        return "l4.llm_synthesis.summary"
    return "l4.missing_summary"


def _interpreted_question(intent: dict[str, Any], matrix: dict[str, Any]) -> str:
    query_type = intent.get("query_type") or matrix.get("mode") or "query"
    primary = matrix.get("primary_result") or {}
    biological_context = intent.get("bio_context") or primary.get("cell") or "available biological models"
    if query_type == "reverse":
        function = intent.get("function_desc") or ", ".join((intent.get("activate") or []) + (intent.get("suppress") or [])) or "the requested functional state"
        return f"find perturbations associated with {function} in {biological_context}"
    perturbation = intent.get("pert_desc") or primary.get("perturbation") or "the requested perturbation"
    return f"estimate functional effects of {perturbation} in {biological_context}"


def _evidence(dossier: dict[str, Any], route: dict[str, Any], matrix: dict[str, Any], synthesis: dict[str, Any]) -> dict[str, Any]:
    routes = matrix.get("executed_routes") or []
    matched_contexts = _dedupe_strings([item.get("cell") or item.get("context") for item in routes])
    matched_perturbations = _dedupe_strings([item.get("perturbation") or item.get("perturbation_label") for item in routes])
    matched_modalities = _dedupe_strings([item.get("modality") for item in routes])
    out = {
        "dossier_status": dossier.get("dossier_status"),
        "evidence_grade": (dossier.get("evidence_layer") or {}).get("evidence_grade"),
        "evidence_audit_summary": synthesis.get("evidence_audit_summary"),
        "route_status": route.get("status"),
        "query_type": dossier.get("query_type"),
        "matched_contexts": matched_contexts,
        "matched_perturbations": matched_perturbations,
        "matched_modalities": matched_modalities,
        "matched_evidence_count": len(routes) if routes else None,
    }
    return {key: value for key, value in out.items() if value is not None}


def _dedupe_strings(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        text = str(value or "").strip()
        key = text.casefold()
        if text and key not in seen:
            seen.add(key)
            output.append(text)
    return output


def _limitations(dossier: dict[str, Any]) -> list[str]:
    items = []
    for item in (dossier.get("uncertainty_layer") or {}).get("limitations", []):
        text = item.get("message") if isinstance(item, dict) else str(item)
        if text and text not in items:
            items.append(text)
    for item in (dossier.get("claim_basis") or {}).get("caution_points", []):
        text = str(item)
        if text and text not in items:
            items.append(text)
    return items


def _rendering_contract(dossier: dict[str, Any], mode: str) -> dict[str, Any]:
    basis = dossier.get("claim_basis") or {}
    hints = dossier.get("rendering_hints") or {}
    return {
        "mode": mode,
        "allowed_transformations": hints.get("allowed_transformations", []),
        "forbidden_transformations": hints.get("forbidden_transformations", []),
        "must_mention": basis.get("must_mention", []),
        "must_not_claim": basis.get("must_not_claim", []),
    }


def _trace(dossier: dict[str, Any]) -> list[dict[str, Any]]:
    audit = dossier.get("audit_layer") or {}
    return [
        {"layer": "l1", "event": "intent_parsed", "schema": (audit.get("schema_versions") or {}).get("l2")},
        {"layer": "l2", "event": "route_selected"},
        {"layer": "l3", "event": "matrix_execution", "status": audit.get("raw_execution_status")},
        {"layer": "l4", "event": "evidence_dossier", "status": dossier.get("dossier_status")},
        {"layer": "l5", "event": "presentation_rendered"},
    ]

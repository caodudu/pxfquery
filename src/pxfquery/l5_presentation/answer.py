from __future__ import annotations

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
    figures = build_figure_specs(dossier)
    limitations = _limitations(dossier)
    contract = _rendering_contract(dossier, mode)

    answer = PxFQueryAnswer(
        question=question,
        interpreted_question=_interpreted_question(intent, matrix),
        headline=_headline(basis),
        summary=_summary(basis, synthesis),
        summary_source=_summary_source(basis, synthesis),
        biological_results=tables["ranked_results"],
        evidence=_evidence(dossier, route, matrix, synthesis),
        limitations=limitations,
        tables=tables,
        figures=figures,
        rendering_contract=contract,
        structured_result=dossier,
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
    primary = matrix.get("primary_result") or {}
    out = {
        "dossier_status": dossier.get("dossier_status"),
        "evidence_grade": (dossier.get("evidence_layer") or {}).get("evidence_grade"),
        "evidence_audit_summary": synthesis.get("evidence_audit_summary"),
        "route_status": route.get("status"),
        "query_type": dossier.get("query_type"),
        "primary_cell": primary.get("cell"),
        "primary_perturbation": primary.get("perturbation"),
        "primary_modality": primary.get("modality"),
        "matched_rows": primary.get("n_rows"),
    }
    return {key: value for key, value in out.items() if value is not None}


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

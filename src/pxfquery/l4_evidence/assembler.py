from __future__ import annotations

from datetime import datetime, timezone
import re
from typing import Any


L4_SCHEMA_VERSION = "l4-evidence-dossier/v1"


def assemble_evidence(
    execution: Any,
    *,
    intent: Any | None = None,
    route_plan: Any | None = None,
    annotation_evidence: dict[str, Any] | None = None,
    llm_provider: Any | None = None,
    synthesize: bool = True,
    literature_provider: Any | None = None,
    debug: bool = False,
) -> dict[str, Any]:
    """Build a renderer-neutral L4 evidence dossier from L1/L2/L3 outputs."""

    execution_dict = _to_dict(execution)
    intent_dict = _to_dict(intent) or _to_dict(execution_dict.get("intent")) or _to_dict((route_plan or {}).get("intent") if isinstance(route_plan, dict) else None)
    route_dict = _to_dict(route_plan)
    status = _dossier_status(execution_dict)
    evidence_grade = _evidence_grade(status, execution_dict, route_dict)
    matrix_evidence = _matrix_evidence(execution_dict)
    route_evidence = _route_evidence(route_dict, include_rejected=False)
    intent_evidence = _intent_evidence(intent_dict)
    limitations = _limitations(status, intent_dict, route_dict, execution_dict, evidence_grade)
    claim_basis = _claim_basis(status, intent_dict, route_evidence, matrix_evidence, evidence_grade, limitations)
    literature_evidence = _literature_evidence(literature_provider, claim_basis, matrix_evidence)
    annotation_evidence = _json_safe(annotation_evidence or {})
    llm_synthesis = _llm_synthesis(llm_provider, synthesize, claim_basis, route_evidence, matrix_evidence, literature_evidence, limitations, annotation_evidence)

    dossier = {
        "schema_version": L4_SCHEMA_VERSION,
        "query_id": execution_dict.get("query_id") or route_dict.get("query_id"),
        "query_type": execution_dict.get("query_type") or intent_dict.get("query_type"),
        "dossier_status": status,
        "claim_basis": claim_basis,
        "evidence_layer": {
            "evidence_grade": evidence_grade,
            "intent_evidence": intent_evidence,
            "route_evidence": route_evidence,
            "matrix_evidence": matrix_evidence,
            "literature_evidence": literature_evidence,
            "annotation_evidence": annotation_evidence,
            "llm_synthesis": llm_synthesis,
        },
        "uncertainty_layer": {
            "confidence": claim_basis["claim_strength"],
            "limitations": limitations,
            "failure_mode": _failure_mode(status, execution_dict, route_dict),
        },
        "rendering_hints": _rendering_hints(claim_basis, evidence_grade),
        "audit_layer": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "schema_versions": {
                "l2": route_dict.get("schema_version"),
                "l3": execution_dict.get("schema_version"),
                "l4": L4_SCHEMA_VERSION,
            },
            "raw_execution_status": execution_dict.get("execution_status"),
            "source_route_schema": execution_dict.get("source_route_schema"),
            "errors": _json_safe(execution_dict.get("errors", [])),
            "warnings": _json_safe(execution_dict.get("warnings", [])),
            "resource_pack": _json_safe(execution_dict.get("resource_pack", {})),
            "matrix_summary": _json_safe(execution_dict.get("matrix_summary", {})),
            "proxy_direction_calibrations": _proxy_direction_calibrations(execution_dict),
            "debug": _debug_layer(route_dict, include_rejected=debug),
        },
    }
    return _json_safe(dossier)


def _to_dict(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    if hasattr(value, "to_dict"):
        converted = value.to_dict()
        return converted if isinstance(converted, dict) else {}
    return {}


def _dossier_status(execution: dict[str, Any]) -> str:
    if execution.get("schema_version") and execution.get("schema_version") != "l3-matrix-execution/v1":
        return "invalid_upstream_schema"
    status = execution.get("execution_status")
    return {
        "executed": "evidence_found",
        "partial": "partial_evidence",
        "route_plan_unresolved": "unresolved_route",
        "resource_missing": "resource_unavailable",
        "schema_mismatch": "invalid_upstream_schema",
        "no_executable_route": "no_executable_route",
        "empty_matrix_hit": "no_matrix_hit",
        "not_executed": "not_executed",
    }.get(str(status), str(status or "not_executed"))


def _evidence_grade(status: str, execution: dict[str, Any], route_plan: dict[str, Any]) -> str:
    if status in {"unresolved_route", "resource_unavailable", "invalid_upstream_schema", "no_executable_route", "not_executed"}:
        return status
    if not execution.get("executed_routes"):
        return "no_matrix"
    routes = execution.get("executed_routes", [])
    tiers = _route_tiers(execution, route_plan)
    has_exact_primary = any("exact_cell_exact_perturbation" in tier or "exact_matrix" in tier for tier in tiers)
    has_proxy_support = any("proxy" in tier for tier in tiers)
    if has_exact_primary and has_proxy_support:
        return "exact_primary_with_proxy_support"
    if has_exact_primary:
        return "exact_matrix"
    best_score = min((_route_quality_score((route.get("route_metadata") or {})) for route in routes), default=1.0)
    labels = {str((route.get("route_metadata") or {}).get("route_quality") or "") for route in routes}
    if "fallback" in labels or best_score > 0.75:
        return "fallback_matrix"
    if best_score <= 0.12:
        return "direct_or_close_representative_matrix"
    if best_score <= 0.3:
        return "strong_representative_matrix"
    if best_score <= 0.55:
        return "usable_neighbor_matrix"
    if status == "partial_evidence":
        return "partial_matrix"
    return "distant_neighbor_matrix"


def _route_tiers(execution: dict[str, Any], route_plan: dict[str, Any]) -> list[str]:
    tiers = []
    for route in execution.get("executed_routes", []) + execution.get("skipped_routes", []):
        metadata = route.get("route_metadata") or {}
        for key in ("tier", "evidence_tier", "pair_search_reason", "cell_role", "perturbation_role"):
            if metadata.get(key):
                tiers.append(str(metadata[key]))
    for route in ((route_plan.get("combination_route") or {}).get("selected_routes") or []):
        for key in ("tier", "evidence_tier", "pair_search_reason", "cell_role", "perturbation_role"):
            if route.get(key):
                tiers.append(str(route[key]))
    return tiers


def _route_quality_score(metadata: dict[str, Any]) -> float:
    try:
        return float(metadata.get("route_quality_score"))
    except (TypeError, ValueError):
        return 1.0


def _intent_evidence(intent: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "raw_query",
        "normalized_query",
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
        "parse_confidence",
        "ambiguity_flags",
        "missing_fields",
        "provider_evidence",
    ]
    return {key: _json_safe(intent.get(key)) for key in keys if key in intent}


def _route_evidence(route_plan: dict[str, Any], *, include_rejected: bool = False) -> dict[str, Any]:
    if not route_plan:
        return {"status": "missing", "reason": "route_plan was not provided to L4"}
    evidence = {
        "status": route_plan.get("route_status"),
        "reason": route_plan.get("reason"),
        "selected_route": _json_safe(route_plan.get("selected_route", {})),
        "selected_routes": _json_safe((route_plan.get("combination_route") or {}).get("selected_routes", [])),
        "cell_route": _json_safe(route_plan.get("cell_route", {})),
        "perturbation_route": _json_safe(route_plan.get("perturbation_route", {})),
        "function_route": _json_safe(route_plan.get("function_route", {})),
        "unresolved_dimensions": _json_safe(route_plan.get("unresolved_dimensions", [])),
        "llm_route_calls": _json_safe(route_plan.get("llm_calls", [])),
        "resource_status": _json_safe(route_plan.get("resource_status", {})),
    }
    if include_rejected:
        evidence["rejected_candidates"] = _json_safe(route_plan.get("rejected_candidates", []))
    return evidence


def _matrix_evidence(execution: dict[str, Any]) -> dict[str, Any]:
    query_type = execution.get("query_type")
    executed = [_route_summary(route) for route in execution.get("executed_routes", [])]
    skipped = [_route_summary(route) for route in execution.get("skipped_routes", [])]
    primary_route = execution.get("executed_routes", [None])[0] if execution.get("executed_routes") else None
    return {
        "mode": query_type,
        "execution_status": execution.get("execution_status"),
        "primary_result": _primary_result(query_type, primary_route),
        "executed_routes": executed,
        "skipped_routes": skipped,
        "raw_route_results": _json_safe(execution.get("executed_routes", [])),
    }


def _proxy_direction_calibrations(execution: dict[str, Any]) -> list[dict[str, Any]]:
    records = []
    for route in execution.get("executed_routes") or []:
        scores = route.get("scores") or {}
        metadata = route.get("route_metadata") or {}
        calibration = scores.get("proxy_direction_calibration") or metadata.get("proxy_direction_calibration")
        if not calibration:
            continue
        records.append(
            {
                "route_id": route.get("route_id"),
                "query_type": route.get("query_type"),
                "modality": route.get("modality"),
                "cell": route.get("cell"),
                "perturbation": metadata.get("perturbation"),
                "calibration": _json_safe(calibration),
            }
        )
    return records


def _route_summary(route: dict[str, Any]) -> dict[str, Any]:
    metadata = route.get("route_metadata") or {}
    row_match = route.get("row_match") or {}
    out = {
        "route_id": route.get("route_id"),
        "query_type": route.get("query_type"),
        "modality": route.get("modality"),
        "status": route.get("status"),
        "cell": route.get("cell"),
        "perturbation": metadata.get("perturbation"),
        "perturbation_alias": (metadata.get("perturbation_record") or {}).get("alias"),
        "tier": metadata.get("tier"),
        "cell_role": metadata.get("cell_role"),
        "perturbation_role": metadata.get("perturbation_role"),
        "cell_match_type": metadata.get("cell_match_type"),
        "perturbation_match_type": metadata.get("perturbation_match_type"),
        "cell_match_distance": metadata.get("cell_match_distance"),
        "perturbation_match_distance": metadata.get("perturbation_match_distance"),
        "modality_match_type": metadata.get("modality_match_type"),
        "modality_rank": metadata.get("modality_rank"),
        "modality_match_distance": metadata.get("modality_match_distance"),
        "modality_reason": metadata.get("modality_reason"),
        "requested_modality": metadata.get("requested_modality"),
        "route_quality_score": metadata.get("route_quality_score"),
        "route_quality": metadata.get("route_quality"),
        "pair_search_reason": metadata.get("pair_search_reason"),
        "score_orientation": (route.get("scores") or {}).get("score_orientation") or metadata.get("score_orientation"),
        "score_multiplier": (route.get("scores") or {}).get("score_multiplier") or metadata.get("score_multiplier"),
        "score_weight": (route.get("scores") or {}).get("score_weight") or metadata.get("score_weight"),
        "effective_score_multiplier": (route.get("scores") or {}).get("effective_score_multiplier") or metadata.get("effective_score_multiplier"),
        "recommended_operation": metadata.get("recommended_operation"),
        "modality_evidence": _json_safe(metadata.get("modality_evidence", [])),
        "n_rows": row_match.get("n_rows"),
        "n_ranked_groups": row_match.get("n_ranked_groups"),
        "diagnostics": _json_safe(route.get("diagnostics", {})),
    }
    if route.get("query_type") == "forward":
        rankings = route.get("rankings") or {}
        out["top_activated"] = _json_safe(rankings.get("top_activated", []))
        out["top_suppressed"] = _json_safe(rankings.get("top_suppressed", []))
        out["requested_function_records"] = _json_safe((route.get("scores") or {}).get("requested_function_records", []))
    elif route.get("query_type") == "reverse":
        rankings = route.get("rankings") or {}
        scores = route.get("scores") or {}
        out["interpretation_set_id"] = scores.get("interpretation_set_id") or metadata.get("interpretation_set_id")
        out["functions"] = _json_safe(metadata.get("functions", []))
        out["target_vector"] = _json_safe(scores.get("target_vector", {}))
        out["ranking_method"] = scores.get("ranking_method")
        out["reverse_ranking_mode"] = scores.get("reverse_ranking_mode") or metadata.get("reverse_ranking_mode")
        out["top_perturbations"] = _json_safe(rankings.get("top_perturbations", []))
        out["rankings"] = _json_safe(rankings)
    return out


def _primary_result(query_type: str | None, route: dict[str, Any] | None) -> dict[str, Any] | None:
    if route is None:
        return None
    metadata = route.get("route_metadata") or {}
    row_match = route.get("row_match") or {}
    scores = route.get("scores") or {}
    rankings = route.get("rankings") or {}
    if query_type == "reverse":
        return {
            "cell": route.get("cell"),
            "modality": route.get("modality"),
            "target_vector": _json_safe(scores.get("target_vector", {})),
            "ranking_method": scores.get("ranking_method"),
            "reverse_ranking_mode": scores.get("reverse_ranking_mode"),
            "interpretation_set_id": scores.get("interpretation_set_id"),
            "n_rows": row_match.get("n_rows"),
            "n_ranked_groups": row_match.get("n_ranked_groups"),
            "top_perturbations": _json_safe(rankings.get("top_perturbations", [])),
            "rankings": _json_safe(rankings),
        }
    return {
        "cell": route.get("cell"),
        "perturbation": metadata.get("perturbation"),
        "perturbation_alias": (metadata.get("perturbation_record") or {}).get("alias"),
        "modality": route.get("modality"),
        "n_rows": row_match.get("n_rows"),
        "pert_ids": _json_safe(row_match.get("pert_ids", [])),
        "cmap_names": _json_safe(row_match.get("cmap_names", [])),
        "requested_function_scores": _json_safe(scores.get("requested_functions", {})),
        "requested_function_records": _json_safe(scores.get("requested_function_records", [])),
        "score_orientation": scores.get("score_orientation"),
        "score_multiplier": scores.get("score_multiplier"),
        "top_activated": _json_safe(rankings.get("top_activated", [])),
        "top_suppressed": _json_safe(rankings.get("top_suppressed", [])),
    }


def _limitations(
    status: str,
    intent: dict[str, Any],
    route_plan: dict[str, Any],
    execution: dict[str, Any],
    evidence_grade: str,
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for field in intent.get("missing_fields", []) or []:
        items.append({"code": "intent_missing_field", "message": f"L1 did not resolve required field: {field}"})
    for flag in intent.get("ambiguity_flags", []) or []:
        items.append({"code": "intent_ambiguity", "message": str(flag)})
    for dim in route_plan.get("unresolved_dimensions", []) or []:
        items.append({"code": "route_unresolved_dimension", "message": str(dim)})
    for error in execution.get("errors", []) or []:
        items.append({"code": error.get("code", "l3_error"), "message": error.get("message") or str(error)})
    for warning in execution.get("warnings", []) or []:
        items.append({"code": warning.get("code", "l3_warning") if isinstance(warning, dict) else "l3_warning", "message": str(warning)})
    if status == "partial_evidence":
        items.append({"code": "partial_evidence", "message": "At least one L3 route executed and at least one selected route was skipped or failed."})
    if evidence_grade in {"fallback_matrix", "distant_neighbor_matrix"}:
        items.append({"code": "distant_route", "message": "The best executed evidence route is distant from the requested concept; present it as a fallback route, not as direct biological coverage."})
    if not items and status == "evidence_found":
        return []
    return items


def _claim_basis(
    status: str,
    intent: dict[str, Any],
    route_evidence: dict[str, Any],
    matrix_evidence: dict[str, Any],
    evidence_grade: str,
    limitations: list[dict[str, Any]],
) -> dict[str, Any]:
    answerability = {
        "evidence_found": "answered",
        "partial_evidence": "partially_answered",
    }.get(status, "not_answered")
    claim_type = _claim_type(status, matrix_evidence)
    main_claim = _main_claim(answerability, claim_type, intent, matrix_evidence, evidence_grade)
    claim_strength = _claim_strength(status, evidence_grade, limitations)
    return {
        "answerability": answerability,
        "user_question": intent.get("raw_query") or intent.get("normalized_query"),
        "main_claim": main_claim,
        "claim_type": claim_type,
        "claim_strength": claim_strength,
        "supporting_points": _supporting_points(route_evidence, matrix_evidence, evidence_grade),
        "caution_points": [item["message"] for item in limitations],
        "must_mention": _must_mention(status, evidence_grade, matrix_evidence),
        "must_not_claim": _must_not_claim(status, evidence_grade),
    }


def _claim_type(status: str, matrix_evidence: dict[str, Any]) -> str:
    if status not in {"evidence_found", "partial_evidence"}:
        return "no_matrix_evidence"
    if matrix_evidence.get("mode") == "reverse":
        return "ranked_candidate"
    return "matrix_backed_effect"


def _main_claim(answerability: str, claim_type: str, intent: dict[str, Any], matrix_evidence: dict[str, Any], evidence_grade: str) -> str:
    if answerability == "not_answered":
        return "PxFquery did not produce matrix-backed evidence for the routed query in the configured resources."
    primary = matrix_evidence.get("primary_result") or {}
    context = intent.get("bio_context") or primary.get("cell") or "the routed biological context"
    if claim_type == "ranked_candidate":
        candidates = primary.get("top_perturbations") or []
        labels = [str(item.get("label") or item.get("cmap_name") or item.get("pert_id")) for item in candidates[:3]]
        return f"PxFquery found matrix-backed ranked perturbation candidates for {context}: {', '.join(labels) if labels else 'no named candidates in the primary route'}."
    pert = intent.get("pert_desc") or primary.get("perturbation") or "the routed perturbation"
    return f"PxFquery found {evidence_grade} functional matrix evidence for {pert} in {context}."


def _claim_strength(status: str, evidence_grade: str, limitations: list[dict[str, Any]]) -> str:
    if status not in {"evidence_found", "partial_evidence"}:
        return "none"
    if status == "partial_evidence":
        return "low"
    if evidence_grade == "direct_or_close_representative_matrix" and not limitations:
        return "high"
    if evidence_grade == "strong_representative_matrix":
        return "moderate"
    if evidence_grade in {"fallback_matrix", "distant_neighbor_matrix"}:
        return "low"
    return "moderate"


def _supporting_points(route_evidence: dict[str, Any], matrix_evidence: dict[str, Any], evidence_grade: str) -> list[str]:
    points = [f"Evidence grade: {evidence_grade}."]
    primary = matrix_evidence.get("primary_result") or {}
    if primary.get("n_rows") is not None:
        points.append(f"Primary L3 route matched {primary['n_rows']} matrix rows.")
    if route_evidence.get("status"):
        points.append(f"L2 route status: {route_evidence['status']}.")
    return points


def _must_mention(status: str, evidence_grade: str, matrix_evidence: dict[str, Any]) -> list[str]:
    out = ["matrix-backed" if status in {"evidence_found", "partial_evidence"} else "no matrix-backed result"]
    out.append(evidence_grade)
    primary = matrix_evidence.get("primary_result") or {}
    if primary.get("n_rows") is not None:
        out.append(f"matched rows: {primary['n_rows']}")
    if status == "partial_evidence":
        out.append("partial evidence")
    return out


def _must_not_claim(status: str, evidence_grade: str) -> list[str]:
    claims = [
        "clinical efficacy",
        "causal validation beyond the configured matrix evidence",
        "PubMed support when literature_evidence is disabled or unavailable",
    ]
    if status != "evidence_found":
        claims.append("the query was fully answered")
    if evidence_grade == "exact_primary_with_proxy_support":
        claims.append("all selected evidence routes were exact")
    if evidence_grade in {"fallback_matrix", "distant_neighbor_matrix"}:
        claims.append("direct coverage of the requested biological concept")
    return claims


def _literature_evidence(literature_provider: Any | None, claim_basis: dict[str, Any], matrix_evidence: dict[str, Any]) -> dict[str, Any]:
    if literature_provider is None:
        return {"status": "disabled", "records": [], "diagnostics": {"reason": "No literature provider was configured for L4."}}
    if not hasattr(literature_provider, "search"):
        return {"status": "unavailable", "records": [], "diagnostics": {"reason": "Configured literature provider does not expose search(...)."}}
    try:
        records = literature_provider.search(claim_basis=claim_basis, matrix_evidence=matrix_evidence)
    except Exception as exc:
        return {"status": "failed", "records": [], "diagnostics": {"reason": str(exc)}}
    return {"status": "searched", "records": _json_safe(records or []), "diagnostics": {}}


def _llm_synthesis(
    llm_provider: Any | None,
    synthesize: bool,
    claim_basis: dict[str, Any],
    route_evidence: dict[str, Any],
    matrix_evidence: dict[str, Any],
    literature_evidence: dict[str, Any],
    limitations: list[dict[str, Any]],
    annotation_evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not synthesize:
        return {"status": "disabled", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "L4 LLM synthesis was not requested."}}
    if llm_provider is None:
        return {"status": "unavailable", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "No LLM provider was configured for L4 synthesis."}}
    if not hasattr(llm_provider, "request_json"):
        return {"status": "unavailable", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "LLM provider does not expose request_json(...)."}}

    biological_payload = _biological_answer_payload(claim_basis, matrix_evidence, annotation_evidence or {})
    audit_payload = _execution_quality_payload(claim_basis, route_evidence, matrix_evidence, literature_evidence, limitations)
    provider_evidence: dict[str, Any] = {}
    diagnostics: dict[str, Any] = {}

    query_mode = str(matrix_evidence.get("mode") or "")
    if query_mode == "forward":
        dimension_payload = _forward_response_dimension_payload(biological_payload)
        try:
            dimension_result, dimension_evidence = _request_json_with_max_tokens(
                llm_provider,
                max_tokens=1100,
                stage="l4_forward_response_dimensions",
                system_prompt=_forward_response_dimension_system_prompt(),
                user_payload=dimension_payload,
            )
        except Exception as exc:
            dimension_result = {}
            dimension_evidence = {}
            diagnostics["response_dimension_error"] = f"{type(exc).__name__}: {exc}"
        provider_evidence["response_dimensions"] = _json_safe(dimension_evidence)
        answer_payload = _forward_dimension_answer_payload(biological_payload, dimension_result if isinstance(dimension_result, dict) else {})
        try:
            biological_result, biological_evidence = _request_json_with_max_tokens(
                llm_provider,
                max_tokens=1100,
                stage="l4_forward_biological_answer",
                system_prompt=_forward_dimension_answer_system_prompt(),
                user_payload=answer_payload,
            )
        except Exception as exc:
            biological_result = {}
            biological_evidence = {}
            diagnostics["biological_error"] = f"{type(exc).__name__}: {exc}"
    else:
        try:
            biological_result, biological_evidence = _request_json_with_max_tokens(
                llm_provider,
                max_tokens=1600,
                stage=f"l4_{query_mode or 'query'}_biological_answer",
                system_prompt=_biological_answer_system_prompt(query_mode),
                user_payload=biological_payload,
            )
        except Exception as exc:
            biological_result = {}
            biological_evidence = {}
            diagnostics["biological_error"] = f"{type(exc).__name__}: {exc}"
    provider_evidence["biological_answer"] = _json_safe(biological_evidence)

    if not isinstance(biological_result, dict):
        biological_result = {}
        diagnostics["biological_error"] = "L4 biological answer returned non-object JSON."

    quality_flags = _biological_answer_quality_flags(biological_result, query_mode)
    if quality_flags:
        try:
            repair_payload = answer_payload if query_mode == "forward" else biological_payload
            repair_prompt = _forward_dimension_answer_system_prompt() if query_mode == "forward" else _biological_answer_system_prompt(query_mode)
            repaired, repair_evidence = _request_json_with_max_tokens(
                llm_provider,
                max_tokens=1600,
                stage="l4_biological_answer_repair",
                system_prompt=(
                    repair_prompt
                    + " The previous JSON failed these quality checks: "
                    + ", ".join(quality_flags)
                    + ". Rewrite only the same biological answer from the same evidence. "
                    + "If a reverse answer has too many gene symbols, keep only the leading one to three genes and summarize the rest by broad candidate class without parenthetical gene-symbol examples."
                ),
                user_payload=repair_payload | {"previous_invalid_answer": biological_result, "quality_flags": quality_flags},
            )
            if isinstance(repaired, dict) and not _biological_answer_quality_flags(repaired, query_mode):
                biological_result = repaired
                provider_evidence["biological_answer"] = {
                    "initial": provider_evidence["biological_answer"],
                    "repair": _json_safe(repair_evidence),
                }
                quality_flags = []
        except Exception as exc:
            quality_flags.append(f"repair_failed:{type(exc).__name__}")
    diagnostics["biological_quality_flags"] = quality_flags

    try:
        audit_result, audit_evidence = _request_json_with_max_tokens(
            llm_provider,
            max_tokens=700,
            stage="l4_execution_quality",
            system_prompt=_execution_quality_system_prompt(),
            user_payload=audit_payload,
        )
    except Exception as exc:
        audit_result = {}
        audit_evidence = {}
        diagnostics["execution_quality_error"] = f"{type(exc).__name__}: {exc}"
    provider_evidence["execution_quality"] = _json_safe(audit_evidence)
    if not isinstance(audit_result, dict):
        audit_result = {}
        diagnostics["execution_quality_error"] = "L4 execution quality summary returned non-object JSON."

    biological_summary = biological_result.get("answer") or biological_result.get("biological_summary") or biological_result.get("summary")
    evidence_audit_summary = audit_result.get("summary") or audit_result.get("evidence_audit_summary")
    status = "completed" if biological_summary or evidence_audit_summary else "failed"
    return {
        "status": status,
        "summary": biological_summary,
        "biological_summary": biological_summary,
        "biological_subquestions": _json_safe(biological_result.get("subquestions") or []),
        "evidence_audit_summary": evidence_audit_summary,
        "verdict_rationale": audit_result.get("verdict_rationale"),
        "confidence_rationale": audit_result.get("confidence_rationale"),
        "limitations_summary": None,
        "provider_evidence": _json_safe(provider_evidence),
        "diagnostics": _json_safe(diagnostics),
    }


def _request_json_with_max_tokens(
    llm_provider: Any,
    *,
    max_tokens: int,
    stage: str,
    system_prompt: str,
    user_payload: dict[str, Any],
) -> tuple[Any, dict[str, Any]]:
    config = getattr(llm_provider, "config", None)
    if config is None or not hasattr(config, "max_tokens"):
        return llm_provider.request_json(stage=stage, system_prompt=system_prompt, user_payload=user_payload, temperature=0)
    previous = config.max_tokens
    config.max_tokens = max(int(previous or 0), max_tokens)
    try:
        return llm_provider.request_json(stage=stage, system_prompt=system_prompt, user_payload=user_payload, temperature=0)
    finally:
        config.max_tokens = previous


def _biological_answer_system_prompt(query_type: str) -> str:
    if query_type == "reverse":
        return _reverse_biological_answer_system_prompt()
    return _forward_biological_answer_system_prompt()


def _forward_response_dimension_system_prompt() -> str:
    return """
Role
You are a biological abstraction step.

Task
Convert increased_evidence and decreased_evidence into functional roles, not prettier pathway names.

Abstraction rule
A valid axis describes what kind of cellular behavior is changing. It must not describe the named assay label, named pathway, named gene set, named signaling module, or named subprogram.

Invalid -> valid abstraction patterns
- named immune or cytokine signaling label -> defense-like activation or immune-state activation
- named growth regulator targets, replication, mitosis, checkpoint, or cell-cycle labels -> growth activity or proliferative drive
- named metabolic pathway labels -> energy use, biosynthetic activity, or metabolic state
- named secretion/extracellular labels -> communication or secretory state
These examples are abstraction patterns, not fixed answer choices. Choose the role that best fits the supplied evidence.

Hard rules
- Use both increased_evidence and decreased_evidence.
- No gene names in axis fields.
- No pathway names in axis fields.
- No label-level process names in axis fields.
- No words copied from evidence labels except very general words such as cell, growth, immune, stress, metabolism, defense, activity, state, or drive.
- Axis fields should be broad plain-language cellular behaviors.
- axis_meanings must explain those broad behaviors at the same abstraction level. Do not use axis_meanings to reintroduce pathway names, gene-set names, signature names, named subprograms, or close paraphrases of evidence labels.
- If a meaning sentence contains wording that could be traced back to an evidence label, rewrite it as a broader behavioral implication.
- evidence_examples is the only field allowed to preserve readable evidence examples.

Return exactly one JSON object:
{
  "promoted_axis": "broad promoted cellular behavior",
  "suppressed_axis": "broad suppressed cellular behavior",
  "overall_state": "short case-specific state-change concept",
  "axis_meanings": {
    "promoted_axis": "one sentence explaining what the promoted axis means for cell behavior, without examples",
    "suppressed_axis": "one sentence explaining what the suppressed axis means for cell behavior, without examples",
    "overall_state": "one sentence explaining the state change, without examples"
  },
  "evidence_examples": ["at most four representative readable examples from supplied programs"],
  "dimension_notes": ["short notes about mixed or unresolved evidence, if any"]
}
""".strip()


def _forward_dimension_answer_system_prompt() -> str:
    return """
Role
You explain functional perturbation results to a general molecular or cancer biologist.

Input
You receive abstract state_axes and axis_meanings only. You do not receive evidence labels or evidence examples.

Task
Write exactly 3 complete sentences answering the user by using only the biological content present in state_axes and axis_meanings.

Rules
- Sentence 1 explains suppressed or decreased biology using suppressed_axis and its meaning.
- Sentence 2 explains promoted or increased biology using promoted_axis and its meaning.
- Sentence 3 explains the overall state change using overall_state and its meaning.
- Each sentence must be informative; do not merely restate the axis name.
- Each sentence must contain a biological interpretation, not only a short label statement.
- You may elaborate only with meaning already present in axis_meanings.
- Do not add examples.
- The queried perturbation name is allowed.
- Do not mention PxFquery.
- Do not mention software, internal layers, routes, evidence grades, exact/proxy status, row counts, scores, benchmarks, missing literature, clinical efficacy, or validation status.
- Match the language of user_question.

Return exactly one JSON object:
{
  "answer": "Exactly 3 complete sentences. Sentence 1 covers suppressed biology, sentence 2 covers promoted biology, and sentence 3 covers overall cellular-state change.",
  "response_theme": "short phrase for the overall perturbation response",
  "subquestions": ["direct subquestion answers, or empty array for a single-question input"],
  "main_program_changes": ["increased: high-level biology", "decreased: high-level biology"],
  "evidence_examples": ["copy the supplied evidence_examples, at most four"],
  "support_notes": ["short grounded note"]
}
""".strip()


def _forward_biological_answer_system_prompt() -> str:
    return """
Role
You explain functional perturbation results to a general molecular or cancer biologist.

Input
You receive exactly five inputs:
- user_question: the user's original question.
- interpreted_intent: parsed biological context, perturbation, modality, score orientation, and primary ranked functions.
- answer_policy: how the supplied matched evidence should be prioritized.
- program_summary: the primary forward program summary already ranked from matched evidence.
- evidence_profiles: one or more matched profiles. Each profile contains a cell/context, perturbation label, activated_programs, and suppressed_programs.

Task
Write the default user-facing biological answer for a forward perturbation query.

The input contains consensus functional programs that changed after a perturbation. These labels are raw evidence materials, not answer text. Your job is not to translate, concatenate, or list those program labels. Your job is to infer the cellular response state implied by the activated and suppressed program groups.

Use only interpreted_intent, answer_policy, program_summary, and evidence_profiles. First identify whether user_question contains one biological question or multiple biological subquestions.

Default answer behavior
- For a single-question input, write exactly 3 complete sentences that answer the user's question for a general molecular or cancer biologist.
- Sentence 1 should describe suppressed or decreased biology, if the evidence supports a decreased direction.
- Sentence 2 should describe promoted or increased biology, if the evidence supports an increased direction.
- Sentence 3 should describe the overall cellular-state change implied by the first two sentences.
- Each sentence must contain a biological interpretation, not only a short label statement.
- The answer field must not contain evidence examples, parenthetical examples, or "including/such as/for example" clauses. Put those examples only in evidence_examples.
- For a multi-subquestion input, first answer the main perturbation response, then include numbered answers for the user's subquestions. Each numbered answer must directly answer one biological subquestion.
- Every subquestion must receive a clear verdict: supported, not supported, mixed, or not resolved from the supplied functional evidence.

Evidence prioritization
- Treat program_summary as the primary program ranking for the answer.
- If answer_policy.mode is direct_anchor_with_support, make program_summary entries with direct_support the anchor of the biological answer. Other matched profiles can support, reinforce, or qualify those claims, but must not displace directly matched evidence solely because they are more numerous or have larger scores.
- If answer_policy.mode is cross_match_consensus, no directly matched anchor is available; answer from the cross-profile consensus represented by program_summary.
- Do not answer from only the first evidence profile unless answer_policy says the directly matched evidence is the anchor and program_summary supports that anchor.

Answer-level abstraction
- Treat supplied program labels as raw materials that should normally disappear from the answer field after interpretation.
- Before writing the answer, internally compress the supplied programs into a small number of biological response dimensions. Derive those dimensions from the supplied evidence; do not choose from a fixed vocabulary supplied by this prompt.
- The answer field must describe these response dimensions and their overall cellular-state implication, not the underlying program-label ingredients.
- Keep response dimensions broad enough that the answer reads like a biological conclusion, not a table caption.
- Do not name individual supplied programs, pathway labels, gene-set labels, raw database labels, gene-centered mechanisms, or label-level sub-processes in the answer field.
- Do not use close paraphrases of supplied program labels when they are merely components of a broader response dimension. For example, multiple cell-cycle, mitotic, replication, or growth-factor labels should usually be summarized as reduced or increased proliferative growth unless a narrower distinction is essential to answer the user's question.
- In the answer field, the only gene or perturbation name that may be mentioned is the user's queried perturbation when needed for grammar. Gene names that appear only because they are embedded in supplied program labels must not appear in the answer field. Convert those labels into the corresponding response dimension when supported.
- Put representative supplied-program examples only in evidence_examples.
- The answer must be understandable if evidence_examples is hidden.
- Use the most compact biological abstraction that preserves the user's requested distinction. Increase granularity only when the user explicitly asks about that biology or when broad categories would hide a real direction conflict.
- Vary the wording according to the actual evidence. Do not reuse a stock sentence such as "the cells shift from a growth-promoting state toward an immune-activated and stress-responsive state" unless that is the most specific conclusion supported by this case.

Required biological reasoning behavior
- Separate increased and decreased biological processes.
- Infer the overall cellular response state from the combination of increased and decreased processes.
- If score_orientation says activation is inferred from loss-of-function evidence, interpret directions as a reverse-direction inference from CRISPR/RNAi loss-of-function data, not as direct overexpression measurements.
- If the user asks whether a named program family is affected, judge it semantically from supplied program labels and directions. Use one of: supported, not supported, or not resolved.
- If evidence is mixed across profiles, say it is mixed and describe the main directions.
- If a requested subquestion is not covered by supplied program labels, say not resolved from the supplied functional evidence.
- Do not collapse multiple user subquestions into one paragraph. Give a separate answer for each subquestion.
- Do not use vague frequency phrases as the main conclusion, such as "some profiles", "a subset", "partial signal", or "may be affected". Convert the evidence into a clear verdict for each subquestion: supported, not supported, mixed, or not resolved.
- If evidence differs across profiles, explain the biological direction of the conflict instead of saying only that it is partial or heterogeneous.
- For program-family questions, do not answer with a vague frequency statement. Say whether the family is supported, not supported, mixed, or not resolved, and name the high-level biology that justifies the verdict.
- If user_question has only one biological question, do not repeat it as a separate subquestion section. Put the full answer in the answer field and set subquestions to an empty array.
- Match the language of user_question.

Forbidden in answer
- Do not mention software, internal layers, routes, evidence grades, exact/proxy status, row counts, scores, benchmarks, missing literature, clinical efficacy, or validation status.
- Do not mention PxFquery.
- Do not invent mechanisms, citations, functions, cells, perturbations, or numeric values.
- Do not expose raw program identifiers such as all-caps database IDs or numbered program codes. Use readable biological phrases instead.
- Do not describe inferred activation evidence as direct overexpression evidence.
- Do not turn the answer field into a comma-separated list of program labels.
- Do not use "including", "such as", "for example", parentheses, or colon-separated examples in the answer field to smuggle evidence examples into the conclusion.
- Do not treat supplied program labels as phrases to preserve. They are evidence ingredients; the answer field should contain the interpreted cellular response, not the ingredients.
- Do not use a stock "Overall, the cells shift from ... toward ..." sentence pattern by default. If a third sentence is used, write a case-specific state interpretation.

Output JSON schema
Return exactly one JSON object:
{
  "answer": "Exactly 3 complete sentences. Sentence 1 covers decreased biology, sentence 2 covers increased biology, and sentence 3 covers the overall cellular-state change.",
  "response_theme": "short phrase for the overall perturbation response",
  "subquestions": ["Short subquestion followed by its direct answer."],
  "main_program_changes": ["increased: high-level biological process", "decreased: high-level biological process"],
  "evidence_examples": ["At most four short representative examples from the supplied programs. These examples may name readable supplied-program categories, but must not appear in the answer field."],
  "support_notes": ["Short grounded note using high-level biological phrases."]
}

Style example
Input summary A: user asks one question: what programs change after perturbation X in a cancer model. Evidence profiles show one coherent group of increased functional biology and one coherent group of decreased functional biology.
Valid single-question output shape:
{
  "answer": "Perturbation X promotes the high-level biological response inferred from the increased functional evidence. It suppresses the high-level biological response inferred from the decreased functional evidence. Together, these changes indicate the case-specific cellular state implied by those two directions.",
  "response_theme": "case-specific response theme",
  "subquestions": [],
  "main_program_changes": [
    "increased: high-level biology inferred from increased programs",
    "decreased: high-level biology inferred from decreased programs"
  ],
  "evidence_examples": [
    "representative increased program category",
    "representative decreased program category"
  ],
  "support_notes": ["The answer is based only on supplied functional program evidence."]
}

Input summary B: user asks what programs change after perturbation X in model Y, and also asks whether program family A is affected. Evidence profiles support one increased biological direction and one decreased biological direction; no supplied program clearly maps to family A.
Valid multi-subquestion output shape:
{
  "answer": "Perturbation X promotes the high-level biology inferred from the increased functional evidence. It suppresses the high-level biology inferred from the decreased functional evidence. Numbered answers:\n1. What functional programs change after perturbation X? Supported: the increased and decreased biological directions described above.\n2. Is program family A affected? Not resolved from the supplied functional evidence.",
  "response_theme": "case-specific response theme",
  "subquestions": [
    "What functional programs change after perturbation X? Supported: the increased and decreased biological directions described in the answer.",
    "Is program family A affected? Not resolved from the supplied functional evidence."
  ],
  "main_program_changes": [
    "increased: high-level biology inferred from increased programs",
    "decreased: high-level biology inferred from decreased programs"
  ],
  "evidence_examples": [
    "representative increased program category",
    "representative decreased program category"
  ],
  "support_notes": ["The answer is based only on supplied functional program evidence."]
}
""".strip()


def _reverse_biological_answer_system_prompt() -> str:
    return """
Role
You explain reverse functional perturbation results to a general molecular or cancer biologist.

Input
You receive exactly four inputs:
- user_question: the user's original question.
- interpreted_intent: parsed biological context, context_scope, searched_cells, and requested functional state.
- candidate_summary: cross-profile candidate summary. It is the primary candidate ranking for reverse queries.
- evidence_profiles: matched profiles containing candidate_perturbations or candidate genes with their functional match evidence.

Task
Write the default user-facing biological answer for a reverse query. The user is asking for a ranked candidate set of perturbations or genes that can move the system toward the requested functional state. Your job is to interpret the ranked candidate set biologically, not to decide whether there is one single best candidate, not to narrate the search process, and not to list every cell-specific match.

Required reasoning behavior
- The answer-level candidate names must come from candidate_summary only.
- evidence_profiles are support context only. Do not introduce, name, or recommend a candidate from evidence_profiles unless that same candidate label also appears in candidate_summary.
- Start with candidate_summary, not the first evidence profile and not route-local candidate_perturbations.
- If interpreted_intent.context_scope is concept_or_disease_model_set, answer at the disease/model-set level. Do not frame the answer as "in [first cell line]" or imply the first searched cell is the user's requested model.
- If interpreted_intent.has_user_specified_cell is true, prioritize candidates with exact_cell_support. Other cells may only be described as supporting or broader-context evidence.
- If interpreted_intent.has_user_specified_cell is false, rank candidates by cross-profile support and mean/best functional match in candidate_summary.
- Name the leading readable candidates and explain what requested functional state they are predicted to move toward.
- Prefer a small interpreted recommendation set over an exhaustive list.
- For genetic reverse queries, name only the leading three to five readable genes in the answer field. Do not list a long comma-separated panel of genes.
- For genetic reverse queries, briefly describe recognizable broad candidate classes when they are obvious from standard gene knowledge, such as kinase, transcriptional regulator, ribosomal/translation factor, metabolic enzyme, transporter, protease, receptor, or signaling adaptor. If you are not confident, do not invent a class.
- Additional genetic candidates should be summarized as lower-ranked genes or supporting candidate groups rather than listed one by one.
- If using a broad class such as ribosomal proteins or kinases, do not add parenthetical gene-symbol examples after the class name.
- For genetic reverse queries, the answer field may contain at most five gene symbols total, including lower-ranked candidates and examples.
- If several candidates have similar support, describe them as a ranked group rather than giving separate cell-by-cell paragraphs.
- Describe searched cell lines only as evidence context, not as the main result, unless the user specified a cell line.
- Distinguish better-supported candidates from lower-ranked candidates using ranking language only. Do not imply lower-ranked candidates are biologically inactive, clinically ineffective, or unrelated.
- Treat reverse answers as ranked candidate-set recommendations. Do not say that the evidence fails to resolve a single best candidate unless the user explicitly asks for one single best candidate.
- If candidate_summary contains several plausible candidates, describe the leading group and then place lower-ranked candidates as secondary follow-up candidates or broader supporting context; do not convert that into a "not resolved" conclusion.
- If the supplied candidate_summary is empty or contains no readable candidate, then say not resolved from the supplied functional evidence.
- Mention searched cell lines only when needed to explain model-set support; do not make them the headline unless the user specified a cell line.
- Anonymous internal compound identifiers are not user-facing candidate names, but they are still real compound candidates. If a drug candidate has no readable name, refer to it as "an unnamed compound candidate" and keep the raw identifier out of the answer field.

Forbidden in answer
- Do not mention software, internal layers, routes, evidence grades, exact/proxy status, row counts, scores, benchmarks, missing literature, clinical efficacy, or validation status.
- Do not mention PxFquery.
- Do not mention input field names or internal evidence containers such as candidate_summary, evidence_profiles, interpreted_intent, or payload.
- Do not invent mechanisms, citations, candidates, functions, cells, perturbations, or numeric values.
- Do not expose raw candidate identifiers such as BRD-K*, BRD-A*, BRDN*, or other internal IDs in the answer field.
- Do not name candidates that are absent from candidate_summary, even if they occur in evidence_profiles.
- Do not write "single best", "does not resolve a single best candidate", or equivalent wording unless the user explicitly asks for one single best candidate.
- Do not say "weaker or no clear association", "no clear association", "not associated", or "no effect" for candidates that are merely lower ranked.
- Do not write a cell-by-cell execution report.
- Do not turn the answer field into a ranked table in sentence form.
- Do not list more than five gene symbols in the answer field.
- Do not write parenthetical gene-symbol lists such as "ribosomal proteins (A, B, C)" in the answer field.

Output JSON schema
Return exactly one JSON object:
{
  "answer": "Three complete sentences: sentence 1 names the leading candidate group from the supplied ranking, sentence 2 explains the requested functional direction they support, sentence 3 describes lower-ranked supplied candidates as secondary follow-up candidates or broader supporting context. Do not mention candidate_summary or evidence_profiles in the answer.",
  "subquestions": ["Short subquestion followed by its direct answer."],
  "candidate_interpretation": ["candidate label: readable functional interpretation"],
  "support_notes": ["Short grounded note using readable biological phrases."]
}

Style example
Input summary: user asks which perturbations could produce functional state Z in model Y. candidate_summary contains X, Y, and Z as the leading ranked candidates. evidence_profiles also contain route-local candidates W and Q that are absent from candidate_summary.
Valid output shape:
{
  "answer": "Candidates X, Y, and Z form the leading ranked group for moving model Y toward functional state Z. Their matched evidence supports movement toward the requested functional direction rather than the opposite state. Other supplied candidates provide secondary follow-up leads within the same functional search space.",
  "subquestions": [
    "Which candidates match functional state Z? Candidates X, Y, and Z form the leading ranked group."
  ],
  "candidate_interpretation": [
    "candidate X: leading candidate from candidate_summary",
    "candidate Y: leading candidate from candidate_summary"
  ],
  "support_notes": ["Answer-level candidate names are restricted to candidate_summary."]
}
""".strip()


def _execution_quality_system_prompt() -> str:
    return (
        "Role: execution-quality auditor for a functional perturbation query. "
        "Input contract: use only audit_context. Do not use biological evidence profiles and do not write the user-facing biological answer. "
        "Task: summarize whether the query ran, how much evidence was available, how strong the routed matrix support is, and what limitations affect interpretation. "
        "This output is for reports, debugging, and structured QA only. It must stay separate from the default answer body. "
        "Do not change any status, score, route count, or evidence grade. Do not add biological claims that are not present in audit_context. "
        "Return exactly one JSON object with keys: summary, verdict_rationale, confidence_rationale."
    )


def _biological_answer_quality_flags(result: dict[str, Any], query_type: str = "") -> list[str]:
    flags = []
    summary = str(result.get("answer") or result.get("biological_summary") or result.get("summary") or "").strip().lower()
    combined = summary
    for opener in ("pxfquery found", "evidence grade", "the evidence", "confidence", "matched rows", "matched profiles"):
        if summary.startswith(opener):
            flags.append(f"summary_starts_with:{opener}")
    for phrase in ("pxfquery", "not exact", "no exact evidence", "not reliable", "unreliable", "evidence grade", "matched rows", "route quality"):
        if phrase in combined:
            flags.append(f"forbidden_phrase:{phrase}")
    raw_patterns = (r"\bHALLMARK_[A-Z0-9_]+\b", r"\bMP\d+\b", r"\bKEGG_[A-Z0-9_]+\b", r"\bREACTOME_[A-Z0-9_]+\b")
    for pattern in raw_patterns:
        if re.search(pattern, str(result.get("answer") or "")):
            flags.append("raw_program_identifier")
            break
    if re.search(r"\bBRD-[A-Z]\d*[A-Z0-9-]*\b|\bBRDN\d+\b", str(result.get("answer") or ""), re.IGNORECASE):
        flags.append("raw_candidate_identifier")
    vague_phrases = ("some profiles", "some cell lines", "a subset", "partial signal", "may be affected")
    for phrase in vague_phrases:
        if phrase in summary:
            flags.append(f"vague_frequency_phrase:{phrase}")
    if query_type == "reverse":
        reverse_forbidden = (
            "weaker or no clear association",
            "no clear association",
            "not associated",
            "no effect",
        )
        for phrase in reverse_forbidden:
            if phrase in summary:
                flags.append(f"reverse_overdismissive_phrase:{phrase}")
        if re.search(r"\([A-Z][A-Z0-9-]{1,14}(?:,\s*[A-Z][A-Z0-9-]{1,14})+\)", str(result.get("answer") or "")):
            flags.append("reverse_parenthetical_gene_list")
        sentences = _answer_sentences(str(result.get("answer") or "").strip())
        if len(sentences) != 3:
            flags.append(f"reverse_answer_sentence_count:{len(sentences)}")
        gene_symbols = re.findall(r"\b[A-Z][A-Z0-9]{1,9}\b", str(result.get("answer") or ""))
        requested_terms = set(re.findall(r"\b[A-Z][A-Z0-9]{1,9}\b", str(result.get("subquestions") or "")))
        gene_like = sorted({item for item in gene_symbols if not item.startswith("BRD") and item not in requested_terms})
        if len(gene_like) > 5:
            flags.append("reverse_too_many_gene_symbols")
    if query_type == "forward":
        if "subquestion answers" in summary and "overall" not in summary:
            flags.append("subquestion_section_without_overall")
        if not result.get("subquestions"):
            answer_text = str(result.get("answer") or "").strip()
            sentences = _answer_sentences(answer_text)
            if len(sentences) != 3:
                flags.append(f"forward_answer_sentence_count:{len(sentences)}")
            for index, sentence in enumerate(sentences, start=1):
                if len(re.findall(r"\b[\w'-]+\b", sentence)) < 8:
                    flags.append(f"forward_answer_sentence_too_short:{index}")
            if re.search(r"\b(including|such as|for example)\b", answer_text, flags=re.IGNORECASE):
                flags.append("forward_answer_contains_example_clause")
    return flags


def _answer_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", str(text or "")).strip()
    if not compact:
        return []
    return [item.strip() for item in re.split(r"(?<=[.!?])\s+", compact) if item.strip()]


def _biological_answer_payload(
    claim_basis: dict[str, Any],
    matrix_evidence: dict[str, Any],
    annotation_evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    primary = matrix_evidence.get("primary_result") or {}
    is_reverse = matrix_evidence.get("mode") == "reverse"
    route_scope = _reverse_route_scope(matrix_evidence) if is_reverse else {}
    forward_policy = _forward_answer_policy(matrix_evidence) if not is_reverse else {}
    annotation_aliases = _annotation_alias_map(annotation_evidence or {})
    return {
        "user_question": claim_basis.get("user_question"),
        "interpreted_intent": {
            "query_type": matrix_evidence.get("mode"),
            "cell": primary.get("cell") if not is_reverse or route_scope.get("has_user_specified_cell") else None,
            "context_scope": route_scope.get("context_scope"),
            "searched_cells": route_scope.get("searched_cells"),
            "has_user_specified_cell": route_scope.get("has_user_specified_cell"),
            "perturbation": primary.get("perturbation"),
            "modality": primary.get("modality"),
            "score_orientation": primary.get("score_orientation"),
            "score_multiplier": primary.get("score_multiplier"),
            "evidence_interpretation": _score_orientation_interpretation(primary.get("score_orientation")),
            "requested_function_scores": primary.get("requested_function_scores"),
            "top_activated": _compact_rankings(primary.get("top_activated", [])),
            "top_suppressed": _compact_rankings(primary.get("top_suppressed", [])),
            "top_perturbations": _compact_rankings(primary.get("top_perturbations", [])) if not is_reverse else [],
        },
        "answer_policy": forward_policy,
        "program_summary": _forward_program_summary(matrix_evidence) if not is_reverse else [],
        "candidate_summary": _reverse_candidate_summary(matrix_evidence, annotation_aliases=annotation_aliases) if is_reverse else [],
        "evidence_profiles": _route_biology_context(matrix_evidence, annotation_aliases=annotation_aliases),
    }


def _forward_dimension_answer_payload(raw_payload: dict[str, Any], dimension_result: dict[str, Any]) -> dict[str, Any]:
    return {
        "user_question": raw_payload.get("user_question"),
        "queried_perturbation": (raw_payload.get("interpreted_intent") or {}).get("perturbation"),
        "state_axes": {
            "promoted_axis": dimension_result.get("promoted_axis"),
            "suppressed_axis": dimension_result.get("suppressed_axis"),
            "overall_state": dimension_result.get("overall_state"),
            "axis_meanings": _json_safe(dimension_result.get("axis_meanings") or {}),
        },
    }


def _forward_response_dimension_payload(raw_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "user_question": raw_payload.get("user_question"),
        "answer_policy": raw_payload.get("answer_policy"),
        "increased_evidence": _directional_profile_evidence(raw_payload, "activated_programs", max_items=10),
        "decreased_evidence": _directional_profile_evidence(raw_payload, "suppressed_programs", max_items=10),
    }


def _directional_profile_evidence(raw_payload: dict[str, Any], key: str, *, max_items: int) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for profile in raw_payload.get("evidence_profiles") or []:
        for item in profile.get(key) or []:
            label = item.get("label") or item.get("function")
            if not label:
                continue
            group = groups.setdefault(str(label), {"label": str(label), "support_profiles": 0, "scores": []})
            group["support_profiles"] += 1
            score = _float_or_none(item.get("score"))
            if score is not None:
                group["scores"].append(score)
    rows = []
    for group in groups.values():
        scores = group.get("scores") or []
        mean_score = sum(scores) / len(scores) if scores else None
        rows.append(
            {
                "label": group["label"],
                "support_profiles": group["support_profiles"],
                "mean_score": mean_score,
            }
        )
    rows.sort(key=lambda item: (-item["support_profiles"], -(abs(item["mean_score"]) if item["mean_score"] is not None else 0.0), item["label"]))
    return rows[:max_items]


def _forward_answer_policy(matrix_evidence: dict[str, Any]) -> dict[str, Any]:
    routes = matrix_evidence.get("executed_routes") or []
    has_direct_anchor = any(_is_direct_forward_route(route) for route in routes)
    if has_direct_anchor:
        return {
            "mode": "direct_anchor_with_support",
            "main_answer_rule": "Anchor the answer on directly matched evidence and use other matched profiles as support or qualification.",
        }
    return {
        "mode": "cross_match_consensus",
        "main_answer_rule": "No directly matched anchor is available; answer from cross-profile consensus.",
    }


def _forward_program_summary(matrix_evidence: dict[str, Any], *, max_programs: int = 12) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for route in matrix_evidence.get("executed_routes") or []:
        route_id = route.get("route_id")
        cell = route.get("cell")
        is_direct = _is_direct_forward_route(route)
        for direction_key, default_direction in (("top_activated", "activated"), ("top_suppressed", "suppressed")):
            for item in route.get(direction_key) or []:
                label = item.get("label") or item.get("function")
                if not label:
                    continue
                score = _float_or_none(item.get("score"))
                if score is None:
                    continue
                direction = str(item.get("direction") or default_direction).lower()
                signed_score = _signed_forward_score(score, direction)
                key = _function_key(str(label))
                group = groups.setdefault(
                    key,
                    {
                        "label": str(label),
                        "scores": [],
                        "route_ids": set(),
                        "cells": set(),
                        "direct_route_ids": set(),
                        "activated_route_ids": set(),
                        "suppressed_route_ids": set(),
                        "best_abs_score": 0.0,
                    },
                )
                group["scores"].append(signed_score)
                if route_id:
                    route_id_str = str(route_id)
                    group["route_ids"].add(route_id_str)
                    if signed_score >= 0:
                        group["activated_route_ids"].add(route_id_str)
                    else:
                        group["suppressed_route_ids"].add(route_id_str)
                    if is_direct:
                        group["direct_route_ids"].add(route_id_str)
                if cell:
                    group["cells"].add(str(cell))
                group["best_abs_score"] = max(group["best_abs_score"], abs(score))

    rows: list[dict[str, Any]] = []
    for group in groups.values():
        scores = group.get("scores") or []
        activated_support = len(group["activated_route_ids"])
        suppressed_support = len(group["suppressed_route_ids"])
        if activated_support > suppressed_support:
            direction = "activated"
        elif suppressed_support > activated_support:
            direction = "suppressed"
        else:
            mean_signed_score = sum(scores) / len(scores) if scores else 0.0
            if mean_signed_score > 0:
                direction = "activated"
            elif mean_signed_score < 0:
                direction = "suppressed"
            else:
                direction = "mixed"
        mean_signed_score = sum(scores) / len(scores) if scores else 0.0
        mean_abs_score = sum(abs(value) for value in scores) / len(scores) if scores else 0.0
        rows.append(
            {
                "label": group["label"],
                "direction": direction,
                "mean_score": mean_signed_score,
                "mean_abs_score": mean_abs_score,
                "best_abs_score": group["best_abs_score"],
                "support_profiles": len(group["route_ids"]),
                "support_contexts": len(group["cells"]),
                "direct_support": bool(group["direct_route_ids"]),
                "direct_support_profiles": len(group["direct_route_ids"]),
                "activated_support_profiles": activated_support,
                "suppressed_support_profiles": suppressed_support,
                "direction_consistent": not (activated_support and suppressed_support),
            }
        )

    has_direct_support = any(item["direct_support_profiles"] for item in rows)
    if has_direct_support:
        rows.sort(
            key=lambda item: (
                -item["direct_support_profiles"],
                -item["support_profiles"],
                -item["support_contexts"],
                not item["direction_consistent"],
                -(item.get("mean_abs_score") or 0.0),
                -(item.get("best_abs_score") or 0.0),
                str(item.get("label") or ""),
            )
        )
    else:
        rows.sort(
            key=lambda item: (
                -item["support_profiles"],
                -item["support_contexts"],
                not item["direction_consistent"],
                -(item.get("mean_abs_score") or 0.0),
                -(item.get("best_abs_score") or 0.0),
                str(item.get("label") or ""),
            )
        )
    for rank, row in enumerate(rows[:max_programs], start=1):
        row["rank"] = rank
    return rows[:max_programs]


def _function_key(label: str) -> str:
    return re.sub(r"\s+", " ", str(label).replace("_", " ").strip()).casefold()


def _float_or_none(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _signed_forward_score(score: float, direction: str) -> float:
    normalized = str(direction or "").strip().casefold().replace("-", "_")
    if normalized in {"activated", "activation", "activate", "up", "upregulated", "up_regulated", "positive"}:
        return abs(score)
    if normalized in {"suppressed", "suppression", "suppress", "down", "downregulated", "down_regulated", "negative"}:
        return -abs(score)
    return abs(score) if score >= 0 else -abs(score)


def _is_direct_forward_route(route: dict[str, Any]) -> bool:
    cell_match = str(route.get("cell_match_type") or route.get("cell_role") or "").casefold()
    pert_match = str(route.get("perturbation_match_type") or route.get("perturbation_role") or "").casefold()
    cell_distance = _float_or_none(route.get("cell_match_distance"))
    pert_distance = _float_or_none(route.get("perturbation_match_distance"))
    cell_direct = "user_specified" in cell_match or "exact" in cell_match or cell_distance == 0.0
    pert_direct = "user_specified" in pert_match or "exact" in pert_match or "mechanism" in pert_match or pert_distance == 0.0
    return bool(cell_direct and pert_direct)


def _route_biology_context(matrix_evidence: dict[str, Any], *, annotation_aliases: dict[str, str] | None = None) -> list[dict[str, Any]]:
    profiles = []
    for route in matrix_evidence.get("executed_routes") or []:
        profile: dict[str, Any] = {
            "cell": route.get("cell"),
            "perturbation": route.get("perturbation_alias") or route.get("perturbation"),
            "modality": route.get("modality"),
            "score_orientation": route.get("score_orientation"),
            "score_multiplier": route.get("score_multiplier"),
            "evidence_interpretation": _score_orientation_interpretation(route.get("score_orientation")),
            "recommended_operation": route.get("recommended_operation"),
        }
        if matrix_evidence.get("mode") == "forward":
            profile["activated_programs"] = _compact_rankings(route.get("top_activated", []))
            profile["suppressed_programs"] = _compact_rankings(route.get("top_suppressed", []))
            requested = route.get("requested_function_records")
            if requested:
                profile["requested_function_records"] = _json_safe(requested)
        elif matrix_evidence.get("mode") == "reverse":
            profile["candidate_perturbations"] = _compact_reverse_candidates(route.get("top_perturbations", []), modality=route.get("modality"), annotation_aliases=annotation_aliases or {})
        profiles.append({key: value for key, value in profile.items() if value not in (None, [], {})})
    return profiles


def _reverse_route_scope(matrix_evidence: dict[str, Any]) -> dict[str, Any]:
    routes = matrix_evidence.get("executed_routes") or []
    searched_cells = [route.get("cell") for route in routes if route.get("cell")]
    has_user_specified = any(route.get("cell_match_type") == "user_specified_cell" for route in routes)
    return {
        "context_scope": "user_specified_cell" if has_user_specified else "concept_or_disease_model_set",
        "has_user_specified_cell": has_user_specified,
        "searched_cells": searched_cells,
    }


def _reverse_candidate_summary(matrix_evidence: dict[str, Any], *, max_candidates: int = 12, annotation_aliases: dict[str, str] | None = None) -> list[dict[str, Any]]:
    routes = matrix_evidence.get("executed_routes") or []
    exact_route_ids = {route.get("route_id") for route in routes if route.get("cell_match_type") == "user_specified_cell"}
    groups: dict[str, dict[str, Any]] = {}
    for route in routes:
        route_id = route.get("route_id")
        cell = route.get("cell")
        modality = route.get("modality")
        is_exact_route = route_id in exact_route_ids
        for item in route.get("top_perturbations") or []:
            if _unreadable_reverse_candidate(item, modality=modality):
                continue
            key = _candidate_key(item)
            if not key:
                continue
            score = item.get("score")
            try:
                score_value = float(score)
            except (TypeError, ValueError):
                continue
            group = groups.setdefault(
                key,
                {
                    "label": item.get("label") or item.get("cmap_name") or item.get("pert_id") or key,
                    "modality": modality,
                    "scores": [],
                    "exact_scores": [],
                    "cells": set(),
                    "route_ids": set(),
                    "best": None,
                },
            )
            group["scores"].append(score_value)
            if is_exact_route:
                group["exact_scores"].append(score_value)
            if cell:
                group["cells"].add(cell)
            if route_id:
                group["route_ids"].add(route_id)
            if group["best"] is None or score_value > group["best"]["score"]:
                group["best"] = {"score": score_value, "cell": cell, "route_id": route_id}
    rows = []
    for group in groups.values():
        scores = group["scores"]
        exact_scores = group["exact_scores"]
        best = group.get("best") or {}
        exact_score = sum(exact_scores) / len(exact_scores) if exact_scores else None
        mean_score = sum(scores) / len(scores)
        rows.append(
            {
                "label": _display_reverse_candidate_label(group["label"], modality=group.get("modality"), annotation_aliases=annotation_aliases or {}),
                "raw_identifier": group["label"] if _raw_candidate_identifier(group["label"]) else None,
                "annotation_status": _reverse_annotation_status(group["label"], modality=group.get("modality"), annotation_aliases=annotation_aliases or {}),
                "score": exact_score if exact_score is not None else mean_score,
                "exact_cell_support": bool(exact_scores),
                "mean_score": mean_score,
                "best_score": best.get("score"),
                "support_routes": len(group["route_ids"]),
                "support_cells": len(group["cells"]),
                "cells": sorted(group["cells"]),
                "best_cell": best.get("cell"),
            }
        )
    if exact_route_ids:
        rows.sort(key=lambda item: (not item["exact_cell_support"], -(item["score"] or 0.0), -item["support_routes"], str(item["label"])))
    else:
        rows.sort(key=lambda item: (-item["support_routes"], -item["support_cells"], -(item["score"] or 0.0), str(item["label"])))
    for rank, row in enumerate(rows[:max_candidates], start=1):
        row["rank"] = rank
    return rows[:max_candidates]


def _compact_reverse_candidates(items: list[dict[str, Any]], *, modality: str | None, annotation_aliases: dict[str, str] | None = None) -> list[dict[str, Any]]:
    compact = []
    for item in items:
        if _unreadable_reverse_candidate(item, modality=modality):
            continue
        row = _compact_rankings([item])[0]
        label = row.get("label")
        row["label"] = _display_reverse_candidate_label(label, modality=modality, annotation_aliases=annotation_aliases or {})
        if _raw_candidate_identifier(label):
            row["raw_identifier"] = label
            row["annotation_status"] = _reverse_annotation_status(label, modality=modality, annotation_aliases=annotation_aliases or {})
        compact.append(row)
        if len(compact) >= 8:
            break
    return compact


def _unreadable_reverse_candidate(item: dict[str, Any], *, modality: str | None) -> bool:
    label = str(item.get("label") or item.get("cmap_name") or item.get("pert_id") or "").strip()
    if modality in {"sh", "xpr"} and re.fullmatch(r"BRDN\d+", label):
        return True
    if modality in {"sh", "xpr"} and not _looks_like_gene_symbol(label):
        return True
    return False


def _looks_like_gene_symbol(value: Any) -> bool:
    text = str(value or "").strip()
    if not text:
        return False
    return bool(re.fullmatch(r"[A-Z][A-Z0-9-]{1,14}", text))


def _display_reverse_candidate_label(value: Any, *, modality: str | None, annotation_aliases: dict[str, str] | None = None) -> str:
    label = str(value or "").strip()
    annotated = (annotation_aliases or {}).get(label.upper())
    if annotated:
        return annotated
    if modality == "cp" and _raw_candidate_identifier(label):
        return "unnamed compound candidate"
    return label


def _reverse_annotation_status(value: Any, *, modality: str | None, annotation_aliases: dict[str, str] | None = None) -> str:
    label = str(value or "").strip()
    if not _raw_candidate_identifier(label):
        return "not_required"
    if modality == "cp" and (annotation_aliases or {}).get(label.upper()):
        return "annotated"
    if modality == "cp":
        return "alias_missing"
    return "not_user_facing"


def _annotation_alias_map(annotation_evidence: dict[str, Any]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for block in annotation_evidence.get("records") or []:
        if block.get("status") not in {"completed", "ok"}:
            continue
        for hit in block.get("records") or []:
            term = str(hit.get("term") or "").strip().upper()
            if not term:
                continue
            for record in hit.get("records") or []:
                pref = str(record.get("pref_name") or "").strip()
                if pref:
                    aliases[term] = pref
                    break
    return aliases


def _raw_candidate_identifier(value: Any) -> bool:
    text = str(value or "").strip()
    return bool(re.fullmatch(r"BRD-[A-Z][A-Z0-9-]*", text, flags=re.IGNORECASE) or re.fullmatch(r"BRDN\d+", text, flags=re.IGNORECASE))


def _candidate_key(item: dict[str, Any]) -> str:
    for key in ("pert_id", "cmap_name", "label", "name"):
        value = item.get(key)
        if value is not None and str(value).strip():
            return str(value).strip().lower()
    return ""


def _score_orientation_interpretation(value: str | None) -> str | None:
    if value == "inferred_activation_from_lof":
        return "activation or overexpression effect inferred by reversing CRISPR/RNAi loss-of-function scores; not direct overexpression data"
    if value == "observed_lof_perturbation_effect":
        return "observed loss-of-function genetic perturbation effect"
    if value == "observed_drug_perturbation_effect":
        return "observed compound perturbation effect"
    if value == "observed_perturbation_effect":
        return "observed perturbation effect"
    return value


def _execution_quality_payload(
    claim_basis: dict[str, Any],
    route_evidence: dict[str, Any],
    matrix_evidence: dict[str, Any],
    literature_evidence: dict[str, Any],
    limitations: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "audit_context": {
            "answerability": claim_basis.get("answerability"),
            "claim_strength": claim_basis.get("claim_strength"),
            "claim_type": claim_basis.get("claim_type"),
            "evidence_grade": _evidence_grade_semantics(claim_basis.get("must_mention", [])).get("grade"),
            "must_not_claim": claim_basis.get("must_not_claim"),
            "limitations": _json_safe(limitations),
            "selected_route_count": len(route_evidence.get("selected_routes") or []),
            "executed_route_count": len(matrix_evidence.get("executed_routes") or []),
            "skipped_route_count": len(matrix_evidence.get("skipped_routes") or []),
            "execution_status": matrix_evidence.get("execution_status"),
            "literature_status": literature_evidence.get("status"),
        },
    }


def _evidence_grade_semantics(must_mention: list[str]) -> dict[str, str]:
    grade = next((str(item) for item in must_mention if str(item).endswith("_matrix") or "proxy_support" in str(item)), "")
    if grade == "exact_primary_with_proxy_support":
        return {
            "grade": grade,
            "meaning": "The primary route is exact matrix evidence. Proxy routes are supporting references only.",
            "required_phrase": "exact primary matrix evidence with proxy support",
            "forbidden_interpretation": "Do not say this means no exact evidence. Do not say all selected routes are exact.",
        }
    if grade == "exact_matrix":
        return {"grade": grade, "meaning": "The selected matrix evidence is exact for the routed query."}
    if "proxy" in grade or grade == "weak_matrix":
        return {"grade": grade, "meaning": "The evidence is proxy or weak matrix evidence, not exact primary evidence."}
    return {"grade": grade, "meaning": "Use claim_basis.must_mention and limitations without upgrading the evidence grade."}


def _compact_rankings(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact = []
    for item in items[:5]:
        compact.append(
            {
                "rank": item.get("rank"),
                "label": item.get("label") or item.get("cmap_name") or item.get("pert_id"),
                "score": item.get("score"),
                "direction": item.get("direction"),
                "recommended_operation": item.get("recommended_operation"),
            }
        )
    return compact


def _failure_mode(status: str, execution: dict[str, Any], route_plan: dict[str, Any]) -> dict[str, Any] | None:
    if status in {"evidence_found", "partial_evidence"}:
        return None
    errors = execution.get("errors") or []
    return {
        "status": status,
        "route_status": route_plan.get("route_status"),
        "first_error": _json_safe(errors[0]) if errors else None,
    }


def _rendering_hints(claim_basis: dict[str, Any], evidence_grade: str) -> dict[str, Any]:
    return {
        "default_user_view": "plain_answer",
        "comparison_ready": claim_basis.get("answerability") in {"answered", "partially_answered", "not_answered"},
        "recommended_l5_modes": ["plain_answer", "evidence_summary", "audit_report"],
        "allowed_transformations": ["summarize", "translate", "format", "tabulate"],
        "forbidden_transformations": [
            "change_execution_status",
            "change_scores",
            "add_candidates",
            "drop_limitations",
            "convert_proxy_to_exact",
            "convert_no_hit_to_found",
            "invent_pubmed_citations",
        ],
        "evidence_grade": evidence_grade,
    }


def _debug_layer(route_plan: dict[str, Any], *, include_rejected: bool) -> dict[str, Any]:
    rejected = route_plan.get("rejected_candidates", []) if include_rejected else []
    return {
        "available": bool(include_rejected),
        "rejected_candidates": _json_safe(rejected),
        "rejected_candidate_count": len(route_plan.get("rejected_candidates", []) or []),
        "default_visibility": "hidden",
    }


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    return str(value)

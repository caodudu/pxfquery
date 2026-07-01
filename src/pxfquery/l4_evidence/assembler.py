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
    llm_synthesis = _llm_synthesis(llm_provider, synthesize, claim_basis, route_evidence, matrix_evidence, literature_evidence, limitations)

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
) -> dict[str, Any]:
    if not synthesize:
        return {"status": "disabled", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "L4 LLM synthesis was not requested."}}
    if llm_provider is None:
        return {"status": "unavailable", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "No LLM provider was configured for L4 synthesis."}}
    if not hasattr(llm_provider, "request_json"):
        return {"status": "unavailable", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": "LLM provider does not expose request_json(...)."}}

    biological_payload = _biological_answer_payload(claim_basis, matrix_evidence)
    audit_payload = _execution_quality_payload(claim_basis, route_evidence, matrix_evidence, literature_evidence, limitations)
    provider_evidence: dict[str, Any] = {}
    diagnostics: dict[str, Any] = {}

    try:
        biological_result, biological_evidence = _request_json_with_max_tokens(
            llm_provider,
            max_tokens=1600,
            stage=f"l4_{matrix_evidence.get('mode') or 'query'}_biological_answer",
            system_prompt=_biological_answer_system_prompt(str(matrix_evidence.get("mode") or "")),
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

    quality_flags = _biological_answer_quality_flags(biological_result, str(matrix_evidence.get("mode") or ""))
    if quality_flags:
        try:
            repaired, repair_evidence = _request_json_with_max_tokens(
                llm_provider,
                max_tokens=1600,
                stage="l4_biological_answer_repair",
                system_prompt=(
                    _biological_answer_system_prompt(str(matrix_evidence.get("mode") or ""))
                    + " The previous JSON failed these quality checks: "
                    + ", ".join(quality_flags)
                    + ". Rewrite only the same biological answer from the same evidence."
                ),
                user_payload=biological_payload | {"previous_invalid_answer": biological_result, "quality_flags": quality_flags},
            )
            if isinstance(repaired, dict) and not _biological_answer_quality_flags(repaired, str(matrix_evidence.get("mode") or "")):
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


def _forward_biological_answer_system_prompt() -> str:
    return """
Role
You are the biological answer writer for a forward functional perturbation query.

Input
You receive exactly three inputs:
- user_question: the user's original question.
- interpreted_intent: parsed biological context, perturbation, modality, and primary ranked functions.
- evidence_profiles: one or more matched profiles. Each profile contains a cell/context, perturbation label, activated_programs, and suppressed_programs.

Task
Write the default user-facing biological answer. First identify whether user_question contains one biological question or multiple biological subquestions. Then answer using only interpreted_intent and evidence_profiles. Synthesize across all evidence_profiles; do not answer from only the first profile when multiple profiles are supplied.

Required reasoning behavior
- Convert raw program labels into readable biological phrases.
- Separate increased and decreased functional programs.
- If score_orientation says activation is inferred from loss-of-function evidence, interpret directions as a reverse-direction inference from CRISPR/RNAi loss-of-function data, not as direct overexpression measurements.
- If the user asks whether a named program family is affected, judge it semantically from supplied program labels and directions. Use one of: supported, not supported, or not resolved.
- If evidence is mixed across profiles, say it is mixed and describe the main directions.
- If a requested subquestion is not covered by supplied program labels, say not resolved from the supplied functional evidence.
- Do not collapse multiple user subquestions into one paragraph. Give a separate answer for each subquestion.
- Do not use vague frequency phrases as the main conclusion, such as "some profiles", "a subset", "partial signal", or "may be affected". Convert the evidence into a clear verdict for each subquestion: supported, not supported, mixed, or not resolved.
- If evidence differs across profiles, explain the biological direction of the conflict instead of saying only that it is partial or heterogeneous.
- For program-family questions, do not answer with a vague frequency statement. Say whether the family is supported, not supported, mixed, or not resolved, and name the readable labels that justify the verdict.
- If user_question has only one biological question, do not repeat it as a separate subquestion section. Put the full answer in the answer field and set subquestions to an empty array.
- If user_question has multiple biological subquestions, the answer field must start with "Overall:" and then include "Subquestion answers:" with numbered answers.
- Match the language of user_question.

Forbidden in answer
- Do not mention software, internal layers, routes, evidence grades, exact/proxy status, row counts, scores, benchmarks, missing literature, clinical efficacy, or validation status.
- Do not mention PxFquery.
- Do not invent mechanisms, citations, functions, cells, perturbations, or numeric values.
- Do not expose raw program identifiers such as all-caps database IDs or numbered program codes. Use readable biological phrases instead.
- Do not describe inferred activation evidence as direct overexpression evidence.

Output JSON schema
Return exactly one JSON object:
{
  "answer": "Complete user-facing answer. Single-question inputs use one direct answer. Multi-subquestion inputs use 'Overall:' plus 'Subquestion answers:'.",
  "subquestions": ["Short subquestion followed by its direct answer."],
  "main_program_changes": ["activated: readable program description", "suppressed: readable program description"],
  "support_notes": ["Short grounded note using readable biological phrases."]
}

Style example
Input summary A: user asks one question: what programs change after perturbation X in model Y. Evidence profiles show activated labels related to program group B and suppressed labels related to program group C.
Valid single-question output shape:
{
  "answer": "In model Y, perturbation X is associated mainly with increased program group B and decreased program group C.",
  "subquestions": [],
  "main_program_changes": [
    "activated: program group B",
    "suppressed: program group C"
  ],
  "support_notes": ["The answer is based only on supplied functional program labels."]
}

Input summary B: user asks what programs change after perturbation X in model Y, and also asks whether program family A is affected. Evidence profiles show activated labels related to program group B and suppressed labels related to program group C; no supplied label clearly maps to family A.
Valid multi-subquestion output shape:
{
  "answer": "Overall: In model Y, perturbation X is associated mainly with increased program group B and decreased program group C. Program family A is not resolved because the changed programs do not clearly correspond to that family.\n\nSubquestion answers:\n1. What functional programs change after perturbation X? The main supported changes are increased program group B and decreased program group C.\n2. Is program family A affected? Not resolved. The supplied changed programs do not clearly map to program family A, so the evidence does not support a confident yes-or-no answer.",
  "subquestions": [
    "What functional programs change after perturbation X? The main supported changes are increased program group B and decreased program group C.",
    "Is program family A affected? Not resolved because the supplied changed programs do not clearly map to program family A."
  ],
  "main_program_changes": [
    "activated: program group B",
    "suppressed: program group C"
  ],
  "support_notes": ["The answer is based only on supplied functional program labels."]
}
""".strip()


def _reverse_biological_answer_system_prompt() -> str:
    return """
Role
You are the biological answer writer for a reverse functional perturbation query.

Input
You receive exactly four inputs:
- user_question: the user's original question.
- interpreted_intent: parsed biological context, context_scope, searched_cells, and requested functional state.
- candidate_summary: cross-profile candidate summary. It is the primary candidate ranking for reverse queries.
- evidence_profiles: matched profiles containing candidate_perturbations or candidate genes with their functional match evidence.

Task
Write the default user-facing biological answer. Identify what functional state the user wants, then explain which candidate perturbations or genes best match that state using only interpreted_intent, candidate_summary, and evidence_profiles.

Required reasoning behavior
- Start with candidate_summary, not the first evidence profile.
- If interpreted_intent.context_scope is concept_or_disease_model_set, answer at the disease/model-set level. Do not frame the answer as "in [first cell line]" or imply the first searched cell is the user's requested model.
- If interpreted_intent.has_user_specified_cell is true, prioritize candidates with exact_cell_support. Other cells may only be described as supporting or broader-context evidence.
- If interpreted_intent.has_user_specified_cell is false, rank candidates by cross-profile support and mean/best functional match in candidate_summary.
- Explain the functional direction each candidate supports.
- Distinguish strong matches, partial matches, and unresolved candidates using the supplied evidence.
- If the supplied evidence does not support a clear candidate, say not resolved from the supplied functional evidence.
- Mention searched cell lines only when needed to explain model-set support; do not make them the headline unless the user specified a cell line.

Forbidden in answer
- Do not mention software, internal layers, routes, evidence grades, exact/proxy status, row counts, scores, benchmarks, missing literature, clinical efficacy, or validation status.
- Do not mention PxFquery.
- Do not invent mechanisms, citations, candidates, functions, cells, perturbations, or numeric values.

Output JSON schema
Return exactly one JSON object:
{
  "answer": "A concise biological answer written in complete sentences.",
  "subquestions": ["Short subquestion followed by its direct answer."],
  "candidate_interpretation": ["candidate label: readable functional interpretation"],
  "support_notes": ["Short grounded note using readable biological phrases."]
}

Style example
Input summary: user asks which perturbation could produce functional state Z in model Y. Evidence profiles contain candidates X and W; X matches the requested activated program group and W is only a partial match.
Valid output shape:
{
  "answer": "Candidate X is the clearest match for functional state Z in model Y because it aligns with the requested activated program group. Candidate W is a weaker, partial match because it covers only part of the requested state.",
  "subquestions": [
    "Which candidate best matches functional state Z? Candidate X is the clearest match."
  ],
  "candidate_interpretation": [
    "candidate X: matches the requested activated program group",
    "candidate W: partial match to the requested state"
  ],
  "support_notes": ["Candidate interpretation is based only on supplied functional match evidence."]
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
    vague_phrases = ("some profiles", "some cell lines", "a subset", "partial signal", "may be affected")
    for phrase in vague_phrases:
        if phrase in summary:
            flags.append(f"vague_frequency_phrase:{phrase}")
    if query_type == "forward":
        if "subquestion answers" in summary and "overall" not in summary:
            flags.append("subquestion_section_without_overall")
    return flags


def _biological_answer_payload(
    claim_basis: dict[str, Any],
    matrix_evidence: dict[str, Any],
) -> dict[str, Any]:
    primary = matrix_evidence.get("primary_result") or {}
    is_reverse = matrix_evidence.get("mode") == "reverse"
    route_scope = _reverse_route_scope(matrix_evidence) if is_reverse else {}
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
        "candidate_summary": _reverse_candidate_summary(matrix_evidence) if is_reverse else [],
        "evidence_profiles": _route_biology_context(matrix_evidence),
    }


def _route_biology_context(matrix_evidence: dict[str, Any]) -> list[dict[str, Any]]:
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
            profile["candidate_perturbations"] = _compact_reverse_candidates(route.get("top_perturbations", []), modality=route.get("modality"))
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


def _reverse_candidate_summary(matrix_evidence: dict[str, Any], *, max_candidates: int = 12) -> list[dict[str, Any]]:
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
                "label": group["label"],
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


def _compact_reverse_candidates(items: list[dict[str, Any]], *, modality: str | None) -> list[dict[str, Any]]:
    compact = []
    for item in items:
        if _unreadable_reverse_candidate(item, modality=modality):
            continue
        compact.extend(_compact_rankings([item]))
        if len(compact) >= 8:
            break
    return compact


def _unreadable_reverse_candidate(item: dict[str, Any], *, modality: str | None) -> bool:
    if modality not in {"sh", "xpr"}:
        return False
    label = str(item.get("label") or item.get("cmap_name") or item.get("pert_id") or "").strip()
    return bool(re.fullmatch(r"BRDN\d+", label))


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

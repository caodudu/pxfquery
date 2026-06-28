from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


L4_SCHEMA_VERSION = "l4-evidence-dossier/v1"


def assemble_evidence(
    execution: Any,
    *,
    intent: Any | None = None,
    route_plan: Any | None = None,
    llm_provider: Any | None = None,
    synthesize: bool = False,
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
    route_text = " ".join(_route_tiers(execution, route_plan)).lower()
    has_exact = "exact_cell_exact_perturbation" in route_text
    has_proxy = "proxy" in route_text or "normal_lineage_anchor" in route_text
    if "observed_anchor" in route_text or "weak" in route_text:
        return "weak_matrix"
    if has_exact and has_proxy:
        return "exact_primary_with_proxy_support" if status == "evidence_found" else "partial_exact_primary_with_proxy_support"
    if has_proxy:
        return "proxy_matrix" if status == "evidence_found" else "partial_proxy_matrix"
    if status == "partial_evidence":
        return "partial_matrix"
    return "exact_matrix"


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


def _route_summary(route: dict[str, Any]) -> dict[str, Any]:
    metadata = route.get("route_metadata") or {}
    row_match = route.get("row_match") or {}
    return {
        "route_id": route.get("route_id"),
        "query_type": route.get("query_type"),
        "modality": route.get("modality"),
        "status": route.get("status"),
        "cell": route.get("cell"),
        "tier": metadata.get("tier"),
        "cell_role": metadata.get("cell_role"),
        "perturbation_role": metadata.get("perturbation_role"),
        "pair_search_reason": metadata.get("pair_search_reason"),
        "n_rows": row_match.get("n_rows"),
        "n_ranked_groups": row_match.get("n_ranked_groups"),
        "diagnostics": _json_safe(route.get("diagnostics", {})),
    }


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
    if evidence_grade in {"exact_primary_with_proxy_support", "partial_exact_primary_with_proxy_support"}:
        items.append({"code": "proxy_support_present", "message": f"Evidence grade is {evidence_grade}; L5 must present proxy routes as supporting references, not as the primary exact route."})
    elif "proxy" in evidence_grade or evidence_grade == "weak_matrix":
        items.append({"code": "proxy_or_weak_evidence", "message": f"Evidence grade is {evidence_grade}; L5 must not describe it as exact evidence."})
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
    if evidence_grade == "exact_matrix" and not limitations:
        return "high"
    if evidence_grade == "exact_primary_with_proxy_support":
        return "moderate"
    if evidence_grade in {"proxy_matrix", "weak_matrix"}:
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
    if evidence_grade not in {"exact_matrix", "exact_primary_with_proxy_support"}:
        claims.append("exact matrix evidence")
    if evidence_grade == "exact_primary_with_proxy_support":
        claims.append("all selected evidence routes were exact")
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
    payload = _synthesis_payload(claim_basis, route_evidence, matrix_evidence, literature_evidence, limitations)
    try:
        result, evidence = llm_provider.request_json(
            stage="l4_evidence",
            system_prompt=(
                "Summarize the supplied compact PxFquery evidence as one small valid JSON object. "
                "Use concise strings. Do not use markdown. Do not add candidates, "
                "do not alter scores, do not invent citations, and do not convert no-hit, proxy, "
                "or partial evidence into exact evidence. Preserve evidence_grade semantics exactly. "
                "For exact_primary_with_proxy_support, state that exact primary matrix evidence is present "
                "and proxy routes are supporting references; do not call it 'not exact' and do not call all routes exact. "
                "Return keys: summary, verdict_rationale, "
                "confidence_rationale, limitations_summary."
            ),
            user_payload=payload,
            temperature=0,
        )
    except Exception as exc:
        return {"status": "failed", "summary": None, "provider_evidence": {}, "diagnostics": {"reason": str(exc)}}
    if not isinstance(result, dict):
        return {"status": "failed", "summary": None, "provider_evidence": _json_safe(evidence), "diagnostics": {"reason": "LLM synthesis returned non-object JSON."}}
    return {
        "status": "completed",
        "summary": result.get("summary"),
        "verdict_rationale": result.get("verdict_rationale"),
        "confidence_rationale": result.get("confidence_rationale"),
        "limitations_summary": result.get("limitations_summary"),
        "provider_evidence": _json_safe(evidence),
        "diagnostics": {},
    }


def _synthesis_payload(
    claim_basis: dict[str, Any],
    route_evidence: dict[str, Any],
    matrix_evidence: dict[str, Any],
    literature_evidence: dict[str, Any],
    limitations: list[dict[str, Any]],
) -> dict[str, Any]:
    primary = matrix_evidence.get("primary_result") or {}
    return {
        "claim_basis": {
            "answerability": claim_basis.get("answerability"),
            "main_claim": claim_basis.get("main_claim"),
            "claim_type": claim_basis.get("claim_type"),
            "claim_strength": claim_basis.get("claim_strength"),
            "must_mention": claim_basis.get("must_mention"),
            "must_not_claim": claim_basis.get("must_not_claim"),
        },
        "evidence_grade_semantics": _evidence_grade_semantics(claim_basis.get("must_mention", [])),
        "route_summary": {
            "status": route_evidence.get("status"),
            "selected_route_count": len(route_evidence.get("selected_routes") or []),
            "primary_route": (route_evidence.get("selected_routes") or [{}])[0],
        },
        "matrix_summary": {
            "mode": matrix_evidence.get("mode"),
            "execution_status": matrix_evidence.get("execution_status"),
            "primary_cell": primary.get("cell"),
            "primary_perturbation": primary.get("perturbation"),
            "primary_modality": primary.get("modality"),
            "primary_n_rows": primary.get("n_rows"),
            "top_activated": _compact_rankings(primary.get("top_activated", [])),
            "top_suppressed": _compact_rankings(primary.get("top_suppressed", [])),
            "top_perturbations": _compact_rankings(primary.get("top_perturbations", [])),
        },
        "literature_status": literature_evidence.get("status"),
        "limitations": limitations[:5],
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

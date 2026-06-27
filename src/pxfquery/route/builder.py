from __future__ import annotations

from typing import Any

from pxfquery.route.models import (
    Diagnostics,
    EvidenceRouteResponse,
    FunctionResponse,
    PerturbationResolution,
    ProxyStep,
    QueryContext,
    Suggestion,
)
from pxfquery.route.types import (
    Confidence,
    FunctionStatus,
    RouteType,
)


def build_route_response(
    route_type: RouteType,
    query_context: QueryContext | None = None,
    perturbation_resolution: PerturbationResolution | None = None,
    function_response: FunctionResponse | None = None,
    confidence: Confidence | None = None,
    proxy_chain: list[ProxyStep] | None = None,
    diagnostics: Diagnostics | None = None,
    suggestions: list[Suggestion] | None = None,
    overrides: dict[str, Any] | None = None,
) -> EvidenceRouteResponse:
    if not isinstance(route_type, RouteType):
        raise ValueError(f"route_type must be a RouteType enum, got {type(route_type).__name__}")

    _validate_required_fields(
        route_type,
        query_context,
        perturbation_resolution,
        proxy_chain,
        diagnostics,
        suggestions,
    )

    defaults = _get_route_defaults(route_type)

    resp = EvidenceRouteResponse(
        route_type=route_type,
        query_context=query_context or defaults.get("query_context"),
        perturbation_resolution=perturbation_resolution or defaults.get("perturbation_resolution"),
        function_response=function_response or defaults.get("function_response"),
        confidence=confidence or defaults.get("confidence"),
        proxy_chain=proxy_chain if proxy_chain is not None else (defaults.get("proxy_chain") or []),
        diagnostics=diagnostics or defaults.get("diagnostics"),
        suggestions=suggestions if suggestions is not None else (defaults.get("suggestions") or []),
    )

    if overrides:
        for key, value in overrides.items():
            if hasattr(resp, key):
                setattr(resp, key, value)

    return resp


def _get_route_defaults(route_type: RouteType) -> dict:
    defaults = {
        RouteType.EXACT_HIT: {
            "confidence": Confidence.HIGH,
            "proxy_chain": [],
            "function_response": FunctionResponse(status=FunctionStatus.OK),
            "suggestions": [],
        },
        RouteType.PROXY_HIT: {
            "confidence": Confidence.MEDIUM,
            "function_response": FunctionResponse(status=FunctionStatus.OK),
        },
        RouteType.NO_HIT: {
            "confidence": Confidence.HIGH,
            "proxy_chain": [],
            "function_response": FunctionResponse(status=FunctionStatus.NO_HIT),
        },
        RouteType.AMBIGUOUS_HIT: {
            "confidence": Confidence.LOW,
            "proxy_chain": [],
            "function_response": FunctionResponse(status=FunctionStatus.AMBIGUOUS),
        },
        RouteType.CONTEXT_MISSING: {
            "confidence": Confidence.N_A,
            "proxy_chain": [],
            "function_response": FunctionResponse(status=FunctionStatus.NO_RETRIEVAL),
        },
        RouteType.TRANSFER_SUGGESTION: {
            "confidence": Confidence.N_A,
            "function_response": FunctionResponse(status=FunctionStatus.NO_HIT),
        },
    }
    return defaults.get(route_type, {})


def _validate_required_fields(
    route_type: RouteType,
    query_context: QueryContext | None,
    perturbation_resolution: PerturbationResolution | None,
    proxy_chain: list[ProxyStep] | None,
    diagnostics: Diagnostics | None,
    suggestions: list[Suggestion] | None,
) -> None:
    if route_type == RouteType.EXACT_HIT:
        if query_context is None or query_context.cell_line is None:
            raise ValueError("exact-hit requires query_context with cell_line")
        if perturbation_resolution is None or perturbation_resolution.method is None:
            raise ValueError("exact-hit requires perturbation_resolution")
    if route_type in (RouteType.PROXY_HIT, RouteType.NO_HIT, RouteType.AMBIGUOUS_HIT):
        if query_context is None or query_context.cell_line is None:
            raise ValueError(f"{route_type.value} requires query_context with cell_line")
    if route_type == RouteType.PROXY_HIT:
        if not proxy_chain:
            raise ValueError("proxy-hit requires at least one proxy_chain entry")
    if route_type == RouteType.CONTEXT_MISSING:
        if diagnostics is None or (not diagnostics.missing_fields and not diagnostics.invalid_fields):
            raise ValueError("context-missing requires diagnostics.missing_fields or diagnostics.invalid_fields")
        if not suggestions:
            raise ValueError("context-missing requires at least one missing-field suggestion")
    if route_type == RouteType.TRANSFER_SUGGESTION:
        if query_context is None:
            raise ValueError("transfer/suggestion requires query_context")
        if not suggestions:
            raise ValueError("transfer/suggestion requires at least one suggestion")

from __future__ import annotations

from dataclasses import dataclass

from pxfquery.l1_nlu import QueryIntent


@dataclass
class RoutePlan:
    """Evidence-routing decision passed from NLU into query execution."""

    intent: QueryIntent
    route_status: str
    required_capabilities: list[str] | None = None
    reason: str = ""

    def to_dict(self) -> dict:
        return {
            "route_status": self.route_status,
            "required_capabilities": self.required_capabilities or [],
            "reason": self.reason,
            "intent": self.intent.to_dict(),
        }


def route_intent(intent: QueryIntent) -> RoutePlan:
    route_status = classify_route(intent)
    return RoutePlan(
        intent=intent,
        route_status=route_status,
        required_capabilities=_required_capabilities(intent),
        reason=_route_reason(intent, route_status),
    )


def classify_route(intent: QueryIntent) -> str:
    if intent.missing_fields:
        return "needs-intent-completion"
    return "requires-resource-routing"


def _required_capabilities(intent: QueryIntent) -> list[str]:
    capabilities = ["entity_resolution", "resource_pack_query"]
    if intent.direction == "forward":
        capabilities.append("forward_query")
    elif intent.direction == "reverse":
        capabilities.append("reverse_query")
    if intent.perturbation_type in {"compound", "gene", "mixed", "perturbation"}:
        capabilities.append(f"{intent.perturbation_type}_routing")
    return capabilities


def _route_reason(intent: QueryIntent, route_status: str) -> str:
    if route_status == "needs-intent-completion":
        return "natural-language layer produced an incomplete intent"
    return "intent requires resource-backed routing before a biological hit can be claimed"

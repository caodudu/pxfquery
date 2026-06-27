from __future__ import annotations

from dataclasses import dataclass

from pxfquery.l1_intent import QueryIntent


@dataclass
class RoutePlan:
    """Evidence-routing decision passed from L1 into resource-backed execution."""

    intent: QueryIntent
    route_status: str
    required_capabilities: list[str]
    reason: str = ""

    def to_dict(self) -> dict:
        return {
            "route_status": self.route_status,
            "required_capabilities": list(self.required_capabilities),
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
    if intent.query_type == "forward" and not intent.pert_desc:
        return "needs-intent-completion"
    if intent.query_type == "reverse" and not (intent.function_desc or intent.activate or intent.suppress):
        return "needs-intent-completion"
    return "requires-resource-routing"


def _required_capabilities(intent: QueryIntent) -> list[str]:
    capabilities = ["entity_resolution", "resource_pack_query"]
    if intent.query_type == "forward":
        capabilities.extend(["forward_query", "perturbation_resolution"])
    if intent.query_type == "reverse":
        capabilities.extend(["reverse_query", "function_resolution"])
    if intent.pert_class:
        capabilities.append(f"{intent.pert_class}_routing")
    if intent.bio_context:
        capabilities.append("context_resolution")
    return capabilities


def _route_reason(intent: QueryIntent, route_status: str) -> str:
    if route_status == "needs-intent-completion":
        return "natural-language layer produced an incomplete intent"
    return f"{intent.query_type} intent requires resource-backed routing and execution"

from __future__ import annotations

from dataclasses import dataclass

from pxfquery.l2_routing import RoutePlan


@dataclass
class QueryExecution:
    """Result produced by the resource-pack query execution layer."""

    route_plan: RoutePlan
    query_status: str
    result: dict
    execution_note: str


def execute_route(route_plan: RoutePlan) -> QueryExecution:
    return QueryExecution(
        route_plan=route_plan,
        query_status="no-retrieval",
        result={"scores": None, "candidates": []},
        execution_note="Resource-pack query execution produced no retrieval in this version.",
    )

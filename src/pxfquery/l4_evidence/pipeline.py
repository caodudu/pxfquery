from __future__ import annotations

from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l3_execution import execute_route
from pxfquery.l1_nlu import parse_query
from pxfquery.l2_routing import route_intent


def run_query_pipeline(text: str) -> dict:
    intent = parse_query(text)
    route_plan = route_intent(intent)
    execution = execute_route(route_plan)
    return assemble_evidence(execution)

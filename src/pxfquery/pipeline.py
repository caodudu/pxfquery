from __future__ import annotations

from pxfquery.evidence import assemble_evidence
from pxfquery.execution import execute_route
from pxfquery.nlu import parse_query
from pxfquery.routing import route_intent


def run_query_pipeline(text: str) -> dict:
    intent = parse_query(text)
    route_plan = route_intent(intent)
    execution = execute_route(route_plan)
    return assemble_evidence(execution)

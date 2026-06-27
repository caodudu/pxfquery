from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l3_execution import execute_route
from pxfquery.l1_nlu import parse_query
from pxfquery.l5_presentation import build_answer
from pxfquery.l2_routing import route_intent


def test_nlu_only_parses_surface_intent():
    intent = parse_query("Find perturbations that increase a requested biological function in a disease model.")

    assert intent.direction == "reverse"
    assert intent.perturbation_type == "perturbation"
    assert intent.function_target == "increase a requested biological function"
    assert intent.biological_context == "disease"
    assert intent.perturbation_identity is None


def test_routing_does_not_create_biological_hits():
    intent = parse_query("Find perturbations that increase a requested biological function in a disease model.")
    route_plan = route_intent(intent)

    assert route_plan.route_status == "requires-resource-routing"
    assert "resource_pack_query" in route_plan.required_capabilities
    assert "score" not in route_plan.to_dict()
    assert "candidate" not in route_plan.to_dict()


def test_execution_without_resource_pack_returns_empty_result():
    route_plan = route_intent(parse_query("Find perturbations that increase a requested biological function in a disease model."))
    execution = execute_route(route_plan)

    assert execution.query_status == "no-retrieval"
    assert execution.result == {"scores": None, "candidates": []}


def test_evidence_and_presentation_do_not_invent_results():
    question = "Find perturbations that increase a requested biological function in a disease model."
    execution = execute_route(route_intent(parse_query(question)))
    evidence = assemble_evidence(execution)
    answer = build_answer(question, evidence)

    assert evidence["evidence_records"] == []
    assert evidence["function_response"]["scores"] is None
    assert evidence["function_response"]["candidates"] == []
    assert answer.biological_results == []

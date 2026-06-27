import pxfquery
from pxfquery import PxFQuery


def test_public_entrypoint_is_single_client():
    assert pxfquery.__all__ == ["PxFQuery"]
    assert PxFQuery().version == "0.4.0"


def test_ask_returns_no_biological_claim_before_resource_backed_retrieval():
    answer = PxFQuery().ask("Which perturbations increase a requested biological function in a disease model?")
    payload = answer.to_dict()

    assert payload["question"]
    assert payload["interpreted_question"]
    assert payload["biological_results"] == []
    assert payload["structured_result"]["function_response"]["scores"] is None
    assert payload["structured_result"]["function_response"]["candidates"] == []
    assert payload["structured_result"]["route_status"] in {
        "requires-resource-routing",
        "needs-intent-completion",
    }


def test_query_exposes_layer_chain():
    result = PxFQuery().query("How does a perturbation change functional programs in a disease model?")
    assert result["layer_chain"] == [
        "l1_nlu.parse_query",
        "l2_routing.route_intent",
        "l3_execution.execute_route",
        "l4_evidence.assemble_evidence",
    ]


def test_scanpy_style_interface_drives_internal_layers():
    pxf = PxFQuery()
    q = pxf.read.query("Find perturbations that increase a requested biological function in a disease model.")
    pxf.pp.parse(q)
    pxf.tl.route(q)
    pxf.tl.execute(q)
    pxf.tl.assemble(q)

    assert q.uns["route_status"] == "requires-resource-routing"
    assert q.uns["execution"]["query_status"] == "no-retrieval"
    assert pxf.get.result(q)["function_response"]["candidates"] == []

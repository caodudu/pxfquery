import pxfquery
from pxfquery import PxFQuery


def test_public_entrypoint_is_single_client():
    assert pxfquery.__all__ == ["PxFQuery"]
    assert PxFQuery().version == "0.3.1"


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
        "nlu.parse_query",
        "routing.route_intent",
        "execution.execute_route",
        "evidence.assemble_evidence",
    ]

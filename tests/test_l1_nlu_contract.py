import os

from pxfquery import PxFQuery


def test_real_l1_diygateway_intent_reaches_l2_route_plan():
    pxf = PxFQuery()
    pxf.settings.use_diygateway(token=os.environ["PXFQUERY_L1_API_KEY"], timeout=60)
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    pxf.pp.parse(q)
    intent = q.uns["intent"]

    assert intent["raw_query"] == "Which drugs activate apoptosis in cancer cells?"
    assert intent["query_type"] in {"forward", "reverse"}
    assert intent["pert_class"] in {"genetic", "drug", None}
    assert isinstance(intent["activate"], list)
    assert isinstance(intent["suppress"], list)
    assert isinstance(intent["ambiguity_flags"], list)
    assert isinstance(intent["missing_fields"], list)
    assert q.uns["_intent"].to_dict() == intent

    pxf.tl.route(q)
    route = pxf.get.route(q)

    assert route["intent"] == intent
    assert route["route_status"] in {"requires-resource-routing", "needs-intent-completion"}

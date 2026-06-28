import os

import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import IntentBackendError, IntentBackendNotConfigured


TUMOR_CONTEXT = "lung" + " cancer"


def test_real_l1_deepseek_intent_reaches_l2_route_plan():
    pxf = PxFQuery()
    token = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("PXFQUERY_LLM_API_KEY")
    if not token:
        pytest.skip("real L1 provider smoke test requires DEEPSEEK_API_KEY or PXFQUERY_LLM_API_KEY")
    pxf.settings.register_llm_provider(token=token, timeout=60)
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    pxf.pp.parse(q)
    intent = q.uns["intent"]

    assert intent["raw_query"] == "Which drugs activate apoptosis in cancer cells?"
    assert intent["query_type"] in {"forward", "reverse"}
    assert intent["pert_class"] in {"genetic", "drug", None}
    assert isinstance(intent["activate"], list)
    assert isinstance(intent["suppress"], list)
    assert isinstance(intent["constraints"], list)
    assert intent["forward_result_scope"] in {"activated_only", "suppressed_only", "both", "open"}
    assert isinstance(intent["ambiguity_flags"], list)
    assert isinstance(intent["missing_fields"], list)
    assert q.uns["_intent"].to_dict() == intent

    pxf.pp.route(q)
    route = pxf.get.route(q)

    assert route["intent"] == intent
    assert route["schema_version"] == "l2-route-plan/v2"
    assert route["route_status"] in {"routed", "llm-required", "resource-missing", "needs-intent-completion", "unresolved"}


def test_l1_intent_requires_registered_provider(monkeypatch):
    monkeypatch.delenv("PXFQUERY_LLM_API_KEY", raising=False)
    monkeypatch.delenv("PXFQUERY_LLM_BASE_URL", raising=False)
    monkeypatch.delenv("PXFQUERY_LLM_MODEL", raising=False)
    pxf = PxFQuery()
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    with pytest.raises(IntentBackendNotConfigured):
        pxf.pp.parse(q)


class _BadProvider:
    def __init__(self, payload):
        self.payload = payload

    def parse_intent(self, text, *, schema, validator=None):
        del text, schema
        if validator is not None and isinstance(self.payload, dict):
            validator(self.payload)
        return self.payload, {"provider": "bad-test-provider"}


def test_l1_intent_rejects_non_object_provider_payload():
    pxf = PxFQuery(llm_provider=_BadProvider(["not", "an", "object"]))
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_invalid_schema_payload():
    payload = {
        "query_type": "bad",
        "bio_context": None,
        "pert_desc": None,
        "pert_class": "drug",
        "genetic_modality": None,
        "function_desc": "apoptosis",
        "activate": ["apoptosis"],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_biological_result_payload():
    payload = {
        "query_type": "reverse",
        "bio_context": "cancer cells",
        "pert_desc": None,
        "pert_class": "drug",
        "genetic_modality": None,
        "function_desc": "apoptosis",
        "activate": ["apoptosis"],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
        "candidates": ["not allowed in L1"],
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Which drugs activate apoptosis in cancer cells?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_reverse_with_perturbation_but_no_function_goal():
    payload = {
        "query_type": "reverse",
        "bio_context": "leukemia",
        "pert_desc": "BCL2",
        "pert_class": "genetic",
        "genetic_modality": "crispr",
        "function_desc": None,
        "activate": [],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("In leukemia context, CRISPR loss of BCL2 should alter which programs?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_accepts_gene_activation_to_reduce_function_as_two_axes():
    payload = {
        "query_type": "reverse",
        "bio_context": TUMOR_CONTEXT,
        "pert_desc": None,
        "pert_class": "genetic",
        "genetic_modality": "overexpression",
        "function_desc": "reduce MYC target programs",
        "activate": [],
        "suppress": ["MYC target programs"],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query(f"Which genes should be activated to reduce MYC target programs in {TUMOR_CONTEXT}?")

    pxf.pp.parse(q)
    intent = pxf.get.intent(q)

    assert intent["genetic_modality"] == "overexpression"
    assert intent["suppress"] == ["MYC target programs"]


def test_l1_intent_accepts_named_perturbation_effect_as_forward_scope():
    payload = {
        "query_type": "forward",
        "bio_context": "pancreatic cancer cells",
        "pert_desc": "KRAS",
        "pert_class": "genetic",
        "genetic_modality": "knockdown",
        "function_desc": None,
        "activate": [],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "suppressed_only",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("What programs are suppressed by KRAS knockdown in pancreatic cancer cells?")

    pxf.pp.parse(q)
    assert pxf.get.intent(q)["query_type"] == "forward"


def test_l1_intent_accepts_without_activating_as_constraint():
    payload = {
        "query_type": "reverse",
        "bio_context": None,
        "pert_desc": None,
        "pert_class": None,
        "genetic_modality": None,
        "function_desc": None,
        "activate": [],
        "suppress": ["MYC targets"],
        "constraints": [{"term": "inflammatory response", "avoid_direction": "activate"}],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Find perturbations that suppress MYC targets without activating inflammatory response.")

    pxf.pp.parse(q)
    intent = pxf.get.intent(q)

    assert intent["suppress"] == ["MYC targets"]
    assert intent["constraints"] == [{"term": "inflammatory response", "avoid_direction": "activate"}]


def test_l1_intent_rejects_function_target_as_bio_context():
    payload = {
        "query_type": "reverse",
        "bio_context": "inflammatory response",
        "pert_desc": None,
        "pert_class": "genetic",
        "genetic_modality": "knockout",
        "function_desc": None,
        "activate": ["differentiation"],
        "suppress": ["inflammatory response"],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Which gene knockouts could decrease inflammatory response but increase differentiation?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_reverse_query_without_function_target():
    payload = {
        "query_type": "reverse",
        "bio_context": "breast cancer models",
        "pert_desc": None,
        "pert_class": "genetic",
        "genetic_modality": "overexpression",
        "function_desc": None,
        "activate": [],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "open",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Find genes whose activation could increase apoptosis in breast cancer models.")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_forward_operation_term_in_function_direction():
    payload = {
        "query_type": "forward",
        "bio_context": None,
        "pert_desc": "CDK4",
        "pert_class": "genetic",
        "genetic_modality": "overexpression",
        "function_desc": None,
        "activate": ["CDK4"],
        "suppress": [],
        "constraints": [],
        "forward_result_scope": "both",
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("For CDK4 activation, what functional consequences should be inferred from loss-of-function evidence?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)

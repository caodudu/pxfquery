import os

import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import IntentBackendError, IntentBackendNotConfigured


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
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("In leukemia context, CRISPR loss of BCL2 should alter which programs?")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)


def test_l1_intent_rejects_molecule_query_with_null_pert_class():
    payload = {
        "query_type": "reverse",
        "bio_context": "neural tumor",
        "pert_desc": None,
        "pert_class": None,
        "genetic_modality": None,
        "function_desc": None,
        "activate": ["differentiation"],
        "suppress": ["cycling"],
        "top_n": None,
    }
    pxf = PxFQuery(llm_provider=_BadProvider(payload))
    q = pxf.read.query("Find molecules that increase differentiation and reduce cycling in neural tumor.")

    with pytest.raises(IntentBackendError):
        pxf.pp.parse(q)

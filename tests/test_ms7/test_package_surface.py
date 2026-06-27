import pathlib


def test_ms7_required_modules_import_from_root_src():
    import pxfquery
    import pxfquery.api
    import pxfquery.cli
    import pxfquery.engines.forward_drug
    import pxfquery.engines.forward_genetic
    import pxfquery.engines.reverse_drug
    import pxfquery.engines.reverse_genetic
    import pxfquery.llm
    import pxfquery.parser
    import pxfquery.query
    import pxfquery.resolver

    package_path = pathlib.Path(pxfquery.__file__).resolve()
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    assert str(package_path).startswith(str(repo_root / "src" / "pxfquery"))


def test_ms7_query_has_anchor_metadata():
    from pxfquery import PxFQuery

    payload = PxFQuery().query("What happens to the functional programs if I knock down KRAS in A549?")
    assert payload["route_type"] == "exact-hit"
    for key in [
        "query_context",
        "perturbation_resolution",
        "function_response",
        "confidence",
        "proxy_chain",
        "diagnostics",
        "suggestions",
        "intent",
    ]:
        assert key in payload
    assert payload["intent"]["direction"] == "forward"
    assert payload["intent"]["perturbation_identity"] == "KRAS"


def test_ms7_context_missing_not_fabricated():
    from pxfquery import PxFQuery

    payload = PxFQuery().query("How does erlotinib change cancer cell function if I do not know the cell line yet?")
    assert payload["route_type"] == "context-missing"
    assert "context" in payload["intent"]["missing_fields"]
    assert payload["suggestions"]

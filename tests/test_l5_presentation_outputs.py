from pathlib import Path

from pxfquery import PxFQuery


def sample_dossier():
    return {
        "schema_version": "l4-evidence-dossier/v1",
        "query_type": "forward",
        "dossier_status": "evidence_found",
        "claim_basis": {
            "answerability": "answered",
            "main_claim": "PxFquery found exact_matrix functional matrix evidence for PERT_X in CONTEXT_X.",
            "claim_type": "matrix_backed_effect",
            "claim_strength": "high",
            "supporting_points": ["Evidence grade: exact_matrix.", "Primary L3 route matched 4 matrix rows."],
            "caution_points": [],
            "must_mention": ["matrix-backed", "exact_matrix", "matched rows: 4"],
            "must_not_claim": ["clinical efficacy", "invented citations"],
        },
        "evidence_layer": {
            "evidence_grade": "exact_matrix",
            "llm_synthesis": {
                "status": "completed",
                "biological_summary": "PERT_X changes FUNCTION_X, FUNCTION_Y, and FUNCTION_Z in CONTEXT_X.",
                "evidence_audit_summary": "Exact matrix evidence was available for the primary route.",
            },
            "intent_evidence": {
                "query_type": "forward",
                "bio_context": "CONTEXT_X",
                "pert_desc": "PERT_X",
            },
            "route_evidence": {
                "status": "routed",
                "selected_routes": [
                    {"route_id": "route_x", "status": "selected", "cell": "CONTEXT_X", "tier": "exact"}
                ],
            },
            "matrix_evidence": {
                "mode": "forward",
                "execution_status": "executed",
                "primary_result": {
                    "cell": "CONTEXT_X",
                    "perturbation": "PERT_X",
                    "modality": "cp",
                    "n_rows": 4,
                    "top_activated": [
                        {"rank": 1, "label": "FUNCTION_X", "score": 0.72, "direction": "activated"},
                        {"rank": 2, "label": "FUNCTION_Y", "score": 0.41, "direction": "activated"},
                    ],
                    "top_suppressed": [
                        {"rank": 1, "label": "FUNCTION_Z", "score": -0.35, "direction": "suppressed"}
                    ],
                },
                "executed_routes": [
                    {"route_id": "route_x", "status": "executed", "cell": "CONTEXT_X", "tier": "exact"}
                ],
            },
        },
        "uncertainty_layer": {"confidence": "high", "limitations": []},
        "rendering_hints": {
            "allowed_transformations": ["summarize", "format", "tabulate"],
            "forbidden_transformations": ["change_scores", "add_candidates"],
        },
        "audit_layer": {"schema_versions": {"l2": "l2-route-plan/v1"}, "raw_execution_status": "executed"},
    }


def test_tl_answer_builds_single_scanpy_style_output_without_changing_l4():
    pxf = PxFQuery()
    qdata = pxf.read.query("show PERT_X effects")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    answer = pxf.get.answer(qdata)

    assert answer.structured_result is dossier
    assert answer.headline == "PxFquery found matrix-backed evidence"
    assert answer.summary == "PERT_X changes FUNCTION_X, FUNCTION_Y, and FUNCTION_Z in CONTEXT_X."
    assert answer.summary_source == "l4.llm_synthesis.biological_summary"
    assert answer.evidence["evidence_audit_summary"] == "Exact matrix evidence was available for the primary route."
    assert answer.biological_results[0]["label"] == "FUNCTION_X"
    assert {spec["kind"] for spec in answer.figures} >= {"bar", "bubble", "heatmap", "route_flow", "evidence_panel"}
    assert all(spec.get("svg", "").startswith("<svg") for spec in answer.figures)
    assert dossier["claim_basis"]["main_claim"].endswith("CONTEXT_X.")


def test_tl_answer_html_mode_can_write_report(tmp_path):
    pxf = PxFQuery()
    qdata = pxf.read.query("render report")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    out = tmp_path / "report.html"

    pxf.tl.answer(qdata, mode="html", output=out)
    answer = pxf.get.answer(qdata)

    assert out.exists()
    html = out.read_text(encoding="utf-8")
    assert "Main Evidence" in html
    assert "<svg" in html
    assert answer.html is not None
    assert qdata.uns["answer_output"] == str(Path(out))


def test_tl_figures_writes_real_svg_files(tmp_path):
    pxf = PxFQuery()
    qdata = pxf.read.query("write figures")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    pxf.tl.figures(qdata, output_dir=tmp_path, prefix="case", format="png")

    paths = [Path(path) for path in qdata.uns["figure_outputs"]]
    assert len(paths) >= 5
    assert all(path.exists() for path in paths)
    assert all(path.suffix == ".png" for path in paths)
    assert all(path.read_bytes().startswith(b"\x89PNG") for path in paths)

    pxf.tl.figures(qdata, output_dir=tmp_path / "svg", prefix="case", format="svg")
    svg_paths = [Path(path) for path in qdata.uns["figure_outputs"]]
    assert all(path.read_text(encoding="utf-8").startswith("<svg") for path in svg_paths)


def test_tl_answer_mcp_mode_reuses_same_answer_payload():
    pxf = PxFQuery()
    qdata = pxf.read.query("mcp payload")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata, mode="mcp")
    payload = pxf.get.answer(qdata).mcp

    assert payload["schema_version"] == "pxfquery-l5-mcp/v1"
    assert payload["answer"]["headline"] == "PxFquery found matrix-backed evidence"
    assert payload["answer"]["summary_source"] == "l4.llm_synthesis.biological_summary"
    assert payload["l4_evidence"] is dossier


def test_tl_chat_fails_without_llm_provider():
    pxf = PxFQuery()
    qdata = pxf.read.query("chat over evidence")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    try:
        pxf.tl.chat(qdata, "解释一下")
    except RuntimeError as exc:
        assert "requires a configured PxFquery LLM provider" in str(exc)
    else:
        raise AssertionError("pxf.tl.chat must fail without a real llm_provider")


def test_tl_chat_uses_provider_and_keeps_history():
    class Provider:
        def request_json(self, **kwargs):
            assert kwargs["stage"] == "l5_chat"
            assert kwargs["user_payload"]["l4_evidence"]["schema_version"] == "l4-evidence-dossier/v1"
            return {"response": "Provider-bound response.", "cited_tables": ["ranked_results"], "warnings": []}, {"provider": "test"}

    pxf = PxFQuery()
    qdata = pxf.read.query("chat with provider")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    pxf.tl.chat(qdata, "解释一下", llm_provider=Provider(), print_response=False)
    response = pxf.get.chat(qdata)
    history = pxf.get.chat_history(qdata)

    assert response == "Provider-bound response."
    assert history[0]["cited_tables"] == ["ranked_results"]
    assert history[0]["provider_evidence"] == {"provider": "test"}
    assert len(history) == 1

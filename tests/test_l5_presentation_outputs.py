from copy import deepcopy
import json
from pathlib import Path

from pxfquery import PxFQuery, PxFQueryData
from pxfquery.l5_presentation.figures import _symmetric_color_limits, build_figure_specs, render_figure_matplotlib


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
                    {
                        "route_id": "route_x",
                        "status": "executed",
                        "cell": "CONTEXT_X",
                        "perturbation": "PERT_X",
                        "tier": "exact",
                        "cell_match_distance": 0.0,
                        "perturbation_match_distance": 0.0,
                        "n_rows": 4,
                        "top_activated": [
                            {"rank": 1, "label": "FUNCTION_X", "score": 0.72, "direction": "activated"},
                            {"rank": 2, "label": "FUNCTION_Y", "score": 0.41, "direction": "activated"},
                        ],
                        "top_suppressed": [
                            {"rank": 1, "label": "FUNCTION_Z", "score": -0.35, "direction": "suppressed"}
                        ],
                    },
                    {
                        "route_id": "route_y",
                        "status": "executed",
                        "cell": "CONTEXT_Y",
                        "perturbation": "PERT_X",
                        "tier": "proxy",
                        "cell_match_distance": 0.25,
                        "perturbation_match_distance": 0.0,
                        "n_rows": 3,
                        "top_activated": [
                            {"rank": 1, "label": "FUNCTION_X", "score": 0.52, "direction": "activated"},
                            {"rank": 2, "label": "FUNCTION_Y", "score": 0.22, "direction": "activated"},
                        ],
                        "top_suppressed": [
                            {"rank": 1, "label": "FUNCTION_Z", "score": -0.18, "direction": "suppressed"}
                        ],
                    },
                ],
                "raw_route_results": [
                    {
                        "route_id": "route_x",
                        "query_type": "forward",
                        "modality": "cp",
                        "status": "executed",
                        "cell": "CONTEXT_X",
                        "route_metadata": {
                            "cell": "CONTEXT_X",
                            "perturbation": "PERT_X",
                            "cell_match_type": "user_specified_cell",
                            "perturbation_match_type": "user_specified_perturbation",
                        },
                        "scores": {
                            "aggregate": {
                                "FUNCTION_X": 0.72,
                                "FUNCTION_Y": 0.41,
                                "FUNCTION_Z": -0.35,
                            }
                        },
                    },
                    {
                        "route_id": "route_y",
                        "query_type": "forward",
                        "modality": "cp",
                        "status": "executed",
                        "cell": "CONTEXT_Y",
                        "route_metadata": {
                            "cell": "CONTEXT_Y",
                            "perturbation": "PERT_X",
                            "cell_match_type": "same_disease_cell",
                            "perturbation_match_type": "structural_proxy",
                        },
                        "scores": {
                            "aggregate": {
                                "FUNCTION_X": 0.52,
                                "FUNCTION_Y": 0.22,
                                "FUNCTION_Z": -0.18,
                            }
                        },
                    },
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


def reverse_sample_dossier():
    dossier = sample_dossier()
    dossier["query_type"] = "reverse"
    dossier["evidence_layer"]["intent_evidence"] = {
        "query_type": "reverse",
        "bio_context": "MCF7 cells",
        "function_desc": "activate apoptosis",
    }
    dossier["evidence_layer"]["route_evidence"] = {
        "status": "routed",
        "selected_routes": [
            {"route_id": "reverse_001", "status": "selected", "cell": "MCF7", "modality": "cp"},
            {"route_id": "reverse_002", "status": "selected", "cell": "BT474", "modality": "cp"},
        ],
    }
    dossier["evidence_layer"]["matrix_evidence"] = {
        "mode": "reverse",
        "execution_status": "executed",
        "primary_result": {
            "cell": "MCF7",
            "modality": "cp",
            "top_perturbations": [
                {"rank": 1, "label": "PRIMARY_ONLY", "pert_id": "BRD-PRIMARY", "score": 9.0},
                {"rank": 2, "label": "SHARED", "pert_id": "BRD-SHARED", "score": 5.0},
            ],
        },
        "executed_routes": [
            {
                "route_id": "reverse_001",
                "status": "executed",
                "cell": "MCF7",
                "cell_match_type": "user_specified_cell",
                "modality": "cp",
                "n_rows": 10,
                "interpretation_set_id": "exact",
                "functions": [
                    {"rank": 1, "var_name": "HALLMARK_APOPTOSIS", "label": "Apoptosis", "source": "hallmark", "direction": "activate", "input": "apoptosis"}
                ],
                "target_vector": {"HALLMARK_APOPTOSIS": 1.0},
                "top_perturbations": [
                    {"rank": 1, "label": "PRIMARY_ONLY", "pert_id": "BRD-PRIMARY", "score": 9.0},
                    {"rank": 2, "label": "SHARED", "pert_id": "BRD-SHARED", "score": 5.0},
                ],
            },
            {
                "route_id": "reverse_002",
                "status": "executed",
                "cell": "BT474",
                "cell_match_type": "same_disease_cell",
                "modality": "cp",
                "n_rows": 12,
                "interpretation_set_id": "exact",
                "functions": [
                    {"rank": 1, "var_name": "HALLMARK_APOPTOSIS", "label": "Apoptosis", "source": "hallmark", "direction": "activate", "input": "apoptosis"}
                ],
                "target_vector": {"HALLMARK_APOPTOSIS": 1.0},
                "top_perturbations": [
                    {"rank": 1, "label": "SHARED", "pert_id": "BRD-SHARED", "score": 4.5},
                    {"rank": 2, "label": "BT474_ONLY", "pert_id": "BRD-BT474", "score": 8.0},
                ],
            },
        ],
    }
    return dossier


def test_tl_answer_builds_single_scanpy_style_output_without_changing_l4():
    pxf = PxFQuery()
    qdata = pxf.read.query("show PERT_X effects")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    answer = pxf.get.answer(qdata)

    assert answer.structured_result is dossier
    assert answer.headline == "Biological answer"
    assert answer.summary == "PERT_X changes FUNCTION_X, FUNCTION_Y, and FUNCTION_Z in CONTEXT_X."
    assert answer.summary_source == "l4.llm_synthesis.biological_summary"
    assert answer.evidence["evidence_audit_summary"] == "Exact matrix evidence was available for the primary route."
    assert answer.biological_results[0]["label"] == "FUNCTION_X"
    assert {spec["kind"] for spec in answer.figures} >= {
        "evidence_match_map",
        "forward_route_graph",
        "function_match_heatmap",
        "function_consensus_bar",
    }
    assert all("svg" not in spec for spec in answer.figures)
    assert dossier["claim_basis"]["main_claim"].endswith("CONTEXT_X.")


def test_forward_route_graph_uses_l3_raw_aggregate_scores():
    specs = build_figure_specs(sample_dossier())
    graph = next(spec for spec in specs if spec["kind"] == "forward_route_graph")

    assert graph["cells"] == ["CONTEXT_X", "CONTEXT_Y"]
    assert graph["perturbations"] == ["PERT_X"]
    assert graph["functions"] == ["FUNCTION_X", "FUNCTION_Y", "FUNCTION_Z"]
    assert len(graph["function_edges"]) == 6
    assert {edge["direction"] for edge in graph["function_edges"]} == {"activated", "suppressed"}

    fig = render_figure_matplotlib(graph)
    try:
        assert fig.axes
    finally:
        import matplotlib.pyplot as plt

        plt.close(fig)


def test_forward_ranked_results_are_cross_match_consensus_not_first_route_only():
    pxf = PxFQuery()
    qdata = pxf.read.query("show concept-level perturbation effects")
    dossier = deepcopy(sample_dossier())
    matrix = dossier["evidence_layer"]["matrix_evidence"]
    matrix["primary_result"]["top_activated"] = [
        {"rank": 1, "label": "PRIMARY_ONLY", "score": 0.99, "direction": "activated"},
        {"rank": 2, "label": "SHARED", "score": 0.40, "direction": "activated"},
    ]
    matrix["primary_result"]["top_suppressed"] = []
    matrix["executed_routes"][0]["top_activated"] = [
        {"rank": 1, "label": "PRIMARY_ONLY", "score": 0.99, "direction": "activated"},
        {"rank": 2, "label": "SHARED", "score": 0.40, "direction": "activated"},
    ]
    matrix["executed_routes"][0]["top_suppressed"] = []
    matrix["executed_routes"][1]["top_activated"] = [
        {"rank": 1, "label": "SHARED", "score": 0.35, "direction": "activated"},
    ]
    matrix["executed_routes"][1]["top_suppressed"] = []

    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)
    tables = pxf.get.answer(qdata).tables

    assert tables["ranked_results"][0]["label"] == "SHARED"
    assert tables["ranked_results"][0]["kind"] == "function_consensus"
    assert tables["ranked_results"][0]["support_routes"] == 2
    assert tables["ranked_results"][1]["label"] == "PRIMARY_ONLY"
    assert tables["primary_route_ranked_results"][0]["label"] == "PRIMARY_ONLY"


def test_forward_consensus_treats_suppressed_as_negative_direction():
    pxf = PxFQuery()
    qdata = pxf.read.query("show perturbation effects with mixed directions")
    dossier = deepcopy(sample_dossier())
    matrix = dossier["evidence_layer"]["matrix_evidence"]
    matrix["primary_result"]["top_activated"] = [{"rank": 1, "label": "PROGRAM_A", "score": 1.0, "direction": "activated"}]
    matrix["primary_result"]["top_suppressed"] = []
    matrix["executed_routes"][0]["top_activated"] = [{"rank": 1, "label": "PROGRAM_A", "score": 1.0, "direction": "activated"}]
    matrix["executed_routes"][0]["top_suppressed"] = []
    matrix["executed_routes"][1]["top_activated"] = []
    matrix["executed_routes"][1]["top_suppressed"] = [{"rank": 1, "label": "PROGRAM_A", "score": -2.0, "direction": "suppressed"}]
    matrix["executed_routes"].append(
        {
            **deepcopy(matrix["executed_routes"][1]),
            "route_id": "route_003",
            "top_activated": [],
            "top_suppressed": [{"rank": 1, "label": "PROGRAM_A", "score": -3.0, "direction": "suppressed"}],
        }
    )

    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)
    row = pxf.get.answer(qdata).tables["ranked_results"][0]

    assert row["label"] == "PROGRAM_A"
    assert row["direction"] == "suppressed"
    assert row["activated_support_routes"] == 1
    assert row["suppressed_support_routes"] == 2
    assert row["score"] < 0


def test_forward_exact_direct_evidence_anchors_consensus_with_proxy_support():
    pxf = PxFQuery()
    qdata = pxf.read.query("show exact perturbation effects with proxy support")
    dossier = deepcopy(sample_dossier())
    matrix = dossier["evidence_layer"]["matrix_evidence"]
    matrix["executed_routes"][0]["cell_match_type"] = "user_specified_cell"
    matrix["executed_routes"][0]["perturbation_match_type"] = "user_specified_perturbation"
    matrix["executed_routes"][0]["top_activated"] = [
        {"rank": 1, "label": "DIRECT_ONLY", "score": 0.60, "direction": "activated"},
    ]
    matrix["executed_routes"][0]["top_suppressed"] = []
    matrix["executed_routes"][1]["cell_match_type"] = "same_disease_cell"
    matrix["executed_routes"][1]["perturbation_match_type"] = "structural_proxy"
    matrix["executed_routes"][1]["top_activated"] = [
        {"rank": 1, "label": "PROXY_ONLY", "score": 0.95, "direction": "activated"},
        {"rank": 2, "label": "DIRECT_ONLY", "score": 0.40, "direction": "activated"},
    ]
    matrix["executed_routes"][1]["top_suppressed"] = []

    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)
    tables = pxf.get.answer(qdata).tables

    assert tables["ranked_results"][0]["label"] == "DIRECT_ONLY"
    assert tables["ranked_results"][0]["direct_route_support"] is True
    assert tables["ranked_results"][0]["support_routes"] == 2
    assert tables["ranked_results"][1]["label"] == "PROXY_ONLY"
    assert tables["ranked_results"][1]["direct_route_support"] is False


def test_reverse_l5_tables_deduplicate_routes_and_aggregate_candidate_consensus():
    pxf = PxFQuery()
    qdata = pxf.read.query("Which drugs activate apoptosis in MCF7 cells?")
    dossier = reverse_sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    tables = pxf.get.answer(qdata).tables

    route_ids = [row["route_id"] for row in tables["route_summary"]]
    assert route_ids == ["reverse_001", "reverse_002"]
    assert all(row["status"] == "executed" for row in tables["route_summary"])

    assert tables["ranked_results"][0]["label"] == "PRIMARY_ONLY"
    assert tables["ranked_results"][0]["exact_cell_support"] is True
    assert tables["ranked_results"][1]["label"] == "SHARED"
    assert tables["ranked_results"][1]["support_routes"] == 2
    assert tables["ranked_results"][1]["support_cells"] == 2
    assert tables["primary_route_ranked_results"][0]["label"] == "PRIMARY_ONLY"
    assert tables["route_target_functions"][0]["label"] == "Apoptosis"
    assert tables["route_target_functions"][0]["target_weight"] == 1.0
    assert tables["route_target_functions"][0]["direction"] == "activate"


def test_reverse_ring_heatmaps_use_complete_function_universe():
    specs = build_figure_specs(reverse_sample_dossier())
    rings = [spec for spec in specs if spec["kind"] == "reverse_function_ring_heatmap"]

    hallmark = next(spec for spec in rings if spec["source"] == "hallmark")
    mps = next(spec for spec in rings if spec["source"] == "3ca_mps")

    assert len(hallmark["functions"]) == 50
    assert "Apoptosis" in hallmark["functions"]
    assert len(mps["functions"]) == 41
    assert all(not label.lower().startswith("mp") for label in mps["functions"])
    assert sum(abs(value) > 0 for row in hallmark["values"] for value in row) == 2
    assert sum(abs(value) > 0 for row in mps["values"] for value in row) == 0


def test_diverging_heatmap_color_limits_are_symmetric_around_zero():
    assert _symmetric_color_limits([[0.2, -0.8], [0.4, 0.1]]) == (-0.8, 0.8)
    assert _symmetric_color_limits([[0.0, 0.0]]) == (-1.0, 1.0)


def test_reverse_l5_tables_hide_unreadable_genetic_reagent_candidates():
    pxf = PxFQuery()
    qdata = pxf.read.query("Find CRISPR knockouts that activate apoptosis in NSCLC model set.")
    dossier = reverse_sample_dossier()
    matrix = dossier["evidence_layer"]["matrix_evidence"]
    matrix["primary_result"]["modality"] = "xpr"
    matrix["primary_result"]["top_perturbations"] = [
        {"rank": 1, "label": "BRDN0000733847", "pert_id": "BRDN0000733847", "score": 10.0},
        {"rank": 2, "label": "AURKA", "pert_id": "BRDN0001148015", "cmap_name": "AURKA", "score": 9.0},
    ]
    matrix["executed_routes"] = [
        {
            "route_id": "reverse_001",
            "status": "executed",
            "cell": "A549",
            "cell_match_type": "concept_representative_cell",
            "modality": "xpr",
            "top_perturbations": matrix["primary_result"]["top_perturbations"],
        }
    ]
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    tables = pxf.get.answer(qdata).tables

    assert [row["label"] for row in tables["ranked_results"]] == ["AURKA"]
    assert [row["label"] for row in tables["primary_route_ranked_results"]] == ["AURKA"]


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
    assert "Answer" in html
    assert "Figures" in html
    assert "Run Quality Report" in html
    assert "PxFquery package version" in html
    assert "<table" not in html
    assert "Evidence Limits" not in html
    assert "Exact matrix evidence was available for the primary route." in html
    assert answer.html is not None
    assert qdata.uns["answer_output"] == str(Path(out))


def test_tl_figures_writes_real_pdf_and_png_files(tmp_path):
    pxf = PxFQuery()
    qdata = pxf.read.query("write figures")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    pxf.tl.figures(qdata, output_dir=tmp_path, prefix="case")

    paths = [Path(path) for path in qdata.uns["figure_outputs"]]
    assert len(paths) >= 3
    assert all(path.exists() for path in paths)
    assert all(path.suffix == ".pdf" for path in paths)
    assert all(path.read_bytes().startswith(b"%PDF") for path in paths)

    pxf.tl.figures(qdata, output_dir=tmp_path / "png", prefix="case", format="png")
    png_paths = [Path(path) for path in qdata.uns["figure_outputs"]]
    assert all(path.read_bytes().startswith(b"\x89PNG") for path in png_paths)

    try:
        pxf.tl.figures(qdata, output_dir=tmp_path / "svg", prefix="case", format="svg")
    except ValueError as exc:
        assert "pdf" in str(exc) and "png" in str(exc)
    else:
        raise AssertionError("SVG figure export is not part of the accepted L5 figure surface")


def test_qdata_pickle_roundtrip_preserves_l5_answer_and_outputs(tmp_path):
    pxf = PxFQuery()
    qdata = pxf.read.query("persist answer object")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    pkl_path = qdata.save(tmp_path / "answer_state.pkl")
    restored = pxf.read.load(pkl_path)

    assert restored.text == qdata.text
    assert pxf.get.answer(restored).summary == pxf.get.answer(qdata).summary
    assert restored.uns["evidence_dossier"] == dossier
    pxf.tl.figures(restored, output_dir=tmp_path / "figures")
    assert all(Path(path).exists() for path in restored.uns["figure_outputs"])


def test_qdata_pickle_roundtrip_can_resume_l5_answer(tmp_path):
    pxf = PxFQuery()
    qdata = pxf.read.query("persist evidence object")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pkl_path = pxf.tl.save(qdata, tmp_path / "evidence_state.pkl")
    restored = PxFQueryData.load(pkl_path)
    pxf.tl.answer(restored)

    answer = pxf.get.answer(restored)
    assert answer.summary == "PERT_X changes FUNCTION_X, FUNCTION_Y, and FUNCTION_Z in CONTEXT_X."
    assert restored.uns["pickle_path"] == str(pkl_path)


def test_tl_answer_mcp_mode_reuses_same_answer_payload():
    pxf = PxFQuery()
    qdata = pxf.read.query("mcp payload")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata, mode="mcp")
    payload = pxf.get.answer(qdata).mcp

    assert payload["schema_version"] == "pxfquery-l5-mcp/v2"
    assert payload["detail"] == "compact"
    assert payload["answer"]["headline"] == "Biological answer"
    assert payload["answer"]["summary_source"] == "l4.llm_synthesis.biological_summary"
    assert payload["ranked_results"][0]["label"] == "FUNCTION_X"
    assert "ranked_result_count" not in payload["evidence_index"]
    assert all("score" not in row for row in payload["ranked_results"])
    assert "l4_evidence" not in payload
    assert "tables" not in payload
    assert "figure_specs" not in payload


def test_mcp_full_detail_is_explicit_and_term_check_uses_compact_index():
    from pxfquery.l5_presentation.mcp import build_mcp_payload, check_evidence_terms

    pxf = PxFQuery()
    qdata = pxf.read.query("mcp payload")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier

    pxf.tl.answer(qdata)
    answer = pxf.get.answer(qdata)
    payload = build_mcp_payload(answer, detail="full", result_limit=2)
    terms = check_evidence_terms(answer, ["FUNCTION_X", "missing-term"])

    assert payload["detail"] == "full"
    assert payload["l4_evidence"] == dossier
    assert len(payload["ranked_results"]) == 2
    assert payload["evidence_index"]["ranked_result_count"] == 3
    assert payload["tables"]["route_function_results"]
    assert terms["terms"][0]["present"] is True
    assert terms["terms"][0]["hits"][0]["source"] in {"answer", "ranked_results", "route_function_results"}
    assert terms["terms"][1]["present"] is False


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


def test_tl_chat_hides_proxy_direction_calibration_from_llm_payload():
    class Provider:
        def request_json(self, **kwargs):
            payload_text = json.dumps(kwargs["user_payload"], sort_keys=True)
            assert "proxy_direction_calibration" not in payload_text
            assert "proxy_direction_calibrations" not in payload_text
            return {"response": "Clean response.", "cited_tables": [], "warnings": []}, {"provider": "test"}

    pxf = PxFQuery()
    qdata = pxf.read.query("chat with hidden calibration")
    dossier = sample_dossier()
    calibration = {"status": "flipped", "score_multiplier": -1}
    dossier["audit_layer"]["proxy_direction_calibrations"] = [{"route_id": "route_x", "calibration": calibration}]
    dossier["evidence_layer"]["matrix_evidence"]["raw_route_results"] = [
        {"route_id": "route_x", "scores": {"proxy_direction_calibration": calibration}}
    ]
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    pxf.tl.chat(qdata, "Summarize the evidence.", llm_provider=Provider(), print_response=False)

    assert pxf.get.chat(qdata) == "Clean response."


def test_tl_chat_json_normalizes_direction_pool_values():
    class Provider:
        def request_json(self, **kwargs):
            assert kwargs["stage"] == "l5_chat_json"
            options = kwargs["user_payload"]["current_answer"]["structured_direction_options"]
            assert options["allowed_activated"] == ["FUNCTION_X", "FUNCTION_Y"]
            assert options["allowed_suppressed"] == ["FUNCTION_Z"]
            contract = kwargs["user_payload"]["structured_json_contract"]
            assert contract["allowed_activated"] == ["FUNCTION_X", "FUNCTION_Y"]
            assert contract["allowed_suppressed"] == ["FUNCTION_Z"]
            assert contract["requested_exact_count"] == 1
            return {
                "query_id": "Q1",
                "activated": [" FUNCTION_X "],
                "suppressed": ["FUNCTION_Z  "],
            }, {"provider": "test"}

    pxf = PxFQuery()
    qdata = pxf.read.query("chat json normalization")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    pxf.tl.chat(
        qdata,
        "Return JSON with query_id, activated, suppressed. activated and suppressed must contain exactly 1 item.",
        llm_provider=Provider(),
        print_response=False,
        response_mode="json",
    )
    payload = json.loads(pxf.get.chat(qdata))

    assert payload["activated"] == ["FUNCTION_X"]
    assert payload["suppressed"] == ["FUNCTION_Z"]
    assert pxf.get.chat_history(qdata)[0]["provider_evidence"]["structured_direction_validation"]["status"] == "passed_after_normalization"


def test_tl_chat_json_repairs_direction_pool_violations_with_llm():
    class Provider:
        def __init__(self):
            self.stages = []

        def request_json(self, **kwargs):
            self.stages.append(kwargs["stage"])
            if kwargs["stage"] == "l5_chat_json":
                return {
                    "query_id": "Q1",
                    "activated": ["FUNCTION_Z"],
                    "suppressed": ["FUNCTION_X"],
                }, {"provider": "initial"}
            assert kwargs["stage"] == "l5_chat_json_direction_repair"
            assert kwargs["user_payload"]["allowed_activated"] == ["FUNCTION_X", "FUNCTION_Y"]
            assert kwargs["user_payload"]["allowed_suppressed"] == ["FUNCTION_Z"]
            return {
                "query_id": "Q1",
                "activated": ["FUNCTION_X"],
                "suppressed": ["FUNCTION_Z"],
            }, {"provider": "repair"}

    provider = Provider()
    pxf = PxFQuery()
    qdata = pxf.read.query("chat json direction repair")
    dossier = sample_dossier()
    qdata.uns["evidence_dossier"] = dossier
    qdata.uns["result"] = dossier
    pxf.tl.answer(qdata)

    pxf.tl.chat(
        qdata,
        "Return JSON with query_id, activated, suppressed. activated and suppressed must contain exactly 1 item.",
        llm_provider=provider,
        print_response=False,
        response_mode="json",
    )
    payload = json.loads(pxf.get.chat(qdata))

    assert provider.stages == ["l5_chat_json", "l5_chat_json_direction_repair"]
    assert payload["activated"] == ["FUNCTION_X"]
    assert payload["suppressed"] == ["FUNCTION_Z"]
    assert pxf.get.chat_history(qdata)[0]["provider_evidence"]["structured_direction_validation"]["status"] == "repaired_by_llm"

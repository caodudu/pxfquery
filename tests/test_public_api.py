import pxfquery
from pxfquery import PxFQuery, PxFQueryData
from pxfquery.cli import main as cli_main
from pxfquery.resources import ResourceManager, default_manifest
from pxfquery.utils.env import load_env_file


def test_public_entrypoint_is_single_client():
    assert pxfquery.__all__ == ["PxFQuery", "PxFQueryData"]
    assert PxFQueryData(text="query").text == "query"
    assert PxFQuery().version == "0.5.28.dev0"


def test_scanpy_style_namespaces_are_available():
    pxf = PxFQuery()

    assert hasattr(pxf, "settings")
    assert hasattr(pxf, "read")
    assert hasattr(pxf, "pp")
    assert hasattr(pxf.pp, "route")
    assert hasattr(pxf, "tl")
    assert hasattr(pxf.tl, "parse")
    assert hasattr(pxf.tl, "anno")
    assert hasattr(pxf.tl, "answer")
    assert hasattr(pxf.tl, "chat")
    assert hasattr(pxf.tl, "figures")
    assert not hasattr(pxf.tl, "route")
    assert hasattr(pxf, "get")
    assert hasattr(pxf.get, "evidence")
    assert hasattr(pxf.get, "chat")
    assert not hasattr(pxf, "load_data")
    assert not hasattr(pxf, "load_data_dir")
    assert not hasattr(pxf, "enable_resolver")
    assert not hasattr(pxf, "pert2func")
    assert not hasattr(pxf, "func2pert")
    assert not hasattr(pxf, "plot")


def test_resource_manifest_switch_does_not_reuse_local_root(tmp_path):
    local_root = tmp_path / "local_pack"
    cache_root = tmp_path / "cache"
    local_root.mkdir()
    manager = ResourceManager(cache_dir=cache_root)

    manager.use(local_root, strict=False)
    local_status = manager.status()
    assert local_status.source == "local_resource_pack"
    assert local_status.root == str(local_root.resolve())

    manager.use_manifest(default_manifest(), strict=False)
    manifest_status = manager.status()
    assert manifest_status.source == "manifest"
    assert manifest_status.root is None
    item = manager._resource_file(group="l3_functional_scores", modality="cp", kind="matrix")
    assert str(local_root.resolve()) not in item.path
    assert str(cache_root.resolve() / "v20260628") in item.path


def test_default_route_prefetch_requires_only_current_l2_proxy_neighbors(tmp_path):
    manager = ResourceManager(cache_dir=tmp_path / "cache")

    status = manager.ensure("l2_proxy_neighbors", auto_download=False)

    assert "l2.cellline_neighbors" in status.missing_files
    assert "l2.drug_neighbors" in status.missing_files
    assert "l2.gene_neighbors" in status.missing_files
    assert len(status.missing_files) == 3


def test_tl_anno_attaches_only_provider_returned_records():
    class Provider:
        name = "fake-annotation"

        def annotate(self, *, query, evidence_dossier):
            return [{"source": "unit-test", "query": query, "status": evidence_dossier["dossier_status"]}]

    pxf = PxFQuery()
    qdata = pxf.read.query("test annotation")
    qdata.uns["evidence_dossier"] = {
        "schema_version": "l4-evidence-dossier/v1",
        "dossier_status": "evidence_found",
        "evidence_layer": {},
    }

    pxf.tl.anno(qdata, providers=[Provider()])

    annotation = qdata.uns["evidence_dossier"]["evidence_layer"]["annotation_evidence"]
    assert annotation["status"] == "completed"
    assert annotation["records"][0]["provider"] == "fake-annotation"
    assert annotation["records"][0]["records"] == [{"source": "unit-test", "query": "test annotation", "status": "evidence_found"}]


def test_cli_load_restores_saved_qdata_for_json_and_answer(tmp_path, capsys):
    pxf = PxFQuery()
    qdata = pxf.read.query("show PERT_X effects")
    qdata.uns["evidence_dossier"] = _sample_dossier()
    qdata.uns["result"] = qdata.uns["evidence_dossier"]
    pkl = tmp_path / "qdata.pkl"
    pxf.tl.save(qdata, pkl)

    assert cli_main(["load", str(pkl), "--json"]) == 0
    json_out = capsys.readouterr().out
    assert '"schema_version": "pxfquery-qdata-cli/v1"' in json_out
    assert '"evidence_dossier"' in json_out
    assert '"_answer"' not in json_out

    assert cli_main(["load", str(pkl), "--answer"]) == 0
    answer_out = capsys.readouterr().out
    assert "Answer" in answer_out
    assert "PERT_X changes FUNCTION_X in CONTEXT_X." in answer_out
    assert "Analysis source: pxfquery 0.5.28.dev0" in answer_out


def test_env_file_loader_accepts_export_and_quoted_deepseek_aliases(tmp_path, monkeypatch):
    for key in [
        "PXFQUERY_LLM_API_KEY",
        "PXFQUERY_LLM_BASE_URL",
        "PXFQUERY_LLM_MODEL",
        "DEEPSEEK_API_KEY",
        "DEEPSEEK_API_BASE",
        "DEEPSEEK_MODEL",
    ]:
        monkeypatch.delenv(key, raising=False)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                'export DEEPSEEK_API_KEY="deepseek-token"',
                "DEEPSEEK_API_BASE='https://deepseek.example/v1'",
                "DEEPSEEK_MODEL=deepseek-test-model",
            ]
        ),
        encoding="utf-8",
    )

    load_env_file(env_file)
    status = PxFQuery().settings.l1_provider_status()

    assert status["configured"] is True
    assert status["base_url"] == "https://deepseek.example/v1"
    assert status["model"] == "deepseek-test-model"


def _sample_dossier():
    return {
        "schema_version": "l4-evidence-dossier/v1",
        "query_type": "forward",
        "dossier_status": "evidence_found",
        "claim_basis": {
            "answerability": "answered",
            "main_claim": "Matrix evidence supports a functional response.",
            "claim_type": "matrix_backed_effect",
            "claim_strength": "high",
        },
        "evidence_layer": {
            "evidence_grade": "exact_matrix",
            "llm_synthesis": {
                "status": "completed",
                "biological_summary": "PERT_X changes FUNCTION_X in CONTEXT_X.",
                "evidence_audit_summary": "A saved query object was restored from pickle.",
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
                    "n_rows": 1,
                    "top_activated": [{"rank": 1, "label": "FUNCTION_X", "score": 0.7, "direction": "activated"}],
                    "top_suppressed": [],
                },
                "executed_routes": [
                    {
                        "route_id": "route_x",
                        "status": "executed",
                        "cell": "CONTEXT_X",
                        "perturbation": "PERT_X",
                        "modality": "cp",
                        "cell_match_distance": 0.0,
                        "perturbation_match_distance": 0.0,
                        "n_rows": 1,
                        "top_activated": [{"rank": 1, "label": "FUNCTION_X", "score": 0.7, "direction": "activated"}],
                        "top_suppressed": [],
                    }
                ],
            },
        },
        "uncertainty_layer": {"confidence": "high", "limitations": []},
    }

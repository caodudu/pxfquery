import pxfquery
from pxfquery import PxFQuery


def test_version_is_public():
    assert pxfquery.__version__ == "0.1.5"
    assert PxFQuery().version == "0.1.5"


def test_only_class_is_exported_at_top_level():
    assert pxfquery.__all__ == ["PxFQuery"]


def test_client_query_api():
    client = PxFQuery()
    result = client.query("What happens to KRAS knockdown in A549?")
    assert result["route_type"] == "exact-hit"
    assert result["intent"]["perturbation_identity"] == "KRAS"


def test_client_ask_api():
    client = PxFQuery()
    result = client.ask("Which drugs activate apoptosis in A549 cells?")
    assert result["route_type"] == "exact-hit"
    assert result["intent"]["direction"] == "reverse"


def test_register_llm_provider():
    client = PxFQuery()
    client.settings.register_llm(
        "local/test-model",
        base_url="http://localhost:3000/v1",
        api_key_env="PXFQUERY_TEST_KEY",
        model="test-model",
        mode="real",
    )
    provider = client.get_llm_provider("local/test-model")
    assert provider.base_url == "http://localhost:3000/v1"
    assert provider.api_key_env == "PXFQUERY_TEST_KEY"
    assert "local/test-model" in client.list_llm_providers()


def test_client_registers_default_provider_when_unset():
    client = PxFQuery()
    client.register_llm_provider("local/instance-model", base_url="http://localhost:3000/v1")
    assert client.provider == "local/instance-model"


def test_scverse_style_workflow_registers_provider_before_query():
    client = PxFQuery()
    client.settings.register_llm(
        "local/workflow-model",
        base_url="http://localhost:3000/v1",
        api_key_env="PXFQUERY_TEST_KEY",
        model="workflow-model",
        mode="real",
    )

    qdata = client.read.query("Run with registered llm_gateway/deepseek-ai/deepseek-v4-flash and record prompt.")
    client.pp.parse(qdata)
    client.tl.resolve(qdata)
    result = client.get.result(qdata)

    assert client.provider == "local/workflow-model"
    assert qdata.uns["provider"]["registered_before_parse"] is True
    assert result["provider"]["name"] == "local/workflow-model"
    assert result["provider"]["registered_before_query"] is True
    assert result["provider"]["mode"] == "real"


def test_asset_registry_is_registered_before_query(tmp_path):
    data_root = tmp_path / "standard_resources"
    data_root.mkdir()
    for filename in [
        "cp_func_ad.h5ad",
        "sh_func_ad.h5ad",
        "xpr_func_ad.h5ad",
        "cellline_info_standard.csv",
        "cellline_meta_standard.csv",
        "compound_info_standard.csv",
        "compound_meta_standard.csv",
        "gene_info_standard.csv",
        "drug_index.json",
        "gene_index.json",
        "gene_index_simple.json",
        "cellline_index.json",
        "drug_neighbors.json",
        "gene_neighbors.json",
        "gene_neighbors_simple.json",
        "cellline_neighbors.json",
        "cellline_tree.json",
        "function_index.json",
        "data_description.yaml",
    ]:
        (data_root / filename).write_text("{}", encoding="utf-8")

    client = PxFQuery()
    registry = client.register_assets(root=data_root)
    qdata = client.read.query("Which drugs activate apoptosis in A549 cells?")
    client.pp.parse(qdata)
    client.tl.resolve(qdata)
    result = client.get.result(qdata)

    assert "matrix.cp_func_ad" in registry.keys()
    assert "metadata.compound_info" in registry.keys()
    assert "provenance.data_description" in registry.keys()
    assert qdata.uns["assets"]["registered_before_parse"] is True
    assert result["asset_registry"]["registered_before_query"] is True
    assert result["assets"]["index.drug_index"]["path"].endswith("drug_index.json")


def test_asset_manifest_allows_moved_files(tmp_path):
    moved = tmp_path / "moved_assets"
    moved.mkdir()
    (moved / "drug_index.custom.json").write_text("{}", encoding="utf-8")
    manifest = {
        "root": str(moved),
        "assets": {
            "index.drug_index": {
                "path": "drug_index.custom.json",
                "role": "drug lookup index",
                "version": "local-test",
            }
        },
    }

    client = PxFQuery()
    registry = client.settings.register_assets(manifest=manifest)

    assert registry.get("index.drug_index").exists is True
    assert registry.get("index.drug_index").metadata["version"] == "local-test"

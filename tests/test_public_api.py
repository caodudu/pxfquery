import pxfquery
from pxfquery import PxFQuery
from pxfquery.resources import ResourceManager, default_manifest


def test_public_entrypoint_is_single_client():
    assert pxfquery.__all__ == ["PxFQuery"]
    assert PxFQuery().version == "0.5.10.dev0"


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

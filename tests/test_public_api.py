import pxfquery
from pxfquery import PxFQuery


def test_public_entrypoint_is_single_client():
    assert pxfquery.__all__ == ["PxFQuery"]
    assert PxFQuery().version == "0.5.5.dev0"


def test_scanpy_style_namespaces_are_available():
    pxf = PxFQuery()

    assert hasattr(pxf, "settings")
    assert hasattr(pxf, "read")
    assert hasattr(pxf, "pp")
    assert hasattr(pxf.pp, "route")
    assert hasattr(pxf, "tl")
    assert not hasattr(pxf.tl, "route")
    assert hasattr(pxf, "get")
    assert not hasattr(pxf, "load_data")
    assert not hasattr(pxf, "load_data_dir")
    assert not hasattr(pxf, "enable_resolver")
    assert not hasattr(pxf, "pert2func")
    assert not hasattr(pxf, "func2pert")
    assert not hasattr(pxf, "plot")

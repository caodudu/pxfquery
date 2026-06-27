from pathlib import Path


def test_source_root_contains_only_thin_entrypoints_and_layer_folders():
    source_root = Path(__file__).resolve().parents[1] / "src" / "pxfquery"
    visible_names = sorted(path.name for path in source_root.iterdir() if path.name != "__pycache__")

    assert visible_names == [
        "__init__.py",
        "__main__.py",
        "cli.py",
        "client.py",
        "l1_nlu",
        "l2_routing",
        "l3_execution",
        "l4_evidence",
        "l5_presentation",
        "settings.py",
        "utils",
        "version.py",
        "workflow.py",
    ]

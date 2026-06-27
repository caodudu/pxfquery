from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "pxfquery"
UNSUPPORTED_OUTPUT_MARKERS = [
    "BRD" + "-",
    "HG" + "NC" + ":",
    "HALL" + "MARK" + "_",
    "score=" + "1.",
]


def test_product_source_has_no_hardcoded_demo_answers():
    text = "\n".join(path.read_text(encoding="utf-8") for path in SRC.rglob("*.py"))
    for marker in UNSUPPORTED_OUTPUT_MARKERS:
        assert marker not in text


def test_tests_do_not_smuggle_demo_biomedical_answers_into_source():
    blocked = [
        "cell" + " death",
        "lung" + " cancer",
        "compound" + "_a",
        "compound" + "_b",
        "model" + "_context_a",
    ]
    text = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "tests").rglob("*.py"))
    for marker in blocked:
        assert marker not in text


def test_user_visible_artifacts_do_not_show_unsupported_biological_outputs():
    blocked = [
        "real resource-pack query is" + " not" + " connected",
        "score=" + "1.",
        "HALL" + "MARK" + "_",
        "BRD" + "-",
        "HG" + "NC" + ":",
    ]
    roots = [ROOT / "README.md", ROOT / "docs"]
    text_parts: list[str] = []
    for root in roots:
        if root.is_file():
            text_parts.append(root.read_text(encoding="utf-8"))
        elif root.exists():
            text_parts.extend(path.read_text(encoding="utf-8") for path in root.rglob("*") if path.is_file())
    text = "\n".join(text_parts)
    for marker in blocked:
        assert marker not in text


def test_product_source_has_five_visible_layers():
    expected = ["nlu", "routing", "execution", "evidence", "presentation"]
    for name in expected:
        assert (SRC / name / "__init__.py").exists()


def test_package_root_is_only_thin_entrypoints():
    expected = {"__init__.py", "__main__.py", "_version.py"}
    actual = {path.name for path in SRC.iterdir() if path.is_file()}
    assert actual == expected


def test_presentation_layer_contains_only_current_files():
    allowed = {"__init__.py", "answer.py", "cli.py", "client.py", "model.py"}
    actual = {path.name for path in (SRC / "presentation").iterdir() if path.is_file()}
    assert actual == allowed

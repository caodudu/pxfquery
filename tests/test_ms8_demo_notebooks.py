import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"


def test_demo_notebooks_cover_four_biomedical_scenarios():
    expected = {
        "01_drug_forward.ipynb": "How does erlotinib change functional programs in A549 lung cancer cells?",
        "02_drug_reverse.ipynb": "Which drugs activate apoptosis in A549 cells?",
        "03_genetic_forward.ipynb": "What happens to functional programs if I knock down KRAS in A549 lung cancer cells?",
        "04_genetic_reverse.ipynb": "What genetic perturbations suppress MYC expression in A549 cells?",
    }

    for filename, question in expected.items():
        path = DEMO / filename
        assert path.exists(), filename
        notebook = json.loads(path.read_text(encoding="utf-8"))
        assert notebook["nbformat"] == 4
        assert notebook["metadata"]["pxfquery_demo"]["question"] == question
        assert "PxFQuery().ask" in "".join(notebook["cells"][0]["source"])
        assert any("PxFquery answer" in "".join(output.get("text", [])) for cell in notebook["cells"] for output in cell.get("outputs", []))

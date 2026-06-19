from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    if str(workspace / "script") not in sys.path:
        sys.path.insert(0, str(workspace / "script"))

    def query_pubchem(name: str) -> dict:
        url = (
            "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
            + urllib.parse.quote(name)
            + "/property/IsomericSMILES,InChIKey/JSON"
        )
        try:
            with urllib.request.urlopen(url, timeout=12) as r:
                d = json.loads(r.read())
            props = d["PropertyTable"]["Properties"][0]
            return {
                "smiles": props.get("IsomericSMILES") or props.get("SMILES"),
                "inchikey": props.get("InChIKey"),
            }
        except Exception as e:
            return {"error": f"{type(e).__name__}: {e}"}

    def query_cellosaurus(name: str) -> dict | None:
        q = urllib.parse.quote(f'id:\"{name}\"')
        url = (
            "https://api.cellosaurus.org/search/cell-line"
            f"?q={q}&format=json&fields=id,ac,sy,di,ca,derived-from-site&nbresults=1"
        )
        try:
            with urllib.request.urlopen(url, timeout=12) as r:
                d = json.loads(r.read())
            cells = d.get("Cellosaurus", {}).get("cell-line-list", [])
            if not cells:
                return None
            cl = cells[0]
            diseases = [x.get("label", "") for x in cl.get("disease-list", [])]
            sites = [s.get("site", {}).get("value", "") for s in cl.get("derived-from-site-list", [])]
            return {
                "site": sites[0] if sites else "",
                "disease": diseases[0] if diseases else "",
                "category": cl.get("category", ""),
            }
        except Exception as e:
            return {"error": f"{type(e).__name__}: {e}"}

    # PubChem runtime demo
    pubchem_cases = ["erlotinib", "tarceva", "not_a_real_drug_name_xyz"]
    pubchem_results = {name: query_pubchem(name) for name in pubchem_cases}

    # Cellosaurus runtime demo
    cell_cases = ["HAP1", "HEK293T", "NCI-H358", "MCLF1234"]
    cell_results = {name: query_cellosaurus(name) for name in cell_cases}

    payload = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "pubchem": pubchem_results,
        "cellosaurus": cell_results,
    }

    out_json = workspace / "output/store/resolver_demo/external_api_demo.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    out_md = workspace / "report/6_llm_resovler_external_api_demo.md"
    lines = [
        "# External API Demo (PubChem + Cellosaurus)",
        "",
        f"- Time: {payload['time']}",
        "",
        "## PubChem",
        "",
        "```json",
        json.dumps(pubchem_results, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Cellosaurus",
        "",
        "```json",
        json.dumps(cell_results, ensure_ascii=False, indent=2),
        "```",
    ]
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"external api json: {out_json}")
    print(f"external api report: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

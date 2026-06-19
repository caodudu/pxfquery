from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path


def _load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _ensure_sys_path(workspace: Path) -> None:
    package_root = workspace / "script"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))


def _has_pair(engine, pert: str, cell: str) -> bool:
    _, mask = engine._match_perturbation(pert)  # pylint: disable=protected-access
    if int(mask.sum()) == 0:
        return False
    cell_mask = engine._obs["cell_iname"] == cell  # pylint: disable=protected-access
    return int((mask & cell_mask).sum()) > 0


def _pick_exact_gene_case(xpr_engine):
    obs = xpr_engine._obs  # pylint: disable=protected-access
    row = obs[(obs["cell_iname"] == "A549")].iloc[0]
    gene = str(row["cmap_name"])
    return {"cell": "A549", "gene": gene}


def _pick_proxy_pert_gene_case(xpr_engine, gene_index, cell="A549"):
    obs = xpr_engine._obs  # pylint: disable=protected-access
    cell_genes = set(obs.loc[obs["cell_iname"] == cell, "cmap_name"].astype(str).str.upper().tolist())
    for base, nbrs in gene_index._neighbors_raw.items():  # pylint: disable=protected-access
        if base in cell_genes:
            continue
        for nbr, _ in nbrs[:20]:
            if nbr in cell_genes:
                return {"cell": cell, "base": base, "neighbor": nbr}
    raise RuntimeError("No proxy-pert gene case found.")


def _pick_proxy_cell_gene_case(xpr_engine, cellline_index, preferred_cell="A549"):
    obs = xpr_engine._obs  # pylint: disable=protected-access
    all_cells = [preferred_cell] + [
        c for c in sorted(obs["cell_iname"].astype(str).unique().tolist()) if c != preferred_cell
    ]
    for cell in all_cells:
        cell_genes = set(obs.loc[obs["cell_iname"] == cell, "cmap_name"].astype(str).str.upper().tolist())
        proxies = cellline_index.proxy_cells_for(cell)
        proxy_cells = proxies["same_subtype"] + proxies["same_disease"] + proxies["same_lineage"]
        if not proxy_cells:
            continue
        proxy_genes = set(obs.loc[obs["cell_iname"].isin(proxy_cells), "cmap_name"].astype(str).str.upper().tolist())
        for g in proxy_genes:
            if g not in cell_genes:
                return {"cell": cell, "proxy_cells": proxy_cells, "gene": g}
    raise RuntimeError("No proxy-cell gene case found.")


def _pick_exact_drug_case(cp_engine, drug_index, cell="A549"):
    obs = cp_engine._obs  # pylint: disable=protected-access
    cell_drugs = set(obs.loc[obs["cell_iname"] == cell, "pert_id"].astype(str).tolist())
    for alias, brd in drug_index._index.items():  # pylint: disable=protected-access
        if brd in cell_drugs:
            return {"cell": cell, "alias": alias, "brd": brd}
    raise RuntimeError("No exact drug case found.")


def _pick_proxy_pert_drug_case(cp_engine, drug_index, cell="A549"):
    obs = cp_engine._obs  # pylint: disable=protected-access
    cell_drugs = set(obs.loc[obs["cell_iname"] == cell, "pert_id"].astype(str).tolist())
    for base_key, nbrs in drug_index._neighbors_raw.items():  # pylint: disable=protected-access
        base = "BRD-" + base_key
        if base in cell_drugs:
            continue
        for nkey, _ in nbrs[:20]:
            nbr = "BRD-" + nkey
            if nbr in cell_drugs:
                alias = None
                for a, b in drug_index._index.items():  # pylint: disable=protected-access
                    if b == base:
                        alias = a
                        break
                return {"cell": cell, "base_brd": base, "base_alias": alias or base, "neighbor": nbr}
    raise RuntimeError("No proxy-pert drug case found.")


def _pick_proxy_both_gene_case(xpr_engine, gene_index, cellline_index):
    obs = xpr_engine._obs  # pylint: disable=protected-access
    all_cells = sorted(obs["cell_iname"].astype(str).unique().tolist())
    for seed_cell in all_cells:
        proxies = cellline_index.proxy_cells_for(seed_cell)
        proxy_cells = proxies["same_subtype"] + proxies["same_disease"] + proxies["same_lineage"]
        if not proxy_cells:
            continue
        base_cell_genes = set(obs.loc[obs["cell_iname"] == seed_cell, "cmap_name"].astype(str).str.upper().tolist())
        proxy_gene_union = set(obs.loc[obs["cell_iname"].isin(proxy_cells), "cmap_name"].astype(str).str.upper().tolist())
        for base, nbrs in gene_index._neighbors_raw.items():  # pylint: disable=protected-access
            if base in base_cell_genes:
                continue
            if base in proxy_gene_union:
                continue  # L3 would hit
            for nbr, _ in nbrs[:30]:
                if nbr in proxy_gene_union and nbr not in base_cell_genes:
                    return {
                        "seed_cell": seed_cell,
                        "proxy_cells": proxy_cells,
                        "base": base,
                        "neighbor_hint": nbr,
                    }
    raise RuntimeError("No proxy-both gene case found.")


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    _ensure_sys_path(workspace)
    _load_env(workspace / ".env")

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / "output/store/gsea_anndata"))

    # Temporary resolver to access indexes/engines for case discovery.
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="mock",
        model="mock-model",
    )
    resolver = pxf._resolver  # pylint: disable=protected-access
    xpr = pxf._forward_engines["xpr"]  # pylint: disable=protected-access
    cp = pxf._forward_engines["cp"]  # pylint: disable=protected-access

    exact_gene = _pick_exact_gene_case(xpr)
    proxy_pert_gene = _pick_proxy_pert_gene_case(xpr, resolver.gene_index, cell=exact_gene["cell"])
    proxy_cell_gene = _pick_proxy_cell_gene_case(xpr, resolver.cellline_index, preferred_cell=exact_gene["cell"])
    proxy_both_gene = _pick_proxy_both_gene_case(
        xpr,
        resolver.gene_index,
        resolver.cellline_index,
    )
    exact_drug = _pick_exact_drug_case(cp, resolver.drug_index, cell=exact_gene["cell"])
    proxy_pert_drug = _pick_proxy_pert_drug_case(cp, resolver.drug_index, cell=exact_gene["cell"])

    query_intents = {
        "CASE_EXACT_GENE": {
            "query_type": "forward",
            "bio_context": exact_gene["cell"],
            "pert_desc": exact_gene["gene"],
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_PROXY_PERT_GENE": {
            "query_type": "forward",
            "bio_context": exact_gene["cell"],
            "pert_desc": proxy_pert_gene["base"],
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_PROXY_CELL_GENE_BY_DISEASE": {
            "query_type": "forward",
            "bio_context": "non-small cell lung carcinoma",
            "pert_desc": proxy_cell_gene["gene"],
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_UNKNOWN_CELL_INPUT": {
            "query_type": "forward",
            "bio_context": "NCI-H358 non-small cell lung cancer",
            "pert_desc": exact_gene["gene"],
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_PROXY_BOTH_GENE": {
            "query_type": "forward",
            "bio_context": proxy_both_gene["seed_cell"],
            "pert_desc": proxy_both_gene["base"],
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_EXACT_DRUG": {
            "query_type": "forward",
            "bio_context": exact_drug["cell"],
            "pert_desc": exact_drug["alias"],
            "pert_class": "drug",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
        "CASE_PROXY_PERT_DRUG": {
            "query_type": "forward",
            "bio_context": proxy_pert_drug["cell"],
            "pert_desc": proxy_pert_drug["base_alias"],
            "pert_class": "drug",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 10,
        },
    }

    def parse_intent_hook(user_input: str):
        return query_intents[user_input]

    def map_cell_hook(bio_desc: str, options: list[str], level_name: str):
        text = bio_desc.lower()
        if "lung" in text:
            if level_name == "lineage":
                return "lung" if "lung" in options else options[0]
            if level_name == "disease":
                for opt in options:
                    if "lung cancer" in opt:
                        return opt
            if level_name == "subtype":
                for opt in options:
                    if "non-small cell lung carcinoma" in opt:
                        return opt
        return options[0]

    hooks = {
        "llm_parse_intent": parse_intent_hook,
        "llm_map_cell_line": map_cell_hook,
        "llm_map_gene": lambda gene_desc, _: [gene_desc],
        "llm_map_drug": lambda _: [],
        "llm_normalize_drug": lambda x: [x],
        "llm_map_function": lambda a, b, c: [],
        "llm_summarize_forward": lambda result, include_numbers=False: f"mock summary {result.resolver_meta.get('hit_level')}",
        "llm_summarize_reverse": lambda result, include_numbers=False: "mock reverse summary",
    }

    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="mock",
        model="mock-model",
        prompt_hooks=hooks,
    )

    cases = [
        ("CASE_EXACT_GENE", "EXACT"),
        ("CASE_PROXY_PERT_GENE", "PROXY_PERT"),
        ("CASE_PROXY_CELL_GENE_BY_DISEASE", "PROXY_CELL"),
        ("CASE_UNKNOWN_CELL_INPUT", "PROXY_CELL"),
        ("CASE_PROXY_BOTH_GENE", "PROXY_BOTH"),
        ("CASE_EXACT_DRUG", "EXACT"),
        ("CASE_PROXY_PERT_DRUG", "PROXY_PERT"),
    ]

    results = []
    for q, expected in cases:
        res = pxf.query(q, top_n=10)
        got = res.resolver_meta.get("hit_level")
        ok = got == expected and bool(res.found)
        results.append(
            {
                "query": q,
                "expected_hit_level": expected,
                "got_hit_level": got,
                "found": bool(res.found),
                "ok": ok,
                "resolver_meta": res.resolver_meta,
            }
        )
        if not ok:
            raise AssertionError(f"{q}: expected {expected}, got {got}, found={res.found}")

    out_dir = workspace / "output/store/resolver_demo"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "forward_matrix_results.json"
    json_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = workspace / "report/6_llm_resovler_forward_matrix.md"
    lines = [
        "# 6_llm_resovler Forward Matrix Test",
        "",
        f"- Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "- Mode: mock hooks (deterministic)",
        "",
        "| Query | Expected | Got | Found | Pass |",
        "|------|----------|-----|-------|------|",
    ]
    for r in results:
        lines.append(
            f"| `{r['query']}` | `{r['expected_hit_level']}` | `{r['got_hit_level']}` | `{r['found']}` | `{r['ok']}` |"
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"forward matrix json: {json_path}")
    print(f"forward matrix report: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

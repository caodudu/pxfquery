from pathlib import Path
from itertools import combinations
import gc
import json

import anndata as ad
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path("/public/home/caojun/project/RUSH/3_work")
TABLE = ROOT / "output/table/fig2d_cellline_signature_similarity"
PIC = ROOT / "output/picture/fig2d_cellline_signature_similarity"
TREE_PATH = ROOT / "input/pxfquery_cellline_tree.json"
PIC.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(20260630)
MAX_PAIRS_PER_PERT_RELATION = 80
MAX_TOTAL_PER_RELATION = 12000
RELATION_ORDER = [
    "Same lung-cancer subgroup",
    "Different lung-cancer subgroup",
    "Lung cancer vs non-lung lineage",
]


def load_cell_paths():
    raw = json.loads(TREE_PATH.read_text())
    tree = raw["tree"] if isinstance(raw, dict) and "tree" in raw else raw
    cell_to_path = {}

    def walk(node, path):
        if isinstance(node, list):
            for cell in node:
                cell_to_path[str(cell).upper()] = path + [str(cell).upper()]
        elif isinstance(node, dict):
            for key, value in node.items():
                walk(value, path + [str(key)])

    walk(tree, [])
    return cell_to_path


cell_to_path = load_cell_paths()


def is_lung_cancer(cell):
    path = cell_to_path.get(str(cell).upper())
    return bool(path and len(path) >= 2 and path[0] == "lung" and path[1] == "lung cancer")


def relation(cell_a, cell_b):
    a = str(cell_a).upper()
    b = str(cell_b).upper()
    pa = cell_to_path.get(a)
    pb = cell_to_path.get(b)
    if not pa or not pb:
        return None
    a_lung = is_lung_cancer(a)
    b_lung = is_lung_cancer(b)
    if a_lung and b_lung:
        if len(pa) >= 3 and len(pb) >= 3 and pa[:3] == pb[:3]:
            return "Same lung-cancer subgroup"
        return "Different lung-cancer subgroup"
    if (a_lung and pb[0] != "lung") or (b_lung and pa[0] != "lung"):
        return "Lung cancer vs non-lung lineage"
    return None


def sample_pairs(pairs, max_n):
    if len(pairs) <= max_n:
        return pairs
    take = RNG.choice(len(pairs), size=max_n, replace=False)
    return [pairs[i] for i in take]


def build_plan():
    idx = pd.read_csv(TABLE / "fig2d_split_signature_index_cp.csv", low_memory=False)
    idx = idx[idx["cell_iname"].notna() & idx["pert_id"].notna()].copy()
    idx["cell_norm"] = idx["cell_iname"].astype(str).str.upper()
    idx = idx[idx["cell_norm"].isin(cell_to_path)].copy()
    idx = idx.sort_values(["pert_id", "cell_norm", "sig_id"])
    rep = idx.groupby(["pert_id", "cell_norm"], as_index=False).first()
    rows = []
    counts = []
    for pert_id, g in rep.groupby("pert_id", dropna=True):
        recs = g.to_dict("records")
        by_rel = {rel: [] for rel in RELATION_ORDER}
        for r1, r2 in combinations(recs, 2):
            rel = relation(r1["cell_norm"], r2["cell_norm"])
            if rel:
                by_rel[rel].append((r1, r2))
        for rel, pairs in by_rel.items():
            pairs = sample_pairs(pairs, MAX_PAIRS_PER_PERT_RELATION)
            counts.append({"pert_id": pert_id, "relation": rel, "n_pairs_after_cap": len(pairs)})
            for r1, r2 in pairs:
                rows.append(
                    {
                        "pert_id": pert_id,
                        "cmap_name": r1.get("cmap_name", ""),
                        "relation": rel,
                        "cell_a": r1["cell_norm"],
                        "cell_b": r2["cell_norm"],
                        "path_a": "/".join(cell_to_path[r1["cell_norm"]][:-1]),
                        "path_b": "/".join(cell_to_path[r2["cell_norm"]][:-1]),
                        "sig_id_a": r1.get("sig_id", ""),
                        "sig_id_b": r2.get("sig_id", ""),
                        "split_file_a": r1["split_file"],
                        "split_file_b": r2["split_file"],
                        "row_in_split_a": int(r1["row_in_split"]),
                        "row_in_split_b": int(r2["row_in_split"]),
                    }
                )
    plan = pd.DataFrame(rows)
    balanced = []
    for rel, d in plan.groupby("relation"):
        if len(d) > MAX_TOTAL_PER_RELATION:
            balanced.append(d.sample(n=MAX_TOTAL_PER_RELATION, random_state=20260630))
        else:
            balanced.append(d)
    plan = pd.concat(balanced, ignore_index=True)
    plan.insert(0, "pair_id", [f"lung_ctx_cp_{i:06d}" for i in range(len(plan))])
    plan.to_csv(TABLE / "fig2d_all_chemical_lung_lineage_boxplot_plan.csv", index=False)
    pd.DataFrame(counts).to_csv(TABLE / "fig2d_all_chemical_lung_lineage_boxplot_plan_counts_by_pert.csv", index=False)
    return plan


cache = {}


def load_split(path):
    path = str(path)
    if path in cache:
        return cache[path]
    a = ad.read_h5ad(path)
    landmark = (a.var["feature_space"].astype(str).str.lower() == "landmark").to_numpy()
    if int(landmark.sum()) != 978:
        raise RuntimeError(f"expected 978 landmark genes in {path}, observed {int(landmark.sum())}")
    x = a.X
    if hasattr(x, "toarray"):
        x = x.toarray()
    x = np.asarray(x[:, landmark], dtype=np.float32)
    cache[path] = x
    return x


def finite_pair(x, y):
    mask = np.isfinite(x) & np.isfinite(y)
    if mask.sum() < 3:
        return None, None
    return x[mask].astype(np.float32, copy=False), y[mask].astype(np.float32, copy=False)


def pearson(x, y):
    x, y = finite_pair(x, y)
    if x is None:
        return np.nan
    x = x - x.mean()
    y = y - y.mean()
    denom = np.sqrt(np.dot(x, x) * np.dot(y, y))
    return float(np.dot(x, y) / denom) if denom else np.nan


def l2_norm(x):
    x = x[np.isfinite(x)].astype(np.float32, copy=False)
    return float(np.sqrt(np.dot(x, x))) if len(x) else np.nan


def compute_metrics(plan):
    rows = []
    plan = plan.sort_values(["split_file_a", "split_file_b", "relation"]).reset_index(drop=True)
    for r in plan.itertuples(index=False):
        xa = load_split(r.split_file_a)[int(r.row_in_split_a), :]
        xb = load_split(r.split_file_b)[int(r.row_in_split_b), :]
        na = l2_norm(xa)
        nb = l2_norm(xb)
        rows.append(
            {
                "pair_id": r.pair_id,
                "pert_id": r.pert_id,
                "cmap_name": r.cmap_name,
                "relation": r.relation,
                "cell_a": r.cell_a,
                "cell_b": r.cell_b,
                "pearson_r": pearson(xa, xb),
                "norm_a": na,
                "norm_b": nb,
                "mean_norm": float(np.nanmean([na, nb])),
                "feature_space": "landmark",
                "n_genes": 978,
            }
        )
    metrics = pd.DataFrame(rows)
    metrics["response_magnitude_quartile"] = pd.qcut(
        metrics["mean_norm"].rank(method="first"),
        4,
        labels=["Q1", "Q2", "Q3", "Q4"],
    ).astype(str)
    metrics.to_csv(TABLE / "fig2d_all_chemical_lung_lineage_boxplot_metrics_long.csv", index=False)
    return metrics


def summarize_and_plot(metrics):
    q4 = metrics[metrics["response_magnitude_quartile"] == "Q4"].copy()
    rows = []
    for rel in RELATION_ORDER:
        x = q4.loc[q4["relation"] == rel, "pearson_r"].dropna()
        rows.append(
            {
                "relation": rel,
                "n_pairs": int(len(x)),
                "median_pearson": float(x.median()),
                "q1_pearson": float(x.quantile(0.25)),
                "q3_pearson": float(x.quantile(0.75)),
                "n_perturbations": int(q4.loc[q4["relation"] == rel, "pert_id"].nunique()),
            }
        )
    summary = pd.DataFrame(rows)
    summary.to_csv(TABLE / "fig2d_all_chemical_lung_lineage_boxplot_q4_summary.csv", index=False)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 7,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.linewidth": 0.8,
        }
    )
    data = [q4.loc[q4["relation"] == rel, "pearson_r"].dropna().to_numpy() for rel in RELATION_ORDER]
    fig, ax = plt.subplots(figsize=(3.2, 2.25))
    bp = ax.boxplot(
        data,
        widths=0.55,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "#111111", "linewidth": 1.4},
        boxprops={"linewidth": 1.0, "color": "#333333"},
        whiskerprops={"linewidth": 0.9, "color": "#333333"},
        capprops={"linewidth": 0.9, "color": "#333333"},
    )
    colors = ["#d94841", "#777777", "#bdbdbd"]
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
    ax.set_xticklabels(["Same\nlung subgroup", "Different\nlung subgroup", "Non-lung\nlineage"])
    ax.set_ylabel("Pearson r")
    ax.set_xlabel("Cell-line relationship")
    ax.set_ylim(-0.2, 0.8)
    ax.grid(axis="y", color="#e5e5e5", lw=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    for ext in ["pdf", "svg", "png"]:
        fig.savefig(PIC / f"figure2_panel_D_all_chemical_lung_lineage_q4_boxplot.{ext}", dpi=300)
    plt.close(fig)
    return summary


def main():
    plan = build_plan()
    print("PLAN_PAIRS", len(plan), flush=True)
    metrics = compute_metrics(plan)
    print("METRICS", len(metrics), "splits_loaded", len(cache), flush=True)
    summary = summarize_and_plot(metrics)
    print(summary.to_string(index=False), flush=True)
    cache.clear()
    gc.collect()


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import json
from pathlib import Path

import anndata as ad
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
from matplotlib.patches import Circle, ConnectionPatch
from rdkit import Chem, DataStructs
from rdkit.Chem import rdFingerprintGenerator


mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams["font.family"] = "DejaVu Sans"

PROJECT_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
TASK_ROOT = PROJECT_ROOT / "5_phase_translation/G-011_paper_figure_planning/T-149_figure5_forward_drug_query_notebook_figure_workb"
RESOURCE_DIR = Path("/Users/dudu/.cache/pxfquery/resources/v20260628")
COMPOUND_INFO = PROJECT_ROOT / "4_phase_development/G-007_precomputed_data_exploration/T-021_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/compound_info_standard.csv"
DRUG_NEIGHBORS = RESOURCE_DIR / "drug_neighbors.json"

ANCHOR_IDS = {
    "decitabine": "BRD-K79254416",
    "cytarabine": "BRD-K33106058",
    "gemcitabine": "BRD-K15108141",
    "azacitidine": "BRD-K55026842",
    "zebularine": "BRD-K87714311",
    "cladribine": "BRD-K93034159",
    "clofarabine": "BRD-K34022604",
}
PLOT_LABEL_IDS = {
    "decitabine": "BRD-K79254416",
    "cytarabine": "BRD-K33106058",
    "gemcitabine": "BRD-K15108141",
}
EVIDENCE_IDS = {"BRD-K79254416", "BRD-K33106058", "BRD-K15108141"}
NEIGHBOR_IDS: set[str] = set()
HIGHLIGHT_FACE = "#f59e0b"
HIGHLIGHT_EDGE = "#92400e"


def _full_brd(short_id: str) -> str:
    text = str(short_id or "").strip()
    if text.startswith("BRD-"):
        return text
    if len(text) == 9 and text[0] in {"A", "K"}:
        return f"BRD-{text}"
    return text


def load_compounds() -> pd.DataFrame:
    info = pd.read_csv(COMPOUND_INFO)
    info = info.dropna(subset=["pert_id", "canonical_smiles"]).copy()
    info["pert_id"] = info["pert_id"].astype(str)
    info["cmap_name"] = info["cmap_name"].astype(str)
    info = info.drop_duplicates("pert_id", keep="first")

    neighbor_obj = json.loads(DRUG_NEIGHBORS.read_text())
    resource_ids = {_full_brd(key) for key in neighbor_obj.keys()}
    for neighbors in neighbor_obj.values():
        for item in neighbors:
            if item:
                resource_ids.add(_full_brd(item[0]))
    selected_ids = resource_ids | set(ANCHOR_IDS.values())

    out = info[info["pert_id"].isin(selected_ids)].copy()
    out["role"] = "Other compounds"
    out.loc[out["pert_id"].isin(NEIGHBOR_IDS), "role"] = "Nucleoside analog neighbors"
    out.loc[out["pert_id"].isin(EVIDENCE_IDS), "role"] = "Figure 5A routed evidence"
    out.loc[out["pert_id"] == ANCHOR_IDS["decitabine"], "role"] = "Query drug"
    out["display_name"] = out["cmap_name"].str.lower()
    for name, pert_id in ANCHOR_IDS.items():
        out.loc[out["pert_id"] == pert_id, "display_name"] = name
    return out.reset_index(drop=True)


def build_fingerprint_matrix(compounds: pd.DataFrame, fp_size: int = 2048) -> tuple[np.ndarray, pd.DataFrame]:
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=fp_size)
    rows = []
    keep = []
    for _, row in compounds.iterrows():
        mol = Chem.MolFromSmiles(str(row["canonical_smiles"]))
        if mol is None:
            continue
        fp = fpgen.GetFingerprint(mol)
        arr = np.zeros((fp_size,), dtype=np.uint8)
        DataStructs.ConvertToNumpyArray(fp, arr)
        rows.append(arr)
        keep.append(row)
    if not rows:
        raise RuntimeError("No valid compound fingerprints were produced.")
    kept = pd.DataFrame(keep).reset_index(drop=True)
    return np.vstack(rows).astype(np.uint8), kept


def build_adata(force: bool, h5ad: Path, n_neighbors: int, min_dist: float, random_state: int) -> ad.AnnData:
    if h5ad.exists() and not force:
        return sc.read_h5ad(h5ad)

    compounds = load_compounds()
    x, obs = build_fingerprint_matrix(compounds)
    obs = obs.set_index("pert_id", drop=False)
    adata = ad.AnnData(X=x, obs=obs)
    adata.uns["figure5b"] = {
        "fingerprint": "Morgan radius=2 fpSize=2048",
        "neighbor_metric": "jaccard distance on binary Morgan fingerprints; equivalent to Tanimoto distance",
        "compound_info": str(COMPOUND_INFO),
        "drug_neighbors": str(DRUG_NEIGHBORS),
        "anchor_ids": ANCHOR_IDS,
    }
    sc.pp.neighbors(
        adata,
        n_neighbors=n_neighbors,
        metric="jaccard",
        use_rep="X",
        random_state=random_state,
    )
    sc.tl.umap(adata, min_dist=min_dist, random_state=random_state)
    h5ad.parent.mkdir(parents=True, exist_ok=True)
    adata.write_h5ad(h5ad)
    return adata


def compute_anchor_similarity(adata: ad.AnnData) -> pd.DataFrame:
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    rows = []
    obs = adata.obs.reset_index(drop=True)
    smiles = dict(zip(obs["pert_id"], obs["canonical_smiles"]))
    dec_mol = Chem.MolFromSmiles(smiles[ANCHOR_IDS["decitabine"]])
    dec_fp = fpgen.GetFingerprint(dec_mol)
    for name, pert_id in ANCHOR_IDS.items():
        mol = Chem.MolFromSmiles(smiles[pert_id])
        fp = fpgen.GetFingerprint(mol)
        rows.append(
            {
                "drug": name,
                "pert_id": pert_id,
                "tanimoto_to_decitabine": DataStructs.TanimotoSimilarity(dec_fp, fp),
                "figure5a_evidence": pert_id in EVIDENCE_IDS,
            }
        )
    return pd.DataFrame(rows).sort_values("tanimoto_to_decitabine", ascending=False)


def plot_umap(adata: ad.AnnData, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    coords = np.asarray(adata.obsm["X_umap"])
    obs = adata.obs.reset_index(drop=True)

    query = (obs["pert_id"] == ANCHOR_IDS["decitabine"]).to_numpy()
    evidence = obs["pert_id"].isin(EVIDENCE_IDS - {ANCHOR_IDS["decitabine"]}).to_numpy()
    neighbors = obs["pert_id"].isin(NEIGHBOR_IDS).to_numpy()
    anchor = query | evidence | neighbors
    other = ~anchor

    anchor_coords = coords[obs["pert_id"].isin(PLOT_LABEL_IDS.values()).to_numpy()]
    center = anchor_coords.mean(axis=0)
    radius = max(np.ptp(anchor_coords[:, 0]), np.ptp(anchor_coords[:, 1])) * 0.72
    radius = max(radius, 0.85)

    fig, (ax_full, ax_zoom) = plt.subplots(
        1,
        2,
        figsize=(9.8, 4.7),
        gridspec_kw={"width_ratios": [0.88, 1.12], "wspace": -0.02},
    )
    for ax in (ax_full, ax_zoom):
        ax.set_axis_off()

    ax_full.scatter(coords[other, 0], coords[other, 1], s=2.2, c="#aeb8c4", alpha=0.62, linewidths=0, rasterized=True)
    ax_full.scatter(coords[neighbors, 0], coords[neighbors, 1], s=24, c=HIGHLIGHT_FACE, alpha=0.95, edgecolors=HIGHLIGHT_EDGE, linewidths=0.35)
    ax_full.scatter(coords[evidence, 0], coords[evidence, 1], s=32, c=HIGHLIGHT_FACE, alpha=0.98, edgecolors=HIGHLIGHT_EDGE, linewidths=0.45)
    ax_full.scatter(coords[query, 0], coords[query, 1], s=46, c=HIGHLIGHT_FACE, alpha=1.0, edgecolors=HIGHLIGHT_EDGE, linewidths=0.55)
    ax_full.add_patch(Circle(center, radius, fill=False, edgecolor="#111827", linewidth=0.8, alpha=0.72))
    ax_full.set_aspect("equal", adjustable="datalim")

    circle = Circle((0.5, 0.5), 0.485, transform=ax_zoom.transAxes, facecolor="none", edgecolor="#111827", linewidth=0.9)
    ax_zoom.add_patch(circle)
    zoom_xlim = (center[0] - radius, center[0] + radius)
    zoom_ylim = (center[1] - radius, center[1] + radius)
    in_zoom = (
        (coords[:, 0] >= zoom_xlim[0])
        & (coords[:, 0] <= zoom_xlim[1])
        & (coords[:, 1] >= zoom_ylim[0])
        & (coords[:, 1] <= zoom_ylim[1])
    )
    collections = [
        ax_zoom.scatter(coords[in_zoom & other, 0], coords[in_zoom & other, 1], s=14, c="#9aa6b2", alpha=0.72, linewidths=0, rasterized=True),
        ax_zoom.scatter(coords[in_zoom & neighbors, 0], coords[in_zoom & neighbors, 1], s=34, c=HIGHLIGHT_FACE, alpha=0.98, edgecolors=HIGHLIGHT_EDGE, linewidths=0.48),
        ax_zoom.scatter(coords[in_zoom & evidence, 0], coords[in_zoom & evidence, 1], s=42, c=HIGHLIGHT_FACE, alpha=0.98, edgecolors=HIGHLIGHT_EDGE, linewidths=0.58),
        ax_zoom.scatter(coords[in_zoom & query, 0], coords[in_zoom & query, 1], s=60, c=HIGHLIGHT_FACE, alpha=1.0, edgecolors=HIGHLIGHT_EDGE, linewidths=0.68),
    ]
    for collection in collections:
        collection.set_clip_path(circle)
    ax_zoom.set_xlim(*zoom_xlim)
    ax_zoom.set_ylim(*zoom_ylim)
    ax_zoom.set_aspect("equal", adjustable="box")

    for xy_full, xy_zoom in [
        ((center[0] + radius, center[1] + radius * 0.62), (0.055, 0.74)),
        ((center[0] + radius, center[1] - radius * 0.62), (0.055, 0.26)),
    ]:
        con = ConnectionPatch(
            xyA=xy_full,
            xyB=xy_zoom,
            coordsA=ax_full.transData,
            coordsB=ax_zoom.transAxes,
            axesA=ax_full,
            axesB=ax_zoom,
            color="#111827",
            linewidth=0.7,
            alpha=0.58,
            zorder=0,
        )
        fig.add_artist(con)

    label_offsets = {
        "decitabine": (-38, 18),
        "cytarabine": (42, -8),
        "gemcitabine": (38, 22),
    }
    id_to_idx = {pert_id: i for i, pert_id in enumerate(obs["pert_id"].tolist())}
    for name, pert_id in PLOT_LABEL_IDS.items():
        idx = id_to_idx.get(pert_id)
        if idx is None:
            continue
        x0, y0 = coords[idx]
        dx, dy = label_offsets.get(name, (24, 18))
        ann = ax_zoom.annotate(
            name,
            xy=(x0, y0),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=7.8,
            weight="bold" if name in {"decitabine", "cytarabine", "gemcitabine"} else "normal",
            color="#111827",
            arrowprops=dict(arrowstyle="-", color="#374151", lw=0.62, alpha=0.85),
            ha="center",
            va="center",
        )
        ann.set_clip_path(circle)

    pdf = output_dir / "fig5b_drug_tanimoto_umap_decitabine_routes.pdf"
    png = output_dir / "fig5b_drug_tanimoto_umap_decitabine_routes.png"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=260, bbox_inches="tight")
    plt.close(fig)
    return pdf, png


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=TASK_ROOT / "4_artifact/4_picture/figure5/panel_b_drug_tanimoto_umap")
    parser.add_argument("--h5ad", type=Path, default=TASK_ROOT / "3_execution/panel_b_drug_tanimoto_umap_outputs/drug_morgan_tanimoto_umap_decitabine.h5ad")
    parser.add_argument("--n-neighbors", type=int, default=15)
    parser.add_argument("--min-dist", type=float, default=0.35)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    adata = build_adata(args.force, args.h5ad, args.n_neighbors, args.min_dist, args.random_state)
    sim = compute_anchor_similarity(adata)
    sim_path = args.output_dir / "fig5b_decitabine_anchor_tanimoto.csv"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sim.to_csv(sim_path, index=False)
    for path in plot_umap(adata, args.output_dir):
        print(path)
    print(sim_path)
    print(f"n_compounds={adata.n_obs}")


if __name__ == "__main__":
    main()


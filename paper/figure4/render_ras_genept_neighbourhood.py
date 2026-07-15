from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams["font.family"] = "DejaVu Sans"

PROJECT_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
EMBEDDING_PATH = PROJECT_ROOT / "2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/genept_embeddings/M-0197_gene_embedding_m3_filtered.npz"
GENE_NAMES_PATH = PROJECT_ROOT / "2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/genept_embeddings/M-0198_gene_names_m3_filtered.csv"
NEIGHBORS_PATH = Path("/Users/dudu/.cache/pxfquery/resources/v20260628/gene_neighbors.json")


def load_genept() -> tuple[list[str], np.ndarray]:
    names = pd.read_csv(GENE_NAMES_PATH, header=None)[0].astype(str).tolist()
    emb = np.load(EMBEDDING_PATH)["data"]
    if len(names) != emb.shape[0]:
        raise ValueError(f"gene name count {len(names)} does not match embedding rows {emb.shape[0]}")
    return names, emb


def selected_genes(neighbors: dict[str, list], anchors: list[str], top_n: int) -> list[str]:
    genes: list[str] = []
    for anchor in anchors:
        if anchor not in genes:
            genes.append(anchor)
        for name, _score in neighbors.get(anchor, [])[:top_n]:
            if name not in genes:
                genes.append(name)
    return genes


def pca2(x: np.ndarray) -> np.ndarray:
    x = x.astype(np.float32)
    x = x / np.maximum(np.linalg.norm(x, axis=1, keepdims=True), 1e-8)
    x = x - x.mean(axis=0, keepdims=True)
    _u, _s, vt = np.linalg.svd(x, full_matrices=False)
    coords = x @ vt[:2].T
    coords = coords / np.maximum(np.abs(coords).max(axis=0, keepdims=True), 1e-8)
    return coords


def cosine_edges(genes: list[str], neighbors: dict[str, list], min_cosine: float, anchors: set[str]) -> list[tuple[str, str, float]]:
    gene_set = set(genes)
    seen = set()
    edges = []
    for gene in genes:
        if gene not in anchors:
            continue
        for nbr, score_int in neighbors.get(gene, []):
            score = float(score_int) / 100.0
            if score < min_cosine:
                break
            if nbr not in gene_set:
                continue
            key = tuple(sorted((gene, nbr)))
            if key in seen or gene == nbr:
                continue
            seen.add(key)
            edges.append((gene, nbr, score))
    return edges


def render(output_dir: Path, top_n: int = 18, min_edge_cosine: float = 0.66) -> tuple[Path, Path]:
    anchors = ["KRAS", "NRAS", "HRAS"]
    neighbors = json.loads(NEIGHBORS_PATH.read_text())
    genes = selected_genes(neighbors, anchors, top_n=top_n)
    names, emb = load_genept()
    index = {name: i for i, name in enumerate(names)}
    genes = [gene for gene in genes if gene in index]
    x = np.asarray([emb[index[gene]] for gene in genes])
    coords = pca2(x)
    pos = {gene: coords[i] for i, gene in enumerate(genes)}
    edges = cosine_edges(genes, neighbors, min_cosine=min_edge_cosine, anchors=set(anchors))
    # KRAS and NRAS are near-identical in the local projection. Separate them
    # slightly for label readability while preserving their visual proximity.
    if "KRAS" in pos and "NRAS" in pos:
        delta = np.asarray([0.045, -0.02])
        pos["KRAS"] = pos["KRAS"] - delta
        pos["NRAS"] = pos["NRAS"] + delta

    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    ax.set_axis_off()

    for a, b, score in edges:
        xa, ya = pos[a]
        xb, yb = pos[b]
        lw = 0.45 + 2.2 * (score - min_edge_cosine) / max(1e-6, 1.0 - min_edge_cosine)
        color = "#d97706" if a in {"KRAS", "NRAS", "HRAS"} and b in {"KRAS", "NRAS", "HRAS"} else "#9ca3af"
        alpha = 0.58 if color == "#d97706" else 0.24
        ax.plot([xa, xb], [ya, yb], color=color, lw=lw, alpha=alpha, zorder=1)

    route_genes = {"KRAS", "NRAS", "HRAS"}
    ras_related = {gene for gene in genes if gene.startswith(("RAS", "RAP", "RAL", "RRAS")) or gene in {"SOS1", "SOS2", "NF1"}}
    for gene in genes:
        x0, y0 = pos[gene]
        if gene in route_genes:
            ax.scatter([x0], [y0], s=420, facecolor="#fef3c7", edgecolor="#d97706", linewidth=2.0, zorder=4)
        elif gene in ras_related:
            ax.scatter([x0], [y0], s=120, facecolor="#e0f2fe", edgecolor="#0284c7", linewidth=1.0, zorder=3)
        else:
            ax.scatter([x0], [y0], s=58, facecolor="#f3f4f6", edgecolor="#9ca3af", linewidth=0.8, zorder=2)

    label_genes = route_genes | {"SOS1", "SOS2", "NF1", "RRAS2", "RAP1A", "RASAL2", "RASGRP1", "RALGDS"}
    label_offsets = {
        "KRAS": (-0.055, -0.065),
        "NRAS": (0.060, 0.060),
        "HRAS": (0.000, 0.070),
        "RAP1A": (0.020, 0.050),
        "RASAL2": (0.000, 0.065),
        "RASGRP1": (0.000, 0.060),
    }
    for gene in genes:
        if gene not in label_genes:
            continue
        x0, y0 = pos[gene]
        dx, dy = label_offsets.get(gene, (0.0, 0.045))
        ax.text(x0 + dx, y0 + dy, gene, ha="center", va="bottom", fontsize=9 if gene in route_genes else 7.2, weight="bold" if gene in route_genes else "normal", zorder=5)

    ax.set_title("GenePT semantic neighborhood of KRAS-family routes", fontsize=11.5, weight="bold", pad=10)
    ax.text(
        0.02,
        0.02,
        "GenePT model-3 local projection; edges show anchor semantic-neighbor cosine similarities",
        transform=ax.transAxes,
        fontsize=7,
        color="#4b5563",
        ha="left",
        va="bottom",
    )
    ax.margins(0.18)

    out_pdf = output_dir / "fig4c_genept_kras_family_semantic_map.pdf"
    out_png = output_dir / "fig4c_genept_kras_family_semantic_map.png"
    fig.savefig(out_pdf, bbox_inches="tight")
    fig.savefig(out_png, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return out_pdf, out_png


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("4_artifact/4_picture/figure4/panel_C_genept_semantic_map"))
    parser.add_argument("--top-n", type=int, default=14)
    parser.add_argument("--min-edge-cosine", type=float, default=0.68)
    args = parser.parse_args()
    for path in render(args.output_dir, top_n=args.top_n, min_edge_cosine=args.min_edge_cosine):
        print(path)


if __name__ == "__main__":
    main()


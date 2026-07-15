from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path("/public/home/caojun/project/RUSH/3_work")
TABLE = ROOT / "output/table/fig2d_cellline_signature_similarity"
PIC = ROOT / "output/picture/fig2d_cellline_signature_similarity"
PIC.mkdir(parents=True, exist_ok=True)

LONG_PATH = TABLE / "fig2d_lung_cancer_landmark978_metrics_long_cp_sh_xpr.csv"
metrics = pd.read_csv(LONG_PATH)

q_order = ["Q1 weakest", "Q2", "Q3", "Q4 strongest"]
group_order = ["same lung cancer subtype", "different lung cancer subtype"]


def bootstrap_median_ci(values, n_boot=2000, seed=20260630):
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if values.size == 0:
        return np.nan, np.nan, np.nan
    rng = np.random.default_rng(seed)
    med = float(np.median(values))
    if values.size == 1:
        return med, med, med
    samples = rng.choice(values, size=(n_boot, values.size), replace=True)
    boot = np.median(samples, axis=1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return med, float(lo), float(hi)


def summarize_metric(df, metric):
    rows = []
    for modality, d_mod in df.groupby("modality"):
        for q in q_order:
            for group in group_order:
                vals = d_mod.loc[
                    (d_mod["strength_quantile"] == q)
                    & (d_mod["lung_group"] == group),
                    metric,
                ]
                med, lo, hi = bootstrap_median_ci(vals, seed=20260630 + len(rows))
                rows.append(
                    {
                        "modality": modality,
                        "strength_quantile": q,
                        "lung_group": group,
                        "metric": metric,
                        "n_pairs": int(vals.notna().sum()),
                        "median": med,
                        "ci_low": lo,
                        "ci_high": hi,
                    }
                )
    return pd.DataFrame(rows)


pearson_summary = summarize_metric(metrics, "pearson_r")
l2_summary = summarize_metric(metrics, "l2_distance")
plot_summary = pd.concat([pearson_summary, l2_summary], ignore_index=True)
plot_summary.to_csv(TABLE / "fig2d_lung_cancer_strength_bootstrap_summary_cp_sh_xpr.csv", index=False)

cp_pearson = pearson_summary[
    (pearson_summary["modality"] == "cp")
    & (pearson_summary["n_pairs"] > 0)
].copy()

delta_rows = []
for q in q_order:
    same = cp_pearson[
        (cp_pearson["strength_quantile"] == q)
        & (cp_pearson["lung_group"] == "same lung cancer subtype")
    ]
    diff = cp_pearson[
        (cp_pearson["strength_quantile"] == q)
        & (cp_pearson["lung_group"] == "different lung cancer subtype")
    ]
    if not same.empty and not diff.empty:
        delta_rows.append(
            {
                "modality": "cp",
                "strength_quantile": q,
                "same_subtype_median_pearson": float(same.iloc[0]["median"]),
                "different_subtype_median_pearson": float(diff.iloc[0]["median"]),
                "delta_same_minus_different": float(same.iloc[0]["median"] - diff.iloc[0]["median"]),
                "same_n": int(same.iloc[0]["n_pairs"]),
                "different_n": int(diff.iloc[0]["n_pairs"]),
            }
        )
pd.DataFrame(delta_rows).to_csv(TABLE / "fig2d_lung_cancer_cp_same_vs_different_delta.csv", index=False)

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 7,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.linewidth": 0.8,
    }
)

fig, ax = plt.subplots(figsize=(3.25, 2.25))
x = np.arange(len(q_order), dtype=float)
offset = 0.16
colors = {
    "same lung cancer subtype": "#d94841",
    "different lung cancer subtype": "#4a4a4a",
}
labels = {
    "same lung cancer subtype": "Same lung-cancer subtype",
    "different lung cancer subtype": "Different lung-cancer subtype",
}
for group, dx in zip(group_order, [-offset, offset]):
    sub = cp_pearson[cp_pearson["lung_group"] == group].set_index("strength_quantile").reindex(q_order)
    y = sub["median"].to_numpy(dtype=float)
    yerr = np.vstack(
        [
            y - sub["ci_low"].to_numpy(dtype=float),
            sub["ci_high"].to_numpy(dtype=float) - y,
        ]
    )
    ax.errorbar(
        x + dx,
        y,
        yerr=yerr,
        fmt="o-",
        lw=1.8,
        ms=4.2,
        capsize=2.5,
        color=colors[group],
        label=labels[group],
        zorder=3,
    )

ax.axhline(0, color="#bdbdbd", lw=0.8, zorder=1)
ax.set_xticks(x)
ax.set_xticklabels(["Q1\nweakest", "Q2", "Q3", "Q4\nstrongest"])
ax.set_ylabel("Median Pearson r")
ax.set_xlabel("Signature strength stratum")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", color="#e5e5e5", lw=0.6)
ax.legend(frameon=False, loc="upper left", fontsize=6.5, handlelength=1.8)
ax.set_ylim(0.0, max(0.28, float(cp_pearson["ci_high"].max()) + 0.02))
fig.tight_layout()

for ext in ["pdf", "svg", "png"]:
    fig.savefig(PIC / f"figure2_panel_D_lung_cancer_cp_strength_pearson.{ext}", dpi=300)
plt.close(fig)

print("WROTE", PIC / "figure2_panel_D_lung_cancer_cp_strength_pearson.pdf")
print(pd.DataFrame(delta_rows).to_string(index=False))


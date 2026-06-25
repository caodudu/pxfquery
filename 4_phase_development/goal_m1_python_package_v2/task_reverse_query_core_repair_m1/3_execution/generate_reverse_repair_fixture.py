from __future__ import annotations

import json
import shutil
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import yaml


TASK_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = TASK_ROOT / "1_asset" / "fixture_package_m1"
OUT_ROOT = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_repair_fixture_m1_1"
MANIFEST_PATH = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_repair_manifest_m1_1.yaml"

MYC_TERM = "HALLMARK_MYC_TARGETS_V1"
LOW_TERM = "NON_DIFFERENTIALLY_SCORED_PROGRAM"


def _copy_sidecars() -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True)
    for path in SOURCE_ROOT.iterdir():
        if path.suffix != ".h5ad":
            shutil.copy2(path, OUT_ROOT / path.name)


def _ensure_columns(adata: ad.AnnData) -> ad.AnnData:
    var_names = list(adata.var_names)
    additions = [name for name in [MYC_TERM, LOW_TERM] if name not in var_names]
    if not additions:
        return adata.copy()
    x = np.asarray(adata.X, dtype=np.float32)
    extra = np.zeros((adata.n_obs, len(additions)), dtype=np.float32)
    combined = np.concatenate([x, extra], axis=1)
    var = pd.DataFrame(index=var_names + additions)
    return ad.AnnData(
        X=combined,
        obs=adata.obs.copy(),
        var=var,
        uns=dict(adata.uns),
        obsm=adata.obsm.copy(),
        varm=adata.varm.copy(),
    )


def _repair_xpr(adata: ad.AnnData) -> ad.AnnData:
    repaired = _ensure_columns(adata)
    var_names = list(repaired.var_names)
    base_rows = np.asarray(repaired.X, dtype=np.float32)
    rows = []
    obs_rows = []

    candidates = [
        ("T060_XPR_A549_SYN_001", "THTPA", 3.00, -3.00),
        ("T060_XPR_A549_SYN_002", "SCD", 2.80, -2.75),
        ("T060_XPR_A549_SYN_003", "BCL2L1", 2.45, -2.30),
        ("T060_XPR_A549_SYN_004", "CDK2", 2.10, -1.95),
        ("T060_XPR_A549_SYN_005", "TP53", 1.70, -1.60),
        ("T060_XPR_A549_SYN_006", "MAPK1", 1.30, -1.20),
        ("T060_XPR_A549_SYN_007", "EGFR", 1.00, -0.90),
        ("T060_XPR_A549_SYN_008", "STAT3", 0.75, -0.65),
        ("T060_XPR_A549_SYN_009", "AKT1", 0.50, -0.45),
        ("T060_XPR_A549_SYN_010", "MYC", 0.25, -0.20),
    ]

    template = {name: 0.0 for name in var_names}
    for idx, (sig_id, cmap_name, apoptosis, myc) in enumerate(candidates, start=1):
        scores = dict(template)
        scores["HALLMARK_APOPTOSIS"] = apoptosis
        scores[MYC_TERM] = myc
        scores["HALLMARK_P53_PATHWAY"] = round(apoptosis / 3.0, 4)
        scores["HALLMARK_TNFA_SIGNALING_VIA_NFKB"] = round(-myc / 4.0, 4)
        rows.append([scores[name] for name in var_names])
        obs_rows.append(
            {
                "sig_id": sig_id,
                "project_code": "T060_REPAIR",
                "cell_iname": "A549",
                "pert_id": f"T060-SYN-{idx:03d}",
                "cmap_name": cmap_name,
                "pert_dose": 0.0,
                "pert_time": 96.0,
                "repair_provenance": "synthetic_reverse_demo_support_not_raw_lincs",
            }
        )

    low_row = dict(template)
    low_row[LOW_TERM] = 0.01
    rows.append([low_row[name] for name in var_names])
    obs_rows.append(
        {
            "sig_id": "T060_XPR_A549_SYN_LOWCONF",
            "project_code": "T060_REPAIR",
            "cell_iname": "A549",
            "pert_id": "T060-SYN-LOW",
            "cmap_name": "LOWCONF_CONTROL",
            "pert_dose": 0.0,
            "pert_time": 96.0,
            "repair_provenance": "synthetic_low_confidence_control_not_raw_lincs",
        }
    )

    synthetic_x = np.asarray(rows, dtype=np.float32)
    combined_x = np.concatenate([base_rows, synthetic_x], axis=0)
    combined_obs = pd.concat(
        [repaired.obs.copy(), pd.DataFrame(obs_rows, index=[r["sig_id"] for r in obs_rows])],
        axis=0,
    )
    combined = ad.AnnData(X=combined_x, obs=combined_obs, var=repaired.var.copy())
    combined.uns["t060_repair_note"] = (
        "Original registered T-043 xpr fixture plus task-local synthetic rows/columns "
        "for T-042 reverse demo repair; not raw LINCS/CMAP data."
    )
    return combined


def _repair_matrix(name: str) -> None:
    src = SOURCE_ROOT / f"{name}_func_fixture_m1.h5ad"
    adata = ad.read_h5ad(src)
    repaired = _repair_xpr(adata) if name == "xpr" else _ensure_columns(adata)
    repaired.write_h5ad(OUT_ROOT / f"{name}_func_fixture_m1.h5ad")


def _write_manifest() -> None:
    manifest = {
        "manifest_id": "reverse_repair_manifest_m1_1",
        "task_id": "T-060",
        "generated": "2026-06-24",
        "fixture_package_root": "4_artifact/2_persist/reverse_repair_fixture_m1_1",
        "provenance": {
            "base_fixture": "T-043 fixture_package_m1 via registered A-004",
            "repair_content": "Synthetic task-local A549 xpr rows and target columns for T-042 DEMO-002",
            "not_raw_data": True,
        },
        "resources": [
            {
                "resource_id": f"m1_fixture_{name}_matrix",
                "path": f"4_artifact/2_persist/reverse_repair_fixture_m1_1/{name}_func_fixture_m1.h5ad",
                "file_type": "h5ad",
                "loader_role": f"T-060 repair {name} functional matrix",
                "required_keys_or_columns": [
                    "sig_id",
                    "project_code",
                    "cell_iname",
                    "pert_id",
                    "cmap_name",
                    "pert_dose",
                    "pert_time",
                    "HALLMARK_APOPTOSIS",
                    MYC_TERM,
                    LOW_TERM,
                ],
                "provenance": "Base copied from A-004; target-column additions are synthetic repair support.",
                "validation_rule": "Readable by T-046 M1FixtureLoader; repair content is task-local synthetic support.",
            }
            for name in ["cp", "sh", "xpr"]
        ],
    }
    with MANIFEST_PATH.open("w") as fh:
        yaml.safe_dump(manifest, fh, sort_keys=False)


def _write_summary() -> None:
    summary = {}
    for name in ["cp", "sh", "xpr"]:
        a = ad.read_h5ad(OUT_ROOT / f"{name}_func_fixture_m1.h5ad")
        summary[name] = {
            "shape": list(a.shape),
            "has_A549": bool("cell_iname" in a.obs and (a.obs["cell_iname"] == "A549").any()),
            "has_HALLMARK_MYC_TARGETS_V1": MYC_TERM in a.var_names,
            "has_low_confidence_term": LOW_TERM in a.var_names,
            "var_names": list(a.var_names),
        }
    with (TASK_ROOT / "3_execution" / "reverse_repair_fixture_summary_v20260624.json").open("w") as fh:
        json.dump(summary, fh, indent=2)


def main() -> None:
    _copy_sidecars()
    for matrix in ["cp", "sh", "xpr"]:
        _repair_matrix(matrix)
    _write_manifest()
    _write_summary()


if __name__ == "__main__":
    main()

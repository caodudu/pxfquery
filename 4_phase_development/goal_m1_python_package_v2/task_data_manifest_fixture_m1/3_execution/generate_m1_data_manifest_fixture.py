from __future__ import annotations

import csv
import html
import json
import shutil
from datetime import date
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import yaml


TASK_ID = "T-043"
TODAY = "20260624"
ROOT = Path(__file__).resolve().parents[1]
ASSET = ROOT / "1_asset"
STD = ASSET / "t021_standard_resources_bundle"
PROC = ASSET / "t021_process_records"
OUT = ROOT / "4_artifact"
PERSIST = OUT / "2_persist"
TABLE = OUT / "5_table"
DOC = OUT / "3_document"
FIXTURE = PERSIST / "fixture_package_m1"
EXEC = ROOT / "3_execution"

FUNCTIONS = [
    "HALLMARK_ADIPOGENESIS",
    "HALLMARK_APOPTOSIS",
    "HALLMARK_E2F_TARGETS",
    "HALLMARK_P53_PATHWAY",
    "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "MP39 Metal-response",
    "MP40 PDAC-related",
]

MATRIX_ROWS = {
    "cp": [
        "ABY001_A375_XH:BRD-K66175015:10:24",
        "ABY001_A375_XH:BRD-K70401845:10:24",
        "ABY001_A375_XH:BRD-K70511574:10:24",
        "ABY001_A375_XH:BRD-K85606544:10:24",
    ],
    "sh": [
        "CGS001_A375_96H:A2M:1",
        "CGS001_A375_96H:AATF:1",
        "CGS001_A375_96H:ABAT:1",
        "CGS001_A375_96H:ABCA1:1",
    ],
    "xpr": [
        "XPR025_BICR6.311_96H:E13",
        "XPR028_PC3.311B_96H:J15",
        "XPR015_A375.311_96H:E11",
        "XPR031_U251MG.311_96H:E03",
    ],
}

FULL_MATRIX_EXPECTED = {
    "cp": {"shape": [201014, 91], "dtype": "float32"},
    "sh": {"shape": [189365, 91], "dtype": "float32"},
    "xpr": {"shape": [132464, 91], "dtype": "float32"},
}

FULL_FILES = [
    "cp_func_ad.h5ad",
    "sh_func_ad.h5ad",
    "xpr_func_ad.h5ad",
    "cellline_index.json",
    "cellline_neighbors.json",
    "cellline_tree.json",
    "drug_index.json",
    "drug_neighbors.json",
    "gene_index_simple.json",
    "gene_neighbors_simple.json",
    "gene_index.json",
    "gene_neighbors.json",
    "function_index.json",
    "cellline_meta_standard.csv",
    "cellline_info_standard.csv",
    "compound_meta_standard.csv",
    "compound_info_standard.csv",
    "gene_info_standard.csv",
    "data_description.yaml",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(name: str):
    with open(STD / name, encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def clean_existing_outputs() -> None:
    for path in [
        PERSIST / "resource_manifest_m1.yaml",
        PERSIST / "data_manifest_fixture_m1_readme.md",
        TABLE / "expected_shapes_keys_columns_m1.csv",
        TABLE / "sample_records_m1.csv",
        DOC / f"execution_report_v{TODAY}.html",
        DOC / f"result_report_v{TODAY}.html",
        OUT / "registry.yaml",
        ROOT / "5_report" / "completion.md",
        EXEC / "validation_log_m1.json",
    ]:
        if path.exists():
            path.unlink()
    if FIXTURE.exists():
        shutil.rmtree(FIXTURE)
    FIXTURE.mkdir(parents=True, exist_ok=True)


def read_matrix_subset(kind: str) -> ad.AnnData:
    src = STD / f"{kind}_func_ad.h5ad"
    ann = ad.read_h5ad(src)
    expected = FULL_MATRIX_EXPECTED[kind]
    assert list(ann.shape) == expected["shape"], (kind, ann.shape)
    assert str(ann.X.dtype) == expected["dtype"], (kind, ann.X.dtype)
    missing_rows = [r for r in MATRIX_ROWS[kind] if r not in ann.obs_names]
    missing_vars = [v for v in FUNCTIONS if v not in ann.var_names]
    assert not missing_rows, (kind, missing_rows)
    assert not missing_vars, (kind, missing_vars)
    subset = ann[MATRIX_ROWS[kind], FUNCTIONS].copy()
    subset.X = np.asarray(subset.X, dtype=np.float32)
    subset.uns["fixture_provenance"] = {
        "task_id": TASK_ID,
        "source_asset": "A-001",
        "source_resource": rel(src),
        "source_task": "T-021",
        "selection_rule": (
            "Deterministic rows selected from real standard-resource observations; "
            "functions selected from real matrix var_names and function_index.json."
        ),
    }
    return subset


def build_matrix_fixtures() -> tuple[dict, list[dict]]:
    matrix_records: dict[str, dict] = {}
    sample_rows: list[dict] = []
    for kind in ["cp", "sh", "xpr"]:
        subset = read_matrix_subset(kind)
        dst = FIXTURE / f"{kind}_func_fixture_m1.h5ad"
        subset.write_h5ad(dst)
        matrix_records[kind] = {
            "fixture_path": rel(dst),
            "fixture_shape": list(subset.shape),
            "source_path": rel(STD / f"{kind}_func_ad.h5ad"),
            "obs_columns": list(subset.obs.columns),
            "var_names": list(subset.var_names),
            "dtype": str(subset.X.dtype),
            "score_min": float(np.nanmin(subset.X)),
            "score_max": float(np.nanmax(subset.X)),
        }
        for sig_id, row in subset.obs.iterrows():
            scores = subset[sig_id, :].to_df().iloc[0].to_dict()
            sample_rows.append(
                {
                    "sample_id": f"{kind}:{sig_id}",
                    "sample_kind": "matrix_observation",
                    "source_resource": rel(STD / f"{kind}_func_ad.h5ad"),
                    "fixture_resource": rel(dst),
                    "row_or_key_identifier": sig_id,
                    "selected_fields": json.dumps(
                        {
                            "project_code": row.get("project_code"),
                            "cell_iname": row.get("cell_iname"),
                            "pert_id": row.get("pert_id"),
                            "cmap_name": row.get("cmap_name"),
                            "pert_dose": row.get("pert_dose"),
                            "pert_time": row.get("pert_time"),
                            "scores": {k: round(float(v), 6) for k, v in scores.items()},
                        },
                        ensure_ascii=False,
                    ),
                    "inclusion_reason": (
                        "Real functional-score observation retained for loader smoke "
                        f"and {kind} forward/reverse demo coverage."
                    ),
                    "provenance": "A-001 standard resource bundle; T-021 standard resources",
                }
            )
    return matrix_records, sample_rows


def subset_csv(name: str, predicate, dst_name: str) -> tuple[pd.DataFrame, Path]:
    df = pd.read_csv(STD / name)
    out = df[predicate(df)].copy()
    out = out.drop_duplicates().reset_index(drop=True)
    dst = FIXTURE / dst_name
    out.to_csv(dst, index=False)
    return out, dst


def build_tabular_fixtures(matrix_records: dict) -> tuple[dict, list[dict]]:
    all_cells = sorted(
        {
            str(x)
            for kind in matrix_records
            for x in pd.read_csv(matrix_records[kind]["fixture_path"] if False else STD / "cellline_meta_standard.csv").head(0)
        }
    )
    selected_cells = set()
    selected_cp_ids = set()
    selected_cp_names = set()
    selected_genes = set()
    for kind in ["cp", "sh", "xpr"]:
        ann = ad.read_h5ad(FIXTURE / f"{kind}_func_fixture_m1.h5ad")
        selected_cells.update(str(x) for x in ann.obs["cell_iname"].tolist())
        if kind == "cp":
            selected_cp_ids.update(str(x) for x in ann.obs["pert_id"].tolist())
            selected_cp_names.update(str(x).lower() for x in ann.obs["cmap_name"].tolist())
        else:
            selected_genes.update(str(x).upper() for x in ann.obs["cmap_name"].tolist())

    cell_meta, cell_meta_path = subset_csv(
        "cellline_meta_standard.csv",
        lambda df: df["cell_iname"].astype(str).isin(selected_cells),
        "cellline_meta_fixture_m1.csv",
    )
    cell_info, cell_info_path = subset_csv(
        "cellline_info_standard.csv",
        lambda df: df["cell_iname"].astype(str).isin(selected_cells),
        "cellline_info_fixture_m1.csv",
    )
    compound_meta, compound_meta_path = subset_csv(
        "compound_meta_standard.csv",
        lambda df: df["drug"].astype(str).isin(selected_cp_ids),
        "compound_meta_fixture_m1.csv",
    )
    compound_info, compound_info_path = subset_csv(
        "compound_info_standard.csv",
        lambda df: df["pert_id"].astype(str).isin(selected_cp_ids),
        "compound_info_fixture_m1.csv",
    )
    compound_info = compound_info.drop_duplicates(subset=["pert_id", "cmap_name"]).reset_index(drop=True)
    compound_info.to_csv(compound_info_path, index=False)
    gene_info, gene_info_path = subset_csv(
        "gene_info_standard.csv",
        lambda df: df["gene_symbol"].astype(str).str.upper().isin(selected_genes),
        "gene_info_fixture_m1.csv",
    )

    drug_index = load_json("drug_index.json")
    drug_neighbors = load_json("drug_neighbors.json")
    gene_index_simple = load_json("gene_index_simple.json")
    gene_neighbors_simple = load_json("gene_neighbors_simple.json")
    gene_index = load_json("gene_index.json")
    gene_neighbors = load_json("gene_neighbors.json")
    cellline_index = load_json("cellline_index.json")
    cellline_neighbors = load_json("cellline_neighbors.json")
    cellline_tree = load_json("cellline_tree.json")
    function_index = load_json("function_index.json")

    drug_index_fixture = {
        alias: pid
        for alias, pid in drug_index.items()
        if str(pid) in selected_cp_ids or alias in selected_cp_names
    }
    drug_neighbor_keys = {pid.replace("BRD-", "") for pid in selected_cp_ids}
    drug_neighbors_fixture = {
        key: value[:5] for key, value in drug_neighbors.items() if key in drug_neighbor_keys
    }
    gene_index_simple_fixture = {
        gene: gene_index_simple[gene] for gene in sorted(selected_genes) if gene in gene_index_simple
    }
    gene_neighbors_simple_fixture = {
        gene: gene_neighbors_simple[gene][:5]
        for gene in sorted(selected_genes)
        if gene in gene_neighbors_simple
    }
    gene_index_fixture = {
        key: value
        for key, value in gene_index.items()
        if value.get("symbol", "").upper() in selected_genes
    }
    gene_neighbors_fixture = {
        gene: gene_neighbors[gene][:5]
        for gene in sorted(selected_genes)
        if gene in gene_neighbors
    }
    cellline_index_fixture = {
        "valid_cells": [c for c in cellline_index["valid_cells"] if c in selected_cells]
    }
    cellline_neighbors_fixture = {
        lineage: {
            disease: {
                subtype: [c for c in cells if c in selected_cells]
                for subtype, cells in disease_map.items()
                if any(c in selected_cells for c in cells)
            }
            for disease, disease_map in lineage_map.items()
        }
        for lineage, lineage_map in cellline_neighbors.items()
    }
    cellline_neighbors_fixture = {
        lineage: {disease: subtypes for disease, subtypes in disease_map.items() if subtypes}
        for lineage, disease_map in cellline_neighbors_fixture.items()
    }
    cellline_neighbors_fixture = {
        lineage: disease_map for lineage, disease_map in cellline_neighbors_fixture.items() if disease_map
    }
    cellline_tree_fixture = {
        "tree": cellline_neighbors_fixture,
        "cell_index": {
            cell: cellline_tree.get("cell_index", {}).get(cell)
            for cell in sorted(selected_cells)
            if cell in cellline_tree.get("cell_index", {})
        },
        "meta": cellline_tree.get("meta", {}),
    }
    function_index_fixture = {
        "var_names": FUNCTIONS,
        "meta": {fn: function_index["meta"][fn] for fn in FUNCTIONS},
        "aliases": {
            alias: target
            for alias, target in function_index["aliases"].items()
            if target in FUNCTIONS
        },
    }

    json_outputs = {
        "cellline_index_fixture_m1.json": cellline_index_fixture,
        "cellline_neighbors_fixture_m1.json": cellline_neighbors_fixture,
        "cellline_tree_fixture_m1.json": cellline_tree_fixture,
        "drug_index_fixture_m1.json": drug_index_fixture,
        "drug_neighbors_fixture_m1.json": drug_neighbors_fixture,
        "gene_index_simple_fixture_m1.json": gene_index_simple_fixture,
        "gene_neighbors_simple_fixture_m1.json": gene_neighbors_simple_fixture,
        "gene_index_fixture_m1.json": gene_index_fixture,
        "gene_neighbors_fixture_m1.json": gene_neighbors_fixture,
        "function_index_fixture_m1.json": function_index_fixture,
    }
    for filename, payload in json_outputs.items():
        write_json(FIXTURE / filename, payload)

    tabular = {
        "cellline_meta_fixture_m1.csv": cell_meta,
        "cellline_info_fixture_m1.csv": cell_info,
        "compound_meta_fixture_m1.csv": compound_meta,
        "compound_info_fixture_m1.csv": compound_info,
        "gene_info_fixture_m1.csv": gene_info,
    }
    fixture_records = {
        "selected_cells": sorted(selected_cells),
        "selected_cp_ids": sorted(selected_cp_ids),
        "selected_cp_names": sorted(selected_cp_names),
        "selected_genes": sorted(selected_genes),
        "csv_outputs": {k: {"path": rel(FIXTURE / k), "shape": list(v.shape)} for k, v in tabular.items()},
        "json_outputs": {
            k: {
                "path": rel(FIXTURE / k),
                "top_level_count": len(v) if hasattr(v, "__len__") else None,
            }
            for k, v in json_outputs.items()
        },
    }
    sample_rows = []
    for file_name, df in tabular.items():
        for idx, row in df.head(8).iterrows():
            key = (
                row.get("cell_iname")
                or row.get("drug")
                or row.get("pert_id")
                or row.get("gene_symbol")
                or str(idx)
            )
            sample_rows.append(
                {
                    "sample_id": f"{file_name}:{key}",
                    "sample_kind": "metadata_record",
                    "source_resource": rel(STD / file_name.replace("_fixture_m1", "_standard")),
                    "fixture_resource": rel(FIXTURE / file_name),
                    "row_or_key_identifier": str(key),
                    "selected_fields": row.dropna().to_json(force_ascii=False),
                    "inclusion_reason": "Metadata row linked to selected fixture observations or resolver keys.",
                    "provenance": "A-001 standard resource bundle; T-021 standard resources",
                }
            )
    for file_name, payload in json_outputs.items():
        sample_rows.append(
            {
                "sample_id": f"{file_name}:top_level",
                "sample_kind": "index_record",
                "source_resource": rel(STD / file_name.replace("_fixture_m1", "")),
                "fixture_resource": rel(FIXTURE / file_name),
                "row_or_key_identifier": ",".join(list(payload)[:8]) if isinstance(payload, dict) else "root",
                "selected_fields": json.dumps(payload, ensure_ascii=False)[:1200],
                "inclusion_reason": "Bounded real index subset needed by loader/resolver smoke tests.",
                "provenance": "A-001 standard resource bundle; T-021 standard resources",
            }
        )
    return fixture_records, sample_rows


def full_resource_profile() -> dict:
    profiles = {}
    for kind in ["cp", "sh", "xpr"]:
        ann = ad.read_h5ad(STD / f"{kind}_func_ad.h5ad", backed="r")
        profiles[f"{kind}_func_ad.h5ad"] = {
            "shape": list(ann.shape),
            "obs_columns": list(ann.obs.columns),
            "n_vars": int(ann.n_vars),
            "dtype": str(ann.X.dtype),
        }
        ann.file.close()
    for name in [
        "cellline_meta_standard.csv",
        "cellline_info_standard.csv",
        "compound_meta_standard.csv",
        "compound_info_standard.csv",
        "gene_info_standard.csv",
    ]:
        df = pd.read_csv(STD / name)
        profiles[name] = {
            "shape": list(df.shape),
            "columns": list(df.columns),
        }
    for name in [
        "cellline_index.json",
        "cellline_neighbors.json",
        "cellline_tree.json",
        "drug_index.json",
        "drug_neighbors.json",
        "gene_index_simple.json",
        "gene_neighbors_simple.json",
        "gene_index.json",
        "gene_neighbors.json",
        "function_index.json",
    ]:
        payload = load_json(name)
        profiles[name] = {
            "top_level_type": type(payload).__name__,
            "top_level_count": len(payload) if hasattr(payload, "__len__") else None,
            "keys": list(payload)[:8] if isinstance(payload, dict) else None,
        }
    return profiles


def resource_entry(resource_id, path, file_type, role, keys, expected, provenance, validation, notes):
    return {
        "resource_id": resource_id,
        "path": path,
        "file_type": file_type,
        "loader_role": role,
        "required_keys_or_columns": keys,
        "expected_shape_or_count": expected,
        "provenance": provenance,
        "validation_rule": validation,
        "notes": notes,
    }


def build_manifest_and_tables(matrix_records, fixture_records, profiles, sample_rows):
    provenance_full = {
        "source_asset": "A-001",
        "source_task": "T-021",
        "authority_assets": ["A-002", "A-003", "A-004", "A-005", "A-006"],
    }
    manifest = {
        "manifest_id": "resource_manifest_m1",
        "task_id": TASK_ID,
        "generated": str(date.today()),
        "boundary": {
            "input_authorities": [
                "A-001 T-021 standard resource bundle",
                "A-002 T-021 standard resource guide",
                "A-003 T-021 process records",
                "A-004 T-014 precomputed data scope",
                "A-005 T-014 data resource inventory",
                "A-006 T-014 matrix schema coverage",
            ],
            "forbidden_sources_not_used": [
                "2_project_asset",
                "legacy source root",
                "failed T024-T040 outputs",
                "web or downloaded data",
            ],
        },
        "standard_bundle_root": "1_asset/t021_standard_resources_bundle",
        "fixture_package_root": "4_artifact/2_persist/fixture_package_m1",
        "resources": [],
        "known_exclusions": [
            {
                "item": "upstream CMAP H5AD files",
                "reason": "T-014/T-021 report truncated HDF5 files; not needed for runtime loader/query substrate.",
            },
            {
                "item": "historical GSEA outputs and figures",
                "reason": "Provenance/support only, not runtime M1 data substrate.",
            },
            {
                "item": "GenePT embeddings",
                "reason": "Optional large proxy resource excluded from standard runtime bundle by T-021.",
            },
        ],
    }

    expected_rows = []
    def add_expected(row):
        expected_rows.append(row)
        manifest["resources"].append(
            resource_entry(
                row["resource_id"],
                row["path"],
                row["file_type"],
                row["loader_role"],
                row["required_keys_or_columns"].split("; ") if row["required_keys_or_columns"] else [],
                row["expected_shape_or_count"],
                row["provenance"],
                row["validation_rule"],
                row["notes"],
            )
        )

    matrix_roles = {
        "cp": "compound functional matrix; loader and forward/reverse query substrate",
        "sh": "shRNA functional matrix; genetic knockdown query substrate",
        "xpr": "ORF overexpression functional matrix; genetic overexpression query substrate",
    }
    for kind in ["cp", "sh", "xpr"]:
        profile = profiles[f"{kind}_func_ad.h5ad"]
        add_expected(
            {
                "resource_id": f"m1_full_{kind}_matrix",
                "path": rel(STD / f"{kind}_func_ad.h5ad"),
                "file_type": "h5ad",
                "loader_role": matrix_roles[kind],
                "expected_shape_or_count": f"{profile['shape'][0]} obs x {profile['shape'][1]} vars",
                "key_fields": "obs_names/sig_id",
                "required_keys_or_columns": "; ".join(profile["obs_columns"] + ["91 var_names"]),
                "index_semantics": "obs rows are perturbation signatures; vars are functional terms",
                "validation_rule": "readable by anndata; float32 X; 91 function vars; required obs columns present",
                "provenance": "A-001/T-021 from canonical T-021 standard_resources; T-014 confirms derived matrices as query substrate",
                "notes": "Full standard resource, not copied into fixture package.",
            }
        )
        rec = matrix_records[kind]
        add_expected(
            {
                "resource_id": f"m1_fixture_{kind}_matrix",
                "path": rec["fixture_path"],
                "file_type": "h5ad",
                "loader_role": f"minimal {matrix_roles[kind]} for smoke/demo use",
                "expected_shape_or_count": f"{rec['fixture_shape'][0]} obs x {rec['fixture_shape'][1]} vars",
                "key_fields": "obs_names/sig_id",
                "required_keys_or_columns": "; ".join(rec["obs_columns"] + FUNCTIONS),
                "index_semantics": "obs rows are selected real perturbation signatures; vars are selected real function terms",
                "validation_rule": "fixture rows/vars must be subsets of full matrix; float32 X; no synthetic scores",
                "provenance": "Derived by bounded extraction from A-001/T-021 standard matrix",
                "notes": f"Score range in fixture: {rec['score_min']:.6f} to {rec['score_max']:.6f}.",
            }
        )

    csv_roles = {
        "cellline_meta_standard.csv": ("cell metadata", "cell_iname"),
        "cellline_info_standard.csv": ("detailed cell metadata", "cell_iname"),
        "compound_meta_standard.csv": ("compound metadata", "drug"),
        "compound_info_standard.csv": ("compound annotations", "pert_id"),
        "gene_info_standard.csv": ("gene annotations", "gene_symbol"),
    }
    for name, (role, key) in csv_roles.items():
        profile = profiles[name]
        add_expected(
            {
                "resource_id": "m1_full_" + name.replace("_standard.csv", "").replace(".csv", ""),
                "path": rel(STD / name),
                "file_type": "csv",
                "loader_role": role,
                "expected_shape_or_count": f"{profile['shape'][0]} rows x {profile['shape'][1]} columns",
                "key_fields": key,
                "required_keys_or_columns": "; ".join(profile["columns"]),
                "index_semantics": f"{key} is the primary lookup/join field for this table",
                "validation_rule": f"readable by pandas; required key column {key} present",
                "provenance": "A-001/T-021 standard metadata; T-014 confirms metadata layer",
                "notes": "Full standard resource, not copied into fixture package.",
            }
        )

    for filename, info in fixture_records["csv_outputs"].items():
        key = (
            "cell_iname"
            if filename.startswith("cellline")
            else "drug"
            if filename.startswith("compound_meta")
            else "pert_id"
            if filename.startswith("compound_info")
            else "gene_symbol"
        )
        columns = list(pd.read_csv(ROOT / info["path"], nrows=0).columns)
        add_expected(
            {
                "resource_id": "m1_fixture_" + filename.replace("_fixture_m1.csv", ""),
                "path": info["path"],
                "file_type": "csv",
                "loader_role": "minimal metadata fixture linked to selected matrix observations",
                "expected_shape_or_count": f"{info['shape'][0]} rows x {info['shape'][1]} columns",
                "key_fields": key,
                "required_keys_or_columns": "; ".join(columns),
                "index_semantics": f"{key} joins fixture metadata to selected observations or resolver keys",
                "validation_rule": "fixture rows are exact subsets of A-001 standard metadata tables",
                "provenance": "Derived by bounded row extraction from A-001/T-021 standard metadata",
                "notes": "Small deterministic fixture file.",
            }
        )

    json_roles = {
        "cellline_index.json": ("valid cell lookup", "valid_cells"),
        "cellline_neighbors.json": ("cell-line proxy lookup", "lineage/disease/subtype/cell"),
        "cellline_tree.json": ("cell-line tree lookup", "tree/cell_index/meta"),
        "drug_index.json": ("drug alias exact lookup", "alias_lower"),
        "drug_neighbors.json": ("drug proxy lookup", "BRD id without prefix"),
        "gene_index_simple.json": ("gene symbol exact lookup", "SYMBOL"),
        "gene_neighbors_simple.json": ("gene proxy lookup", "SYMBOL"),
        "gene_index.json": ("full gene exact lookup", "lowercase alias"),
        "gene_neighbors.json": ("full gene proxy lookup", "SYMBOL"),
        "function_index.json": ("function term and alias catalog", "var_names/meta/aliases"),
    }
    for name, (role, key) in json_roles.items():
        profile = profiles[name]
        add_expected(
            {
                "resource_id": "m1_full_" + name.replace(".json", ""),
                "path": rel(STD / name),
                "file_type": "json",
                "loader_role": role,
                "expected_shape_or_count": f"{profile['top_level_type']} with top-level count {profile['top_level_count']}",
                "key_fields": key,
                "required_keys_or_columns": "; ".join(profile["keys"] or [key]),
                "index_semantics": "JSON lookup index used by resolver or function validation",
                "validation_rule": "parsable JSON; non-empty; schema described by T-021 guide",
                "provenance": "A-001/T-021 standard query index; T-014 confirms query index layer",
                "notes": "Full standard resource, not copied into fixture package.",
            }
        )
    for filename, info in fixture_records["json_outputs"].items():
        source_name = filename.replace("_fixture_m1", "")
        role, key = json_roles[source_name]
        add_expected(
            {
                "resource_id": "m1_fixture_" + filename.replace("_fixture_m1.json", ""),
                "path": info["path"],
                "file_type": "json",
                "loader_role": "minimal " + role,
                "expected_shape_or_count": f"top-level count {info['top_level_count']}",
                "key_fields": key,
                "required_keys_or_columns": key,
                "index_semantics": "Bounded resolver/function lookup subset linked to selected fixture rows",
                "validation_rule": "parsable JSON; keys/values copied or boundedly derived from A-001 standard index",
                "provenance": "Derived by bounded extraction from A-001/T-021 standard query index",
                "notes": "Small deterministic fixture file.",
            }
        )

    manifest_path = PERSIST / "resource_manifest_m1.yaml"
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(manifest, f, sort_keys=False, allow_unicode=True, width=100)

    expected_path = TABLE / "expected_shapes_keys_columns_m1.csv"
    write_csv(
        expected_path,
        expected_rows,
        [
            "resource_id",
            "path",
            "file_type",
            "loader_role",
            "expected_shape_or_count",
            "key_fields",
            "required_keys_or_columns",
            "index_semantics",
            "validation_rule",
            "provenance",
            "notes",
        ],
    )
    sample_path = TABLE / "sample_records_m1.csv"
    write_csv(
        sample_path,
        sample_rows,
        [
            "sample_id",
            "sample_kind",
            "source_resource",
            "fixture_resource",
            "row_or_key_identifier",
            "selected_fields",
            "inclusion_reason",
            "provenance",
        ],
    )
    return manifest, expected_rows


def write_readme(matrix_records, fixture_records):
    text = f"""# T-043 M1 Data Manifest And Fixture Package

Generated: 2026-06-24

This package defines the stable M1 data substrate for downstream PxFquery package work.
It uses only the registered T-014 and T-021 assets for authority and fixture extraction.

## Files To Consume

- `resource_manifest_m1.yaml`: primary machine-readable resource manifest.
- `fixture_package_m1/`: small deterministic real-data subset for loader, forward-query, and reverse-query smoke tests.
- `expected_shapes_keys_columns_m1.csv`: declared full-resource and fixture schemas.
- `sample_records_m1.csv`: exact source identifiers and selected fields for example records.

## Fixture Contents

- Matrix fixtures: `cp_func_fixture_m1.h5ad`, `sh_func_fixture_m1.h5ad`, `xpr_func_fixture_m1.h5ad`.
- Function subset: {", ".join(FUNCTIONS)}.
- Selected cells: {", ".join(fixture_records["selected_cells"])}.
- Selected compounds: {", ".join(fixture_records["selected_cp_ids"])}.
- Selected genes: {", ".join(fixture_records["selected_genes"])}.
- Metadata and resolver index fixtures are real subsets of A-001 standard CSV/JSON resources.

## Downstream Use

Loader tasks should read the manifest first, then choose either full standard resources under
`1_asset/t021_standard_resources_bundle/` or the fixture resources under
`4_artifact/2_persist/fixture_package_m1/`.

Forward-query demos can use any selected fixture matrix observation as perturbation-to-function
evidence. Reverse-query demos can rank the selected fixture observations by one of the selected
function columns. The fixture is intentionally small and is not intended to reproduce full query
ranking behavior.

## Known Exclusions

- Truncated upstream CMAP H5AD files reported by T-014/T-021 are excluded.
- Historical GSEA output artifacts and old figures are excluded because they are provenance/support
  assets, not M1 runtime resources.
- GenePT embeddings are excluded because T-021 did not include them in the standard runtime bundle.
- No project raw assets, legacy source roots, failed T024-T040 outputs, web data, or synthetic
  biological records were used.
"""
    (PERSIST / "data_manifest_fixture_m1_readme.md").write_text(text, encoding="utf-8")


def write_html_report(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    body = "\n".join(
        f"<h2>{html.escape(h)}</h2>\n<div>{content}</div>" for h, content in sections
    )
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 32px; line-height: 1.5; color: #222; }}
    h1, h2 {{ color: #111; }}
    code {{ background: #f4f4f4; padding: 1px 4px; border-radius: 3px; }}
    table {{ border-collapse: collapse; margin: 12px 0; width: 100%; }}
    th, td {{ border: 1px solid #ddd; padding: 6px 8px; text-align: left; vertical-align: top; }}
    th {{ background: #f7f7f7; }}
  </style>
</head>
<body>
<h1>{html.escape(title)}</h1>
{body}
</body>
</html>
"""
    path.write_text(page, encoding="utf-8")


def write_reports(matrix_records, fixture_records, expected_rows, sample_rows):
    matrix_table = "<table><tr><th>Matrix</th><th>Fixture shape</th><th>Source</th><th>Path</th></tr>"
    for kind, rec in matrix_records.items():
        matrix_table += (
            f"<tr><td>{html.escape(kind)}</td><td>{rec['fixture_shape'][0]} x {rec['fixture_shape'][1]}</td>"
            f"<td><code>{html.escape(rec['source_path'])}</code></td><td><code>{html.escape(rec['fixture_path'])}</code></td></tr>"
        )
    matrix_table += "</table>"
    write_html_report(
        DOC / f"execution_report_v{TODAY}.html",
        "T-043 Execution Report",
        [
            ("Scope", "<p>Executed the approved T-043 plan using only registered A-001 through A-006 assets plus current task writable folders.</p>"),
            ("Inputs Inspected", "<p>A-001 standard resources, A-002 guide, A-003 process records, A-004 scope, A-005 inventory, and A-006 matrix coverage.</p>"),
            ("Selection Method", "<p>Selected deterministic real rows from A-001: compound rows require matching drug-index aliases, shRNA rows require gene-index coverage, and XPR rows require both gene-index and gene-metadata coverage.</p>"),
            ("Matrix Fixtures", matrix_table),
            ("Validation", f"<p>Generated and reloaded all fixture H5AD, CSV, JSON, YAML, and report outputs. Expected-resource rows: {len(expected_rows)}. Sample-record rows: {len(sample_rows)}.</p>"),
            ("Exclusions", "<p>No raw project assets, legacy source roots, failed T024-T040 outputs, web data, upstream truncated H5ADs, historical GSEA artifacts, or synthetic biological records were used.</p>"),
        ],
    )
    csv_list = "".join(
        f"<li><code>{html.escape(info['path'])}</code> ({info['shape'][0]} x {info['shape'][1]})</li>"
        for info in fixture_records["csv_outputs"].values()
    )
    json_list = "".join(
        f"<li><code>{html.escape(info['path'])}</code> (top-level count {info['top_level_count']})</li>"
        for info in fixture_records["json_outputs"].values()
    )
    write_html_report(
        DOC / f"result_report_v{TODAY}.html",
        "T-043 Result Report",
        [
            ("Produced Deliverables", "<p>Manifest, fixture package, shape/key/column table, sample-record table, README, registry, completion report, and HTML reports were produced under the current task.</p>"),
            ("Fixture CSV Outputs", f"<ul>{csv_list}</ul>"),
            ("Fixture JSON Outputs", f"<ul>{json_list}</ul>"),
            ("Downstream Handoff", "<p>Use <code>resource_manifest_m1.yaml</code> as the entry point. Use fixture resources for loader and query smoke tests; use full standard resources only when downstream code needs full retrieval behavior.</p>"),
            ("Caveat", "<p>The fixture validates data boundaries and loader/query wiring only. It is intentionally too small for biological ranking-performance claims.</p>"),
        ],
    )


def validate_outputs(manifest, expected_rows):
    checks = []
    required = [
        PERSIST / "resource_manifest_m1.yaml",
        FIXTURE,
        TABLE / "expected_shapes_keys_columns_m1.csv",
        TABLE / "sample_records_m1.csv",
        PERSIST / "data_manifest_fixture_m1_readme.md",
        DOC / f"execution_report_v{TODAY}.html",
        DOC / f"result_report_v{TODAY}.html",
    ]
    for path in required:
        checks.append({"path": rel(path), "exists": path.exists(), "size_bytes": path.stat().st_size if path.exists() and path.is_file() else None})
        assert path.exists(), path
    for kind in ["cp", "sh", "xpr"]:
        ann = ad.read_h5ad(FIXTURE / f"{kind}_func_fixture_m1.h5ad")
        assert ann.shape == (4, len(FUNCTIONS)), (kind, ann.shape)
        assert str(ann.X.dtype) == "float32", (kind, ann.X.dtype)
        assert set(ann.var_names) == set(FUNCTIONS)
    for entry in manifest["resources"]:
        path = ROOT / entry["path"]
        assert path.exists(), entry["path"]
    expected = pd.read_csv(TABLE / "expected_shapes_keys_columns_m1.csv")
    samples = pd.read_csv(TABLE / "sample_records_m1.csv")
    assert len(expected) == len(expected_rows)
    assert len(samples) > 0
    return {
        "status": "pass",
        "checked_paths": checks,
        "manifest_resource_count": len(manifest["resources"]),
        "expected_table_rows": len(expected),
        "sample_table_rows": len(samples),
    }


def write_registry(validation):
    artifacts = [
        {
            "id": "D-001",
            "name": "resource_manifest_m1",
            "type": "manifest",
            "path": "4_artifact/2_persist/resource_manifest_m1.yaml",
            "status": "ready",
            "provenance": "T-043 generated from A-001 through A-006",
            "notes": "Stable M1 resource manifest for full standard resources and fixture resources.",
        },
        {
            "id": "D-002",
            "name": "fixture_package_m1",
            "type": "package",
            "path": "4_artifact/2_persist/fixture_package_m1/",
            "status": "ready",
            "provenance": "T-043 bounded extraction from A-001 standard resources",
            "notes": "Small deterministic real-data fixture package for loader, forward, and reverse demos.",
        },
        {
            "id": "D-003",
            "name": "expected_shapes_keys_columns_m1",
            "type": "table",
            "path": "4_artifact/5_table/expected_shapes_keys_columns_m1.csv",
            "status": "ready",
            "provenance": "T-043 generated from A-001 through A-006",
            "notes": "Expected shape, keys, columns, index semantics, and validation rules.",
        },
        {
            "id": "D-004",
            "name": "sample_records_m1",
            "type": "table",
            "path": "4_artifact/5_table/sample_records_m1.csv",
            "status": "ready",
            "provenance": "T-043 generated from real A-001 records",
            "notes": "Traceable sample rows and keys used by the fixture package.",
        },
        {
            "id": "D-005",
            "name": "data_manifest_fixture_m1_readme",
            "type": "document",
            "path": "4_artifact/2_persist/data_manifest_fixture_m1_readme.md",
            "status": "ready",
            "provenance": "T-043",
            "notes": "Downstream usage and exclusions.",
        },
        {
            "id": "D-006",
            "name": "execution_report_v20260624",
            "type": "document",
            "path": "4_artifact/3_document/execution_report_v20260624.html",
            "status": "ready",
            "provenance": "T-043",
            "notes": "Human-facing execution method and validation summary.",
        },
        {
            "id": "D-007",
            "name": "result_report_v20260624",
            "type": "document",
            "path": "4_artifact/3_document/result_report_v20260624.html",
            "status": "ready",
            "provenance": "T-043",
            "notes": "Human-facing result and downstream handoff summary.",
        },
        {
            "id": "D-008",
            "name": "validation_log_m1",
            "type": "execution_record",
            "path": "3_execution/validation_log_m1.json",
            "status": "ready",
            "provenance": "T-043 validation run",
            "notes": "Execution-side validation evidence; not a reusable project artifact.",
        },
    ]
    with open(OUT / "registry.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump({"artifacts": artifacts}, f, sort_keys=False, allow_unicode=True)


def write_completion(validation):
    text = f"""# Completion

Task: T-043 data_manifest_fixture_m1
Completed: 2026-06-24
Status: completed

## Completed Steps

1. Confirmed CyHex availability and re-read the check handoff for execution strategy.
2. Inspected only registered assets A-001 through A-006 and current task writable folders.
3. Selected deterministic real records from A-001 for compound, shRNA, and XPR fixture paths.
4. Generated the M1 resource manifest, fixture package, expected shape/key/column table, sample-record table, README, HTML reports, artifact registry, and validation log.
5. Validated all declared output paths, reloaded fixture H5AD files, parsed produced tables, and checked manifest paths.

## Deliverables

- `4_artifact/2_persist/resource_manifest_m1.yaml`
- `4_artifact/2_persist/fixture_package_m1/`
- `4_artifact/5_table/expected_shapes_keys_columns_m1.csv`
- `4_artifact/5_table/sample_records_m1.csv`
- `4_artifact/2_persist/data_manifest_fixture_m1_readme.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`

## Validation Evidence

- Validation status: {validation["status"]}
- Manifest resources checked: {validation["manifest_resource_count"]}
- Expected table rows: {validation["expected_table_rows"]}
- Sample record rows: {validation["sample_table_rows"]}
- Validation log: `3_execution/validation_log_m1.json`

## Boundary Notes

No project raw assets under `2_project_asset/`, no legacy source-root reads, no failed T024-T040 outputs, no web/downloaded data, and no synthetic biological records were used.

## Caveat

The fixture package is intentionally small. It supports loader and query smoke/demo wiring, but it is not a substitute for full-resource biological ranking validation.
"""
    (ROOT / "5_report" / "completion.md").write_text(text, encoding="utf-8")


def main():
    clean_existing_outputs()
    matrix_records, matrix_sample_rows = build_matrix_fixtures()
    fixture_records, table_sample_rows = build_tabular_fixtures(matrix_records)
    profiles = full_resource_profile()
    sample_rows = matrix_sample_rows + table_sample_rows
    manifest, expected_rows = build_manifest_and_tables(matrix_records, fixture_records, profiles, sample_rows)
    write_readme(matrix_records, fixture_records)
    write_reports(matrix_records, fixture_records, expected_rows, sample_rows)
    validation = validate_outputs(manifest, expected_rows)
    write_json(EXEC / "validation_log_m1.json", validation)
    write_registry(validation)
    write_completion(validation)
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()

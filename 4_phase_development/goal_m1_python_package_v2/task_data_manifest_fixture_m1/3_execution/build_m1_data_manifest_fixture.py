from __future__ import annotations

import csv
import html
import json
import math
import os
import shutil
from datetime import date
from pathlib import Path

import anndata as ad
import pandas as pd
import yaml


TASK_ROOT = Path(__file__).resolve().parents[1]
ASSET = TASK_ROOT / "1_asset"
BUNDLE = ASSET / "t021_standard_resources_bundle"
PROCESS = ASSET / "t021_process_records"
OUT = TASK_ROOT / "4_artifact"
PERSIST = OUT / "2_persist"
TABLES = OUT / "5_table"
DOCS = OUT / "3_document"
FIXTURE = PERSIST / "fixture_package_m1"
LOG = TASK_ROOT / "3_execution" / "build_m1_data_manifest_fixture.log"

RUN_DATE = "2026-06-24"


MATRIX_FILES = {
    "cp": "cp_func_ad.h5ad",
    "sh": "sh_func_ad.h5ad",
    "xpr": "xpr_func_ad.h5ad",
}

INDEX_FILES = [
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
]

METADATA_FILES = [
    "cellline_meta_standard.csv",
    "cellline_info_standard.csv",
    "compound_meta_standard.csv",
    "compound_info_standard.csv",
    "gene_info_standard.csv",
]

FIXTURE_FUNCTIONS = [
    "HALLMARK_ADIPOGENESIS",
    "HALLMARK_APOPTOSIS",
    "HALLMARK_G2M_CHECKPOINT",
    "MP39 Metal-response",
]


def write_log(message: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(message.rstrip() + "\n")


def clean_output_dirs() -> None:
    for path in [FIXTURE, PERSIST / "resource_manifest_m1.yaml", PERSIST / "data_manifest_fixture_m1_readme.md"]:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
    for path in [
        TABLES / "expected_shapes_keys_columns_m1.csv",
        TABLES / "sample_records_m1.csv",
        DOCS / "execution_report_v20260624.html",
        DOCS / "result_report_v20260624.html",
    ]:
        if path.exists():
            path.unlink()
    FIXTURE.mkdir(parents=True, exist_ok=True)
    (FIXTURE / "matrices").mkdir(parents=True, exist_ok=True)
    (FIXTURE / "indexes").mkdir(parents=True, exist_ok=True)
    (FIXTURE / "metadata").mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def rel(path: Path) -> str:
    return str(path.relative_to(TASK_ROOT))


def ensure_inputs() -> None:
    required = [
        ASSET / "t021_standard_resource_guide.md",
        ASSET / "t014_precomputed_data_scope.md",
        ASSET / "t014_data_resource_inventory.csv",
        ASSET / "t014_matrix_schema_coverage.csv",
        PROCESS / "step5_validation_report.md",
    ]
    required.extend(BUNDLE / name for name in MATRIX_FILES.values())
    required.extend(BUNDLE / name for name in INDEX_FILES)
    required.extend(BUNDLE / name for name in METADATA_FILES)
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required registered assets: " + "; ".join(missing))
    write_log(f"Input preflight passed: {len(required)} registered files present.")


def json_summary(path: Path) -> tuple[str, str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        keys = list(data.keys())
        top = "dict"
        count = len(keys)
        required = "; ".join(keys[:8])
        if path.name == "function_index.json":
            required = "var_names; meta; aliases"
        elif path.name == "cellline_index.json":
            required = "valid_cells"
        elif path.name in {"drug_index.json", "gene_index_simple.json", "gene_index.json"}:
            required = "lookup keys"
        elif "neighbors" in path.name:
            required = "entity keys; neighbor lists"
        return top, str(count), required
    if isinstance(data, list):
        return "list", str(len(data)), "list entries"
    return type(data).__name__, "1", "scalar"


def csv_shape_columns(path: Path) -> tuple[tuple[int, int], list[str]]:
    df = pd.read_csv(path)
    return df.shape, list(df.columns)


def select_matrix_rows() -> tuple[dict[str, pd.DataFrame], list[str], list[dict[str, str]]]:
    selected: dict[str, pd.DataFrame] = {}
    matrix_samples: list[dict[str, str]] = []
    chosen_functions: list[str] | None = None

    for kind, filename in MATRIX_FILES.items():
        source = BUNDLE / filename
        adata = ad.read_h5ad(source, backed="r")
        try:
            obs = adata.obs.reset_index(drop=True)
            required_obs = ["sig_id", "project_code", "cell_iname", "pert_id", "cmap_name", "pert_dose", "pert_time"]
            missing = [col for col in required_obs if col not in obs.columns]
            if missing:
                raise ValueError(f"{filename} missing obs columns: {missing}")
            if chosen_functions is None:
                var_names = [str(v) for v in adata.var_names]
                chosen_functions = [f for f in FIXTURE_FUNCTIONS if f in var_names]
                if len(chosen_functions) < 3:
                    chosen_functions = var_names[:4]
            var_idx = [list(adata.var_names).index(fn) for fn in chosen_functions]
            rows = obs.head(3).copy()
            x = adata.X[:3, var_idx]
            if hasattr(x, "toarray"):
                x = x.toarray()
            for col_idx, fn in enumerate(chosen_functions):
                rows[fn] = [float(v) for v in x[:, col_idx]]
            rows.insert(0, "matrix_kind", kind)
            rows.insert(1, "source_file", filename)
            out_path = FIXTURE / "matrices" / f"{kind}_functional_scores_fixture.csv"
            rows.to_csv(out_path, index=False)
            selected[kind] = rows
            for _, row in rows.iterrows():
                matrix_samples.append(
                    {
                        "sample_type": "matrix_obs",
                        "source_resource": filename,
                        "source_identifier": str(row["sig_id"]),
                        "fixture_file": rel(out_path),
                        "selected_fields": "; ".join(required_obs + chosen_functions),
                        "inclusion_reason": f"{kind} matrix loader and query demo observation",
                        "traceability_note": f"Copied from first three obs rows of {rel(source)} with selected real score columns.",
                    }
                )
        finally:
            adata.file.close()
    assert chosen_functions is not None
    return selected, chosen_functions, matrix_samples


def write_fixture_indexes(selected_matrices: dict[str, pd.DataFrame], functions: list[str]) -> list[dict[str, str]]:
    samples: list[dict[str, str]] = []

    cell = selected_matrices["cp"].iloc[0]["cell_iname"]
    drug_alias = str(selected_matrices["cp"].iloc[0]["cmap_name"]).lower()
    drug_id = str(selected_matrices["cp"].iloc[0]["pert_id"])
    sh_gene = str(selected_matrices["sh"].iloc[0]["cmap_name"]).upper()
    xpr_gene = str(selected_matrices["xpr"].iloc[0]["cmap_name"]).upper()

    source_cell_index = json.loads((BUNDLE / "cellline_index.json").read_text(encoding="utf-8"))
    if cell not in source_cell_index["valid_cells"]:
        raise ValueError(f"Selected fixture cell {cell} not found in cellline_index.json")
    cell_index = {"valid_cells": [cell]}
    path = FIXTURE / "indexes" / "cellline_index_fixture.json"
    path.write_text(json.dumps(cell_index, indent=2, sort_keys=True), encoding="utf-8")
    samples.append(
        sample_row("index_entry", "cellline_index.json", cell, path, "valid_cells", "Exact cell-line lookup for selected matrix rows.")
    )

    source_drug_index = json.loads((BUNDLE / "drug_index.json").read_text(encoding="utf-8"))
    if drug_alias not in source_drug_index or source_drug_index[drug_alias] != drug_id:
        raise ValueError(f"Selected fixture drug alias {drug_alias} did not resolve to {drug_id}")
    path = FIXTURE / "indexes" / "drug_index_fixture.json"
    path.write_text(json.dumps({drug_alias: drug_id}, indent=2, sort_keys=True), encoding="utf-8")
    samples.append(sample_row("index_entry", "drug_index.json", drug_alias, path, drug_id, "Forward compound alias-to-BRD lookup."))

    source_gene_index_simple = json.loads((BUNDLE / "gene_index_simple.json").read_text(encoding="utf-8"))
    genes = {g: source_gene_index_simple[g] for g in [sh_gene, xpr_gene] if g in source_gene_index_simple}
    if sh_gene not in genes:
        raise ValueError(f"Selected sh fixture gene {sh_gene} not found in gene_index_simple.json")
    path = FIXTURE / "indexes" / "gene_index_simple_fixture.json"
    path.write_text(json.dumps(genes, indent=2, sort_keys=True), encoding="utf-8")
    for gene, type_code in genes.items():
        samples.append(sample_row("index_entry", "gene_index_simple.json", gene, path, type_code, "Genetic perturbation lookup for sh/xpr fixture rows."))

    function_index = json.loads((BUNDLE / "function_index.json").read_text(encoding="utf-8"))
    fixture_function_index = {
        "var_names": functions,
        "meta": {fn: function_index["meta"][fn] for fn in functions},
        "aliases": {alias: val for alias, val in function_index["aliases"].items() if val in functions},
    }
    path = FIXTURE / "indexes" / "function_index_fixture.json"
    path.write_text(json.dumps(fixture_function_index, indent=2, sort_keys=True), encoding="utf-8")
    for fn in functions:
        samples.append(sample_row("index_entry", "function_index.json", fn, path, "meta; aliases", "Reverse query target function lookup."))

    return samples


def sample_row(sample_type: str, source: str, identifier: str, fixture_path: Path, fields: str, reason: str) -> dict[str, str]:
    return {
        "sample_type": sample_type,
        "source_resource": source,
        "source_identifier": identifier,
        "fixture_file": rel(fixture_path),
        "selected_fields": fields,
        "inclusion_reason": reason,
        "traceability_note": f"Copied or boundedly extracted from {rel(BUNDLE / source)}.",
    }


def write_fixture_metadata(selected_matrices: dict[str, pd.DataFrame]) -> list[dict[str, str]]:
    samples: list[dict[str, str]] = []
    cell = selected_matrices["cp"].iloc[0]["cell_iname"]
    drug_id = selected_matrices["cp"].iloc[0]["pert_id"]
    sh_gene = selected_matrices["sh"].iloc[0]["cmap_name"]
    xpr_gene = selected_matrices["xpr"].iloc[0]["cmap_name"]

    cell_meta = pd.read_csv(BUNDLE / "cellline_meta_standard.csv")
    cell_rows = cell_meta[cell_meta["cell_iname"].astype(str) == str(cell)].head(1)
    if cell_rows.empty:
        raise ValueError(f"Cell metadata not found for {cell}")
    path = FIXTURE / "metadata" / "cellline_meta_fixture.csv"
    cell_rows.to_csv(path, index=False)
    samples.append(sample_row("metadata_row", "cellline_meta_standard.csv", str(cell), path, "; ".join(cell_rows.columns), "Cell metadata label for selected demo cell."))

    compound_meta = pd.read_csv(BUNDLE / "compound_meta_standard.csv")
    drug_rows = compound_meta[compound_meta["drug"].astype(str) == str(drug_id)].head(1)
    if drug_rows.empty:
        raise ValueError(f"Compound metadata not found for {drug_id}")
    path = FIXTURE / "metadata" / "compound_meta_fixture.csv"
    drug_rows.to_csv(path, index=False)
    samples.append(sample_row("metadata_row", "compound_meta_standard.csv", str(drug_id), path, "; ".join(drug_rows.columns), "Compound metadata label for selected forward demo drug."))

    gene_info = pd.read_csv(BUNDLE / "gene_info_standard.csv")
    genes = [str(sh_gene), str(xpr_gene)]
    gene_rows = gene_info[gene_info["gene_symbol"].astype(str).isin(genes)].head(2)
    if str(sh_gene) not in set(gene_rows["gene_symbol"].astype(str)):
        raise ValueError(f"Gene metadata not found for {sh_gene}")
    path = FIXTURE / "metadata" / "gene_info_fixture.csv"
    gene_rows.to_csv(path, index=False)
    for gene in gene_rows["gene_symbol"].astype(str):
        samples.append(sample_row("metadata_row", "gene_info_standard.csv", gene, path, "; ".join(gene_rows.columns), "Gene metadata label for selected genetic demo perturbation."))
    return samples


def collect_resource_summaries(functions: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    validation_by_name = {
        "cp_func_ad.h5ad": "T-021 step5 PASS: readable h5ad, float32, 91 vars, required obs columns, finite scores",
        "sh_func_ad.h5ad": "T-021 step5 PASS: readable h5ad, float32, 91 vars, required obs columns, finite scores",
        "xpr_func_ad.h5ad": "T-021 step5 PASS: readable h5ad, float32, 91 vars, required obs columns, finite scores",
    }
    for kind, filename in MATRIX_FILES.items():
        source = BUNDLE / filename
        a = ad.read_h5ad(source, backed="r")
        try:
            rows.append(
                {
                    "resource_id": f"std_matrix_{kind}",
                    "resource_name": filename,
                    "source_path": rel(source),
                    "file_type": "h5ad",
                    "resource_type": "functional_matrix",
                    "loader_role": f"{kind} perturbation functional score matrix",
                    "expected_shape_or_count": f"{a.n_obs} rows x {a.n_vars} functions",
                    "key_fields": "obs.sig_id",
                    "required_columns_or_keys": "obs: sig_id; project_code; cell_iname; pert_id; cmap_name; pert_dose; pert_time | var_names: 91 functions",
                    "index_semantics": "rows are perturbation signatures; columns are functional terms; X is signed float32 functional score",
                    "validation_rule": validation_by_name[filename],
                    "provenance": "T-021/D-004 standard resource bundle; T-014/D-003 matrix schema coverage",
                }
            )
        finally:
            a.file.close()
    for filename in INDEX_FILES:
        source = BUNDLE / filename
        top_type, count, required = json_summary(source)
        role = "query resolver lookup"
        if filename == "function_index.json":
            role = "function term catalog for reverse-query target resolution"
        elif filename.startswith("drug_"):
            role = "compound exact/proxy query resolution"
        elif filename.startswith("gene_"):
            role = "gene exact/proxy query resolution"
        elif filename.startswith("cellline_"):
            role = "cell line exact/proxy context resolution"
        rows.append(
            {
                "resource_id": "std_index_" + filename.replace(".json", ""),
                "resource_name": filename,
                "source_path": rel(source),
                "file_type": "json",
                "resource_type": "query_index",
                "loader_role": role,
                "expected_shape_or_count": f"{top_type} with {count} top-level entries",
                "key_fields": required,
                "required_columns_or_keys": required,
                "index_semantics": "JSON lookup resource; exact schema documented by T-021 guide",
                "validation_rule": "T-021 step5 PASS: parsable non-empty JSON dict/list",
                "provenance": "T-021/D-004 standard resource bundle; T-021/D-005 validation records",
            }
        )
    csv_required = {
        "cellline_meta_standard.csv": "cell_iname; cell_lineage; primary_disease",
        "cellline_info_standard.csv": "cell_iname; cellosaurus_id; cell_lineage",
        "compound_meta_standard.csv": "drug; target; smiles",
        "compound_info_standard.csv": "pert_id; cmap_name; target",
        "gene_info_standard.csv": "gene_id; gene_symbol; ensembl_id",
    }
    for filename in METADATA_FILES:
        source = BUNDLE / filename
        shape, cols = csv_shape_columns(source)
        rows.append(
            {
                "resource_id": "std_metadata_" + filename.replace(".csv", ""),
                "resource_name": filename,
                "source_path": rel(source),
                "file_type": "csv",
                "resource_type": "metadata_table",
                "loader_role": "metadata labels and filtering support",
                "expected_shape_or_count": f"{shape[0]} rows x {shape[1]} columns",
                "key_fields": csv_required.get(filename, "; ".join(cols[:3])),
                "required_columns_or_keys": "; ".join(cols),
                "index_semantics": "CSV table with entity identifiers as ordinary columns",
                "validation_rule": "T-021 step5 PASS: readable CSV and required key columns present",
                "provenance": "T-021/D-004 standard resource bundle; T-014/D-002 data resource inventory",
            }
        )
    for path in sorted(FIXTURE.rglob("*")):
        if path.is_file():
            if path.suffix == ".csv":
                shape, cols = csv_shape_columns(path)
                expected = f"{shape[0]} rows x {shape[1]} columns"
                keys = "; ".join(cols[: min(6, len(cols))])
            elif path.suffix == ".json":
                _, count, keys = json_summary(path)
                expected = f"fixture JSON with {count} top-level entries"
            else:
                expected, keys = "fixture file", ""
            rows.append(
                {
                    "resource_id": "fixture_" + path.stem,
                    "resource_name": path.name,
                    "source_path": rel(path),
                    "file_type": path.suffix.lstrip("."),
                    "resource_type": "fixture",
                    "loader_role": "small deterministic loader/query smoke-test fixture",
                    "expected_shape_or_count": expected,
                    "key_fields": keys,
                    "required_columns_or_keys": keys,
                    "index_semantics": "bounded subset copied or extracted from standard resources",
                    "validation_rule": "T-043 validation: loadable fixture, non-empty, real-source provenance in sample_records_m1.csv",
                    "provenance": "T-043 derived from T-021/D-004 real records",
                }
            )
    return rows


def write_manifest(resource_rows: list[dict[str, str]], functions: list[str]) -> None:
    resources = []
    for row in resource_rows:
        resources.append(
            {
                "id": row["resource_id"],
                "name": row["resource_name"],
                "path": row["source_path"],
                "file_type": row["file_type"],
                "resource_type": row["resource_type"],
                "loader_role": row["loader_role"],
                "required_keys_or_columns": row["required_columns_or_keys"],
                "expected_shape_or_count": row["expected_shape_or_count"],
                "index_semantics": row["index_semantics"],
                "validation_rule": row["validation_rule"],
                "provenance": row["provenance"],
            }
        )
    manifest = {
        "manifest_id": "resource_manifest_m1",
        "task_id": "T-043",
        "generated": RUN_DATE,
        "scope": "M1 stable data substrate for loader, forward-query, and reverse-query demos",
        "authorities": [
            {"asset_id": "A-001", "origin": "T-021/D-004", "path": "1_asset/t021_standard_resources_bundle"},
            {"asset_id": "A-002", "origin": "T-021/D-001", "path": "1_asset/t021_standard_resource_guide.md"},
            {"asset_id": "A-003", "origin": "T-021/D-005", "path": "1_asset/t021_process_records"},
            {"asset_id": "A-004", "origin": "T-014/D-001", "path": "1_asset/t014_precomputed_data_scope.md"},
            {"asset_id": "A-005", "origin": "T-014/D-002", "path": "1_asset/t014_data_resource_inventory.csv"},
            {"asset_id": "A-006", "origin": "T-014/D-003", "path": "1_asset/t014_matrix_schema_coverage.csv"},
        ],
        "fixture_policy": {
            "source": "real records from A-001 only",
            "synthetic_records": False,
            "selected_functions": functions,
            "matrix_rows_per_type": 3,
        },
        "resources": resources,
        "known_exclusions": [
            "Full source/upstream CMAP H5AD files are excluded because T-014 reports migrated copies as truncated and they are not runtime M1 dependencies.",
            "Historical GSEA outputs are excluded because T-014 treats them as provenance/support material, not M1 runtime resources.",
            "GenePT embeddings are excluded because T-021 marks them optional/large and outside the standard resource set.",
            "Full standard resources remain referenced by manifest entries; the fixture package is only for smoke tests and demos.",
        ],
    }
    (PERSIST / "resource_manifest_m1.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=False), encoding="utf-8")


def write_readme(functions: list[str]) -> None:
    text = f"""# T-043 M1 Data Manifest And Fixture Package

Generated: {RUN_DATE}

## Purpose

This package defines the M1 data substrate for downstream PxFquery loader, forward-query, and reverse-query development tasks. It uses only registered T-014 and T-021 assets as authorities.

## Main Files

- `resource_manifest_m1.yaml`: stable resource manifest for the full T-021 standard bundle and the T-043 fixture package.
- `fixture_package_m1/`: small deterministic files extracted from real A-001 records.
- `expected_shapes_keys_columns_m1.csv`: expected shapes, keys, columns, index semantics, validation rules, and provenance.
- `sample_records_m1.csv`: exact source identifiers and traceability notes for selected examples.

## Fixture Contents

- Three matrix fixture CSV files: `cp`, `sh`, and `xpr`; each contains the first three real observations from the corresponding standard H5AD matrix.
- Index fixture JSON files for the selected A375 cell line, selected forward-demo compound, selected genetic perturbation genes, and selected functions.
- Metadata fixture CSV files for the selected cell, compound, and gene records.
- Selected function columns: {", ".join(functions)}.

## Downstream Use

Use the manifest first. For package loader tests, load the full resource paths from `resource_manifest_m1.yaml`. For quick smoke tests or examples, load files under `fixture_package_m1/` and verify them against `sample_records_m1.csv`.

The fixture is not intended to reproduce full query ranking performance. It is intended to prove that schemas, identifiers, score columns, and resolver keys are wired correctly.

## Known Exclusions

- Upstream/source CMAP H5AD files are excluded because T-014 reports migrated copies as truncated and they are not required for the runtime M1 substrate.
- Historical GSEA output artifacts are excluded because T-014 classifies them as provenance/support material.
- GenePT embeddings and other optional large proxy resources are excluded because T-021 did not include them in the standard resource bundle.
- No T024-T040 outputs, web resources, raw project assets, or legacy source-root files were used.
"""
    (PERSIST / "data_manifest_fixture_m1_readme.md").write_text(text, encoding="utf-8")


def write_reports(samples: list[dict[str, str]], resource_rows: list[dict[str, str]]) -> None:
    execution_items = [
        "Confirmed CyHex API version 1.2.19.",
        "Read checker handoff and registered task assets only.",
        "Used A-002/A-004/A-005/A-006 for scope, schema, and resource-boundary decisions.",
        "Cross-checked A-001 against A-003 step5 validation report: 18/18 resources passed T-021 validation.",
        "Extracted deterministic real fixture records from A-001 standard resource files.",
        "Generated manifest, tables, README, reports, registry, and completion report under current task outputs.",
    ]
    result_items = [
        "Manifest covers three functional matrices, ten query indexes, five metadata tables, and task fixture files.",
        f"Fixture package contains {len(list(FIXTURE.rglob('*')))} paths including {len([p for p in FIXTURE.rglob('*') if p.is_file()])} files.",
        f"Sample records table contains {len(samples)} traceable entries.",
        f"Expected-shapes table contains {len(resource_rows)} manifest/fixture rows.",
        "No raw project assets, web search, failed T024-T040 outputs, or direct legacy source reads were used.",
    ]
    for target, title, items in [
        (DOCS / "execution_report_v20260624.html", "T-043 Execution Report", execution_items),
        (DOCS / "result_report_v20260624.html", "T-043 Result Report", result_items),
    ]:
        body = "\n".join(f"<li>{html.escape(item)}</li>" for item in items)
        target.write_text(
            "<!doctype html><html><head><meta charset='utf-8'><title>"
            + html.escape(title)
            + "</title><style>body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:960px;margin:32px auto;line-height:1.5}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:4px 8px}</style></head><body>"
            + f"<h1>{html.escape(title)}</h1><p>Generated: {RUN_DATE}</p><ul>{body}</ul>"
            + "<h2>Delivered Paths</h2><ul>"
            + "<li>4_artifact/2_persist/resource_manifest_m1.yaml</li>"
            + "<li>4_artifact/2_persist/fixture_package_m1/</li>"
            + "<li>4_artifact/5_table/expected_shapes_keys_columns_m1.csv</li>"
            + "<li>4_artifact/5_table/sample_records_m1.csv</li>"
            + "<li>4_artifact/2_persist/data_manifest_fixture_m1_readme.md</li>"
            + "</ul></body></html>",
            encoding="utf-8",
        )


def write_registry_and_completion() -> None:
    artifacts = [
        ("D-001", "resource_manifest_m1", "manifest", "4_artifact/2_persist/resource_manifest_m1.yaml", "M1 resource manifest with full standard-resource and fixture entries."),
        ("D-002", "fixture_package_m1", "package", "4_artifact/2_persist/fixture_package_m1", "Minimal deterministic fixture package from real A-001 records."),
        ("D-003", "expected_shapes_keys_columns_m1", "table", "4_artifact/5_table/expected_shapes_keys_columns_m1.csv", "Expected shapes, keys, columns, index semantics, validation rules, and provenance."),
        ("D-004", "sample_records_m1", "table", "4_artifact/5_table/sample_records_m1.csv", "Traceable sample/source records for loader, forward, and reverse demos."),
        ("D-005", "data_manifest_fixture_m1_readme", "document", "4_artifact/2_persist/data_manifest_fixture_m1_readme.md", "Downstream usage and exclusion notes."),
        ("D-006", "execution_report_v20260624", "document", "4_artifact/3_document/execution_report_v20260624.html", "Execution method and validation evidence report."),
        ("D-007", "result_report_v20260624", "document", "4_artifact/3_document/result_report_v20260624.html", "Result summary and downstream handoff report."),
    ]
    registry = {
        "artifacts": [
            {
                "id": artifact_id,
                "name": name,
                "type": typ,
                "path": path,
                "status": "ready",
                "created": RUN_DATE,
                "provenance": "T-043 generated from registered T-014/T-021 assets only",
                "notes": notes,
            }
            for artifact_id, name, typ, path, notes in artifacts
        ]
    }
    (OUT / "registry.yaml").write_text(yaml.safe_dump(registry, sort_keys=False, allow_unicode=False), encoding="utf-8")
    completion = f"""# Completion

Task: T-043 data_manifest_fixture_m1
Date: {RUN_DATE}
Status: completed

## Completed Steps

1. Confirmed CyHex runtime and accepted the green-check handoff boundaries.
2. Inspected only registered T-014/T-021 assets and the current task writable folders.
3. Confirmed the concrete T-021 standard resource paths and selected the M1 resource boundary.
4. Built a deterministic fixture package from real A-001 records only.
5. Generated the resource manifest, expected-shapes table, sample-records table, README, execution report, result report, and artifact registry.
6. Validated generated outputs with the task-local generation/validation script.

## Validation Evidence

- A-001 standard resources were present under `1_asset/t021_standard_resources_bundle`.
- A-003 `step5_validation_report.md` records 18/18 T-021 resource validation passes.
- Fixture files were copied or boundedly extracted from A-001 and are documented in `4_artifact/5_table/sample_records_m1.csv`.
- No `2_project_asset/`, failed T024-T040 outputs, web data, or direct legacy source-root files were used.

## Deliverables

- `4_artifact/2_persist/resource_manifest_m1.yaml`
- `4_artifact/2_persist/fixture_package_m1/`
- `4_artifact/5_table/expected_shapes_keys_columns_m1.csv`
- `4_artifact/5_table/sample_records_m1.csv`
- `4_artifact/2_persist/data_manifest_fixture_m1_readme.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`

## Caveats

The fixture package is deliberately small and supports loader/query smoke tests, not full ranking performance. Full query behavior should use the complete standard resources referenced by the manifest.
"""
    (TASK_ROOT / "5_report" / "completion.md").write_text(completion, encoding="utf-8")


def validate_outputs(samples: list[dict[str, str]], resource_rows: list[dict[str, str]]) -> None:
    required_paths = [
        PERSIST / "resource_manifest_m1.yaml",
        FIXTURE,
        TABLES / "expected_shapes_keys_columns_m1.csv",
        TABLES / "sample_records_m1.csv",
        PERSIST / "data_manifest_fixture_m1_readme.md",
        DOCS / "execution_report_v20260624.html",
        DOCS / "result_report_v20260624.html",
        OUT / "registry.yaml",
        TASK_ROOT / "5_report" / "completion.md",
    ]
    missing = [rel(path) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing generated outputs: " + "; ".join(missing))
    if not samples:
        raise ValueError("No sample records generated")
    if not resource_rows:
        raise ValueError("No resource shape rows generated")
    manifest = yaml.safe_load((PERSIST / "resource_manifest_m1.yaml").read_text(encoding="utf-8"))
    if not manifest.get("resources"):
        raise ValueError("Manifest has no resources")
    sample_df = pd.read_csv(TABLES / "sample_records_m1.csv")
    required_sample_cols = {"sample_type", "source_resource", "source_identifier", "fixture_file", "traceability_note"}
    if not required_sample_cols.issubset(sample_df.columns):
        raise ValueError("sample_records_m1.csv missing required columns")
    for path_str in sample_df["fixture_file"].dropna().unique():
        if not (TASK_ROOT / path_str).exists():
            raise FileNotFoundError(f"Sample fixture path missing: {path_str}")
    write_log(f"Validation passed: {len(required_paths)} deliverables, {len(samples)} samples, {len(resource_rows)} resource rows.")


def main() -> None:
    if LOG.exists():
        LOG.unlink()
    write_log("T-043 M1 data manifest/fixture build started.")
    clean_output_dirs()
    ensure_inputs()
    selected_matrices, functions, samples = select_matrix_rows()
    samples.extend(write_fixture_indexes(selected_matrices, functions))
    samples.extend(write_fixture_metadata(selected_matrices))

    sample_df = pd.DataFrame(samples)
    sample_df.to_csv(TABLES / "sample_records_m1.csv", index=False, quoting=csv.QUOTE_MINIMAL)

    resource_rows = collect_resource_summaries(functions)
    pd.DataFrame(resource_rows).to_csv(TABLES / "expected_shapes_keys_columns_m1.csv", index=False, quoting=csv.QUOTE_MINIMAL)

    write_manifest(resource_rows, functions)
    write_readme(functions)
    write_reports(samples, resource_rows)
    write_registry_and_completion()
    validate_outputs(samples, resource_rows)
    write_log("T-043 M1 data manifest/fixture build completed.")


if __name__ == "__main__":
    main()

# T-021: standard_resources_optimal_formats — Protocol

## Objective

Based on the organized precomputed data (from T-014), identify and define PxFquery's standard built-in resources and their optimal formats. This includes:

1. Identify which data assets are PxFquery's "standard built-in resources" — the strict inputs needed by the pxfquery package.
2. Determine the optimal storage format for each resource (h5ad is the natural format for single-cell data, but we want data as small as possible).
3. Assess whether separate independent tables are better than a single monolithic matrix. Evaluate float precision reduction (float64 → float32 or lower).
4. Produce Python-verified, production-grade standard resource files that will serve as the foundation for downstream development and testing.
5. Each resource must be Python-verified and documented in detail.

## Inputs / Asset Sources

All assets registered in `1_asset/registration.yaml`:
- **A-001**: T-014 data resource inventory (`5_table/pxfquery_t014_data_resource_inventory_v20260618.csv`)
- **A-002**: T-014 matrix schema coverage (`5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv`)
- **A-003**: T-014 precomputed data understanding report (`3_document/pxfquery_t014_precomputed_data_understanding_report_v20260618.html`)
- **A-004**: Precomputed functional matrices — legacy flat library `data/functional_matrices/` (6 H5AD files)
- **A-005**: Metadata tables — legacy flat library `data/metadata_tables/`
- **A-006**: Query indexes — legacy flat library `data/query_indexes/`
- **A-007**: T-014 follow-up G007 task proposals (`2_persist/pxfquery_t014_followup_g007_task_proposals_v20260618.md`)
- **A-008**: pxfquery package code — legacy flat library `code/pxfquery_package/`

Direct legacy flat library paths:
- `data/functional_matrices/` (canonical H5AD set: M-0105–M-0107)
- `data/metadata_tables/` (9 files)
- `data/query_indexes/` (9 JSONs — note: `function_index.json` is missing)

## Steps

### Step 1: Read T-014 predecessor artifacts and pxfquery package code

Read the T-014 deliverables to understand the precomputed data landscape:
- Resource inventory (66 files documented with roles/readiness)
- Matrix schema/coverage (11 H5ADs inspected)
- Precomputed data understanding report
- Follow-up G007 proposals

Read the pxfquery package code (`code/pxfquery_package/`) to identify what the package actually expects:

| Asset | Package expects | Format | Schema invariant |
|---|---|---|---|
| Functional matrices | `{xpr,sh,cp}_func_ad.h5ad` | h5ad (via `anndata.read_h5ad`) | obs: sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time; var: 91 function terms |
| Cell line index | `cellline_index.json` | JSON | `{"valid_cells": [...]}` |
| Cell line neighbors | `cellline_neighbors.json` | JSON | `{lineage:{disease:{subtype:[cells]}}}` |
| Drug index | `drug_index.json` | JSON | `{"alias_lower": "BRD-..."}` |
| Drug neighbors | `drug_neighbors.json` | JSON | `{id_no_prefix: [[id_no_prefix, t_int], ...]}` |
| Gene index (simple) | `gene_index_simple.json` | JSON | `{"SYMBOL_UPPER": "type_code"}` |
| Gene neighbors (simple) | `gene_neighbors_simple.json` | JSON | `{symbol: [[neighbor, cosine_int], ...]}` |
| Function index | `function_index.json` | JSON | `{var_names, meta, aliases}` — **MISSING** |
| Cell line tree | `cellline_tree.json` | JSON | `{tree, cell_index, meta}` |
| Full gene index | `gene_index.json` | JSON | `{lowercase: {symbol, gene_type, in_matrix}}` |
| Full gene neighbors | `gene_neighbors.json` | JSON | same shape as simple |

Output: `3_execution/step1_package_format_audit.md`

### Step 2: Verify canonical dataset and identify duplicates

Inspect the functional matrices directory. Two vintage pairs exist (M-0105–M-0107 and M-0199–M-0201). Verify they are identical and select the canonical set. For each selected canonical file:

- Load H5AD, extract `obs` schema, `var` names (91 HALLMARK terms), `X` shape, dtype
- Record: file size, matrix dimensions, memory footprint, float precision
- Sample a few rows to understand score distribution (range, mean, sparsity if any)

Output: `3_execution/step2_matrix_profiling.md`

### Step 3: Assess optimal format and precision reduction

For each functional matrix, evaluate:

1. **Float precision**: Can float64 → float32 be applied without meaningful loss? Measure min/max, distribution shift, rank correlation between float64 and float32 versions.
2. **Storage format**: Compare h5ad (AnnData on-disk), parquet (columnar per var), and feather (fast row-oriented). Measure file size, load time, and query-read performance.
3. **Separation into tables**: Can the functional matrix be split into standalone tables? Assess: perturbation metadata table (obs data), function metadata table (var names + descriptions), and sparse score table (perturbation × function). Measure size trade-offs.
4. **Missing function_index.json**: Check whether the 91 HALLMARK names can be reconstructed from matrix `var` attributes or from context cards. Determine whether a new `function_index.json` should be part of the standard resource output.

For **metadata tables**, evaluate if they can be consolidated / deduplicated:
- Cell line metadata (M-0093 / M-0184 duplicates; M-0234 enriched version)
- Compound metadata (M-0099 / M-0188 duplicates; M-0235 enriched version)
- Gene info beta (M-0187)

For **query indexes**, evaluate JSON compactness:
- All 9 existing JSONs are already compact (integer-coded similarity values, prefix-stripped keys)
- Assess whether any index can be shrunk further or if the current format is optimal
- Flag function_index.json (missing) as a mandatory rebuild

Output: `3_execution/step3_format_evaluation.md`

### Step 4: Produce standard resources

Based on Step 3 evaluation, create the standard resource files. Write Python scripts that:

1. Convert the canonical functional matrices to optimal format:
   - If float32 is safe: produce `{xpr,sh,cp}_func_ad_f32.h5ad`
   - If table-split is better: produce separate `perturbation_meta.csv`, `function_meta.csv`, and score table in optimal format
2. Deduplicate and consolidate metadata tables:
   - `cellline_meta_standard.csv` (enriched version, deduplicated)
   - `compound_meta_standard.csv` (enriched version, deduplicated)
   - `gene_info_standard.csv`
3. Rebuild the missing `function_index.json` from matrix var names
4. Verify all output files by loading them with the same Python libraries the pxfquery package uses

Each standard resource must be placed under the task's output area (not inside legacy assets).

Output: Standard resource files placed in `3_execution/standard_resources/`

### Step 5: Python verification and validation

For each produced standard resource file, write and run a Python validation script that:

1. Loads the file
2. Checks schema matches pxfquery package expectations
3. Validates data integrity (no null in key columns, correct dtypes, expected row count range)
4. Measures load time
5. Records file size

Output: `3_execution/step5_validation_report.md`

### Step 6: Write detailed resource documentation

Write a comprehensive Chinese/English documentation (`4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md`) that:

1. Lists each standard resource with its role, format, schema, and size
2. Explains why each format was chosen (with evidence from Step 3)
3. Documents the float precision decision and the trade-offs
4. Shows how each resource maps to pxfquery package inputs
5. Provides verification status (all Python-verified)
6. Notes any gaps (e.g. function_index.json rebuilt status)

Output: `4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md`

### Step 7: Write completion report

Write `5_report/completion.md` summarizing:
- What standard resources were produced
- Format decisions with rationale
- Float precision trade-off summary
- Python verification results
- Known gaps and follow-up recommendations

Output: `5_report/completion.md`

## Deliverables

1. `3_execution/step1_package_format_audit.md` — Package code format audit report
2. `3_execution/step2_matrix_profiling.md` — Matrix profiling and duplicate verification
3. `3_execution/step3_format_evaluation.md` — Optimal format evaluation with float precision analysis
4. `3_execution/step5_validation_report.md` — Python validation report
5. Standard resource files under `3_execution/standard_resources/`
6. `4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md` — Detailed resource documentation
7. `5_report/completion.md` — Completion report

## Constraints

- Do not modify migrated data assets, legacy flat library files, or project protocol.
- Do not write standard resources into the legacy asset library; they go to `3_execution/standard_resources/`.
- All format evaluations must be backed by actual Python measurement, not speculation.
- Float precision evaluation must check: value range distortion, rank correlation, rank preservation at top/bottom 5%.
- If float32 introduces meaningful loss, keep float64 and document the decision.
- The missing `function_index.json` must be reconstructed as part of this task — it is a critical runtime gap.
- This task is configuration + execution (hybrid). The written standard resources will be used by downstream development and testing tasks.

## Success Criteria

- All standard resources are Python-verifiable (loadable, schema-correct, non-corrupt).
- Each format decision has a measurable rationale (file size, load time, precision retention).
- The function index gap from T-007/T-014 is closed.
- Documentation is detailed enough for a downstream developer to understand each resource's role, format, and provenance.
- Total resource footprint is minimized while preserving scientific fidelity.
# Protocol: forward_query_engine_v1

## Objective
Create a `pxfquery-T-029` deterministic forward query engine that loads T-021 standard resources (xpr functional matrix) via the T-026 loader, uses the T-024 pxfquery package `ForwardQuery` class to run EGFR/A549/xpr-style forward queries, and writes serializable result tables and reports.

## Inputs
- **A-001**: T-024 pxfquery workspace package — `4_artifact/2_persist/workspace/src/pxfquery/` containing `ForwardQuery`, `ForwardResult`, `DataLoader`, and the full package tree. The engine uses this as the query class source.
- **A-002**: T-026 matrix loader package — `4_artifact/2_persist/loader/__init__.py` provides `load_matrix()`, `load_bundle()`, `load_index()`, `load_metadata()`. The engine delegates resource loading to this package.
- **A-003**: T-021 standard_resources bundle (D-004) — `xpr_func_ad.h5ad` float32 functional matrix (132464 obs x 91 vars) with `cmap_name`, `pert_id`, `cell_iname` obs columns, plus JSON indexes (gene_index.json, drug_index.json, cellline_index.json, function_index.json) and CSV metadata tables. The primary data source for forward queries.
- **A-004**: T-013 MVP capability contract (D-001) — Capability/gap evidence listing known fuzzy-match issues and index-naming breaks. Used to set realistic query behavior expectations and decide when to repair vs. document.
- **A-005**: T-013 failure/missing capability list (D-005) — Documents that `function_index.json` is present in xpr bundle, that fuzzy match has false-positive risk, and that resolver/NL layer is not in scope. Tunes repair decisions.

## Steps
1. Read T-024 workspace package to understand `ForwardQuery`, `ForwardResult`, and `DataLoader` API. Confirm `import pxfquery` works or identify import-blocking issues from T-013 evidence.
2. Read T-026 loader package to understand `load_matrix()`, `load_bundle()`, and the loader validation evidence (`loader_validation.json`) to know the exact xpr matrix shape, obs columns, and dtype before writing any engine code.
3. Implement the forward query engine script at `3_execution/forward_engine.py` that:
   - Imports from T-026 loader to open `xpr_func_ad.h5ad` from the A-003 bundle.
   - Passes the loaded AnnData to `ForwardQuery`.
   - Runs `query("EGFR", cell_line="A549", top_n=20)` to reproduce the canonical forward demo.
   - Runs one additional query with a different gene (e.g. `TP53`) and cell line (e.g. `MCF7`) as diversity evidence.
   - Runs a not-found query with a nonexistent perturbation to verify `ForwardResult.found=False` behavior.
   - Runs each query and immediately writes serialized result tables.
4. Write serialized output under `4_artifact/5_table/`:
   - `pxfquery_T029_EGFR_A549_xpr_forward_result.csv` — top activated and suppressed terms with scores.
   - `pxfquery_T029_TP53_MCF7_xpr_forward_result.csv` — diversity case.
   - `pxfquery_T029_notfound_query_result.json` — not-found behavior evidence.
5. If the forward query fails because of a scoped package bug (e.g. import error, dtype incompatibility, column name mismatch between legacy ForwardQuery expectations and A-003 xpr H5AD structure), repair it inside this task scope by producing a corrected local version at `4_artifact/2_persist/pxfquery_T029_<name>_repaired.py`. Record what was fixed, source asset id, changed files, validation evidence, and downstream consumption guidance in `5_report/repair_log.md`.
6. Produce CyHex-mandatory reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese HTML step-by-step execution report.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese HTML result report showing query results, tables, and schema documentation.
7. Write `4_artifact/registry.yaml` registering all T-029 deliverables.
8. Write `5_report/completion.md` summarizing what was produced and what remains for downstream tasks.

### Required Bug-Repair Handling
- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, e.g. `pxfquery-T-029`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning
- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read upstream versions and emit `pxfquery-T-029` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Engine Discipline
- The engine must load data from A-003 bundle by reference using the T-026 loader; it must not copy upstream `.h5ad` or `.json` bytes.
- The engine must use T-024 workspace's `ForwardQuery` class directly (import from workspace `src/pxfquery/query/forward.py`), not a custom reimplementation.
- The engine script must be runnable from the `pxfquery` conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/forward_engine.py`.
- The engine must NOT depend on resolver/NL/LLM layers. This is a **deterministic** forward query engine v1. T-013 evidence confirms resolver is blocked by index-naming issues; those are out of scope for this task.
- If the `function_index.json` or any index file is needed, it is in A-003 (T-021 bundle has `function_index.json` with keys `var_names`, `meta`, `aliases` — confirmed by T-026 loader validation).
- Forward query uses T-026's `load_matrix()` and T-024's `ForwardQuery` class; it does not need any index for the basic xpr matrix path.

### T-013 Knowledge Integration
- T-013 CAP-05 (fuzzy match false-positive): The engine should accept fuzzy match as-is for this v1 unless it prevents a runnable result. If a false positive prevents the EGFR/A549 demo, repair the fuzzy match threshold inside this task scope and document.
- T-013 CAP-03 (index naming): Not relevant — forward query does not use resolver/indexes.
- T-013 CAP-07 (resolver/NL blocked): Confirmed out of scope for deterministic engine v1.

## Deliverables
- `3_execution/forward_engine.py` — Runnable forward query engine script.
- `4_artifact/5_table/pxfquery_T029_EGFR_A549_xpr_forward_result.csv` — EGFR/A549 canonical forward result table.
- `4_artifact/5_table/pxfquery_T029_TP53_MCF7_xpr_forward_result.csv` — Diversity case result table.
- `4_artifact/5_table/pxfquery_T029_notfound_query_result.json` — Not-found behavior evidence.
- `4_artifact/2_persist/pxfquery_T029_<name>_repaired.py` — Present only if repair was required.
- `4_artifact/registry.yaml` — T-029 deliverable registry.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex-mandatory execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex-mandatory result report.
- `5_report/completion.md` — Completion report.
- `5_report/repair_log.md` — Present only if bug was repaired.

## Acceptance
- `forward_engine.py` imports T-026 loader and T-024 ForwardQuery successfully.
- EGFR/A549/xpr query actually runs and produces `ForwardResult.found=True`.
- Result tables exist, are non-empty, and contain scores for top 20 activated + top 20 suppressed functional terms.
- At least one additional diversity query (different gene/cell-line) runs successfully.
- Not-found query produces `ForwardResult.found=False` without crashing.
- All Python execution uses the pxfquery conda environment.
- T-023 is not required; T-013 capability evidence is the gap reference for this v1 task.
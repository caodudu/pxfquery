# Protocol: function_index_pack_v1

## Objective

Produce a `pxfquery-T-028` runtime function-index pack that:

- contains **exactly the 91 function terms** that appear as `var` columns in the upstream H5AD matrices (`cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`), as observed by the T-026 loader using `anndata.read_h5ad` on the T-021 standard resources bundle; and
- carries, for each function term, a list of **aliases** that downstream query/resolver tasks can use for proxy/match-style retrieval.

The deliverable must be a JSON pack (`function_index.json`) accompanied by a machine-readable validation table that proves every entry in the pack maps to a real loader-observed matrix var term, plus a short downstream-usage note.

If the upstream `function_index.json` (resolved through the T-027 runtime query index pack) is missing or insufficient, T-028 must produce a **corrected** `pxfquery-T-028` local version inside its own `4_artifact/2_persist/` directory and record lineage, source asset id, repairs performed, validation evidence, and downstream consumer guidance. T-028 must not overwrite the upstream T-021/D-004 file.

## Inputs

- A-001 T-026 loader package (D-001) — used to call `load_matrix('cp_func_ad' / 'sh_func_ad' / 'xpr_func_ad')` and read `var_names` at runtime.
- A-002 T-026 loader validation record (D-003) — JSON evidence confirming the upstream matrix var dimensions (n_var = 91). Source of the 91-row function-term list before re-reading from H5AD.
- A-003 T-026 loader validation summary (D-004) — Markdown cross-reference for matrix schemas.
- A-004 T-027 runtime query index pack (D-001) — symlink directory; T-028 reads `function_index.json` from here (or its canonical T-021 target) as the alias seed.
- A-005 T-027 schema report (D-002) — describes the upstream `function_index.json` top-level key shape (`{var_names, meta, aliases}`) for cross-reference.
- A-006 T-021 standard resources bundle (D-004) — canonical read-only source. The `function_index.json` actually consumed is here; it is also symlinked by T-027.
- A-007 T-013 MVP capability contract (D-001) — explicit gap evidence: legacy `function_index.json` is missing or incomplete.
- A-008 T-013 failure / missing capability list (D-005) — official predecessor gap record.
- A-009 T-013 MVP run-through review report (D-006) — Chinese HTML context for the function-index gap.

## Steps

### Step 1 — Verify the 91-term matrix var source

Use the T-026 loader (A-001) to read `cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad` from the T-021 bundle (A-006) and cross-check `var_names`. Confirm:

- `len(var_names) == 91` for all three matrices.
- The three `var_names` lists are identical (same 91 terms, same order) so a single function index can serve all matrices.

Do **not** hard-code the 91 terms in source code. They must be read from the H5AD files via `anndata.read_h5ad` and the T-026 loader. Write the observed `var_names` to `3_execution/01_var_names.json` as evidence.

### Step 2 — Read upstream function_index.json (when present)

Resolve `function_index.json` through the T-027 runtime index pack (A-004) and read it with `json.load`:

- If present and well-formed (top-level keys include `var_names`, `meta`, `aliases`), capture its `aliases` mapping as the seed.
- If absent or malformed, record the gap with explicit evidence (file existence, `json.load` success/failure, key shape mismatch) and proceed using alias seeds from other legitimate sources (T-021 metadata CSV columns, T-013 evidence notes, conservative default empty list).

Write the upstream-read record to `3_execution/02_upstream_function_index.json`.

### Step 3 — Build pxfquery-T-028 function index pack

Construct `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` with structure:

```json
{
  "version": "pxfquery-T-028",
  "matrix_source": "T-021 standard_resources bundle (D-004)",
  "loader_source": "pxfquery-T-026 matrix loader",
  "n_functions": 91,
  "var_names": [...91 strings...],
  "aliases": {"function_term": ["alias1", "alias2", ...], ...},
  "meta": {
    "built_on": "YYYY-MM-DD",
    "upstream_function_index_status": "present|missing|partial",
    "alias_seed_sources": [...],
    "notes": "..."
  }
}
```

Rules:

- `var_names` MUST be exactly the loader-observed 91 matrix var terms in their original order.
- For every term, `aliases[term]` must be a non-null list. Each term MUST include itself as its primary entry. Additional aliases are accepted from the upstream file when present, or are explicitly empty when absent — never silently dropped.
- Do not invent or guess aliases beyond what the upstream file or accepted metadata sources provide; missing aliases are recorded as empty lists and reported in the validation table.
- Persist the file at `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json`. The directory is the task-versioned pack; the JSON inside is the core artifact.

### Step 4 — Build machine-readable validation table

Produce `3_execution/03_validation.csv` (also exposed as `4_artifact/5_table/pxfquery_t028_function_index_validation.csv`) with one row per function term:

```
function_term, var_index, in_matrix_var_names, alias_count, aliases_json, status
```

- `status ∈ {OK, ALIASES_MISSING_UPSTREAM, MATRIX_VAR_MISMATCH}`. When `status != OK`, the row is included explicitly with a short reason in `5_report/validation_notes.md`.
- The table MUST cover all 91 terms; do not silently skip any.

### Step 5 — Validate pack loads & is consistent

Run a Python validation script (`3_execution/validate_function_index.py`) inside the `pxfquery` conda environment using `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python …`:

1. Open the T-026 loader (A-001) and read all three matrices to confirm `var_names`.
2. Open the upstream `function_index.json` and capture its status (present/missing/partial).
3. Open the T-028 pack JSON and verify:
   - top-level keys present and JSON is well-formed;
   - `n_functions == 91`;
   - every term in `var_names` is present;
   - `set(var_names) == set(observed_matrix_var_names)`;
   - `aliases` covers every term (key present, value is a list, list contains the term itself).
4. Write structured evidence to `3_execution/03_validation.json` with per-check pass/fail and any mismatches.
5. Write a short readable summary to `3_execution/03_validation_summary.md`.

The validation script is mandatory; file-existence checks alone are insufficient.

### Step 6 — Write downstream usage notes

Produce `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md` (and a Chinese variant `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md`) explaining:

- What the pack contains and what changed vs. upstream.
- Why it is a corrected local version (if any repair was needed).
- How query/resolver tasks should `json.load` it, iterate over `var_names`, and look up aliases by term.
- Which downstream task(s) should consume it (the next-readiness query/resolver tasks in this DAG).

### Step 7 — Register artifacts & write completion

- Register every deliverable in `4_artifact/registry.yaml`. The T-028 function index JSON is the core artifact (`core: true`, `lineage_anchor: true`, `stars: 5`).
- Write `5_report/completion.md` summarizing: 91 terms loaded, alias coverage, missing alias terms, repairs performed (if any), validation pass/fail, downstream consumer guidance.
- Write `5_report/repair_log.md` **only if** a repair was performed (upstream `function_index.json` missing or partial) — record: source asset id, changed files, validation evidence, downstream consumer of the repaired version.
- Per CyHex §3.3.4, generate required Chinese HTML reports (execution + result) into `4_artifact/3_document/`. Use `task_function_index_pack_v1` and date in filenames; register them with `stars: 5`.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- T-028 may read an upstream `function_index.json` (T-021/D-004 via T-027 symlinks) and emit `pxfquery-T-028` as a corrected local version when the upstream is missing or partial.
- Do not overwrite the T-021/D-004 bundle or its `function_index.json` in place. Always emit the corrected version under `4_artifact/2_persist/pxfquery_T028_function_index/`.
- Repairs must stay inside this task boundary. Record lineage, validation evidence, and downstream consumption guidance.

### Loader Discipline

- The function index MUST derive its 91 terms from the T-026 loader via `anndata.read_h5ad` on the actual H5AD files. No hard-coded term lists in source code.
- All loads are by reference to the T-021 bundle. Do **not** byte-copy the upstream `function_index.json` into the new pack — when the upstream is present, parse and re-emit it; when absent, emit a synthesized structure with explicit notes.

### Acceptance Discipline

- Every alias gap must be visible in the validation table (no silent omissions).
- The validation script must run inside the `pxfquery` conda environment.
- A failure of the 91-term check is a hard stop for the task; it must be reported as `config_mismatch` or via `stage_incident` + `5_report/incident.md`, not silently corrected by guessing.

## Deliverables

1. `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` — the 91-function index pack (core, T-028/D-001).
2. `3_execution/01_var_names.json` — observed `var_names` evidence (T-028/D-002).
3. `3_execution/02_upstream_function_index.json` — upstream-read record (T-028/D-003).
4. `3_execution/validate_function_index.py` — validation driver (T-028/D-004).
5. `3_execution/03_validation.json` — machine-readable run-time validation record (T-028/D-005).
6. `3_execution/03_validation_summary.md` — short readable validation summary (T-028/D-006).
7. `4_artifact/5_table/pxfquery_t028_function_index_validation.csv` — per-term validation table (T-028/D-007).
8. `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md` — English usage notes (T-028/D-008).
9. `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md` — Chinese usage notes (T-028/D-009).
10. `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex-mandatory execution report (T-028/D-010, `stars: 5`).
11. `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex-mandatory result report (T-028/D-011, `stars: 5`).
12. `4_artifact/registry.yaml` — T-028 deliverable registry.
13. `5_report/completion.md` — completion report.
14. `5_report/repair_log.md` — written **only if** the upstream `function_index.json` needed repair.
15. `5_report/validation_notes.md` — explicit notes on validation findings, especially any alias gaps or matrix-var mismatches.

## Acceptance

- The T-028 `function_index.json` contains exactly the 91 function terms that the T-026 loader actually observes in the three upstream H5AD matrices (`cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`); i.e. `set(var_names) == set(loader.var_names)` for each matrix.
- `n_functions == 91` and every term has a non-null `aliases[term]` list that contains the term itself.
- The validation table lists exactly 91 rows, one per term, with explicit `status` per row.
- The validation script (`validate_function_index.py`) actually opens the H5AD files and the JSON, not just file paths.
- When the upstream `function_index.json` is missing or partial, T-028 emits a corrected local version under `4_artifact/2_persist/pxfquery_T028_function_index/` and writes `5_report/repair_log.md` documenting source asset id, changed files, validation evidence, and downstream consumer.
- The Chinese HTML execution and result reports exist and contain the 91-term validation evidence and alias coverage summary.
- T-023 is **not** required for this v1 task; T-026 + T-027 + T-013 evidence are sufficient sources.
# Protocol: reverse_stability_guard_v1

## Objective

Add a numerical stability guard to the PxFquery reverse query path so that abnormal inputs — zero-norm rows, zero-norm target vectors, NaN/Inf in score rows, fully-empty matrices after cell-line filtering, and unmatched terms — are handled explicitly and never silently corrupt the ranked candidate output. Produce a task-versioned `pxfquery-T-032` package (built on top of the T-024 / pxfquery-T-024 workspace), with an automated stability demo, a normal positive control against T-021/D-004, and visible ranking-sanity evidence so that downstream tasks and humans can trust reverse-query results without re-auditing every cosine call.

## Inputs

- A-001: T-024 workspace package (pxfquery-T-024) — current editable install of pxfquery with `query/reverse.py` (ReverseQuery, ReverseResult), `query/forward.py`, `query/resolver.py`, `data/loader.py` (DataLoader), `core.PxFquery`, and the utility functions `fuzzy_match`, `build_target_vector`, `cosine_similarity_matrix` in `utils.py`. T-032 reads these modules to identify the zero-norm / abnormal-similarity code paths and to install the final repaired workspace as `pxfquery-T-032`.
- A-002: T-026 loader outputs (pxfquery-T-026) — loader package (`load_bundle`, `load_matrix`) and `loader_validation.json` reporting observed matrix shapes, obs columns, and dtypes for 19/19 files. Used at the start of the stability demo to confirm runtime schema before injecting abnormal inputs.
- A-003: T-021 standard resources bundle (D-004) — canonical 19-file float32 H5AD matrices (cp/sh/xpr), JSON indexes, CSV metadata. The actual data for both the positive-control reverse query (apoptosis activate / MYC suppress) and the stability scenarios. Loaded by reference, never copied.
- A-004: T-013 MVP capability review deliverables — capability status matrix (D-003) and failure/missing capability list (D-005). Documents the warning evidence that motivates this guard: `cosine_similarity_matrix` silently fills zero denominators with `1e-10`, which produces arbitrarily large similarity values for zero-norm rows or zero-activation targets and corrupts reverse-query ranking.
- A-005: Current project protocol — pxfquery conda env, workspace boundaries, legacy-source non-modification rules, and the hard rule that any ranked output be saved as a runnable artifact (not a placeholder).

## Steps

1. Read A-001 (`utils.py`, `query/reverse.py`, `core.py`, `data/loader.py`) and audit each function for numerical-stability risk paths: zero-norm row in `cosine_similarity_matrix`, zero-norm target vector (`build_target_vector` returning an all-zero array when no terms fuzzy-match), unmatched terms, NaN/Inf in row data (which can appear after upstream slicing), and the empty-after-aggregation branch.
2. Read A-002's `loader_validation.json` (or completion report) to confirm matrix shapes, obs columns (`pert_id`, `cmap_name`, `cell_iname`), functional term var_names, and dtype (`float32`). Identify which bundle path contains `cp_func_ad.h5ad` (preferred data source for both control and stability scenarios).
3. Build a repaired workspace copy at `3_execution/pxfquery_T-032_repaired/` that mirrors T-024's src/-layout but adds a stability guard layer. Register this copy as a task-versioned PxFquery asset named `pxfquery-T-032`. Required changes inside the repaired copy only:
   - Replace `utils.cosine_similarity_matrix` with a guarded version that emits a `(severity, scenario, message, indices)` warning per guarded event: zero-norm row, zero-norm target, NaN row, Inf row; rows involved in a guarded case get similarity = `0.0` (and are excluded from ranking) rather than `inf`/`-inf`/`nan`.
   - Extend `utils.build_target_vector` to return `(vector, matched_terms, unmatched_terms)` so the caller can distinguish "no activation terms were fuzzy-matched" from "user requested zero activation". If matched is empty, emit a `target_empty` warning and the caller short-circuits with the standard "not found" path instead of returning NaN/Inf.
   - Add a `GuardEvent` dataclass (or equivalent) and a `GuardReport` aggregator on `ReverseResult`, exposing `.warnings` as a list of dicts so the stability demo and downstream consumers can serialize them.
   - Ensure backward compatibility: any non-abnormal input must produce identical similarity values within floating-point tolerance (no ranking regression).
4. Install the repaired workspace as editable (`pip install -e .`) into the `pxfquery` conda env. Verify the installation via `python -c "import pxfquery; print(pxfquery.__file__)"` resolves to the `3_execution/pxfquery_T-032_repaired/` copy.
5. Implement `3_execution/run_stability_guard.py` that executes both required scenarios in one run, all inside `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`:
   - **Scenario A — Normal positive control**: load `cp_func_ad.h5ad` from the A-003 bundle, run `func2pert(activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="MCF7", top_k=20)`, assert all top-K similarities are finite values within `[-1.0, 1.0]` and that the guard report contains zero "zero_norm_row" / "zero_norm_target" / "nan_row" / "inf_row" warnings for this run. Serialize candidates to `pxfquery_T-032_positive_control_candidates.json` and metadata to `pxfquery_T-032_positive_control_meta.json` under `4_artifact/2_persist/`.
   - **Scenario B — Abnormal-similarity guard**: construct a synthetic ReverseQuery (or `PxFquery` instance) over a small matrix that contains (i) an all-zero row, (ii) a NaN row, (iii) an Inf row, (iv) a target activation list that fuzzy-matches to nothing, and (v) a near-empty matrix slice where every row has norm 0. For each sub-case assert that the guard fires the expected warning and that the surviving ranked candidates (if any) contain only finite values in `[-1, 1]`. Serialize the aggregated warnings to `pxfquery_T-032_guard_warnings.json` under `4_artifact/2_persist/`.
6. Write a machine-readable validation record `3_execution/stability_guard_validation.json` capturing: exact command executed, conda env, python version, key package versions, repaired workspace path, scenario inventory, per-scenario expected vs actual (guard warned?, similarity clipped?, ranking preserved?, NaN/Inf counts), and summary pass/fail flags.
7. Write Chinese HTML reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — step-by-step record of guard implementation, scenarios, and outcomes.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — human-readable summary of guard semantics, positive-control top-K ranking, and ranking-sanity evidence.
8. If any repaired code was needed, write `5_report/repair_log.md` describing the source asset (T-024), changed files (inside the `pxfquery-T-032` copy), what was fixed (e.g. zero-denominator fill, unmatched-target no-op, NaN/Inf clipping), validation evidence, and which downstream task should consume the corrected version.
9. Write `5_report/completion.md` summarizing guard behavior, repaired issues, positive-control evidence, and downstream consumption guidance for any follow-up task that depends on stable reverse-query output.
10. Register outputs via `4_artifact/registry.yaml`.

### Required Bug-Repair Handling

- If a bug (e.g. silent division-by-zero, unhandled NaN/Inf, aggregation masking zero rows) prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, named `pxfquery-T-032`.
- Record what was fixed, the source asset or task id, changed files, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task reads `pxfquery-T-024` and emits `pxfquery-T-032` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. Do not modify A-001 (`pxfquery-T-024`), A-002 (`pxfquery-T-026`), A-003 (`T-021/D-004`), or A-004 (`T-013`) in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary. Preserve lineage, validation evidence, and downstream consumption guidance.

### Guard Semantics

- Guard behavior must NEVER corrupt the normal ranking. For any row with non-zero norm and a non-zero target, the similarity returned by the repaired `cosine_similarity_matrix` must equal the legacy cosine within `1e-12` relative tolerance.
- Every guarded event (zero-norm row, zero-norm target, NaN row, Inf row, unmatched-only target) must emit a structured `GuardEvent` warning that is observable to the caller and persisted in JSON. Silent epsilon fills are not acceptable evidence paths.
- Guarded rows must be excluded from the ranked candidate output (similarity → 0, dropped) rather than allowed to dominate the top-K with `inf` / `-inf` / `nan`.
- The positive control must run on the same data, the same env, and the same query as T-030 to make no-regression verifiable by direct comparison.

### Execution Discipline

- All Python execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- The repaired `pxfquery-T-032` workspace must be installed as editable (`pip install -e .`) in the pxfquery conda env before running either scenario.
- Do not copy T-021/D-004 matrix bytes into this task; load by reference through A-001's `DataLoader` / `core.PxFquery` or A-002's `load_matrix`.
- Do not hard-code matrix shapes, column names, function term names, or file paths from planning notes — discover them at runtime.
- The demo must actually run and produce non-empty artifacts; the stability demo and the positive control must each yield at least one serializable structured output. File existence alone is not acceptable.
- Synthetic abnormal inputs must be built inside this task's `3_execution/`. Do not write or rely on a mutated copy of the upstream H5AD files.

## Deliverables

- `3_execution/run_stability_guard.py` — stability guard demo + positive-control script.
- `3_execution/stability_guard_validation.json` — machine-readable validation record with per-scenario pass/fail.
- `3_execution/pxfquery_T-032_repaired/` — repaired workspace copy (`pxfquery-T-032`) implementing the guard; editable install target for the demo.
- `4_artifact/2_persist/pxfquery_T-032_guard_warnings.json` — structured guard warnings emitted by the abnormal-similarity scenarios.
- `4_artifact/2_persist/pxfquery_T-032_positive_control_candidates.json` — ranked candidate output (rank, cmap_name, cell_iname, similarity, driving_terms) for the normal reverse query.
- `4_artifact/2_persist/pxfquery_T-032_positive_control_meta.json` — query metadata (activate, suppress, cell_line, note, guard_warning_count).
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — T-032 artifact registry.
- `5_report/completion.md` — completion report.
- `5_report/repair_log.md` — only if a `pxfquery-T-024` workspace bug was repaired inside this task.

## Acceptance

- Abnormal similarity cases are handled explicitly: every injected zero-norm row, NaN row, Inf row, and unmatched-only target produces the expected guard warning in `pxfquery_T-032_guard_warnings.json`, and no guarded value leaks into the top-K of any scenario.
- Normal reverse query still returns ranked candidates: the positive-control candidates JSON contains ≥ 1 ranked row, all similarities are finite within `[-1.0, 1.0]`, automobile cell-line and apoptosis/MYC terms are honored, and the guard report shows zero abnormal-similarity warnings for this run.
- The repaired `pxfquery-T-032` workspace is installed as editable and demonstrably imports from its own path, with lineage back to `pxfquery-T-024` recorded in `repair_log.md` when repair happened.
- Validation JSON is non-empty, captures the exact run parameters, and explicitly asserts each scenario outcome.

## Notes

- T-030 reverse-query engine output is consumed transitively via A-001 (the `pxfquery-T-024` ReverseQuery/ReverseResult classes) and A-003 (the standard resources bundle). T-030 itself does not produce required artifacts for T-032; T-032 generates the stability evidence directly from `pxfquery-T-024` plus its own repaired copy.
- T-013 review (A-004) is the warning evidence source. If T-013's gap list is updated in the future, T-032's scenario set should be re-audited; for now the scenarios listed in step 5 cover the failures documented by T-013.
- Downstream task T-033 (or equivalent) that depends on stable reverse-query ranking should consume `pxfquery-T-032` (the edited repaired workspace), not the upstream `pxfquery-T-024`.

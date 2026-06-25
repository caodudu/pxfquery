# Protocol: no_hit_guard_v1

## Objective
Create a `pxfquery-T-031` no-hit safety guard in `ForwardQuery` so that unsupported perturbations return explicit NOT_FOUND behavior instead of false-positive fuzzy matches. Deliver the guard patch, a negative no-hit test, a positive-control forward query re-run, and NOT_FOUND evidence.

## Inputs
- **A-001**: Current project protocol — pxfquery conda environment and workspace boundary rules.
- **A-002**: T-029 sibling deliverable bundle — `3_execution/forward_engine.py`, result tables, and not-found JSON evidence. Used as the positive-control baseline plus the existing engine script template for the patch.
- **A-003**: T-024 pxfquery workspace package — `ForwardQuery`, `ForwardResult`, `DataLoader` and full package tree. Target of the guard patch; read-only upstream artifact that serves as the source for the local corrected copy.
- **A-004**: T-026 matrix loader package — `load_matrix()`, `load_bundle()`, `load_index()`, `load_metadata()` from `4_artifact/2_persist/loader/`. Required to open the A-005 bundle for guard validation tests.
- **A-005**: T-021 standard_resources bundle (D-004) — `xpr_func_ad.h5ad` float32 functional matrix with `cmap_name`/`pert_id`/`cell_iname` obs columns. Primary data source for positive-control and no-hit tests.
- **A-006**: T-013 MVP capability contract (D-001) — Defines CAP-05 as required MVP behavior: unsupported perturbations must return safely.
- **A-007**: T-013 failure/missing capability list (D-005) — Documents CAP-05 fail: "当前 fuzzy fallback 对无意义扰动名仍会给出相近 token，存在误报风险" and assigns next action to this guard.

## Steps
1. Read A-003 (T-024 workspace `ForwardQuery`) to locate the perturbation resolution path and fuzzy-match fallback logic. Identify where near-token false positives originate.
2. Read A-002 (T-029 forward engine script `3_execution/forward_engine.py`) as the baseline positive-control script template.
3. Read A-006 and A-007 (T-013 capability contract and failure list) to confirm the exact CAP-05 requirement: unsupported perturbations must return `found=False` with a clear not-found message rather than silently matching a near-token gene.
4. Reproduce the false-positive evidence: run a fuzzy fallback test with a nonsense perturbation (e.g. `NONSENSE_ZZZ999`) against the A-005 matrix via A-004 loader and the T-024 ForwardQuery, capturing the current erroneous near-token match.
5. Implement the no-hit guard in a local corrected copy at `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` (or a minimal patch script that wraps ForwardQuery with the guard, or a patched version of the ForwardQuery class). The guard must:
   - Accept a similarity threshold or an explicit allowlist mode for perturbation matching.
   - When no perturbation match meets the required threshold, return `ForwardResult.found=False` with a clear NOT_FOUND message and no activated/suppressed terms.
   - When a perturbation match meets the threshold, proceed with the normal forward query path.
   - Not alter the behavior of the legacy `ForwardQuery` class in-place; the patched version must be locally versioned as `pxfquery-T-031`.
6. Write a negative no-hit test script at `3_execution/test_no_hit_guard.py` that:
   - Imports the T-031 patched forward query guard and the T-026 loader.
   - Runs `NONSENSE_ZZZ999/A549` through the guard and asserts `found=False`.
   - Runs at least two additional nonsense perturbation names through the guard and asserts `found=False` for each.
   - Writes evidence to `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json`.
7. Write a positive-control re-run at `3_execution/test_positive_control.py` that:
   - Imports the T-031 patched guard and the T-026 loader.
   - Runs `EGFR/A549/xpr` through the guard and asserts `found=True` with at least one activated term.
   - Writes evidence to `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json`.
8. Produce CyHex-mandatory reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese HTML step-by-step execution report.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese HTML result report.
9. Write `4_artifact/registry.yaml` registering all T-031 deliverables.
10. Write `5_report/completion.md` summarizing guard implementation and test outcomes.

### Required Bug-Repair Handling
- If the guard finds that ForwardQuery's fuzzy-match code is structurally blocking any patch approach, repair the blocking code within this task scope by producing a corrected local copy (`pxfquery_T031_<component>_repaired.py`).
- Record what was fixed, the source asset id (A-003), changed files, validation evidence, and which downstream task should consume the repaired version in `5_report/repair_log.md`.
- The guard itself is a scoped local correction; do not modify T-024 workspace files in place.

## Constraints

### Scoped Repair And Versioning
- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task reads upstream T-024 ForwardQuery and emits `pxfquery-T-031` as a corrected local guard.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Guard Discipline
- The guard must target only perturbation matching false positives (CAP-05). It is not responsible for resolver issues, NL layer blocking, function_index gaps, or index naming (those are separate issues documented in T-013).
- The guard must not break the deterministic forward query path: known perturbations (EGFR, TP53) must still return found=True with functional terms.
- The guard threshold or allowlist must be tunable in the guard script so downstream tasks can calibrate it.
- The guard must be importable as a Python module in the pxfquery conda environment.
- The guard must write explicit NOT_FOUND evidence for each no-hit query, not just an empty table.

## Deliverables
- `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` — The no-hit guard module.
- `4_artifact/2_persist/pxfquery_T031_<_component_>_repaired.py` — Present only if repair was required.
- `3_execution/test_no_hit_guard.py` — Negative no-hit test script.
- `3_execution/test_positive_control.py` — Positive-control re-run script.
- `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json` — No-hit test evidence.
- `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json` — Positive-control evidence.
- `4_artifact/5_table/pxfquery_T031_false_positive_reproduced.json` — Reproduced false-positive evidence.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex execution report (Chinese).
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex result report (Chinese).
- `4_artifact/registry.yaml` — T-031 deliverable registry.
- `5_report/completion.md` — Completion report.
- `5_report/repair_log.md` — Repair log if guard implementation required patching blocking upstream code.

## Acceptance
- `test_no_hit_guard.py` runs and produces `found=False` for at least three nonsense perturbation names.
- `test_positive_control.py` runs and produces `found=True` with functional terms for EGFR/A549/xpr.
- No-hit evidence JSON contains explicit `NOT_FOUND` status per query, not empty tables.
- Positive-control evidence JSON shows at least one activated and one suppressed term.
- All Python execution uses the pxfquery conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- The guard patch is versioned as `pxfquery-T-031` and T-024 workspace files remain unmodified.
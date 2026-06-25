# Protocol: demo_cli_v1

## Objective
Create `pxfquery-T-036`, a user-facing demo CLI/script that produces readable deterministic forward, reverse, and no-hit outputs from already validated milestone evidence. This task should not require optional resolver or LLM success.

## Inputs
- **A-001**: T-029 forward query artifacts. Required source for forward demo outputs and validation JSON.
- **A-002**: T-035 smoke test artifacts. Required integration evidence showing which upstream paths are runnable. T-035 records T-030 as `UNMET_DEPENDENCY`, so T-036 must not hard-depend on T-030 artifacts.
- **A-003**: T-031 no-hit guard artifacts. Required source for user-visible no-hit/negative demo output.
- **A-004**: T-032 reverse stability artifacts. Required source for reverse positive-control candidates and guard warning examples.
- **A-005**: T-032 reverse stability execution. Required validation JSON and repaired package path for reverse demo fallback.
- **A-006**: T-030 reverse query task record. Optional lineage reference only; visible artifact registry is empty.
- **A-007**: Current project protocol. Runtime and boundary rules.

## Steps
1. Verify required assets resolve and are non-empty: T-029 validation/result tables, T-035 smoke results, T-031 no-hit evidence, T-032 positive-control/reverse stability evidence.
2. Implement `3_execution/pxfquery_demo_cli.py`, a lightweight demo CLI with deterministic modes:
   - `forward`: read and display T-029 EGFR/A549 output in a readable table/JSON.
   - `reverse`: read and display T-032 positive-control reverse candidates and metadata.
   - `no-hit`: read and display T-031 no-hit evidence showing guarded negative behavior.
   - `all`: run all three modes and write consolidated demo output.
3. Run the demo CLI in the `pxfquery` conda environment:
   `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/pxfquery_demo_cli.py all`.
4. Write outputs:
   - `4_artifact/5_table/pxfquery_T036_forward_demo.json`
   - `4_artifact/5_table/pxfquery_T036_reverse_demo.json`
   - `4_artifact/5_table/pxfquery_T036_no_hit_demo.json`
   - `4_artifact/5_table/pxfquery_T036_demo_summary.json`
   - `4_artifact/2_persist/pxfquery_demo_cli.py`
   - `4_artifact/2_persist/pxfquery_T036_usage.md`
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html`
   - `4_artifact/3_document/result_report_vYYYYMMDD.html`
   - `4_artifact/registry.yaml`
   - `5_report/completion.md`
5. If a scoped integration issue prevents a runnable demo, repair only inside T-036 outputs and document in `5_report/repair_log.md`.

### Required Bug-Repair Handling
- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-036`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints
- Do not modify upstream completed artifacts in T-029/T-031/T-032/T-035.
- Do not require T-030 artifact content; T-030 is a lineage reference only because T-035 recorded its executable reverse demo as unmet.
- Do not require T-033 resolver output or any LLM adapter output.
- All Python execution must use the `pxfquery` conda environment.
- The demo should use lightweight JSON/CSV evidence already produced by upstream tasks; do not load large H5AD matrices.

## Deliverables
- `3_execution/pxfquery_demo_cli.py` — runnable demo CLI/script.
- `4_artifact/2_persist/pxfquery_demo_cli.py` — registered reusable copy.
- `4_artifact/2_persist/pxfquery_T036_usage.md` — usage notes.
- `4_artifact/5_table/pxfquery_T036_forward_demo.json` — readable forward demo output.
- `4_artifact/5_table/pxfquery_T036_reverse_demo.json` — readable reverse demo output.
- `4_artifact/5_table/pxfquery_T036_no_hit_demo.json` — readable no-hit demo output.
- `4_artifact/5_table/pxfquery_T036_demo_summary.json` — consolidated demo evidence.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — result report.
- `4_artifact/registry.yaml` — deliverable registry.
- `5_report/completion.md` — completion report.

## Acceptance
- Demo CLI runs locally in the `pxfquery` conda environment.
- Demo writes visible, readable forward, reverse, and no-hit outputs.
- Demo does not require optional LLM/resolver success.
- Demo does not fail because T-030 direct artifacts are absent; it uses T-032 reverse evidence for the reverse user demo.
- Output includes actual command results and files, not just file-existence claims.

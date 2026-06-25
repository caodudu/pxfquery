I’ll execute T-060 inside the task-local boundaries only. I’ll first turn the approved plan into a concrete checklist and inspect just the registered assets needed to derive the contract, fixture gap, and loader shape.
Step list for execution: extract the contract into `3_execution`, verify the registered input gap, create the repair substrate, implement the reverse core, run evidence commands in the `pxfquery` conda env, then register and report the outputs. I’m starting with only the selected asset links under this task.
The T-042 reverse contract is clear: `func2pert` must return `found`, `activate`, `suppress`, `cell_line`, `candidate_columns`, `top_candidates`, `warnings`, and `note`; no-hit/error variants must be JSON objects rather than tracebacks. I’m now checking the registered fixture and loader shape before creating any task-local outputs.
The selected fixture package has the expected three h5ad matrices and sidecar index files, and the accepted loader resolves a manifest-adjacent `fixture_package_m1` unless a root is provided. I’ll use that behavior for compatibility by making the repair fixture load through the same filenames and loader semantics.
The package skeleton is only a stub, so this task needs a complete task-local package implementation rather than a small patch. Before editing, I’m probing the actual fixture matrix fields with the approved conda runtime so the repair substrate matches the loader’s real objects.
T-049’s incident confirms the prior block was missing usable fixture/manifest coverage and the required `HALLMARK_MYC_TARGETS_V1`. In this task, A-004 is present and loadable, but A-011 confirms the original fixture has only seven function vars and lacks MYC V1, so the repair substrate is justified.
The conda probe is slower than a plain file read because it imports AnnData and opens h5ad files. I’m waiting for that result rather than guessing matrix orientation; the reverse scoring depends on whether cell context is in `obs` metadata or matrix columns.
The h5ad probe confirms the repair needs two additions: the original xpr fixture has no A549 rows and no `HALLMARK_MYC_TARGETS_V1`. I’m going to create a task-local M1.1 fixture by copying the registered fixture files, then adding clearly synthetic A549 reverse-demo rows and target columns in the task output only.
I’ve staged the task-local package copy under `4_artifact/1_package/pxfquery` and copied the accepted loader implementation into it. Next I’m adding the contract checklist, repair-fixture generator, and reverse-query implementation.
The repair generator is now task-local and records the synthetic provenance in both the manifest and matrix metadata. I’m replacing the stub package with a deterministic M1 implementation that handles direct h5ad loading and loader-compatible fixture access.
The package currently exposes only `PxFquery`, so I’m keeping that entry point and adding the reverse implementation behind it plus a small CLI module for reproducible evidence commands.
The first patch targeted paths relative to the project root instead of the task root, so it did not change files. I’m reapplying the same scoped edits with absolute task paths.
The reverse core now uses deterministic cosine similarity over requested activate/suppress terms and stable tie-breaking by similarity, candidate name, cell line, and signature ID. I’m generating the repair fixture next and then I’ll run the validation commands.
The generation and compile checks are running in the configured conda env. If the loader-compatible fixture writes cleanly, I’ll immediately run the positive demo twice to confirm stable ranking before writing evidence files.
The fixture generator landed in the project root by path mistake, and the conda command correctly failed because the task-local script was absent. I’m cleaning up only that accidental file I created, then placing the same script under the task’s allowed `3_execution/` directory.
The accidental root-level files are moved into the task-local execution directory and the temporary root directory is removed. I’m rerunning generation and compile/import checks now.
Generation is still running, likely writing h5ad files. I’m letting it finish and will verify the resulting manifest and matrix summary before using it for demos.
The repair fixture generation and compile step passed; the import failed because the skeleton `query/__init__.py` still imports placeholder classes that were replaced. I’m patching package init files to expose the new functions cleanly.
The generated summary shows the repair xpr matrix now has 15 rows, A549 support, `HALLMARK_MYC_TARGETS_V1`, and the low-confidence control term. I’m making the query package exports explicit, including reverse, then rerunning import validation.
The package exports are patched. I’m running import/compile again plus the positive reverse query through the task-local matrix before writing the formal evidence bundle.
The compile/import command exited cleanly, but the heredoc did not return visible stdout through `conda run`. I’m switching the evidence commands to checked `python -c`/script files so the JSON artifacts are written to disk and visible.
The evidence runner now checks loader compatibility, positive demo assertions, repeatability, and no-hit/error variants in one reproducible command. I’m running it in the conda environment and saving the JSON/CSV artifacts.
The validation command is still running; it is loading the repair h5ad matrices through the accepted loader and then writing evidence files. I’ll inspect the evidence immediately after it exits.
The evidence runner failed before writing deliverables because the positive result was not a `found` object. I’m inspecting that result directly, then I’ll adjust the repair scores if the target vector is being classified as low confidence or a structured error.
The failure came from importing an installed/older `pxfquery` implementation instead of this task’s package. I’m rerunning with `conda run ... env PYTHONPATH=<task package>` so Python resolves T-060 code first, and I’ll record that exact command in the evidence.
The task-local `core.py` still contained the forward-repair stub from the copied skeleton, including a hardcoded T-059 `func2pert` response. I’m patching that file in place to call the T-060 reverse implementation and to keep manifest/fixture loading support.
The hardcoded reverse stub is removed. I’m rerunning compile, a direct positive demo inspection, and then the full evidence runner with the corrected task-local import path.
The full evidence run is active now. It should either produce the demo/error JSON and ranking CSV or fail on a concrete assertion, which I’ll preserve if it happens.
Positive demo and most no-hit cases passed far enough to reach the low-confidence assertion. The low-confidence term is a one-dimensional query, so cosine is 1.0 by definition; I’m adjusting the implementation to classify low confidence by raw candidate signal magnitude as well as cosine magnitude.
Low-confidence detection now records both `max_abs_similarity` and `max_signal_norm`, avoiding the one-dimensional cosine edge case. I’m rerunning the evidence command.
The rerun is underway. If it passes, the next work is only documentation and registry writing.
The evidence runner passed and produced the required positive demo, structured no-hit/error JSON, and ranking CSV. I’m tightening the recorded reproduction command to match the actual `conda run env PYTHONPATH=...` invocation, then I’ll write provenance, reports, registry, and completion.
The evidence script now records the same conda/PYTHONPATH pattern used in validation. I’m rerunning it once to refresh the JSON files, then I’ll run a CLI smoke check.
The refreshed evidence plus CLI smoke command is running. After this I only need to serialize the reports and registry.
The API evidence refreshed, but CLI smoke exposed another copied skeleton issue: `python -m pxfquery.cli` is still resolving the old forward-only CLI entry. I’m inspecting the CLI package and patching the package-level entrypoint to include reverse.
The module entrypoint imports `pxfquery.cli.__init__.main`, and that file still had the forward-only CLI from the skeleton. I’m replacing that package-level `main` with the same reverse-capable parser.
The CLI package-level parser now includes `reverse`. I’m rerunning the CLI smoke and keeping stdout under `3_execution/` as auxiliary evidence.
The CLI smoke is running with the task package on PYTHONPATH. After that, I’ll write the final artifacts and remove generated bytecode caches from the deliverable package.
API evidence and CLI smoke both pass. I’m now writing the provenance report, HTML execution/result reports, artifact registry, and completion report with the actual commands and caveats.
Provenance and reports are written. I’m updating the artifact registry and completion report now, then I’ll run a final file/existence and JSON sanity check.
The registry and completion report are written. I’m doing a final sanity pass now: remove bytecode caches from the deliverable package, verify required outputs exist, parse the JSON/YAML, and confirm the positive demo fields.
The final sanity command is still running under conda. It is parsing the produced JSON/YAML and checking that required deliverables are present.
The sanity command exited successfully, though the heredoc stdout was suppressed again by `conda run`. I’m running a compact `python -c` check so I have visible final confirmation to report.
Final sanity confirms the demo is `found=true`, includes `HALLMARK_MYC_TARGETS_V1`, repeatability is true, and the registry has 9 artifacts. I’m doing one last cleanup check for stale T-059 strings or bytecode caches in the delivered package.
`rg` is not installed in this shell, so I’m using `grep` for the stale-string check. No bytecode caches or accidental project-root `3_execution/` directory were found.
The only stale T-059 strings are in automatic CLI session logs under `5_report/cli_sessions`, documenting the earlier failed probe; the delivered package and reports are clean. I’m marking the execution checklist complete.
Completed T-060.

Delivered the reverse-query repair package and all required artifacts under:

- [package code](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/1_package/pxfquery)
- [repair fixture](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_fixture_m1_1)
- [repair manifest](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml)
- [positive demo JSON](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_demo_evidence_v20260624.json)
- [no-hit/error JSON](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json)
- [ranking CSV](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/5_table/reverse_ranking_evidence_v20260624.csv)
- [execution report](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/3_document/execution_report_v20260624.html)
- [result report](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/3_document/result_report_v20260624.html)

Registry updated at [registry.yaml](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/registry.yaml). Completion report written at [completion.md](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/completion.md).

Validation performed in the `pxfquery` conda env: repair fixture generation, package compile/import, accepted-loader compatibility, positive reverse demo, repeatability check, structured no-hit/error cases, and CLI reverse smoke. Final sanity check passed: `found=True`, suppress target `HALLMARK_MYC_TARGETS_V1`, repeatability `True`, 9 registry artifacts, top candidate `THTPA`.

Caveat: the repair substrate is explicitly synthetic contract-bridge support, not raw LINCS/CMAP data or biological evidence.

# Protocol: milestone_package_core_parallel_v1

## Objective
Create `pxfquery-T-040`, a parallel package-core milestone branch that assembles the package workspace, loader/resource access, deterministic forward query, no-hit guard, and minimal package-core verification from completed predecessor assets. T-040 must be independent of T-038; T-039 is the only later aggregation point.

## Inputs
- A-001: T-024 pxfquery workspace package — package foundation, `src/pxfquery/` tree, workspace `pyproject.toml`, import/compile smoke evidence, and workspace summary.
- A-002: T-026 matrix/resource loader — loader package, validation script, observed resource schema records, and loader reports.
- A-003: T-029 forward query engine — deterministic forward query script, canonical/diversity result tables, not-found evidence, and validation summary.
- A-004: T-031 no-hit guard — guard module, false-positive reproduction evidence, no-hit evidence, positive-control evidence, and reports.
- A-005: Current project protocol — project boundaries, default `pxfquery` conda environment, and source-use rules.

## Steps
1. Verify A-001 through A-004 are present and readable by reading each predecessor artifact registry, completion report, and only the implementation/evidence files needed for package-core assembly. Confirm no T-038 input is read.
2. Create a T-040-local package-core artifact under `4_artifact/2_persist/pxfquery-T-040/` using A-001 as the package base.
3. Integrate the T-026 loader/resource-access component into the T-040 artifact as a package-local module or documented importable support component. Preserve resource access by reference; do not copy H5AD, JSON index, or CSV metadata bytes into T-040.
4. Integrate the deterministic forward-query path from A-003 and the no-hit safety guard from A-004 into the T-040 artifact so a downstream task can import one package-core branch without re-reading low-level predecessor tasks.
5. Write a runnable verification driver at `3_execution/05_run_verification/verify_package_core.py` that checks, at minimum: package import, Python compile, loader smoke against the standard resource location used by A-002/A-003/A-004, EGFR/A549 forward demo, and at least one no-hit negative demo.
6. Run verification in the project `pxfquery` conda environment using `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`. Record exact commands, exit statuses, stdout/stderr summaries, and output paths.
7. Write package-core evidence under `4_artifact/5_table/`, including a machine-readable test result JSON and a demo summary JSON.
8. Write `4_artifact/2_persist/pxfquery_T040_lineage.md` documenting how A-001/A-002/A-003/A-004 were assembled into T-040 and confirming that T-038 was not used.
9. Write `4_artifact/2_persist/pxfquery_T040_handoff.md` for T-039. The handoff must state what T-039 may consume from T-040 and what remains out of scope.
10. Write the artifact registry, completion report, and the two required Chinese HTML reports.

## Constraints
- T-040 has four hard predecessor deliverable inputs: T-024, T-026, T-029, and T-031.
- T-040 must not depend on, read from, or wait for T-038. T-039 is downstream aggregation only, not an input.
- Do not read or modify the archived old T-037 task.
- Do not depend on T-030, T-032, T-035, or T-036 for this branch.
- Do not modify any predecessor task directory or any project raw asset under `2_project_asset/`.
- Do not promote anything into `6_project_deliverable/`.
- Optional resolver, reverse query, natural-language, LLM, manuscript, and final-deliverable behavior are outside this branch unless already required by package-core verification.
- If a scoped integration bug blocks the package-core artifact, repair it only inside T-040, preserve the predecessor input unchanged, and document the divergence in the lineage and completion reports.

## Deliverables
- `4_artifact/2_persist/pxfquery-T-040/` — runnable package-core artifact.
- `3_execution/05_run_verification/verify_package_core.py` — verification driver for import, compile, loader smoke, forward demo, and no-hit demo.
- `4_artifact/5_table/pxfquery_T040_test_results.json` — package-core verification evidence.
- `4_artifact/5_table/pxfquery_T040_demo_summary.json` — forward/no-hit demo summary.
- `4_artifact/2_persist/pxfquery_T040_handoff.md` — package-core handoff for T-039.
- `4_artifact/2_persist/pxfquery_T040_lineage.md` — lineage from T-024/T-026/T-029/T-031 to T-040.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — artifact registry.
- `5_report/completion.md` — completion report.

## Acceptance
- `4_artifact/2_persist/pxfquery-T-040/` exists and contains an importable package-core branch assembled from A-001/A-002/A-003/A-004.
- Verification evidence includes actual commands, exit statuses, stdout/stderr summaries, and output paths.
- Import/compile checks pass for the T-040 package-core artifact, or any failure is explicitly documented with a scoped T-040 repair or blocker.
- Loader smoke opens the same resource family used by A-002/A-003/A-004 by reference, without copying matrix/index/metadata bytes.
- Forward demo returns found behavior for a supported query, and no-hit demo returns explicit not-found behavior for an unsupported query.
- Lineage and handoff documents confirm that T-040 has no dependency on T-038 and is sufficient for T-039 aggregation without re-reading low-level predecessor tasks directly.

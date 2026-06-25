# Protocol: milestone_reverse_demo_reports_v1

## Objective
Create `pxfquery-T-038`, a parallel reverse/demo/report milestone branch for T-039 aggregation. Consume only T-030, T-032, T-035, and T-036 context; do not depend on T-040 or the archived old T-037.

## Inputs
- A-001: T-030 reverse query engine task record — required lineage and configuration context. The current visible `4_artifact/registry.yaml` is empty, `5_report/completion.md` is pending, and shallow inventory found no concrete `3_execution/` or `4_artifact/` deliverable files beyond `registry.yaml`; execution must verify whether any concrete reverse-engine artifacts exist and record missing deliverables explicitly.
- A-002: T-032 reverse stability guard artifacts — usable reverse/stability package, repaired workspace, validation JSON, guard warnings, positive-control candidates, reports, registry, completion report, and repair log.
- A-003: T-035 smoke test artifacts — integration smoke evidence, including PASS evidence for T-032 and `UNMET_DEPENDENCY` evidence for T-030 at smoke time.
- A-004: T-036 demo CLI task record — required demo CLI lineage and configuration context. The current visible `4_artifact/registry.yaml` is empty, `5_report/completion.md` is pending, and shallow inventory found no concrete `3_execution/` or `4_artifact/` deliverable files beyond `registry.yaml`; execution must verify whether any concrete demo CLI artifacts exist and record missing deliverables explicitly.

## Steps
1. During config/check, verify only that the four required predecessor task roots exist and that this task's asset registration and asset rule are coherent. Do not bulk-read upstream protocols, reports, or artifacts in config.
2. During execute, inventory concrete usable files from T-030, T-032, T-035, and T-036. Mark T-030 or T-036 deliverables as missing if their registries remain empty, completion reports remain pending, or expected execution/artifact files are absent; do not infer completion from task status alone.
3. Build a T-038-local reverse/demo/report evidence package under `4_artifact/2_persist/pxfquery-T-038/` that copies or summarizes only verified predecessor evidence. Use T-032 positive-control reverse candidates and guard warnings as the stable reverse evidence when T-030 direct reverse artifacts are missing.
4. Generate machine-readable summary tables under `4_artifact/5_table/` that record predecessor status, registry state, completion state, available concrete files, missing artifacts, smoke outcomes, reverse/stability evidence, and demo-readiness notes.
5. Write T-039 handoff and lineage addenda that state exactly which upstream tasks T-038 consumed, which upstream deliverables were usable, which were missing, and why T-039 is the only aggregation point.
6. Write the CyHex execution and result reports in Chinese HTML, register T-038 artifacts in `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints
- T-038 has exactly four required predecessor contexts: T-030, T-032, T-035, and T-036.
- T-038 must not read, wait for, depend on, copy from, or summarize T-040.
- T-038 must not read, depend on, copy from, or revive the archived old T-037 task.
- T-039 is the only downstream aggregation point for this branch.
- Do not modify T-030, T-032, T-035, or T-036 in place. All derived summaries, repaired notes, or packaging must be T-038-local.
- Do not promote T-024/T-026/T-029/T-031/T-033/T-034/T-040 into T-038 as hard inputs. Mention them only when they appear inside the four required predecessor records.
- Do not treat LLM/resolver success as a completion gate.
- Do not treat empty registries, pending completion reports, or task status fields alone as usable deliverables.
- If a predecessor is marked `done` but has an empty registry, pending completion stub, or no concrete execution/artifact files, record the inconsistency as evidence instead of repairing that predecessor.
- Config must remain lightweight: it should not read large upstream outputs or recursively inspect predecessor task trees. Heavy inspection belongs to execute.

## Deliverables
- `4_artifact/2_persist/pxfquery-T-038/` — T-038 reverse/demo/report milestone evidence package.
- `4_artifact/5_table/pxfquery_T038_predecessor_inventory.json` — predecessor registry, completion, and concrete-file inventory.
- `4_artifact/5_table/pxfquery_T038_reverse_stability_results.json` — reverse/stability evidence derived from verified T-032 and T-035 files.
- `4_artifact/5_table/pxfquery_T038_demo_summary.json` — demo-readiness summary, including missing T-030/T-036 artifacts if still absent.
- `4_artifact/2_persist/pxfquery_T038_handoff_addendum.md` — handoff notes for T-039.
- `4_artifact/2_persist/pxfquery_T038_lineage_addendum.md` — lineage addendum documenting the four predecessor contexts and forbidden branches.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — T-038 artifact registry.
- `5_report/completion.md` — completion report.

## Acceptance
- The predecessor inventory names exactly T-030, T-032, T-035, and T-036 as required contexts.
- The output contains no dependency on T-040 and no use of archived old T-037.
- T-030 and T-036 empty/missing deliverable states, if unchanged at execution time, are explicitly recorded as missing rather than treated as successful inputs.
- T-032 and T-035 concrete evidence is traceably reused without modifying upstream files.
- T-039 can aggregate this branch by reading T-038 outputs without directly re-reading low-level predecessor tasks.

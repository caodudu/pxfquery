# Protocol: milestone_final_aggregation_v1

## Objective
Create `pxfquery-T-039`, the final aggregation layer for the package milestone. Consume only the parallel T-040 package-core branch and T-038 reverse/demo/report branch, verify the milestone evidence is complete, and produce the final index, acceptance summary, handoff, and promotion-ready manifest. Do not redo implementation.

## Inputs
- A-001: T-040 package core deliverables — package core, forward/no-hit tests, handoff, and lineage.
- A-002: T-038 reverse/demo/report deliverables — reverse/stability evidence, combined demo summary, reports, and addenda.

## Steps
1. Verify T-040 and T-038 are done and their registries expose the required package-core and reverse/demo/report artifacts.
2. Read only T-040/T-038 registries, completion reports, handoff files, lineage files, and final JSON summaries.
3. Build a final milestone index and acceptance summary that points to package, tests, demo evidence, reports, and known limitations.
4. Create a promotion-ready package manifest for later human delivery without copying all upstream raw artifacts.
5. Write final aggregation reports and registry.

## Constraints
- T-039 has only two hard predecessors: T-040 and T-038.
- Do not read or modify T-024/T-026/T-029/T-030/T-031/T-032/T-035/T-036 directly unless a T-040/T-038 report explicitly references a missing file needed to verify an artifact path.
- Do not implement new package code. If T-040/T-038 are incomplete, report the gap instead of patching around it.

## Deliverables
- `4_artifact/2_persist/pxfquery_T039_final_milestone_index.md`
- `4_artifact/2_persist/pxfquery_T039_acceptance_summary.md`
- `4_artifact/2_persist/pxfquery_T039_promotion_manifest.yaml`
- `4_artifact/5_table/pxfquery_T039_final_acceptance.json`
- `4_artifact/3_document/execution_report_vYYYYMMDD.html`
- `4_artifact/3_document/result_report_vYYYYMMDD.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Acceptance
- T-039 does not have more than 2 hard predecessors.
- Final acceptance JSON names every required T-040/T-038 artifact and states pass/fail.
- Final milestone index can be read without loading any upstream task beyond T-040/T-038.

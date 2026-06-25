# AI Handoff: T-060 reverse_query_core_repair_m1

## Task Goal
T-060 should replace failed T-049 by delivering a task-local synthetic/repair reverse substrate and a task-local reverse query core package that satisfies the T-042 reverse demo contract, including `HALLMARK_MYC_TARGETS_V1`, deterministic ranking, structured JSON evidence, and no-hit/error behavior.

## What Was Delivered
The task directory contains the repair fixture, manifest, provenance report, positive demo evidence JSON, no-hit/error evidence JSON, ranking CSV, and human-readable HTML reports under `4_artifact/`.

Delivery QA did not accept the task because the registered package-code artifact is not task-local package code. `4_artifact/1_package/pxfquery` is a symlink to the predecessor T-044 package skeleton outside this task, and no T-060 reverse query package source files were present inside the T-060 artifact package directory.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T-060/D-002 | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Repair fixture substrate for the reverse demo case. | Can be reused after execute revision verifies package code against it. |
| T-060/D-003 | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Manifest for loading the repair fixture. | Use with the accepted loader path during revised execution. |
| T-060/D-004 | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | States synthetic/repair provenance and non-biological-evidence caveat. | Read before reusing or extending the fixture. |
| T-060/D-005 | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Positive reverse demo evidence claimed by execution. | Re-check after task-local package code is actually delivered. |
| T-060/D-006 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Structured no-hit/error evidence claimed by execution. | Re-check after task-local package code is actually delivered. |
| T-060/D-007 | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Ranking evidence for candidate order and similarity. | Re-check deterministic ranking after execute revision. |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html`: human-readable execution summary.
- `4_artifact/3_document/result_report_v20260624.html`: human-readable result summary and caveat.
- `3_execution/`: scripts, smoke output, fixture summary, and checklist for revision audit.

## Downstream Use
Do not treat T-060 as accepted downstream input until execute revision delivers task-local package code under `4_artifact/1_package/pxfquery/` and reruns the validation evidence from that task-local package.

## Known Limits / Risks
- Current package-code registry entry points to an upstream predecessor symlink, not a self-contained T-060 package artifact.
- Existing JSON and CSV evidence may still be useful for audit, but it must be regenerated or explicitly revalidated after the package-code placement is fixed.
- The repair substrate is synthetic contract-bridge support, not raw LINCS/CMAP data or biological evidence.

## Do Not Read / Do Not Reuse
- Do not reuse `4_artifact/1_package/pxfquery` as accepted T-060 package code in its current state.
- Do not read project raw assets or T024-T040 blocked assets for this revision.
- Do not modify predecessor task artifacts to fix T-060.

## Recommended Next Reads
1. `5_report/delivery_qa.md`
2. `4_artifact/registry.yaml`
3. `5_report/completion.md`
4. `3_execution/run_reverse_evidence.py`
5. `4_artifact/2_persist/reverse_repair_provenance_v20260624.md`

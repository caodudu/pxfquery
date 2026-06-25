# Check Handoff Before Exec: T-041 legacy_source_digest_for_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1`
- Allowed write dirs: `4_artifact/`, `5_report/`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `1_asset/registration.yaml`
- Forbidden dirs: `/Users/dudu/Documents/3_Project/8_functional_query` (historical root), `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1` (T024-T040 failed route), `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1`. Also forbidden: arbitrary `2_project_asset/` scanning, completed task folders outside registered assets, legacy package source modifications.
- Required registry: `4_artifact/registry.yaml` (exists, currently empty).
- Must stop if: A-003 directory is inaccessible/unreadable; any required asset becomes missing; source map contradicts A-003 path; protocol scope drifts beyond A-003.

## Objective Restatement
Digest the migrated PxFquery package source (at the single path registered in T-007's source map) into a concise M1 reference asset: inventory the package structure, identify reusable modules/functions/patterns, flag unsafe or non-reusable legacy parts, and produce a reuse matrix + boundary YAML so downstream M1 tasks (T046, T048, T049, T052) can use digested knowledge instead of reading raw legacy source.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/T-007 development source map.md` | Authority for A-003 path and source priority | ok |
| A-002 | `1_asset/T-007 development state report.md` | Secondary context for component status/readiness | ok |
| A-003 | `1_asset/Migrated PxFquery package source` (→ `legacy_flat_asset_library_v20260614/code/pxfquery_package`) | Only legacy package-source directory to inspect | ok |
| A-004 | `1_asset/T-007 module asset status matrix.csv` | Optional cross-check for module/asset status | ok |
| A-005 | `1_asset/T-007 development gap and risk list.md` | Optional risk cross-check for unsafe components | ok |

## Execution Strategy
1. Read A-001 (source map) to confirm A-003 path and understand source priority rules.
2. Read A-003 directory tree: inventory top-level files/modules (core.py, data/, index/, query/, llm/, viz/, utils.py, logging_utils.py, stubs).
3. Read individual package files in A-003 to identify: entry points, loader API patterns, forward/reverse query logic, index access patterns, no-hit behavior.
4. Read A-005 (gap/risk list) for cross-reference on unsafe legacy parts; read A-002/A-004 if ambiguity arises.
5. Produce three deliverables:
   - `4_artifact/2_persist/legacy_source_digest_m1.md`: concise human-readable source digest.
   - `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: module/file status + reuse recommendation + downstream task mapping.
   - `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden reference boundaries.
6. Register deliverables in `4_artifact/registry.yaml`.
7. Write `5_report/completion.md` with exact A-003 path and scope confirmation.

## Conservative Execution Advice
- Start with: Read A-001 source map → confirm A-003 path is correct → list A-003 top-level contents.
- Smoke/demo command or method: `ls -R` on A-003 to verify directory structure matches expectations before detailed reading.
- Full run only after: Source map confirms A-003 is the correct and sufficient path; no ambiguity about which files belong to package source vs. unrelated files.
- Cost/time risk: Low — all reads are local filesystem. No API calls, no network, no compute-heavy processing.
- Checkpoint advice: After step 2 (inventory), confirm the structure vs. expected modules listed in the protocol. If a major module is missing, flag in digest rather than blocking.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Source digest | `4_artifact/2_persist/legacy_source_digest_m1.md` | Names concrete files/modules, gives guidance for T046/T048/T049/T052 |
| Reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv` | Distinguishes usable/risky/incomplete/forbidden entries |
| Boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml` | States downstream tasks must use T-041 outputs, not raw legacy source |
| Completion note | `5_report/completion.md` | Documents exact A-003 path inspected, confirms no broader scan |
| Registry | `4_artifact/registry.yaml` | All deliverable paths registered |

## Failure / Stop Conditions
- A-003 symlink broken or target missing → block, write `5_report/blocked.md`.
- Source map (A-001) reports a different package path than resolved A-003 → block for contradiction.
- Any attempt to read outside A-003 within legacy package tree → stop, document gap, do not expand scope.
- Artifact registry write fails due to permissions → stop and report.

## Notes For Delivery QA
- All deliverables must refer only to A-003 content; no external package scanning.
- Reuse matrix must explicitly map to downstream task IDs (T046, T048, T049, T052).
- Boundary YAML must forbid downstream tasks from reading raw legacy source directly — they must consume T-041 outputs.
- The task must NOT write any implementation code for M1.
- The completion note must affirm that `2_project_asset/` was not broadly scanned.
- Established symlinks verified: all 5 assets link to valid resolved targets. No repair needed.

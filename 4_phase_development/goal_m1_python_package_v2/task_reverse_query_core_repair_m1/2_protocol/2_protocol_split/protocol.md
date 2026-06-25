# T-060 reverse_query_core_repair_m1 — Protocol

## Objective
Create a same-layer replacement for T-049 reverse_query_core_m1. This task must repair the missing reverse-query demo substrate honestly and then deliver the M1 reverse query core that T-049 could not complete.

The execution must produce a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest supplement or contract-bridge fixture, that supports the T-042 reverse positive demo case including `HALLMARK_MYC_TARGETS_V1`. The substrate must be clearly labeled as synthetic/repair support, not as original raw LINCS data. Completed upstream task artifacts must not be modified.

## Position In Project
T-060 replaces T-049 for downstream reverse-query work. Downstream tasks should consume T-060 as the required reverse-query core deliverable and should treat T-049 only as a reference incident explaining why the previous route failed.

This is a development task, not a digestion task. It may create package code, execution evidence, and task-local repair assets, but it must not read project-level raw assets.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. |
| A-002 | T-042 | `4_artifact/2_persist/m1_demo_cases.yaml` | Authoritative forward/reverse demo cases and pass/fail assertions, including the reverse positive case. |
| A-003 | T-043 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. |
| A-004 | T-043 | `4_artifact/2_persist/fixture_package_m1/` | Original small M1 fixture package to inspect through registered task input only. |
| A-005 | T-043 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Expected resource shapes, columns, key semantics, and validation rules. |
| A-006 | T-043 | `4_artifact/5_table/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. |
| A-007 | T-044 | `4_artifact/1_package/pyproject.toml` | Canonical package metadata and editable package shape. |
| A-008 | T-044 | `4_artifact/1_package/pxfquery/` | Base package skeleton to extend with reverse-query code. |
| A-009 | T-046 | `4_artifact/1_package/pxfquery/data/m1_loader.py` | Accepted M1 fixture loader implementation that reverse code should use or remain compatible with. |
| A-010 | T-046 | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-011 | T-046 | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Loader smoke evidence and observed fixture coverage. |
| A-012 | T-045 | `4_artifact/2_persist/index_health_summary.json` | Optional context for known index shape/coverage gaps and deterministic field handling. |
| A-013 | T-047 | `4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened resource loading and index normalization. |
| A-014 | T-047 | `4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap reference to avoid rediscovering accepted loader limitations. |
| A-015 | T-049 | `5_report/completion.md` | Incident reference documenting the prior reverse-core block and missing fixture/manifest coverage. |

## Execution Steps
1. Read the T-042 contract and demo cases first. Extract the required reverse API fields, JSON shape, ranking expectations, no-hit/error behavior, and the exact positive demo requirements.
2. Read the T-043/T-046 fixture and loader assets through the registered inputs. Confirm the missing `HALLMARK_MYC_TARGETS_V1` or fixture-package/manifest gap without reading project-level raw assets.
3. Create a task-local reverse repair substrate under `4_artifact/2_persist/`, such as `reverse_repair_fixture_m1_1/` plus `reverse_repair_manifest_m1_1.yaml` or an equivalent contract-bridge supplement. It must include enough records/metadata to run the T-042 reverse positive demo honestly and deterministically.
4. Document substrate provenance in a task-local report: what is copied from registered predecessor fixtures, what is synthetic/repair content, why it exists, and why it must not be represented as original raw data.
5. Build the reverse query core from the T-044 package skeleton and T-046 loader API. Use deterministic scoring/ranking with stable tie-breaking and finite-score filtering. Do not depend on T-049 partial code unless execution records a deliberate reason and compatibility check.
6. Implement required no-hit/error behavior from T-042, including missing program, missing context, empty/low-confidence result, and invalid/no-matrix cases as applicable.
7. Run the reverse positive demo against the task-local repair substrate. Save visible structured JSON evidence and record the command used to reproduce it.
8. Run no-hit/error smoke cases and import/compile checks in the project `pxfquery` conda environment.
9. Produce concise execution/result reports, update `4_artifact/registry.yaml`, and write completion status.

## Constraints
- Follow T-042 output JSON, API, CLI, error, and no-hit contract unless a compatibility note is explicitly written and justified.
- Use T-046 loader API behavior as the baseline loader contract; T-047 may be used only as an optional hardening reference.
- The reverse repair substrate must be task-local, registered, and labeled synthetic/repair provenance where applicable.
- Keep ranking deterministic. Ties must use documented stable sort keys.
- Keep code and evidence inside this task directory. Do not modify upstream done tasks.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not use T024-T040 blocked assets.

## Forbidden
- Do not edit T-042, T-043, T-044, T-045, T-046, T-047, or T-049 artifacts.
- Do not mark T-049 as complete or green.
- Do not present repair/synthetic fixture content as original raw LINCS or CMAP data.
- Do not create a private ad hoc data loader that bypasses the accepted loader API without a written compatibility reason.
- Do not perform web search or external lookup.

## Web Search Allowance
Allowed: no

Reason: The task can be configured from project protocol and selected predecessor handoffs/registries. No current external evidence is required.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Reverse repair substrate package or supplement | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` or equivalent | yes |
| Reverse repair manifest | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` or equivalent | yes |
| Repair provenance report | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | yes |
| Reverse query package code | `4_artifact/1_package/pxfquery/` | yes |
| Reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Reverse no-hit/error JSON evidence | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | yes |
| Ranking/scoring notes or table | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` or equivalent | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria
- The reverse positive demo actually runs in the `pxfquery` conda environment and writes visible structured JSON.
- The JSON output follows T-042 field names, object nesting, success/error/no-hit conventions, and pass/fail assertions.
- The demo includes the required suppress target `HALLMARK_MYC_TARGETS_V1`.
- Ranking is deterministic across repeated runs on the same substrate.
- No-hit/error cases are represented as structured JSON rather than uncaught tracebacks.
- The task-local repair substrate is registered in `4_artifact/registry.yaml` with explicit synthetic/repair provenance.
- Upstream completed artifacts remain unchanged.

## Failure / Stop Rules
- Stop if execution cannot satisfy the T-042 reverse positive demo without reading forbidden raw project assets.
- Stop if the only available route is to use T024-T040 blocked assets.
- Stop if the repair substrate cannot be honestly labeled and documented as task-local repair/synthetic support.
- Stop rather than silently changing the T-042 contract.

## Delivery Requirements
- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

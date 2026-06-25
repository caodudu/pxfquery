# Check Handoff Before Exec: T-053 m1_python_package_milestone

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, all predecessor task directories (T-050, T-051, T-052)
- Required registry: `1_asset/registration.yaml` (12 assets, all symlinked, all ok)
- Must stop if: any required asset is missing/empty, or predecessor-reported evidence stream fails verdict

## Objective Restatement
Aggregate three completed predecessor evidence streams (T-050 forward validation, T-051 reverse validation, T-052 package assembly) into a single M1 milestone deliverable. Produce: final package path/version, demo commands, evidence index, layered asset map, known gap report. Do not repair or reimplement anything.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/forward_validation_results_table.csv` | 11-check forward pass/fail table | ok |
| A-002 | `1_asset/forward_validation_report.md` | Forward validation narrative | ok |
| A-003 | `1_asset/reverse_validation_report_json.json` | 42-check reverse structured report | ok |
| A-004 | `1_asset/reverse_validation_comparison_csv.csv` | Per-check pass/fail table | ok |
| A-005 | `1_asset/reverse_validation_html_report.html` | Human-readable reverse report | ok |
| A-006 | `1_asset/assembled_package_source` | M1 package source v0.1.0 | ok |
| A-007 | `1_asset/import_smoke_evidence.txt` | pip install + import + CLI evidence | ok |
| A-008 | `1_asset/forward_demo_json.json` | Forward demo output | ok |
| A-009 | `1_asset/reverse_demo_json.json` | Reverse demo output | ok |
| A-010 | `1_asset/cli_help_text.txt` | CLI help capture | ok |
| A-011 | `1_asset/package_assembly_execution_report.html` | Assembly execution report | ok |
| A-012 | `1_asset/package_assembly_result_report.html` | Assembly result with acceptance criteria | ok |

## Execution Strategy
1. **Read evidence trio** — Read A-001/A-002 (forward), A-003/A-004/A-005 (reverse), A-007 (smoke) to confirm all PASS verdicts and extract key metrics.
2. **Read demo and package evidence** — Read A-006 (package source path), A-008/A-009 (demo JSONs), A-010 (CLI help), A-011/A-012 (reports) to capture package location, version, acceptance criteria, and working demo commands.
3. **Build layered asset map** — Create CSV mapping each asset to its predecessor task, layer (skeleton → forward impl → reverse impl → package assembly → forward validation → reverse validation), and milestone consumption role.
4. **Write evidence index** — Produce `evidence_index_v<timestamp>.json` with all three streams, verdicts, metrics, and cross-references.
5. **Write demo commands reference** — Extract working CLI commands from A-008/A-009/A-010 into `demo_commands_v<timestamp>.md`.
6. **Write known gap report** — Scan predecessor outputs for reported limits, incomplete coverage, or missing evidence. List explicitly.
7. **Write milestone report** — Compile into `milestone_report_v<timestamp>.md` with summary, evidence index, asset map, gaps, and demo commands.
8. **Register deliverables** — Update `4_artifact/registry.yaml` with all output artifacts.

## Conservative Execution Advice
- Start with: Read A-001 (forward table), A-003 (reverse JSON), and A-007 (smoke evidence) to confirm all three gates are green before building anything.
- Smoke/demo method: `python -c "import pxfquery; print(pxfquery.__version__)"` at the assembled package source to verify installability (read-only check).
- Full run only after: all three evidence streams confirmed PASS.
- Cost/time risk: negligible — all data is local text/JSON/CSV/HTML. Estimated 10-15 min for reading + writing 6 deliverables.
- Checkpoint advice: After Step 1, if any evidence stream shows FAIL or missing data, stop and switch to gap reporting.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Milestone report | `4_artifact/3_document/milestone_report_v<timestamp>.md` | Contains all three evidence stream summaries, package path, version 0.1.0 |
| Evidence index | `4_artifact/2_persist/evidence_index_v<timestamp>.json` | Structured JSON with verdicts per stream |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v<timestamp>.csv` | CSV with layer, predecessor task, asset ID, description |
| Known gap report | `4_artifact/5_table/known_gaps_v<timestamp>.md` | Lists any predecessor-reported limits or missing coverage |
| Demo commands | `4_artifact/2_persist/demo_commands_v<timestamp>.md` | Working forward/reverse/info CLI commands |
| Completion report | `5_report/completion.md` | Updated to reflect completed status |

## Failure / Stop Conditions
- If any required asset is missing or empty (contradicting preflight), write blocked.md instead.
- If any predecessor evidence stream reports FAIL or INCOMPLETE, document as known gap and do not mark PASS.
- If asset registry.yaml or protocol.md is internally inconsistent and cannot be repaired, write blocked.md.
- Do not proceed to execution if human approval is required after this check.

## Notes For Delivery QA
- This is a pure aggregation task; all evidence must come from predecessor handoffs, not fresh execution.
- Final package location is the symlink at `1_asset/assembled_package_source/` → T-052's `4_artifact/1_package/`.
- Version is v0.1.0 — confirm in smoke evidence and pyproject.toml.
- Known gaps may include: missing edge-case coverage, small test count, or predecessor-reported limitations. These are acceptable if explicitly documented.
- Each output file must include a timestamp in its filename matching the pattern `v<YYYYMMDD_HHMMSS>`.

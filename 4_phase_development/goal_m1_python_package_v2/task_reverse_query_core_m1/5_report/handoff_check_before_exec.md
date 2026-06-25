# Check Handoff Before Exec: T-049 reverse_query_core_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`, `/Users/dudu/Documents/3_Project/8_functional_query`, predecessor task directories, `1_project_init/`
- Required registry: `1_asset/registration.yaml`
- Must stop if: the T-046 loader cannot expose data needed by the T-042 reverse contract; reverse behavior would require raw project assets, direct legacy-root reads, failed T024-T040 artifacts, or private ad hoc parsing.

## Objective Restatement
Implement the M1 reverse query core for PxFquery using the T-042 contract/demo specification and the T-046 fixture loader as the only data access route. The execution must produce deterministic ranking/scoring behavior, task-local package code, structured JSON demo evidence, and a concise result report. If loader or fixture capabilities are insufficient, execution should document the precise contract/loader gap rather than invent hidden data handling.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | Authoritative M1 reverse API/CLI contract, JSON shape, errors, no-hit behavior, and pass/fail scope. | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | Exact reverse demo case, expected output fields, ranking/scoring assertions, and no-hit variants. | ok |
| A-003 | `1_asset/m1_contract_summary.md` | Optional orientation for contract boundaries and M1 scope. | ok |
| A-004 | `1_asset/m1_fixture_loader_code.py` | Required fixture loader implementation; all reverse query data access must use this loader API. | ok |
| A-005 | `1_asset/m1_loader_api_documentation.md` | Public loader API documentation for M1FixtureLoader, M1Fixture, and M1Manifest. | ok |
| A-006 | `1_asset/m1_loader_smoke_evidence.csv` | Optional smoke evidence for diagnosing expected fixture structures without bypassing the loader. | ok |

## Execution Strategy
1. Read A-001 and A-002 to extract the exact reverse callable/API signature, required input fields, JSON output shape, no-hit/error behavior, and demo pass/fail assertions; record the extracted contract notes in `3_execution/`.
2. Read A-005 and A-004 to identify public loader methods and returned fixture structures; run a minimal loader smoke check through the documented API and save temporary observations in `3_execution/`.
3. Implement task-local reverse query package code under `4_artifact/1_package/`, importing or vendoring the T-046 loader code as appropriate while preserving loader-only data access.
4. Implement deterministic scoring/ranking from loaded fixture data, including explicit tie-breaking rules based on stable fields such as score, perturbation identifier, or contract-defined ordering.
5. Run the T-042 reverse demo case and write structured JSON evidence to `4_artifact/2_persist/reverse_demo_evidence_v20260624.json`.
6. Run no-hit/error variants if required by A-001/A-002 and write `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` when applicable.
7. Write a concise human-readable execution/result report in `4_artifact/3_document/`, register accepted outputs in `4_artifact/registry.yaml`, and finish with `5_report/completion.md`.

## Conservative Execution Advice
- Start with: contract extraction plus one minimal loader smoke check through documented T-046 API methods.
- Smoke/demo command or method: use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` from the task path, with temporary scripts kept under `3_execution/`.
- Full run only after: the loader smoke check confirms fixture matrices/indexes/metadata needed by the reverse contract are reachable without private parsing.
- Cost/time risk: expected to be low; fixture-level execution should be small and offline. No web search, network crawling, raw asset loading, plotting, or full-resource analysis is allowed.
- Checkpoint advice: before writing reusable outputs, checkpoint the extracted contract fields and loader-access assumptions in `3_execution/` so any incompatibility can be reported precisely.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reverse query package code | `4_artifact/1_package/` | Code exposes reverse behavior matching T-042 and uses T-046 loader-only data access. |
| Reverse demo evidence JSON | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | JSON contains required contract fields and satisfies T-042 demo ranking/scoring assertions. |
| Reverse no-hit/error evidence JSON | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Present when required by T-042; shows required no-hit/error shape. |
| Execution/result report | `4_artifact/3_document/` | Concise report explains implementation, deterministic ranking, demo result, and any limitations. |
| Optional ranking/scoring validation table | `4_artifact/5_table/` | Useful if ranking assertions need tabular reproduction evidence. |
| Artifact registry | `4_artifact/registry.yaml` | Registers all accepted reusable outputs with paths and descriptions. |
| Completion report | `5_report/completion.md` | Summarizes completion status, evidence paths, and any unresolved gap. |

## Failure / Stop Conditions
- Stop if any required contract behavior can only be satisfied by reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Stop if implementation would require direct reads from `/Users/dudu/Documents/3_Project/8_functional_query`.
- Stop if the only available implementation path depends on failed T024-T040 assets.
- Stop if T-046 public loader methods do not expose the matrix, index, or metadata fields required by T-042.
- Stop if ranking/scoring would require guessing undocumented thresholds or silently changing T-042 fields.
- Stop if a private manifest reader, direct fixture parser, or other ad hoc data loader seems necessary.

## Notes For Delivery QA
- Verify the delivered code imports and runs from the task-local package path under the `pxfquery` conda environment.
- Confirm no accepted reusable output remains only in `3_execution/`.
- Confirm `4_artifact/registry.yaml` exists and names every accepted code/evidence/report artifact.
- Confirm demo JSON is structured, deterministic, and contract-shaped rather than only a prose log.
- Confirm completion reporting distinguishes successful implementation from any precise loader/contract gap.

# AI Handoff: T-042 contract_and_demo_spec_m1

## Task Goal
Define the M1 API, CLI, demo-case, and error/no-hit contract for the PxFquery Python package using trusted T-007 and T-013 inputs.

## What Was Delivered
T-042 delivered a structured API/CLI contract, concrete forward/reverse demo cases, and a concise human-readable contract summary. It did not implement code, inspect raw project assets, or use T024-T040 outputs as authority.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/m1_api_contract.yaml` | Defines the M1 public API, CLI commands, return shapes, and error/no-hit objects. | T048/T049/T052 should treat this as the contract authority. |
| D-002 | `4_artifact/2_persist/m1_demo_cases.yaml` | Defines exact forward and reverse demo cases plus pass/fail assertions. | T048/T049 should implement against these shapes; T050/T051 should validate them. |
| D-003 | `4_artifact/3_document/m1_contract_summary.md` | Human-readable summary of scope and constraints. | Use as a quick orientation document before reading the YAML files. |

## Supporting Artifacts
- `4_artifact/registry.yaml`
- `5_report/completion.md`
- `5_report/handoff_check_before_exec.md`

## Downstream Use
T048 and T049 should implement deterministic forward/reverse behavior only. T052 should wire package/API/CLI behavior against the YAML contract. LLM resolver, fuzzy matching, plotting, Zenodo download, and full-resource biological claims remain out of M1 scope.

## Known Limits / Risks
This is a contract task, not an implementation task. If a later implementation needs to change a field or threshold, it should create an explicit compatibility note rather than silently diverging from this contract.

## Do Not Read / Do Not Reuse
Do not treat T024-T040 outputs, migrated raw code, or raw `2_project_asset/` files as authority for this contract. Do not use this task as evidence that implementation already runs.

## Recommended Next Reads
1. `4_artifact/2_persist/m1_api_contract.yaml`
2. `4_artifact/2_persist/m1_demo_cases.yaml`
3. `4_artifact/3_document/m1_contract_summary.md`
4. `5_report/completion.md`

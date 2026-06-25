# Check Handoff Before Exec: T-045 index_health_check_m1

## Check Verdict
yellow_repair

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: T-021 standard_resources (read-only), legacy source root `/Users/dudu/Documents/3_Project/8_functional_query`, raw `2_project_asset/`, any `.h5ad` or `.csv` in T-021 standard_resources
- Required registry: `1_asset/registration.yaml` (repaired), `2_protocol/3_asset_rule/asset_rule.yaml` (repaired)
- Must stop if: any required T-021 index is unreadable, function_index.json has != 91 terms, a core index is missing M1-forward/reverse required keys, or index corruption prevents valid JSON parsing

## Objective Restatement
Audit the 10 M1-relevant query indexes from T-021's standard-resource output (D-004). Verify JSON schema validity, required keys for forward/reverse query demos, neighbor graph completeness, and coverage gaps against M1 demo cases. Produce machine-readable health summary + human-readable report + gap notes. Do not modify any index; only report and recommend patches. This is input for T-047 loader hardening.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| T-021/D-004/cellline_index | standard_resources/cellline_index.json | Core index for cell line name validation in queries | required (3.5 KB, exists) |
| T-021/D-004/drug_index | standard_resources/drug_index.json | Core index for drug alias → BRD-id resolution | required (176 KB, exists) |
| T-021/D-004/gene_index | standard_resources/gene_index.json | Core index for gene symbol lookup and type | required (6.1 MB, exists) |
| T-021/D-004/function_index | standard_resources/function_index.json | Core index for function term catalog (91 terms) | required (17 KB, exists) |
| T-021/D-004/data_description | standard_resources/data_description.yaml | Field-level index semantics reference | required (5 KB, exists) |
| T-021/D-004/cellline_neighbors | standard_resources/cellline_neighbors.json | Optional: lineage-based cell grouping for proxy matches | optional (6.5 KB, exists) |
| T-021/D-004/cellline_tree | standard_resources/cellline_tree.json | Optional: cell line ontology tree for reverse query context expansion | optional (49 KB, exists) |
| T-021/D-004/drug_neighbors | standard_resources/drug_neighbors.json | Optional: drug similarity graph for proxy perturbation matching | optional (4.4 MB, exists) |
| T-021/D-004/gene_index_simple | standard_resources/gene_index_simple.json | Optional: compact gene symbol-to-type index | optional (356 KB, exists) |
| T-021/D-004/gene_neighbors | standard_resources/gene_neighbors.json | Optional: full gene semantic neighbor graph | optional (21.8 MB, exists) |
| T-021/D-004/gene_neighbors_simple | standard_resources/gene_neighbors_simple.json | Optional: compact gene semantic neighbor graph | optional (19.5 MB, exists) |

## Execution Strategy
1. **Load required core indexes** — Python read cellline_index, drug_index, gene_index, function_index, and data_description.yaml. Verify valid JSON/YAML parse. Record top-level type, schema shape, and element count per index. Write `3_execution/step1_core_schema/step1_core_schema_summary.json`.
2. **Validate M1-required keys** — For each core index, check: cellline_index has valid name list; drug_index has alias→BRD-id bidirectional mapping; gene_index has symbol→type lookup; function_index has exactly 91 terms with id/name/category fields. Report anomalies (nulls, duplicates, malformed). Write `3_execution/step2_key_validation/step2_key_validation.json`.
3. **Inspect optional neighbor/tree indexes** — Load cellline_neighbors, cellline_tree, drug_neighbors, gene_neighbors (simple+full), gene_index_simple. Check: neighbor graphs have non-empty edges for major entities; cellline_tree is valid tree structure. Flag empty/degenerate graphs that would break proxy matching. Write `3_execution/step3_neighbor_health/step3_neighbor_health.json`.
4. **Cross-reference with M1 demo requirements** — Compare index entity coverage against forward-query needs (perturbation→function) and reverse-query needs (function→perturbation). Use T-042 contract demo cases if accessible via standard resource references; otherwise flag as coverage-gap-tbd. Write `3_execution/step4_coverage_gap/step4_coverage_gap.json`.
5. **Produce machine-readable health summary** — Consolidate steps 1-4 into `4_artifact/2_persist/index_health_summary.json` with per-index status (valid/warning/invalid), key completeness, size/element counts, gap list, and patch recommendations.
6. **Produce human-readable health report** — Write `4_artifact/2_persist/index_health_report.md` with pass/warning/block per index, T-047 handoff advice, and verdict on fixture-only vs real-index readiness.
7. **Write gap notes** — Produce `4_artifact/3_document/gap_notes.md` with human-readable gap narrative, severity, affected demo case, and resolution path.

## Conservative Execution Advice
- **Start with:** step 1 — load just `function_index.json` (smallest required core index, 17 KB) to verify JSON parse and schema shape before loading the 6 MB gene_index or 21 MB neighbor graphs
- **Smoke/demo command or method:** `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "import json; d=json.load(open('...standard_resources/function_index.json')); print(type(d), len(d) if isinstance(d, (dict,list)) else 'scalar', list(d.keys())[:5] if isinstance(d, dict) else '')"`
- **Full run only after:** all 4 required core indexes pass JSON parse and have non-empty, well-structured content
- **Cost/time risk:** very low — all indexes are local JSON/YAML under ~330 MB total; no network, no API, no compute-heavy operations. Largest file is gene_neighbors.json at 21.8 MB, parseable in seconds
- **Checkpoint advice:** after step 2 (key validation) — if core indexes are structurally valid, the task is ~60% done and the rest is optional-inspection + report-writing. If any core index is corrupt, stop and write incomplete-gap into summary

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| index_health_summary.json | `4_artifact/2_persist/index_health_summary.json` | Valid JSON with per-index schema status, key completeness, element counts, gap list, patch recommendations for all 4 required + up to 6 optional indexes |
| index_health_report.md | `4_artifact/2_persist/index_health_report.md` | Clear pass/warn/block per index; explicit T-047 handoff sentence; fixture-only vs real-index M1 readiness verdict |
| gap_notes.md | `4_artifact/3_document/gap_notes.md` | Each gap has severity, affected demo case, and resolution path. No gap should be listed without a severity label |

## Failure / Stop Conditions
- Any required core index (cellline_index, drug_index, gene_index, function_index) fails JSON parse → record error, continue with remaining, flag as blocker in summary
- function_index.json does not contain 91 terms → flag as schema violation
- A core index is structurally valid but has 0 elements → flag as empty-index gap
- Any write to T-021 standard_resources directory is attempted → hard stop
- Python environment (`pxfquery` conda env) is unavailable → stop and report in summary

## Notes For Delivery QA
- T-045 is an audit — 100% of value is in the 3 output files. No code is produced, no indexes are modified
- The health_summary.json is the primary input for T-047 (resource_loader_hardening_m1)
- If indexes are clean, T-047 can proceed with real-index hardening. If indexes have gaps, T-047 should use fixture-only path per M1 fallback strategy
- T-021 already verified these indexes at build time (18/18 Python-verified), so most should pass. Focus on M1-fit questions: are the keys and shapes what forward/reverse queries actually need?
# Protocol: ms8_10_l2_resource_routing_repair

## Objective
Repair and verify PxFquery L2 evidence routing/resource-aware resolution as a scanpy-style layer. L2 must consume a valid `QueryIntent` plus real registered indexes, resolve cell/drug/gene/function resources, produce exact/proxy/no-hit route plans with evidence metadata, and never use demo dictionaries, hardcoded biomedical outcomes, fake LLM success, or L3 matrix execution as a substitute for routing.

## Inputs
- A-001: T135 legacy core layered recovery task - inspect claims, source layout, and recovered L2/L3 split.
- A-002: T136 original logic and layer target anchor - use as the responsibility boundary for L2 versus L1/L3.
- A-003: GitHub export package workspace - target source tree for L2 repair and tests.
- A-004: Current CyHex workspace package source - compare current degraded route behavior and contracts.
- A-005: Current route/API tests - audit and replace weak route tests that pass with toy behavior.
- A-006: Project protocol anti-fake rules - enforce no fake LLM/NLU, no demo data, no silent milestone downgrade.

## Steps
1. Write a short L2 source audit before editing: identify current L2 entrypoints, which code actually reads indexes, which code is misplaced under L3 execution, and which tests allow fake routing.
2. Define the L2 scanpy-style interface target: `q = pxf.read.query(...)`; L1-produced or test-constructed `QueryIntent` exists in `q.uns`; `pxf.pp.route(q)` produces a route plan and evidence metadata without executing h5ad matrices.
3. Repair L2 source so resource-aware resolution lives in `l2_routing`, not hidden inside `tl.execute()`. L2 should resolve:
   - cell context from exact cell index or cell hierarchy/proxy candidates;
   - drug descriptions through `drug_index.json` and `drug_neighbors.json`;
   - gene descriptions through `gene_index*.json` and `gene_neighbors*.json`;
   - function terms through `function_index.json`;
   - exact/proxy/no-hit/ambiguous/context-missing route status and route diagnostics.
4. If L2 needs LLM-assisted controlled selection for mapping, it must call the configured real provider and record non-secret evidence. If no provider is configured or the provider fails, L2 must fail or report unresolved routing; it must not silently switch to local keyword rules.
5. Add focused tests for L2 using real registered index files from the standard resource pack when available. Minimal fixtures may be used only as clearly labeled test fixtures and must not enter product source or docs as real biological evidence.
6. Add negative tests proving unsupported entities, missing context, absent indexes, provider failure, ambiguous mapping, and no-hit routes remain visible as failure/unresolved metadata rather than fake success.
7. Verify that `pxf.pp.route(q)` does not load h5ad matrices, does not return biological scores/candidates, and does not invoke L3 execution.
8. Run exact verification commands in the `pxfquery` conda environment and record them in `3_execution/02_verification_commands/command_log.md`.
9. Update documentation only for true L2 behavior and terminal reproduction commands. Do not claim L1, L3, L4, L5, resource-pack download, or full package completion.
10. If all L2 gates pass, write completion and optionally commit/tag an L2-only checkpoint. If any real index/provider gate fails, write `5_report/blocked.md` with failing commands and evidence.

## Constraints
- Do not modify or depend on T-137 execution. T-137 owns L1 real-LLM repair.
- Do not use local keyword/regex/template parsing to mimic L1.
- Do not use demo dictionaries, hardcoded biomedical entities, fake scores, fake candidates, or hand-built success payloads in product source.
- L2 may accept a manually constructed `QueryIntent` in tests because L1 is a separate layer, but that test input must be labeled as a structured L2 unit input and must not be presented as LLM parsing success.
- L2 must not run matrix execution or use h5ad query results to decide whether routing passed.
- L2 must expose source index names, matched/resolved identifiers, proxy chains, unresolved reasons, and provider evidence when LLM-assisted mapping is used.
- Resource index absence is a real blocked/failure condition for index-backed L2 tests, not a reason to substitute a toy in-memory index in product code.

## Deliverables
- `3_execution/01_source_audit/l2_source_audit.md`
- `3_execution/02_verification_commands/command_log.md`
- Updated L2 source under `/Users/dudu/Documents/3_Project/12_PxFquery_github_export/src/pxfquery/l2_routing/`
- Minimal interface updates under `workflow.py`, `client.py`, or `settings.py` only if needed for the L2 boundary.
- Hardened L2 tests under `/Users/dudu/Documents/3_Project/12_PxFquery_github_export/tests/`
- `4_artifact/5_table/l2_route_verification_matrix.json`
- `4_artifact/5_table/l2_route_evidence_examples.json`
- `4_artifact/2_persist/l2_terminal_reproduction_guide.md`
- `4_artifact/2_persist/l2_boundary_and_failure_policy.md`
- `4_artifact/3_document/execution_report_vYYYYMMDD.html`
- `4_artifact/3_document/result_report_vYYYYMMDD.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md` only if all gates pass; otherwise `5_report/blocked.md`.

## Acceptance
- Human can run a terminal command that performs `read.query -> pp.parse or inject QueryIntent -> pp.route -> get.route` and sees a resource-index-backed L2 route plan.
- L2 route tests read real registered index files for at least exact hit, proxy hit, no-hit, and context-missing cases, or explicitly fail with missing-resource evidence.
- `pp.route` produces route metadata without loading h5ad matrices or producing biological score/candidate outputs.
- L2 LLM-assisted mapping, if used, records real provider evidence and fails when provider calls fail.
- Missing indexes, unsupported entities, ambiguous mappings, and absent context do not pass as successful exact routes.
- Source scan finds no product-source demo entities, hardcoded route successes, fixture payloads, or local fake LLM success path in L2.
- Completion report explicitly states L2-only scope and does not claim real L1 NLU, L3 matrix execution, L4 evidence assembly, L5 answer presentation, or full MS8 completion.

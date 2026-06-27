# T138 L2 Resource Routing Repair Completion Report

Date: 2026-06-28

## Scope

This task repaired the T138 PxFquery L2 resource-routing layer in the task-local package copy:

`3_execution/03_package_source_v2_l2`

The public route entry is `pxf.pp.route(qdata)`. No `tl.route` compatibility path is exposed.

## Implemented L2 Behavior

- Resource-backed `RoutePlan` with cell, perturbation, function, combination, selected route, rejected candidates, unresolved dimensions, LLM evidence, and L3 handoff payload.
- Cell routing through exact alias lookup or bounded LLM cell-tree traversal.
- Drug routing through exact/BRD lookup, fuzzy top-k retrieval, LLM normalization/hypothesis, index validation, structural proxy expansion, and mechanism-class evidence marking.
- Gene routing through full/simple gene indexes, LLM normalization/hypothesis, index validation, noncoding gene support, in-matrix gating, and GenePT proxy expansion.
- Function routing through the fixed T021 91-function index, exact/alias matching, controlled LLM list selection, reverse three-pass interpretation sets, and forward broad-output no-filter scope.
- Forward and reverse beam-limited combination routing with candidate caps.
- Explicit failure states including `resource-missing`, `llm_unavailable`, `llm_output_invalid`, `unresolved`, and `no_pair_available`.

## Verification

Commands run from the task/package directories:

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m pytest -q
python 3_execution/run_l2_real_llm_validation.py
python 3_execution/run_t137_60_l2_validation.py
python 3_execution/run_generalization_50_l1_l2_validation.py
```

Final results:

- Package tests: `19 passed, 1 skipped`
- Real DeepSeek L2 design validation: passed
- T137 60-question L2 replay: `60 passed, 0 failed`
- Separate 50-question L1+L2 generalization validation: `50 passed, 0 failed`

Latest validation artifacts:

- `4_artifact/2_persist/l2_real_llm_validation/l2_real_llm_validation_report.json`
- `4_artifact/2_persist/l2_real_llm_validation/l2_real_llm_validation_report_zh.md`
- `4_artifact/5_table/t137_60_l2_validation_latest.json`
- `4_artifact/3_document/t137_60_l2_validation_latest.html`
- `4_artifact/5_table/generalization_50_l1_l2_validation_latest.json`
- `4_artifact/3_document/generalization_50_l1_l2_validation_latest.html`

## Integrity Checks

- `.env` was not committed.
- No package-source match for the T137 case IDs or known T137 query text was found.
- No package-source match for `tl.route` remained.
- No package-source API key pattern was found.
- Validation scripts use real DeepSeek via externally loaded environment variables; package internals do not read `DEEPSEEK_API_KEY`.

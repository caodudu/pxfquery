# T-031 Completion: no_hit_guard_v1

Generated: 2026-06-23

## Result Summary

T-031 produced `pxfquery-T-031`, a no-hit safety guard that prevents fuzzy false-positive perturbation matches in `ForwardQuery`.

### Guard Implementation
- File: `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py`
- Class: `NoHitGuardForwardQuery(ForwardQuery)` with two tunable thresholds:
  - `min_query_length_for_substring=4` — blocks short random tokens like `egr` (3 chars)
  - `min_overlap_for_token_fallback=2` — blocks single-token overlaps like `egfr_random`
- Does **not** modify T-024 workspace or any upstream artifact.
- Drop-in compatible: replaces `ForwardQuery(adata)` with `NoHitGuardForwardQuery(adata)`.

### CAP-05 Resolution
- Reproduced: 7/9 false positives with unguarded ForwardQuery (evidence: `pxfquery_T031_false_positive_reproduced.json`)
- Resolved: 11/11 nonsense names correctly blocked by guard (`pxfquery_T031_no_hit_evidence.json`)
- Positive-control preserved: EGFR/A549 (found=True, 20 act + 20 sup) and TP53/MCF7 (found=True, 20 act + 20 sup) (`pxfquery_T031_positive_control_evidence.json`)

### Output List
- `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` — Guard module
- `3_execution/test_no_hit_guard.py` — Negative test (11/11)
- `3_execution/test_positive_control.py` — Positive-control test (2/2)
- `4_artifact/5_table/pxfquery_T031_false_positive_reproduced.json` — CAP-05 reproduction evidence
- `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json` — No-hit evidence
- `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json` — Positive-control evidence
- `4_artifact/3_document/execution_report_v20260623.html` — Execution report
- `4_artifact/3_document/result_report_v20260623.html` — Result report
- `4_artifact/registry.yaml` — Deliverable registry
- `5_report/completion.md` — This file

### Upstream Asset Integrity
No upstream artifact was modified. T-024 workspace, T-026 loader, T-021 bundle, T-029 engine, and T-013 reports remain unchanged.
No local repair was needed.

### Downstream Consumption
- Replacement: `from pxfquery_T031_forward_no_hit_guard import NoHitGuardForwardQuery`
- Tuning: `NoHitGuardForwardQuery(adata, min_overlap_for_token_fallback=3)` for stricter matching
- The guard targets only CAP-05 (perturbation fuzz false-positives); it does not address resolver, NL, or function_index issues.
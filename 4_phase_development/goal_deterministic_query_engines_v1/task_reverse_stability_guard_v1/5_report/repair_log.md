# T-032 Repair Log

Source asset: T-024 workspace package (`pxfquery-T-024`).

Repaired task-versioned output: `3_execution/pxfquery_T-032_repaired/`.

Changed scope:
- Added guarded cosine-similarity behavior for zero-norm rows, zero-norm target vectors, NaN rows, and Inf rows inside the T-032 repaired package copy.
- Added structured warning output so abnormal-similarity events are serialized instead of silently absorbed by epsilon denominator replacement.
- Preserved backward compatibility for normal finite, non-zero-norm inputs; validation reports `max_diff: 0.0` against legacy cosine behavior.

Validation evidence:
- `3_execution/stability_guard_validation.json` reports 8/8 scenarios passed.
- Positive control returned 20 ranked candidates for `HALLMARK_APOPTOSIS` activate + `HALLMARK_MYC_TARGETS_V1` suppress in `MCF7`, all finite and within range.
- Abnormal synthetic cases emitted expected warnings and returned finite guarded similarities.

Downstream guidance:
- Downstream reverse-query stability consumers should use `pxfquery-T-032` from `3_execution/pxfquery_T-032_repaired/`, not the upstream T-024 package copy.

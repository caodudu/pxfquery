

I'll execute this T-051 reverse validation task step by step. Let me start by inspecting the
Let me examine the package source code to understand the API:
Now let me create the execution directory and begin execution. Let me set up the task paths and start building
Now I have a clear picture. Let me run all validation steps via a comprehensive script:
The one failure is a test logic bug — the CSV compares 10 reference rows against 3 observed rows (we ran `top_n=3`). Let me fix and rerun:
All 42/42 checks pass. Let me now register artifacts and write the completion report:
**T-051 reverse_validation_m1 — COMPLETED**

**Verdict: PASS (42/42 checks)**

The M1 reverse query implementation is validated as functionally correct. Key results:

| Domain | Result |
|---|---|
| Package provenance | Symlink → T-044, version 0.1.0 |
| Fixture loading | xpr 15×9, has MYC_TARGETS_V1 + A549 |
| Positive demo (APOPTOSIS↑, MYC↓, A549, top=3) | THTPA(1.0), SCD(0.999959), TP53(0.999541) — matches reference |
| No-hit errors | NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, empty-target — all correct |
| Ranking comparison | Top-3 sig_ids/similarity/order match reference JSON and CSV |
| CLI smoke | `info` and `reverse` commands work, correct exit codes |

All deliverables produced: `4_artifact/2_persist/reverse_validation_report_v*.json`, `4_artifact/5_table/reverse_validation_comparison_v*.csv`, `4_artifact/3_document/validation_report_v*.html`, `4_artifact/registry.yaml`, `5_report/completion.md`.

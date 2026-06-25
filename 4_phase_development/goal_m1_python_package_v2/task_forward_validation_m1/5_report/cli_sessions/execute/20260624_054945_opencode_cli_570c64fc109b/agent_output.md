Now
First, let me check if the package is already installed and set up the environment:
The package is installed but from a different source (task_package_skeleton_m1, not T-059). Let me reinstall from the T-059 package symlink:
The import error suggests the editable install is pointing to the local copy which may have cached an old `__
The only diff is the `_evidence` field (present in T-059 reference but not in re-run output — expected since that was added by T-059's harness). Key structural fields all match. Now let me do all the remaining steps:
All checks pass. Now producing deliverables:
Now let me check the no-hit keys comparison more carefully and then produce all deliverables:
Only `_evidence` field difference (expected — T-059 added it, the core query function doesn't). Now producing all deliverables:
Now write the validation report and HTML reports:
Now register artifacts and write completion report:
All 7 deliverables exist. Now register artifacts and write completion:
## T-050 Forward Validation M1 — Complete

**Overall Verdict: PASS** (11/11 checks passed)

### What was done
1. **Installed** T-059 package (pxfquery v0.1.0) from asset symlink
2. **Fixture load** — `M1FixtureLoader` loaded repair fixture, xpr shape `(5, 7)` ✓
3. **Positive demo** — `pert2func("EGFR", "A549", "xpr")` → `found: true`, correct perturbation/cell_line, non-empty `top_activated` and `top_suppressed` ✓
4. **No-hit demo** — `pert2func("UNKNOWN_GENE_XYZ999", ...)` → structured `{"error": "PerturbationNotFound", ...}`, no traceback ✓
5. **Reference comparison** — Structural keys match T-059 reference (only `_evidence` differs, T-059 harness metadata) ✓
6. **CLI smoke test** — `pxfquery forward` → exit code 0, valid JSON ✓
7. **Traceability** — Recorded: package v0.1.0, `M1FixtureLoader`, `synthetic_repair` provenance, manifest path, reference evidence paths

### Deliverables
| Path | Status |
|---|---|
| `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | ✓ |
| `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | ✓ |
| `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | ✓ |
| `4_artifact/5_table/forward_validation_results_v20260624.csv` | ✓ |
| `4_artifact/3_document/forward_validation_report_v20260624.md` | ✓ |
| `4_artifact/3_document/execution_report_v20260624.html` | ✓ |
| `4_artifact/3_document/result_report_v20260624.html` | ✓ |

All 7 deliverables produced, artifact registry updated, completion report written.

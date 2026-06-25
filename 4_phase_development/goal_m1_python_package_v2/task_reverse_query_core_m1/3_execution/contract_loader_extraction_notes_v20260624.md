# T-049 Contract And Loader Extraction Notes

Generated: 2026-06-24

## Step List

1. Extract reverse contract and demo assertions.
   - Operation: read registered A-001 and A-002.
   - Evidence: this note.
   - Dependency: none.
2. Inspect loader API/code and fixture availability.
   - Operation: read registered A-004 and A-005, inspect accepted T-046 artifact package for the documented manifest/fixture package.
   - Evidence: this note and command observations.
   - Dependency: step 1.
3. Implement task-local reverse query code.
   - Operation: write package under `4_artifact/1_package/`.
   - Evidence: package files and import/syntax validation.
   - Dependency: step 2 API shape.
4. Run demo and error/no-hit evidence.
   - Operation: execute T-042 DEMO-002 through the task-local package.
   - Evidence: JSON files under `4_artifact/2_persist/`.
   - Dependency: fixture manifest/package reachable through T-046 loader.
5. Write registry and reports.
   - Operation: create registry, HTML reports, completion/blocked report.
   - Evidence: files under `4_artifact/` and `5_report/`.
   - Dependency: prior steps.

## Reverse Contract Extracted From A-001/A-002

- Public method: `PxFquery.func2pert(activate: list[str], suppress: list[str], cell_line: str, matrix_type: str | None = None, top_n: int = 10)`.
- Demo input: activate `["HALLMARK_APOPTOSIS"]`, suppress `["HALLMARK_MYC_TARGETS_V1"]`, cell line `"A549"`, matrix type `"xpr"`, top_n `10`.
- Successful result shape:
  - `found: true`
  - `activate`, `suppress`, `cell_line` echoed from input
  - `candidate_columns` includes at least `cmap_name`, `cell_iname`, `similarity`, `driving_terms`
  - `top_candidates` list length is at least 1 and at most `top_n`
  - each candidate has finite numeric `similarity`
  - candidates sorted by similarity descending
  - `warnings` may be empty or contain numerical warnings
- Reverse errors/no-hit required by contract/demo:
  - unknown program: `ProgramNotFound`, with `unknown_activate`, `unknown_suppress`, `query_type: reverse`
  - unknown cell line: `ContextNotFound`, with `cell_line`, `matrix_type`, `query_type: reverse`
  - no matrix: `NoMatrixLoaded`
  - low confidence: `LowConfidenceResult` when all similarities are near zero; threshold must be defined.

## Loader API Extracted From A-004/A-005

- Public loader: `M1FixtureLoader(manifest_path: str, fixture_root: Optional[str] = None)`.
- Public data object: `loader.fixture`.
- Public matrix access methods:
  - `M1Fixture.matrix_shape(name)`
  - `M1Fixture.matrix_obs_columns(name)`
  - `M1Fixture.matrix_var_names(name)`
  - `M1Fixture.get_sig_ids(name)`
  - `M1Fixture.get_matrix_row(name, sig_id)`
- Matrix `.obs` columns documented/observed in A-006:
  - `sig_id`, `project_code`, `cell_iname`, `pert_id`, `cmap_name`, `pert_dose`, `pert_time`
- Observed fixture functional terms in A-006:
  - `HALLMARK_ADIPOGENESIS`
  - `HALLMARK_APOPTOSIS`
  - `HALLMARK_E2F_TARGETS`
  - `HALLMARK_P53_PATHWAY`
  - `HALLMARK_TNFA_SIGNALING_VIA_NFKB`
  - `MP39 Metal-response`
  - `MP40 PDAC-related`

## Fixture Availability Gap

Targeted inspection of the accepted T-046 `4_artifact/` tree found only:

- `4_artifact/1_package/pxfquery/data/m1_loader.py`
- `4_artifact/2_persist/API_REFERENCE_v20260624.md`
- `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv`
- reports and registry

No `resource_manifest_m1.yaml` or `fixture_package_m1/` was present in the accepted T-046 artifact tree. Because T-049 is forbidden from raw project assets, direct legacy roots, and unregistered asset discovery, the required DEMO-002 run cannot be executed independently through the loader from the selected assets.

There is also a contract/fixture term mismatch in the registered smoke evidence: T-042 DEMO-002 requires `HALLMARK_MYC_TARGETS_V1`, but A-006 observed fixture terms do not include it.


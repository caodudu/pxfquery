# T-043 M1 Data Manifest And Fixture Package

Generated: 2026-06-24

This package defines the stable M1 data substrate for downstream PxFquery package work.
It uses only the registered T-014 and T-021 assets for authority and fixture extraction.

## Files To Consume

- `resource_manifest_m1.yaml`: primary machine-readable resource manifest.
- `fixture_package_m1/`: small deterministic real-data subset for loader, forward-query, and reverse-query smoke tests.
- `expected_shapes_keys_columns_m1.csv`: declared full-resource and fixture schemas.
- `sample_records_m1.csv`: exact source identifiers and selected fields for example records.

## Fixture Contents

- Matrix fixtures: `cp_func_fixture_m1.h5ad`, `sh_func_fixture_m1.h5ad`, `xpr_func_fixture_m1.h5ad`.
- Function subset: HALLMARK_ADIPOGENESIS, HALLMARK_APOPTOSIS, HALLMARK_E2F_TARGETS, HALLMARK_P53_PATHWAY, HALLMARK_TNFA_SIGNALING_VIA_NFKB, MP39 Metal-response, MP40 PDAC-related.
- Selected cells: A375, BICR6, PC3, U251MG.
- Selected compounds: BRD-K66175015, BRD-K70401845, BRD-K70511574, BRD-K85606544.
- Selected genes: A2M, AATF, ABAT, ABCA1, CPVL, ORAI3, SLC19A3, STAC.
- Metadata and resolver index fixtures are real subsets of A-001 standard CSV/JSON resources.

## Downstream Use

Loader tasks should read the manifest first, then choose either full standard resources under
`1_asset/t021_standard_resources_bundle/` or the fixture resources under
`4_artifact/2_persist/fixture_package_m1/`.

Forward-query demos can use any selected fixture matrix observation as perturbation-to-function
evidence. Reverse-query demos can rank the selected fixture observations by one of the selected
function columns. The fixture is intentionally small and is not intended to reproduce full query
ranking behavior.

## Known Exclusions

- Truncated upstream CMAP H5AD files reported by T-014/T-021 are excluded.
- Historical GSEA output artifacts and old figures are excluded because they are provenance/support
  assets, not M1 runtime resources.
- GenePT embeddings are excluded because T-021 did not include them in the standard runtime bundle.
- No project raw assets, legacy source roots, failed T024-T040 outputs, web data, or synthetic
  biological records were used.

# pxfquery-T-024

T-024 workspace build of PxFquery. This is a src-layout snapshot produced from the migrated legacy package code as a read-only source. The code is byte-identical to the legacy source except for the workspace-level pyproject.toml which fixes the build-backend for `pip install` compatibility.

## Lineage

- Source: `legacy_flat_asset_library_v20260614/code/pxfquery_package/`
- Divergence: `build-backend` corrected from `setuptools.backends.legacy:build` to `setuptools.build_meta` in workspace-level `pyproject.toml`
- Downstream: later development tasks should consume this workspace as `pxfquery-T-024`
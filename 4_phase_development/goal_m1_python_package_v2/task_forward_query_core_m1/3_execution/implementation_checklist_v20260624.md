# T-048 Implementation Checklist

Date: 2026-06-24

## Contract Inputs

- Forward API: `PxFquery.pert2func(perturbation, cell_line, matrix_type=None, top_k=20)`.
- Demo hit: `perturbation="EGFR"`, `cell_line="A549"`, `matrix_type="xpr"`, `top_k=20`.
- Required hit shape: `found`, `perturbation`, `cell_line`, `n_obs`, `cells_used`, `top_activated`, `top_suppressed`, `note`, `warnings`.
- Required no-hit variants: unknown perturbation, unknown cell line, no matrix loaded.
- Required error keys: `error`, `message`, query-specific echo fields, `matrix_type`, `query_type`.

## Loader Use

- Use `M1FixtureLoader` from the T-046 implementation.
- Loader input used for evidence: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/1_asset/resource_manifest_m1.yaml`.
- All matrix objects, rows, obs metadata, and function names must come from `loader.fixture` and `M1Fixture` methods or AnnData objects returned by the loader.

## Implementation Scope

- Implement forward query core only.
- Provide `func2pert` and `load_data_dir` placeholders matching the contract's not-implemented behavior.
- Do not implement resolver, LLM, reverse ranking, proxy retrieval, plotting, or direct fixture parsing.

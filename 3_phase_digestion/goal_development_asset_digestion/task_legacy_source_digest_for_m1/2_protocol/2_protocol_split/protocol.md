# Protocol: legacy_source_digest_for_m1

## Objective

Digest the explicitly allowed migrated PxFquery package source into a small reusable M1 reference asset. The task identifies which legacy modules, functions, entry points, data/index access patterns, and known risks should inform the M1 Python package DAG. It does not implement new package code, does not modify legacy files, and does not scan the whole project asset tree.

## Inputs

- A-001: T-007 development source map — use as the authority for the migrated package-source path and source priority.
- A-002: T-007 development state report — use as secondary context for package component status, data/index readiness, and validation state.
- A-003: Migrated PxFquery package source — the only legacy package-source directory this task may inspect.
- A-004: T-007 module asset status matrix — optional tabular cross-check for module and asset status.
- A-005: T-007 development gap and risk list — optional risk cross-check for unsafe legacy components and claims to avoid.

## Steps

1. Confirm the registered A-003 package-source directory exists and limit source inspection to that directory.
2. Inventory top-level package files and modules, including core API, loader, query, index, resolver/LLM, visualization, utilities, and obvious stubs.
3. Identify candidate code and concepts that downstream M1 tasks may safely reference: loader API ideas, forward query logic, reverse query logic, index access patterns, no-hit behavior, and package entry points.
4. Identify unsafe or non-reusable legacy pieces: hard-coded relative paths, pass stubs, NotImplementedError paths, fragile LLM calls, stale README/main entry points, and direct assumptions about old working directories.
5. Produce a concise M1 reuse recommendation table that maps each downstream task type to allowed legacy references and forbidden legacy references.
6. Write deliverables under `4_artifact/` and register them in `4_artifact/registry.yaml`.

## Constraints

- This digestion task is the only new M1 DAG task allowed to inspect the explicit legacy package-source path.
- Do not scan arbitrary project assets or the entire `2_project_asset/` tree.
- Do not modify files under the legacy source path, T-007, or any completed task.
- Do not write M1 implementation code for T046-T053.
- Do not use T024-T040 outputs as authorities.
- If a useful source path is outside A-003, mention it as a gap or future digestion need rather than opening it.

## Deliverables

- `4_artifact/2_persist/legacy_source_digest_m1.md`: concise source digest with package structure, reusable modules, risks, and M1 recommendations.
- `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: table of modules/files, status, reuse recommendation, downstream task relevance, and risk notes.
- `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden legacy reference boundaries for downstream tasks.
- `4_artifact/registry.yaml`: registry entries for all reusable deliverables.
- `5_report/completion.md`: completion note including the exact source path inspected and confirmation that no broader project asset scan was performed.

## Acceptance

- The source digest names concrete files/modules and gives direct guidance for T046, T048, T049, and T052.
- The reuse matrix distinguishes usable, risky, incomplete, and forbidden legacy pieces.
- The boundary YAML clearly states that downstream development tasks must use T041 outputs rather than reading raw legacy source directly.
- The task does not create or modify implementation code outside its own `4_artifact/` and `5_report/`.
- The deliverables are registered in `4_artifact/registry.yaml`.

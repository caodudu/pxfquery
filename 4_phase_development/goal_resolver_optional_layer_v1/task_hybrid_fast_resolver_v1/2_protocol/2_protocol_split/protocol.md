# Protocol: task_hybrid_fast_resolver_v1

## Objective

Produce a `pxfquery-T-033` optional hybrid fast resolver asset that demonstrates exact / proxy / NOT_FOUND resolver behavior when a perturbation and biological context are resolved through the runtime query indexes (T-027), the function index (T-028), and the perturbation no-hit guard (T-031) / reverse stability guard (T-032) outputs. The deliverable is a runnable resolver module plus exact / proxy / not_found example outputs and visible metadata evidence.

This task is **optional** for the deterministic forward/reverse milestone. If validation is clean it may be consumed by the milestone merge or demo; if it cannot be made runnable, it must not block the milestone.

## Inputs

- **A-001**: T-027 normalized runtime query index pack — `pxfquery_T027_runtime_query_index/` symlinks to T-021/D-004 JSON indexes, including the seven resolver-required filenames (`cellline_index.json`, `cellline_neighbors.json`, `gene_index_simple.json`, `gene_neighbors_simple.json`, `drug_index.json`, `drug_neighbors.json`, `function_index.json`).
- **A-002**: T-028 function index pack (D-001) — `pxfquery_T028_function_index/function_index.json` with 91 functions and aliases (self / lowercase / label). Used to back the resolver's function_desc → var_name mapping for forward query plans.
- **A-003**: T-031 no-hit guard module — `pxfquery_T031_forward_no_hit_guard.py` providing `NoHitGuardForwardQuery` with tunable thresholds. The hybrid fast resolver must wrap the perturbation resolution path with this guard so nonsense perts return `found=False` instead of fuzzy false positives.
- **A-004**: T-032 reverse stability guard package — `pxfquery_T-032_repaired/` workspace with `ReverseQuery` emitting structured `GuardEvent` warnings for zero-norm / NaN / Inf / unmatched-target cases. Used so reverse query metadata stays consistent.
- **A-005** (optional): T-024 pxfquery workspace package — `pxfquery-T-024` `QueryResolver`, `ForwardQuery`, `ForwardResult`, `ReverseQuery`, `ReverseResult` from `task_workspace_package_v1/4_artifact/2_persist/workspace/`. Reference for the original resolver API surface; not mutated.
- **A-006** (optional): T-013 MVP capability review deliverables (D-001 MVP contract, D-005 failure list). Used as context for the CAP-05 no-hit and reverse-stability guard specifications this hybrid resolver layers on top of.
- **A-007** (optional): T-007 PxFquery project intent digestion — `task_digest_pxfquery_development_state/4_artifact/`. Soft reference for project intent only; not a blocking dependency.

## Steps

1. **Read the upstream artifacts**: load A-001 (T-027 runtime query index directory), A-002 (T-028 function index JSON), A-003 (T-031 no-hit guard source), A-004 (T-032 stability guard hint references), and A-005 (T-024 resolver code, optional) to understand the resolver surface area and the guard semantics.
2. **Design a hybrid fast resolver** that combines:
   - exact match via `cellline_index` / `gene_index_simple` / `drug_index` lookups,
   - proxy match via `cellline_neighbors` / `gene_neighbors_simple` / `drug_neighbors`,
   - **no-hit guard** semantics so unsupported or near-token perturbations return an explicit NOT_FOUND result instead of fuzzy false positives,
   - **stability guard semantics** so reverse query metadata reports guard warnings for abnormal inputs,
   - **function alias matching** via the T-028 function index aliases (self / lowercase / human-readable label).
   The resolver must be importable as a Python module and runnable inside the `pxfquery` conda environment.
3. **Implement the local corrected copy** at `3_execution/pxfquery_T033_hybrid_fast_resolver.py` exposing a top-level class `HybridFastResolver` (or equivalent) with at least:
   - `resolver_meta` echoing the resolver plan (intent, hit_level, used_cell, used_perturbation, guard_warnings, score/proxy info),
   - `resolve(user_input, pert_type=None, top_n=20) -> ResolverOutput` that runs an exact → proxy → not_found escalation and tags the chosen hit level,
   - explicit `NOT_FOUND` output for unresolved or guard-blocked queries.
4. **Create three runnable example scripts** under `3_execution/`:
   - `example_exact_match.py` — run a known exact match (e.g. `EGFR/A549/xpr`) and assert `found=True` with `hit_level=EXACT` plus the chosen cmap_name, cell_iname, perturbation token, and term counts.
   - `example_proxy_match.py` — run a perturbation that triggers proxy resolution (exact perturbation, unknown cell, or known cell, proxy perturbation), assert `found=True` with `hit_level` in `PROXY_PERT` / `PROXY_CELL` / `PROXY_BOTH`, and surface proxy evidence.
   - `example_not_found.py` — run a nonsense query (e.g. `NONSENSE_ZZZ999/UNKNOWN_CELL/xpr`) and assert an explicit NOT_FOUND response — `found=False`, no activated/suppressed terms, and explicit not-found note.
5. **Run all three examples** inside the `pxfquery` conda env (`/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`) and capture structured evidence:
   - `4_artifact/5_table/pxfquery_T033_example_exact.json`,
   - `4_artifact/5_table/pxfquery_T033_example_proxy.json`,
   - `4_artifact/5_table/pxfquery_T033_example_not_found.json`,
   - plus a single machine-readable metadata roll-up `4_artifact/5_table/pxfquery_T033_examples_metadata.json` capturing resolver version, conda env, python version, key package versions, seed inputs, and per-example pass/fail flags.
6. **Write a usage guide** at `4_artifact/2_persist/pxfquery_T033_downstream_usage_notes.md` (and a Chinese companion `..._zh.md`) explaining: what the resolver does, how to import it, how the optional layer plugs into or detaches from a deterministic forward/reverse pipeline, and how a downstream demo or merge task may consume `pxfquery-T-033`.
7. **Write CyHex-mandatory Chinese HTML reports** at `4_artifact/3_document/execution_report_vYYYYMMDD.html` (step-by-step) and `4_artifact/3_document/result_report_vYYYYMMDD.html` (visible metadata, exact / proxy / not_found summary, guard integration evidence). Date stamp using the actual execution date.
8. **Register outputs** in `4_artifact/registry.yaml`: the resolver module is the core deliverable (T-033/D-001, `core: true`, `lineage_anchor: true`); each example script + evidence file is a support deliverable; the HTML reports are `stars: 5`.
9. **Write completion material**: `5_report/completion.md` summarizing exact / proxy / not_found results, guard integration evidence, and downstream consumption guidance. **Only** if the upstream guards (T-031 / T-032) had to be locally adapted to make the resolver runnable, write `5_report/repair_log.md` describing source asset id, changed files, validation evidence, and downstream consumer.

### Required Bug-Repair Handling

- If a bug prevents delivering a runnable resolver, repair it inside this task scope (e.g., a forward-engine wrapper that supports the upstream `NoHitGuardForwardQuery`, a small reverse-query metadata helper that surfaces T-032 guard warnings).
- Produce repaired output as a task-versioned `pxfquery-T-033` asset. Do not modify the upstream T-021/D-004 bundle, T-024 workspace, T-026 loader, T-027 / T-028 / T-031 / T-032 artifacts, or any project-level raw materials in place.
- Record the source asset id, changed file(s), validation evidence, and downstream consumer of the repaired version in `5_report/repair_log.md` if a repair was performed.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may consume upstream T-027 / T-028 / T-031 / T-032 outputs and emit `pxfquery-T-033` as a corrected local version when needed.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary. Preserve lineage, validation evidence, and downstream consumer guidance.

### Resolver Discipline

- The resolver must be importable as a Python module and runnable inside the `pxfquery` conda env.
- Every example output (exact / proxy / not_found) must contain visible metadata: query input, intent, hit_level, used_cell, used_perturbation, query_name (for forward), top-K summary (for reverse), guard_warnings list, and pass/fail flag. Empty / placeholder evidence is not acceptable.
- The not-found example must be an explicit NOT_FOUND response — `found=False` with a clear not-found note — **not** an empty result or a fuzzy false-positive match.
- The exact example must reach `hit_level=EXACT` (same cell + same perturbation) without falling through to proxy.
- The proxy example must reach one of `PROXY_PERT` / `PROXY_CELL` / `PROXY_BOTH` with the proxy evidence visible in `resolver_meta`.
- The resolver must integrate (or document non-integration with) the T-031 no-hit guard semantics: nonsense perturbations must not silently fall through to fuzzy matches.
- The optional nature of the layer must be preserved: failure of this task or its validation must not block the deterministic forward/reverse package milestone; the recorded `5_report/completion.md` should explicitly state success or non-blocking failure.

### Execution Discipline

- All Python execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- Load indexes by reference through the T-027 runtime query index pack; load matrix data by reference through the T-028 function index pack and the T-026 loader path. Do not byte-copy T-021/D-004 JSON files into the hybrid resolver.
- The resolver module must run end-to-end against the T-027 symlinks + T-028 function index without additional setup beyond `pip install -e .` of the pxfquery workspace.

## Deliverables

1. `3_execution/pxfquery_T033_hybrid_fast_resolver.py` — the hybrid fast resolver module (`HybridFastResolver` or equivalent). (T-033/D-001, **core**)
2. `3_execution/example_exact_match.py`, `3_execution/example_proxy_match.py`, `3_execution/example_not_found.py` — three runnable example drivers. (T-033/D-002..D-004)
3. `4_artifact/5_table/pxfquery_T033_example_exact.json` — exact-match example evidence with visible metadata. (T-033/D-005)
4. `4_artifact/5_table/pxfquery_T033_example_proxy.json` — proxy-match example evidence. (T-033/D-006)
5. `4_artifact/5_table/pxfquery_T033_example_not_found.json` — not-found example evidence. (T-033/D-007)
6. `4_artifact/5_table/pxfquery_T033_examples_metadata.json` — single roll-up of resolver version, conda env, python version, key package versions, seed inputs, and pass/fail summary. (T-033/D-008)
7. `4_artifact/2_persist/pxfquery_T033_downstream_usage_notes.md` — English usage notes for the optional hybrid layer. (T-033/D-009)
8. `4_artifact/2_persist/pxfquery_T033_downstream_usage_notes_zh.md` — Chinese usage notes. (T-033/D-010)
9. `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex execution report (Chinese). (T-033/D-011, `stars: 5`)
10. `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex result report (Chinese). (T-033/D-012, `stars: 5`)
11. `4_artifact/registry.yaml` — T-033 deliverable registry.
12. `5_report/completion.md` — completion summary or non-blocking failure note.
13. `5_report/repair_log.md` — only if a local bug repair was required.

## Acceptance

- `HybridFastResolver` (or equivalent) imports successfully and runs end-to-end against the T-027 / T-028 inputs inside the `pxfquery` conda env.
- `example_exact_match.py` reports `hit_level=EXACT`, `found=True`, with a single chosen (cell, perturbation, query_name) and term counts visible in metadata.
- `example_proxy_match.py` reports `hit_level ∈ {PROXY_PERT, PROXY_CELL, PROXY_BOTH}`, `found=True`, with proxy evidence visible in metadata.
- `example_not_found.py` reports `found=False`, no activated/suppressed terms, and an explicit `NOT_FOUND` note. Nonsense perturbations do **not** fall through to fuzzy false positives.
- The metadata roll-up JSON contains resolver version, conda env, seed inputs, and per-example pass/fail flags for all three examples.
- The optional-layer contract is preserved: failure of any example (or all) does not block the deterministic forward/reverse milestone. The completion report explicitly states success or non-blocking failure.
- All upstream artifacts (T-021/D-004 bundle, T-024 workspace, T-026 loader, T-027 / T-028 / T-031 / T-032 deliverables) remain unmodified, except when an in-scope local repair copy named `pxfquery-T-033` is created and recorded in `5_report/repair_log.md`.

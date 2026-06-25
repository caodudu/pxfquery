# T-061 Legacy Source Digest Repair for M1

Date: 2026-06-24

## Scope And Provenance

This digest is a fresh T-061 replacement for the failed T-041 dependency role. T-041 artifacts were not read or reused as authoritative evidence. The source authority for locating the package is A-001/T-007, which identifies `code/pxfquery_package/` as the static code source and notes that `core.py` is the usable modern entry point while `main.py` is historical/incomplete.

Raw source inspection was limited to A-002, the registered symlink `1_asset/migrated_pxfquery_package_source`, resolving to:

`/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package`

No historical source root, T-041 output, matrix file, notebook, cache, or broad `2_project_asset/` scan was used.

## Bounded Read Method

Execution followed a static-only method:

1. Confirmed A-001 and A-002 symlinks resolved to the registered paths.
2. Used `find -H` only on `1_asset/migrated_pxfquery_package_source` so the task-local symlink was followed without leaving the registered package directory.
3. Recorded a filename/size inventory in `3_execution/a002_file_inventory_20260624.txt`.
4. Recorded Python line counts, symbol definitions, AST structure, and risk-pattern grep outputs in `3_execution/`.
5. Inspected targeted source windows for entry points, query behavior, indexes, resolver behavior, LLM coupling, plotting, and incomplete legacy sketches. Large modules were not dumped wholesale; extra windows were opened only for specific behavior-bearing symbols.

Inventory summary: 25 files total; 22 Python files; no notebooks or h5ad files were read. Largest Python files were `query/resolver.py` (1072 lines), `core.py` (477), `llm/prompts.py` (386), `llm/client.py` (337), and `viz/plots.py` (300).

## High-Level Package Shape

The migrated package is a usable but not production-clean skeleton for a LINCS perturbation-to-function workflow:

- Modern public facade: `core.PxFquery`.
- Deterministic query engines: `query.forward.ForwardQuery`, `query.reverse.ReverseQuery`.
- Result containers: `ForwardResult`, `ReverseResult`.
- Data loading: `data.loader.DataLoader` for local h5ad matrices.
- Index-backed resolver: `query.resolver.QueryResolver` with `ResolverConfig` and `ForwardPlan`.
- Lookup indexes: `CellLineIndex`, `DrugIndex`, `FunctionIndex`, `GeneIndex`.
- Optional LLM layer: `llm.client.LLMClient` and `llm.prompts`.
- Plotting helpers: `viz.plots`.
- Historical sketch: `main.py` and `prompt/check_link.py`.

## Reusable Pieces

### `query/forward.py`

`ForwardQuery.query()` matches a perturbation by `cmap_name` with fallback to `pert_id`, optionally filters by `cell_iname`, averages selected matrix rows, and returns top activated/suppressed functional terms through `ForwardResult`. This is the most direct reusable forward-query core for M1.

Reuse conditions:

- AnnData `.obs` must contain `pert_id`, `cmap_name`, and `cell_iname`.
- `.var_names` must be the functional terms to report.
- Fuzzy matching is simple and should be tested on realistic aliases before manuscript use.

### `query/reverse.py`

`ReverseQuery.query()` builds a target vector from activate/suppress terms, optionally filters by cell line, aggregates by `(cmap_name, cell_iname)`, ranks perturbations by cosine similarity, and reports driving terms. This is reusable for M1 reverse-query smoke tests and manuscript-grade examples after validation.

Reuse conditions:

- Reverse targets must map to actual matrix `var_names`.
- Empty or unmatched activate/suppress lists currently produce weak user feedback.
- Ranking is deterministic but biologically interpretive claims need downstream validation.

### `utils.py`

`fuzzy_match`, `build_target_vector`, and `cosine_similarity_matrix` are compact deterministic helpers. They are reusable, but `fuzzy_match` is intentionally simple and should not be treated as a robust biomedical synonym resolver.

### `index/*.py`

The index classes are reusable as adapters over precomputed JSON assets:

- `CellLineIndex`: validates cell names, canonicalizes case, traverses lineage/disease/subtype trees, and returns proxy cells.
- `DrugIndex`: exact alias lookup and structural neighbor lookup from compressed BRD neighbor records.
- `GeneIndex`: gene symbol lookup, matrix-gene membership, and semantic neighbors.
- `FunctionIndex`: exact/alias function lookup, var-name validation, labels, sources, and LLM list formatting.

Reuse conditions:

- Later tasks must provide the exact JSON files expected under an index directory.
- The classes do not build indexes; they only load existing files.
- Missing JSONs are hard failures at construction time.

### `logging_utils.py`

`LoggingSettings`, `QueryIdFilter`, `resolve_log_level`, and `configure_logger` are small reusable support utilities. File logging writes to caller-selected paths and can create directories.

### `viz/plots.py`

`plot_forward_bar`, `plot_reverse_table`, and `plot_heatmap` are reusable for exploratory or manuscript-supporting figures. Plotly and matplotlib imports are lazy inside plotting functions. Figures should still be visually checked in later figure-generation tasks.

## Adaptable Or Risky Pieces

### `core.py`

`PxFquery` is the preferred modern entry point. It wires `DataLoader`, forward/reverse engines, optional `LLMClient`, optional `QueryResolver`, and plotting.

Useful methods:

- `load_data(pert_type, path)`
- `load_data_dir(directory)`
- `load_llm(api_key, base_url, model, test)`
- `enable_resolver(index_dir=..., provider=..., ...)`
- `pert2func(...)`
- `func2pert(...)`
- `query(...)`
- `plot(...)`
- `list_loaded()`, `list_terms()`

Risks:

- Default resolver `index_dir` is `output/store/query_index`, which is not guaranteed relative to later task cwd.
- `load_data_dir` expects `xpr_func_ad.h5ad`, `sh_func_ad.h5ad`, and `cp_func_ad.h5ad`.
- `query()` without resolver requires LLM intent parsing; `enable_resolver()` also builds an API client unless provider is changed to `mock`.
- The package `__init__.py` usage example calls `load_data("path/to/xpr_func_ad.h5ad")`, but the actual method requires `load_data(pert_type, path)`.

Recommended M1 action: adapt `core.PxFquery` as the public API pattern, but explicitly configure matrix paths and index paths in current-task code rather than relying on defaults.

### `query/resolver.py`

The resolver is substantial and potentially valuable for M1.1, but it is too coupled to precomputed indexes and OpenAI-compatible LLM providers to treat as a low-risk M1 core.

Useful elements:

- `ResolverConfig` controls provider, model, evidence budgets, must-answer behavior, logging, and fast-path mode.
- `ForwardPlan` stores resolved perturbation, cell, proxy cells, and neighbor perturbations.
- `QueryResolver.resolve_and_query()` parses intent, dispatches forward/reverse, attaches `resolver_meta`, and records LLM call stats.
- Forward resolver evidence policy ranks `EXACT`, `PROXY_PERT`, `PROXY_CELL`, and `PROXY_BOTH`.
- Genetic forward queries can compare `xpr` and `sh` sources and choose the best evidence level.
- Reverse resolver maps function terms through `FunctionIndex` and `llm_map_function`.

Risks:

- Constructor eagerly loads all index JSONs and builds an OpenAI-compatible client unless provider is `mock`.
- Default provider is `minimax`; missing API keys raise errors.
- `must_answer=True` can create `FORCED_MATCH` or `FORCED_FALLBACK` results by text similarity, which must be clearly labeled and should not be used as strong evidence.
- Resolver touches protected `ForwardQuery._obs` internals for pair lookup.
- Fast parsing is heuristic and English cue-heavy.
- LLM prompt functions can raise unless `use_fast_path` catches specific failures.

Recommended M1 action: do not make resolver required for the first deterministic algorithm run-through. Treat it as M1.1 evidence-aware retrieval logic after index paths, mock hooks, and fallback labeling are tested.

### `llm/client.py` And `llm/prompts.py`

The LLM layer is optional and useful for natural-language parsing and summaries, but it is not safe as a deterministic M1 dependency.

Useful elements:

- `LLMClient.health_check()`, `parse_query()`, `summarize_forward()`, and `summarize_reverse()`.
- Prompt functions for intent parsing, cell-line mapping, gene/drug/function mapping, and summaries.
- JSON-cleaning and fallback summary helpers.

Risks:

- Requires API keys or provider credentials.
- Network/provider behavior affects reproducibility.
- `llm/prompts.py` includes provider-specific reasoning options for MiniMax.
- Results must not be cited as primary algorithmic evidence without deterministic metadata.

Recommended M1 action: permit only optional narrative summaries or resolver-assisted mapping in later tasks. Use deterministic query outputs as manuscript evidence.

### `data/loader.py`

`DataLoader` is a simple adapter for local h5ad loading and is appropriate for current workflows if matrix paths are explicitly supplied. Its `download_zenodo()` method is intentionally unimplemented.

Risks:

- Imports `anndata` only at load time.
- Reads actual h5ad matrices, which this digestion task did not inspect.
- Uses `print()` for load messages.

## Incomplete Or Historical Pieces

### `main.py`

`main.py` defines a lowercase `pxfquery` class with many methods containing only `pass`: `load_pxf`, `load_anno`, `pert2func`, `func2pert`, `_parse_user_query`, `_bio_match`, `_pert_match`, `_func_match`, `_summary_p2f`, `_summary_f2p`, `plot_pert2func`, and `plot_func2pert`. It also imports heavier exploratory packages (`scanpy`, `seaborn`, `openai`) and calls `check_link` in `load_llm`.

Classification: historical/incomplete. Do not reuse for M1 implementation except as a record of early design intent.

### `prompt/check_link.py`

`check_link()` is an ad hoc API connectivity helper that imports analysis/plotting libraries unrelated to connection checking and performs direct `client.chat.completions.create()` calls.

Classification: historical/risky. Do not reuse as M1 runtime code.

### Empty `data/__init__.py` And `viz/__init__.py`

These are harmless but provide no behavior.

## Forbidden For Downstream M1/M1.1 Use

- T-041 outputs as source authority.
- Historical source root files outside A-002.
- `main.py` as an implementation base.
- `prompt/check_link.py` as production connectivity logic.
- Any claim that resolver forced fallbacks are exact evidence.
- Any reuse that requires reading raw matrices, notebooks, caches, or binary files during source-digest interpretation.

## Data And Index Access Patterns

Matrix data:

- `DataLoader.load_local()` reads caller-supplied `.h5ad` paths with `anndata.read_h5ad`.
- `load_all_local()` expects `xpr_func_ad.h5ad`, `sh_func_ad.h5ad`, and `cp_func_ad.h5ad`.
- Query engines assume matrix rows are observations and columns are functional terms.

Index data:

- Resolver default index directory: `output/store/query_index`.
- Required JSON filenames include `cellline_index.json`, `cellline_neighbors.json`, `gene_index_simple.json`, `gene_neighbors_simple.json`, `drug_index.json`, `drug_neighbors.json`, and `function_index.json`.
- Index classes load JSON files directly and do not validate complete schema beyond normal key access.

LLM/API:

- `LLMClient` falls back to `OPENAI_API_KEY`, `SILICONFLOW_API_KEY`, or `PXFQUERY_API_KEY`.
- Resolver defaults to provider `minimax`, uses `MINIMAX_API_KEY` or `OPENAI_API_KEY`, and default base URL `https://api.minimax.chat/v1`.
- Provider `mock` avoids client construction in resolver, but prompt hooks or fast paths must be configured for useful behavior.

## M1/M1.1 Recommendation

For M1 deterministic algorithm run-through:

1. Use `core.PxFquery` only as a reference for facade shape, or instantiate it with explicit matrix paths.
2. Use `DataLoader`, `ForwardQuery`, `ReverseQuery`, `ForwardResult`, `ReverseResult`, and `utils` as primary reusable logic.
3. Use index classes only when the current task explicitly registers the JSON index directory.
4. Exclude `main.py`, `prompt/check_link.py`, and required LLM/API behavior.

For M1.1 evidence-aware retrieval:

1. Adapt `QueryResolver` after deterministic tests cover index presence, pair lookup, evidence levels, forced fallback labeling, and provider/mock behavior.
2. Treat `EXACT`, `PROXY_PERT`, `PROXY_CELL`, and `PROXY_BOTH` as ordered evidence categories.
3. Treat `FORCED_MATCH` and `FORCED_FALLBACK` as exploratory only unless manually reviewed.
4. Keep LLM output as mapping/summarization support, not as primary biological evidence.

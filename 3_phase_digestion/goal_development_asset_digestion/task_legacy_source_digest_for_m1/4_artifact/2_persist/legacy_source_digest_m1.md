# Legacy Source Digest for M1

Generated: 2026-06-24
Task: T-041 legacy_source_digest_for_m1
Source inspected: `A-003 → legacy_flat_asset_library_v20260614/code/pxfquery_package/`

## Package Structure

```
pxfquery_package/
├── __init__.py          # Exports PxFquery; version 0.1.0
├── core.py              # Modern entry point: PxFquery class
├── main.py              # Legacy stub class (pxfquery, all pass) — DO NOT USE
├── pyproject.toml       # Package metadata, deps (anndata, numpy, pandas, plotly, matplotlib, openai)
├── README.md            # Old Windows paths only — obsolete
├── utils.py             # fuzzy_match, build_target_vector, cosine_similarity_matrix
├── logging_utils.py     # LoggingSettings, configure_logger, QueryIdFilter
├── data/
│   ├── __init__.py      # Empty
│   └── loader.py        # DataLoader: load_local, load_all_local, get, download_zenodo (NotImplementedError)
├── query/
│   ├── __init__.py      # Exports forward, reverse, resolver classes
│   ├── forward.py       # ForwardQuery, ForwardResult
│   ├── reverse.py       # ReverseQuery, ReverseResult
│   └── resolver.py      # QueryResolver, ResolverConfig, ForwardPlan
├── index/
│   ├── __init__.py      # Exports CellLineIndex, DrugIndex, FunctionIndex, GeneIndex
│   ├── cellline_index.py
│   ├── drug_index.py
│   ├── gene_index.py
│   └── function_index.py
├── llm/
│   ├── __init__.py      # Exports LLMClient
│   ├── client.py        # LLMClient: health_check, parse_query, summarize_forward, summarize_reverse
│   └── prompts.py       # All resolver prompt functions (llm_parse_intent, llm_map_*, llm_summarize_*)
├── viz/
│   ├── __init__.py      # Empty
│   └── plots.py         # plot_forward_bar, plot_reverse_table, plot_heatmap
├── prompt/
│   ├── __pycache__/
│   └── check_link.py    # Legacy health check — DO NOT USE; superseded by LLMClient.health_check
```

## Reusable Components for M1

### 1. Package Entry Point (core.py)
- `class PxFquery` is the modern API entry point.
- Methods: `load_data`, `load_data_dir`, `load_llm`, `enable_resolver`, `pert2func`, `func2pert`, `query`, `plot`, `list_loaded`, `list_terms`.
- **Recommendation**: T046 should use core.py as the API template. The `PxFquery` class interface is clean and well-documented.

### 2. Data Loader (data/loader.py)
- `DataLoader` loads local h5ad matrices (xpr/sh/cp) using anndata.
- `load_local(pert_type, path)` and `load_all_local(directory)` are usable patterns.
- `download_zenodo()` raises `NotImplementedError` — not reusable.
- **Recommendation**: T048 should reuse the loader API pattern directly. The interface is stable.

### 3. Forward Query (query/forward.py)
- `ForwardQuery` takes AnnData, implements `query(perturbation, cell_line, top_n)` and `list_perturbations`, `list_cell_lines`.
- `ForwardResult` holds scores, top_activated, top_suppressed, found flag, note.
- Fuzzy matching via `utils.fuzzy_match`.
- **Recommendation**: T048/T049 should reuse forward.py logic as-is or with minimal adaptation. The no-hit behavior (`ForwardResult.empty`) is a well-defined pattern.

### 4. Reverse Query (query/reverse.py)
- `ReverseQuery` implements `query(activate, suppress, cell_line, top_k, aggregate)`.
- Uses cosine similarity against a target vector built by `utils.build_target_vector`.
- `ReverseResult` holds candidates_df with similarity, driving_terms.
- **Recommendation**: T049 should reuse reverse.py as the reverse-query reference. The driving_terms logic is useful for manuscript tables.

### 5. Index Wrappers (index/*.py)
All four index classes are well-structured and self-contained:

| Class | File | Runtime JSON | Status |
|---|---|---|---|
| CellLineIndex | cellline_index.py | cellline_index.json, cellline_neighbors.json | Ready |
| DrugIndex | drug_index.py | drug_index.json, drug_neighbors.json | Ready |
| GeneIndex | gene_index.py | gene_index_simple.json, gene_neighbors_simple.json | Ready |
| FunctionIndex | function_index.py | **function_index.json MISSING** | Ready but asset absent |

- **Recommendation**: T052 should use these index wrapper classes. FunctionIndex requires rebuilding function_index.json first.

### 6. Utilities (utils.py)
- `fuzzy_match(query, candidates, top_n)` — reusable string matching.
- `build_target_vector(term_names, activate, suppress)` — reusable for reverse query.
- `cosine_similarity_matrix(matrix, vec)` — reusable for ranking.
- **Recommendation**: Reusable as-is.

### 7. Logging (logging_utils.py)
- `LoggingSettings`, `configure_logger`, `QueryIdFilter` — clean and reusable.
- **Recommendation**: Reuse in T048/T049 for structured logging.

### 8. Visualization (viz/plots.py)
- `plot_forward_bar`, `plot_reverse_table`, `plot_heatmap` with plotly and matplotlib backends.
- **Recommendation**: T052 may reference these as figure templates, but should verify output quality for manuscript readiness.

## Risky / Non-Reusable Parts

### 1. main.py — Legacy Stub
- All methods are `pass`. Imports old stack (scanpy, seaborn, OpenAI directly). **DO NOT USE** for M1.

### 2. Resolver Pipeline (query/resolver.py)
- **Risk HIGH**: Contains hard-coded defaults with old workspace paths:
  - `index_dir: str = "output/store/query_index"` (line 161)
  - `log_dir: str = "report/04_management/logs"` (line 169)
- Mixes LLM calls directly via `openai.OpenAI`.
- `_call_prompt` dispatches to `llm.prompts.*` functions that make real LLM API calls.
- `llm_parse_intent` and `llm_map_*` paths are fragile (6/9 LLM stability).
- `use_fast_path=True` provides a deterministic fallback but is less featureful.
- genetic_multi_source logic (xpr+sh) adds complexity.
- **Recommendation**: T049 may reference resolver architecture (L1-L4 proxy levels) but should NOT reuse the resolver class directly without significant adaptation. New code should:
  - Replace hard-coded paths with configurable project-root-relative paths.
  - Decouple LLM prompts into a separate optional module.
  - Use hybrid_fast as default; keep full LLM as optional add-on.

### 3. LLM Client (llm/client.py)
- Depends on `openai` package and external API keys.
- `health_check`, `parse_query`, `summarize_forward`, `summarize_reverse` work but are network-dependent.
- Falls back to `_empty_intent()` on parse failure — graceful but may hide errors.
- **Recommendation**: Keep as an optional module for manuscript summarization but do not make it a required dependency.

### 4. LLM Prompt Functions (llm/prompts.py)
- All functions make real API calls via `_chat_text` / `_chat_json`.
- `llm_parse_intent` uses MiniMax-specific reasoning_split extra_body — vendor lock-in risk.
- **Recommendation**: Reference the prompt structure but treat as optional/inspirational.

### 5. prompt/check_link.py
- Legacy health check with full scanpy/seaborn imports — **DO NOT USE**.

### 6. README.md
- Contains only old Windows paths (`D:\Projects\...`). **DO NOT USE**.

### 7. pyproject.toml
- Build system uses `setuptools.backends.legacy:build` — outdated. T046 should update to modern `setuptools` or `hatchling`.

### 8. Hard-Coded Path Risks Throughout
- `core.py:156`: `index_dir: str = "output/store/query_index"`
- `core.py:169`: `log_dir: str = "report/04_management/logs"`
- `core.py:396`: `save: Optional[str] = None` — example shows `'output/picture/fig1.png'`
- `logging_utils.py:27`: `log_dir: str = "report/04_management/logs"`
- `resolver.py` passes hard-coded index_dir to index constructors.
- **All must be replaced** with configurable or project-relative paths in M1 tasks.

## Data / Index Access Summary

### Migrated Runtime Indexes (Available in data/query_indexes/)
| Index File | Used By | Status |
|---|---|---|
| cellline_index.json | CellLineIndex | Present |
| cellline_neighbors.json | CellLineIndex | Present |
| drug_index.json | DrugIndex | Present |
| drug_neighbors.json | DrugIndex | Present |
| gene_index_simple.json | GeneIndex | Present |
| gene_neighbors_simple.json | GeneIndex | Present |
| cellline_tree.json | (not used in code, present in flat lib) | Present |
| gene_index.json | (full, not used by simple wrapper) | Present |
| gene_neighbors.json | (full, not used by simple wrapper) | Present |

### Missing Runtime Index
| Index File | Used By | Gap |
|---|---|---|
| function_index.json | FunctionIndex | NOT FOUND in migrated data/query_indexes/ — builder exists at index_builders/M-0373 |

### Matrix Data (data/functional_matrices/)
- xpr_func_ad.h5ad, sh_func_ad.h5ad, cp_func_ad.h5ad — present as raw assets but unverified for current-project compatibility.

## Guidance for Downstream M1 Tasks

| Task | Allowed Legacy References | Forbidden Legacy References |
|---|---|---|
| **T046** (Package scaffolding) | `core.py` API design, `__init__.py` exports, `pyproject.toml` deps list | `main.py`, `prompt/`, old README, legacy build config |
| **T048** (Data loading + forward query) | `data/loader.py` API, `query/forward.py` logic, `utils.py` fuzzy_match | `resolver.py` old paths, `main.py`, LLM dependencies |
| **T049** (Reverse query) | `query/reverse.py` logic, `utils.py` build_target_vector + cosine_similarity_matrix, resolver L1-L4 proxy concepts | Full `resolver.py` reuse with hard-coded paths; unstable LLM paths for core logic |
| **T052** (Index layer) | All 4 index classes in `index/*.py` as-is | Direct JSON path assumptions (`output/store/query_index/`); function_index.json dependency without rebuild |


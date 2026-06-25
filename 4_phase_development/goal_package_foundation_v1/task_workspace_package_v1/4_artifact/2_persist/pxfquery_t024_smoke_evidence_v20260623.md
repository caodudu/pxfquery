# T-024 Import/Compile Smoke Evidence Log

Generated: 2026-06-23

## Environment

- **Timestamp**: 2026-06-23T07:00
- **Python**: 3.10.20 (main, Mar 11 2026, 17:43:48) [Clang 20.1.8]
- **Interpreter**: /Users/dudu/Softwares/miniconda/envs/pxfquery/bin/python
- **Conda env**: pxfquery
- **Source**: legacy_flat_asset_library_v20260614/code/pxfquery_package/

## Workspace Repairs

| Issue | Source | Fix |
|-------|--------|-----|
| `build-backend = "setuptools.backends.legacy:build"` (typo) | Legacy `pyproject.toml` line 3 | Changed to `setuptools.build_meta` in workspace-level `pyproject.toml` |
| `version = "0.1.0-t024"` (PEP440 failure) | Workspace `pyproject.toml` | Changed to `"0.1.0"` to pass setuptools validation |

## Import Smoke

```
$ python -c "from pxfquery import PxFquery; print('import OK')"
import OK
class: PxFquery
```

Import succeeded.

## Compile Smoke (py_compile)

All 22 .py modules compiled without errors:

| Module | Status |
|--------|--------|
| __init__.py | PASS |
| core.py | PASS |
| data/__init__.py | PASS |
| data/loader.py | PASS |
| index/__init__.py | PASS |
| index/cellline_index.py | PASS |
| index/drug_index.py | PASS |
| index/function_index.py | PASS |
| index/gene_index.py | PASS |
| llm/__init__.py | PASS |
| llm/client.py | PASS |
| llm/prompts.py | PASS |
| logging_utils.py | PASS |
| main.py | PASS |
| prompt/check_link.py | PASS |
| query/__init__.py | PASS |
| query/forward.py | PASS |
| query/resolver.py | PASS |
| query/reverse.py | PASS |
| utils.py | PASS |
| viz/__init__.py | PASS |
| viz/plots.py | PASS |

22 / 22 PASS (100%)

## Integrity Check

- `__init__.py` byte-identical to legacy source: MD5 `47165121ab56ed5cc7b08bdf0c87b75f` (both files match)
- No `__pycache__` files copied from legacy source
- Legacy asset library remains unmodified

## Divergence Summary

The only intentional divergence from the legacy package is in the workspace-level `pyproject.toml`:

- Package name: `pxfquery` → `pxfquery-T-024` (task-versioned)
- `build-backend`: `setuptools.backends.legacy:build` → `setuptools.build_meta` (fix)
- `[tool.setuptools.packages.find].where`: `["."]` → `["src"]`

All source `.py` files remain byte-identical copies of the legacy source.
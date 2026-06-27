# PxFquery

PxFquery is a Python package for natural-language perturbation queries over local PxFquery digital assets. The intended runtime path is:

```text
natural-language query
  -> LLM/rule-assisted parse
  -> entity and context routing
  -> local index lookup
  -> local functional matrix query
  -> structured route result, trace events, and warnings
```

The public Python entry point is:

```python
from pxfquery import PxFQuery
```

The README documents one primary interface: the `PxFQuery` namespace workflow. Other internal modules are not public user entry points.

## Current Status

Version `0.1.3` establishes the public client shape and source-first package layout. It does not yet complete the full data-backed runtime query path. The next tasks must connect the workflow to the existing local digital assets and make the internal route trace/warning system real.

Do not read the current repository as a finished data-query engine yet. Read it as the source package under active convergence toward that engine.

## Install From Source

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
python -m pip install pytest PyYAML
```

Wheel installation is not the project workflow.

## Local Data Assets

PxFquery should query the existing local assets, not invented demo data. The large matrices and indexes live in the local project workspace and are tracked through CyHex task lineage:

```text
/Users/dudu/Documents/3_Project/12_PxFquery
```

Core runtime asset lineage:

| CyHex source | Asset | Runtime role |
| --- | --- | --- |
| T-021/T-026 | `cp_func_ad.h5ad` | compound perturbation function matrix, `201014 x 91` |
| T-021/T-026 | `sh_func_ad.h5ad` | shRNA perturbation function matrix, `189365 x 91` |
| T-021/T-026 | `xpr_func_ad.h5ad` | overexpression perturbation function matrix, `132464 x 91` |
| T-027 | runtime query indexes | drug, gene, cell line, and neighbor lookup |
| T-028 | `function_index.json` | validated 91-function index |

See `docs/data_assets.md` for the current asset map. A later task must add the runtime data loader/configuration entry point; until then, route outputs are not sufficient evidence of real matrix querying.

## LLM Provider

Register the provider before provider-dependent parsing, routing, or checks:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()

pxf.settings.register_llm(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
    mode="real",
)
```

Set the key outside Python:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
```

Provider check:

```python
check = pxf.settings.provider_check(timeout=30)
print(check.to_dict())
```

## Standard Workflow

The standard Python workflow is stepwise:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()

pxf.settings.register_llm(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
    mode="real",
)

q = pxf.read.query("Which drugs activate apoptosis in A549 cells?")
pxf.pp.parse(q)
pxf.tl.resolve(q)

result = pxf.get.result(q)
print(result["route_type"])
print(result["diagnostics"])
```

Namespace roles:

| Namespace | Role |
| --- | --- |
| `pxf.settings` | runtime/provider configuration |
| `pxf.read` | create query inputs |
| `pxf.pp` | parse and normalize inputs |
| `pxf.tl` | route and resolve queries |
| `pxf.get` | retrieve structured outputs |

`q` is a lightweight work object with `text`, `obs`, and `uns` fields.

## Internal Route Trace Target

T-127 will formalize structured parse and route events. The intended trace target is:

```text
[pxfquery] settings.provider  name=llm_gateway/deepseek-ai/deepseek-v4-flash mode=real registered=true
[pxfquery] read.query         text="Which drugs activate apoptosis in A549 cells?"
[pxfquery] pp.normalize       language=en biomedical_terms=3
[pxfquery] pp.parse           direction=reverse perturbation_type=compound context=A549
[pxfquery] route.index        drug_index=T-027/runtime_query_index/drug_index.json
[pxfquery] route.index        cellline_index=T-027/runtime_query_index/cellline_index.json
[pxfquery] route.index        function_index=T-028/function_index.json terms=91
[pxfquery] tl.route           route_type=exact-hit confidence=high
[pxfquery] tl.resolve         matrix=T-021/cp_func_ad.h5ad shape=201014x91 candidates=2
[pxfquery] warning            code=provider.real_check_required level=info message="real provider route should be checked for LLM-dependent runs"
[pxfquery] get.result         route_type=exact-hit schema=2026-06-27
```

This is a design target, not a saved execution log.

## Tests

```bash
python -m pytest -q tests
```

Current source test target:

```text
56 passed
```

## Version

```python
import pxfquery
from pxfquery import PxFQuery

pxf = PxFQuery()

print(pxfquery.__version__)
print(pxf.version)
```

Current version:

```text
0.1.3
```

## Release Notes

Each public version is tied to a CyHex task and an immutable Git tag.

- `v0.1.0`: MS7 recovery package baseline
- `v0.1.1`: version governance
- `v0.1.2`: single-class API baseline
- `v0.1.3`: namespace workflow baseline

See `CHANGELOG.md`, `docs/release_policy.md`, `docs/development_task_policy.md`, and `docs/data_assets.md`.

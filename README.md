# PxFquery

PxFquery is a Python package for natural-language perturbation queries. It turns biomedical questions such as "Which drugs activate apoptosis in A549 cells?" into structured route metadata, perturbation resolution, function-response records, diagnostics, and suggestions.

The public Python entry point is intentionally small:

```python
from pxfquery import PxFQuery
```

The client follows a scverse-style workflow: configure runtime settings, read a query into a small work object, preprocess it, run tools, then retrieve results.

## Install

Install from source during development:

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

Install test dependencies:

```bash
python -m pip install pytest PyYAML
```

## Quick Start

```python
from pxfquery import PxFQuery

pxf = PxFQuery()

q = pxf.read.query("Which drugs activate apoptosis in A549 cells?")
pxf.pp.parse(q)
pxf.tl.resolve(q)

result = pxf.get.result(q)
print(result["route_type"])
print(result["function_response"])
```

For scripts, the client also provides one-step convenience methods:

```python
result = pxf.query("What happens to KRAS knockdown in A549?")
intent = pxf.parse("What happens to KRAS knockdown in A549?")
```

Those methods use the same `read -> pp -> tl -> get` workflow internally.

## Real LLM Route Check

Register the provider before running provider-dependent checks or queries:

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

check = pxf.settings.provider_check(timeout=30)
print(check.to_dict())

q = pxf.read.query(
    "Run with registered llm_gateway/deepseek-ai/deepseek-v4-flash and record the route."
)
pxf.pp.parse(q)
pxf.tl.resolve(q)
print(pxf.get.result(q)["provider"])
```

Set the API key outside Python:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
```

Use disabled mode only as an explicit negative control:

```python
pxf = PxFQuery(provider_mode="disabled")
q = pxf.read.query("What happens to KRAS knockdown in A549?")
pxf.pp.parse(q)
pxf.tl.resolve(q)
print(pxf.get.result(q)["diagnostics"]["warnings"])
```

## Workflow API

The main namespaces are:

| Namespace | Role | Example |
| --- | --- | --- |
| `pxf.settings` | runtime/provider configuration | `pxf.settings.register_llm(...)` |
| `pxf.read` | create query or corpus inputs | `q = pxf.read.query(text)` |
| `pxf.pp` | parse and normalize inputs | `pxf.pp.parse(q)` |
| `pxf.tl` | route and resolve queries | `pxf.tl.resolve(q)` |
| `pxf.get` | retrieve structured outputs | `pxf.get.result(q)` |

`q` is a lightweight `PxFQueryData` object with:

- `q.text`: original query text
- `q.obs`: per-query observations
- `q.uns`: parsed intent, route, result, provider metadata, and diagnostics

## Internal Trace Preview

T-127 will formalize the internal parse pipeline and event/warning system. The intended developer-facing trace shape is:

```text
[pxfquery] read.query         text="Which drugs activate apoptosis in A549 cells?"
[pxfquery] settings.provider  name=llm_gateway/deepseek-ai/deepseek-v4-flash mode=real registered=true
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

This block is a design preview, not a saved execution log. The implementation task will make these events structured and testable.

## Data Assets

PxFquery is intended to query the local PxFquery digital assets, not invented demo data. The large matrices and indexes are kept in the local project workspace and tracked through CyHex task lineage.

See `docs/data_assets.md` for the current local asset map, including:

- T-021/T-026 functional matrices: `cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`
- T-027 runtime query indexes: drug, gene, cell line, and neighbor indexes
- T-028 function index: 91 validated function terms

## CLI Demo

```bash
pxfquery parse "What happens to KRAS knockdown in A549?"
pxfquery query "Which drugs activate apoptosis in A549 cells?" --json
```

Run the MS7 corpus:

```bash
pxfquery run-corpus \
  --corpus tests/fixtures/ms7_execution_corpus_v20260627.yaml \
  --jsonl /tmp/pxfquery_ms7.jsonl \
  --summary /tmp/pxfquery_ms7_summary.json
```

Provider route check:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
pxfquery provider-check \
  --provider llm_gateway/deepseek-ai/deepseek-v4-flash \
  --mode real \
  --json
```

## Tests

```bash
python -m pytest -q tests
```

The current release target is:

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
- `v0.1.3`: scverse-style workflow API and corrected provider-first README

See `CHANGELOG.md`, `docs/release_policy.md`, and `docs/development_task_policy.md` for task-linked release discipline.

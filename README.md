# PxFquery

PxFquery is a Python package for natural-language and semi-structured perturbation query routing. It parses user queries into structured intents, resolves route types, executes deterministic forward/reverse query engines, and exposes both Python API and CLI surfaces.

## Features

- Natural-language parser for forward and reverse biological perturbation queries
- Route classification: `exact-hit`, `proxy-hit`, `no-hit`, `ambiguous-hit`, `context-missing`, `transfer/suggestion`
- Four engine entry points:
  - forward drug
  - forward genetic
  - reverse drug
  - reverse genetic
- Python API and command-line interface
- Provider honesty check for `llm_gateway/deepseek-ai/deepseek-v4-flash`
- MS7 regression corpus fixture and tests

## Version

```python
import pxfquery

print(pxfquery.__version__)
```

Current version:

```text
0.1.1
```

## Install From Source

From a local checkout:

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

The editable source install is the recommended development path. Wheel install is only for release candidate reproduction:

```bash
python -m pip install dist/pxfquery-0.1.1-py3-none-any.whl
```

## Python Usage

Use the `PxFQuery` class as the main API:

```python
from pxfquery import PxFQuery

client = PxFQuery()

intent = client.parse("What happens to KRAS knockdown in A549?")
print(intent["direction"])

result = client.query("Which drugs activate apoptosis in A549 cells?")
print(result["route_type"])
print(result["function_response"])
```

The module-level functions are still available for short scripts:

```python
from pxfquery import query

result = query("Which drugs activate apoptosis in A549 cells?")
print(result["route_type"])
```

## LLM Provider Registration

PxFquery does not hard-code secrets. Register an OpenAI-compatible provider route, then run a provider check:

```python
from pxfquery import PxFQuery

client = PxFQuery()
client.register_llm_provider(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
)

check = client.provider_check(mode="real", timeout=30)
print(check.to_dict())
```

Or register globally:

```python
from pxfquery import register_llm_provider, get_llm_provider, list_llm_providers

register_llm_provider(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
)

print(get_llm_provider("llm_gateway/deepseek-ai/deepseek-v4-flash"))
print(list_llm_providers())
```

Set the key outside the code:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
```

## CLI Usage

Parse a query:

```bash
pxfquery parse "What happens to KRAS knockdown in A549?"
```

Run a query:

```bash
pxfquery query "Which drugs activate apoptosis in A549 cells?" --json
```

Run the bundled MS7 corpus:

```bash
pxfquery run-corpus \
  --corpus tests/fixtures/ms7_execution_corpus_v20260627.yaml \
  --jsonl /tmp/pxfquery_ms7.jsonl \
  --summary /tmp/pxfquery_ms7_summary.json
```

Provider route check with local llm_gateway. The CLI uses the built-in default registration for `llm_gateway/deepseek-ai/deepseek-v4-flash`, and the key comes from `LLM_GATEWAY_API_KEY`:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
pxfquery provider-check \
  --provider llm_gateway/deepseek-ai/deepseek-v4-flash \
  --mode real \
  --json
```

Disabled provider negative control:

```bash
pxfquery provider-check \
  --provider llm_gateway/deepseek-ai/deepseek-v4-flash \
  --mode disabled \
  --json
```

## Demo Tests

Install test dependencies:

```bash
python -m pip install -e .
python -m pip install pytest PyYAML
```

Run all tests:

```bash
python -m pytest -q tests
```

Expected current result:

```text
54 passed
```

Run only the MS7 corpus test:

```bash
python -m pytest -q tests/test_ms7/test_corpus.py
```

Run a quick CLI smoke test:

```bash
pxfquery query "What happens to KRAS knockdown in A549?" --json
```

Expected fields include:

- `route_type`
- `query_context`
- `perturbation_resolution`
- `function_response`
- `diagnostics`
- `intent`

## Build

```bash
python setup.py sdist bdist_wheel
```

The package exposes a console script named `pxfquery`.

## Release Discipline

Each package version is tied to a specific CyHex task and Git tag. New versions must not overwrite old versions.

- Current version: `0.1.1`
- Current CyHex task: `T-124 task_ms7_version_governance_v011`
- Current Git tag: `v0.1.1`
- Previous preserved tag: `v0.1.0`

For future changes:

1. Create or use one CyHex task for one change direction.
2. Bump `src/pxfquery/_version.py`.
3. Update `CHANGELOG.md` and `docs/releases/`.
4. Run tests.
5. Commit and push to GitHub.
6. Tag the exact commit as `vX.Y.Z` and push the tag.

# PxFquery

PxFquery is a Python package for natural-language perturbation queries. It parses biomedical query text, resolves route types, runs deterministic forward/reverse query engines, and returns machine-readable evidence routing metadata.

The public Python interface is intentionally narrow:

```python
from pxfquery import PxFQuery
```

Everything users need is available from a `PxFQuery` instance.

## Install From Source

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

Editable source install is the default development workflow. Wheel install is for release reproduction:

```bash
python -m pip install dist/pxfquery-0.1.2-py3-none-any.whl
```

## Quick Start

```python
from pxfquery import PxFQuery

pxf = PxFQuery()

intent = pxf.parse("What happens to KRAS knockdown in A549?")
print(intent["direction"])
print(intent["perturbation_identity"])

result = pxf.query("Which drugs activate apoptosis in A549 cells?")
print(result["route_type"])
print(result["function_response"])
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
0.1.2
```

## LLM Provider

PxFquery does not hard-code secrets. Register an OpenAI-compatible provider on the client:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.register_llm_provider(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
)

check = pxf.provider_check(mode="real", timeout=30)
print(check.to_dict())
```

Set the key outside Python:

```bash
export LLM_GATEWAY_API_KEY="<your-local-gateway-key>"
```

Provider inspection also stays on the client:

```python
print(pxf.get_llm_provider("llm_gateway/deepseek-ai/deepseek-v4-flash"))
print(pxf.list_llm_providers())
```

## CLI

The CLI mirrors the client methods for smoke tests and demos.

```bash
pxfquery parse "What happens to KRAS knockdown in A549?"
pxfquery query "Which drugs activate apoptosis in A549 cells?" --json
```

Run the bundled MS7 corpus:

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

Disabled provider negative control:

```bash
pxfquery provider-check \
  --provider llm_gateway/deepseek-ai/deepseek-v4-flash \
  --mode disabled \
  --json
```

## Tests

```bash
python -m pip install -e .
python -m pip install pytest PyYAML
python -m pytest -q tests
```

Expected current result:

```text
55 passed
```

Run the MS7 corpus test only:

```bash
python -m pytest -q tests/test_ms7/test_corpus.py
```

## Build

```bash
python setup.py sdist bdist_wheel
```

## Public API Contract

The intended user-facing Python import is:

```python
from pxfquery import PxFQuery
```

Top-level function imports are not part of the public API contract. Internal modules remain available for package implementation and tests, but downstream user code should use the `PxFQuery` class.

## Release Discipline

Each package version is tied to a specific CyHex task and Git tag. New versions must not overwrite old versions.

- Current version: `0.1.2`
- Current CyHex task: `T-125 task_ms7_public_api_single_class_v012`
- Current Git tag: `v0.1.2`
- Preserved tags: `v0.1.0`, `v0.1.1`

For future changes:

1. Create or use one CyHex task for one change direction.
2. Bump `src/pxfquery/_version.py`.
3. Update `CHANGELOG.md` and `docs/releases/`.
4. Run tests.
5. Commit and push to GitHub.
6. Tag the exact commit as `vX.Y.Z` and push the tag.

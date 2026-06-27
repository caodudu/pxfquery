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

## Install

From a local checkout:

```bash
python -m pip install -e .
```

Or install from a built wheel:

```bash
python -m pip install dist/pxfquery-0.1.0-py3-none-any.whl
```

## Python Usage

```python
from pxfquery import parse, query, run_corpus, summarize_records

intent = parse("What happens to KRAS knockdown in A549?")
print(intent["direction"])

result = query("Which drugs activate apoptosis in A549 cells?")
print(result["route_type"])
print(result["function_response"])
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

Provider route check with local llm_gateway:

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
50 passed
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

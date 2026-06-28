# PxFquery

PxFquery is a Python package for asking biomedical perturbation questions in natural language.

It is designed for evidence routing over a local PxFquery resource pack: a user asks in biological language, PxFquery interprets the question, routes it to available perturbation-function resources, and returns a readable answer with evidence and limitations.

Example questions:

```text
Which perturbations increase a requested biological function in a disease model?
How does a perturbation change functional programs in a disease model?
Find perturbations associated with a requested phenotype in available models.
```

This package version is an L1-L2-L3 repair package. It does not claim final L4 evidence assembly or L5 human answer rendering.

## Install

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
python -m pip install pytest PyYAML
```

PxFquery is source-install first.

## Basic Use

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.settings.use_deepseek(token="...", timeout=60)
pxf.resources.use("/path/to/pxfquery_resource_pack")
q = pxf.read.query("Which perturbations increase a requested biological function in a disease model?")
pxf.pp.parse(q)
pxf.pp.route(q)
pxf.tl.execute(q)

execution = pxf.get.execution(q)
```

The L3 execution payload contains:

- how PxFquery interpreted the question
- the selected L2 route plan
- extracted matrix-backed route results
- empty-hit or resource errors when a route cannot be executed

Programmatic output is still available:

```python
route = pxf.get.route(q)
execution = pxf.get.execution(q)
```

Stepwise use follows a scanpy-style interface. This is the user interface; the five numbered folders are the internal functional layers.

```python
pxf = PxFQuery()
pxf.settings.use_deepseek(token="...", timeout=60)
pxf.resources.use("/path/to/pxfquery_resource_pack")
q = pxf.read.query("Which perturbations increase a requested biological function in a disease model?")
pxf.pp.parse(q)
pxf.pp.route(q)
pxf.tl.execute(q)
execution = pxf.get.execution(q)
```

`tl.assemble()` and final answer rendering are later L4/L5 responsibilities. The current repaired path is L1 parse, L2 route, and L3 execute.

Direct legacy matrix query helpers are intentionally not exposed in this L3 package source.

## Resource Pack

PxFquery uses a local resource pack containing perturbation matrices, indexes, and metadata. Normal users should think about this as one PxFquery resource pack, not as individual matrix/index files.

Current local-pack flow:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.resources.use("/path/to/pxfquery_resource_pack")
print(pxf.resources.status())
```

Download flow:

```python
pxf = PxFQuery()
pxf.resources.download()
```

The download/cache implementation is planned for the unified resource manager. Current tests use explicit local resource-pack paths.

## Interface Layers

PxFquery source is organized into explicit layers.

```text
User biomedical question
  -> pxfquery.l1_intent
  -> pxfquery.l2_routing
  -> pxfquery.l3_execution
  -> pxfquery.l4_evidence
  -> pxfquery.l5_presentation
```

The current `0.5.5.dev1` implementation keeps the five-layer structure and repairs L3 execution against current L2 route plans. `l1_intent` parsing requires a configured OpenAI-compatible LLM provider. L3 biological scores come from loaded functional matrices and resource-pack indexes.

## Current Status

Version `0.5.5.dev1` keeps the package capabilities inside the layered source architecture and repairs L3 execution:

- `pxfquery.l1_intent` parses the user's biomedical question into resolver-compatible intent through the configured LLM provider.
- `pxfquery.l2_routing` performs resource-backed route planning with exact/proxy/unresolved dimensions.
- `pxfquery.l3_execution` extracts matrix-backed function scores or reverse perturbation candidates from L2 route plans.
- `pxfquery.l4_evidence` is reserved for downstream evidence assembly.
- `pxfquery.l5_presentation` is reserved for downstream answer rendering and plots.

The package root is intentionally thin. Product code lives inside the five visible layer directories.

## Test

```bash
export PXFQUERY_LLM_API_KEY="..."
python -m pytest -q tests
```

The L1 contract test makes one real DiyGateway request. If the gateway is unavailable or the token is missing, the test fails.

Current source test target:

```text
23 passed, 1 skipped
```

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current version:

```text
0.5.5.dev1
```

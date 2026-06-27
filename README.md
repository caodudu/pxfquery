# PxFquery

PxFquery is a Python package for asking biomedical perturbation questions in natural language.

It is designed for evidence routing over a local PxFquery resource pack: a user asks in biological language, PxFquery interprets the question, routes it to available perturbation-function resources, and returns a readable answer with evidence and limitations.

Example questions:

```text
Which perturbations increase a requested biological function in a disease model?
How does a perturbation change functional programs in a disease model?
Find perturbations associated with a requested phenotype in available models.
```

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
answer = pxf.ask("Which perturbations increase a requested biological function in a disease model?")

print(answer)
```

The default answer is meant for a biomedical reader. It contains:

- how PxFquery interpreted the question
- biological results
- evidence used
- biological interpretation
- limitations

Programmatic output is still available:

```python
payload = answer.to_dict()
structured = answer.structured_result
diagnostics = answer.diagnostics
```

Stepwise use follows a scanpy-style interface. This is the user interface; the five numbered folders are the internal functional layers.

```python
pxf = PxFQuery()
q = pxf.read.query("Which perturbations increase a requested biological function in a disease model?")
pxf.pp.parse(q)
pxf.tl.route(q)
pxf.tl.execute(q)
pxf.tl.assemble(q)
result = pxf.get.result(q)
answer = pxf.get.answer(q)
```

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

The download/cache implementation is not active in `0.4.0`; `resources.download()` reports that official resource-pack download is not configured and asks users to provide a local pack for now.

## Interface Layers

PxFquery source is organized into explicit layers.

```text
User biomedical question
  -> pxfquery.l1_nlu
  -> pxfquery.l2_routing
  -> pxfquery.l3_execution
  -> pxfquery.l4_evidence
  -> pxfquery.l5_presentation
```

The current `0.4.0` implementation does not hard-code demo entities, scores, ranked candidates, or matrix hits. Natural-language intent parsing is present; biological hits require later resource-backed routing and query execution.

## Current Status

Version `0.4.0` corrects the source architecture:

- `pxfquery.l1_nlu` parses the user's biomedical question into surface intent.
- `pxfquery.l2_routing` decides what downstream evidence capabilities are required.
- `pxfquery.l3_execution` is the resource-pack query layer and does not fabricate results before implementation.
- `pxfquery.l4_evidence` assembles structured evidence from actual layer outputs.
- `pxfquery.l5_presentation` renders the biomedical answer.

The package root is intentionally thin. Product code lives inside the five visible layer directories.

## Test

```bash
python -m pytest -q tests
```

Current source test target:

```text
14 passed
```

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current version:

```text
0.4.0
```

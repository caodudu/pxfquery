# PxFquery

PxFquery is a Python package for asking biomedical perturbation questions in natural language.

It is designed for evidence routing over a local PxFquery resource pack: a user asks in biological language, PxFquery interprets the question, routes it to available perturbation-function resources, and returns a readable answer with evidence and limitations.

Example questions:

```text
Which drugs may activate apoptosis in lung cancer?
What does EGFR inhibition do to functional programs in A549?
Are there perturbations that suppress MYC targets in breast cancer models?
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
answer = pxf.ask("Which drugs may activate apoptosis in lung cancer?")

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

## Demo Notebooks

The `demo/` folder is the current GitHub-facing observation surface for MS8 package behavior:

- `demo/01_drug_forward.ipynb`: drug perturbation -> function response
- `demo/02_drug_reverse.ipynb`: desired function -> ranked drugs
- `demo/03_genetic_forward.ipynb`: genetic perturbation -> function response
- `demo/04_genetic_reverse.ipynb`: desired function -> ranked genetic perturbations

These notebooks are designed to evolve into the paper application scenes for later figures.

## Resource Pack

PxFquery uses a local resource pack containing perturbation matrices, indexes, and metadata. Normal users should think about this as one PxFquery resource pack, not as individual matrix/index files.

Current local-pack flow:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.resources.use("/path/to/pxfquery_resource_pack")
print(pxf.resources.status())
```

Planned default flow:

```python
pxf = PxFQuery()
pxf.resources.download()
```

The download/cache implementation is not active yet in `0.2.1`; `resources.download()` reports that official resource-pack download is planned and asks users to provide a local pack for now.

For compatibility, the older registration API remains available:

```python
pxf.register_assets(root="/path/to/standard_resources")
pxf.register_assets(manifest="assets.yaml")
```

## Interface Layers

PxFquery separates the user-facing interface from the internal kernel.

```text
User biomedical question
  -> natural-language interpretation
  -> evidence routing
  -> resource-pack query execution
  -> evidence assembly
  -> biological result presentation
```

Internal route status, JSON payloads, trace events, and matrix filenames are kept as structured/debug surfaces. They should not be the primary user experience.

## Current Status

Version `0.2.1` provides the layered product skeleton plus GitHub-previewable demo notebooks:

- `PxFQuery.ask(...)` returns a human-readable `PxFQueryAnswer`.
- `PxFQuery.query(...)` keeps the structured dictionary interface for tests and integrations.
- `pxf.resources.status()`, `pxf.resources.use(...)`, and `pxf.resources.download(...)` provide the resource-pack management surface.
- CLI `pxfquery query "..."` prints a readable answer by default; `--json` prints the structured payload.

Important limitation: the biological query kernel still uses the earlier placeholder resolver internals. The new interface is the product skeleton for later MS8 work; real resource-pack-backed query execution is the next implementation layer.

## Test

```bash
python -m pytest -q tests
```

Current source test target:

```text
62 passed
```

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current version:

```text
0.2.1
```

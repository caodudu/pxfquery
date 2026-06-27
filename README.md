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
pxf.settings.use_deepseek(token="...", timeout=60)
pxf.load_data_dir("/path/to/functional_matrices")
pxf.enable_resolver(index_dir="/path/to/query_indexes", api_key="...")
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
pxf.settings.use_deepseek(token="...", timeout=60)
pxf.load_data_dir("/path/to/functional_matrices")
pxf.enable_resolver(index_dir="/path/to/query_indexes", api_key="...")
q = pxf.read.query("Which perturbations increase a requested biological function in a disease model?")
pxf.pp.parse(q)
pxf.tl.route(q)
pxf.tl.execute(q)
pxf.tl.assemble(q)
result = pxf.get.result(q)
answer = pxf.get.answer(q)
```

Direct matrix queries are also available:

```python
forward = pxf.pert2func("EGFR", pert_type="xpr", cell_line="A549")
reverse = pxf.func2pert(
    activate=["HALLMARK_APOPTOSIS"],
    suppress=["HALLMARK_MYC_TARGETS_V1"],
    pert_type="cp",
    cell_line="A549",
)
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

The download/cache implementation is not active in `0.5.1`; `resources.download()` reports that official resource-pack download is not configured and asks users to provide a local pack for now.

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

The current `0.5.1` implementation restores the original matrix-backed forward/reverse query core and resolver architecture. `l1_intent` parsing requires a configured OpenAI-compatible LLM provider. Biological hits come from loaded functional matrices and query indexes.

## Current Status

Version `0.5.1` keeps the restored package capabilities inside the layered source architecture and repairs the L1 intent provider boundary:

- `pxfquery.l1_intent` parses the user's biomedical question into resolver-compatible intent through the configured LLM provider.
- `pxfquery.l2_routing` performs index-backed entity resolution and exact/proxy evidence routing.
- `pxfquery.l3_execution` loads functional matrices and runs forward/reverse perturbation-function queries.
- `pxfquery.l4_evidence` assembles route metadata, function scores, candidates, and diagnostics.
- `pxfquery.l5_presentation` renders biomedical answers and plots.

The package root is intentionally thin. Product code lives inside the five visible layer directories.

## Test

```bash
export PXFQUERY_LLM_API_KEY="..."
python -m pytest -q tests
```

The L1 contract test makes one real DiyGateway request. If the gateway is unavailable or the token is missing, the test fails.

Current source test target:

```text
10 passed
```

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current version:

```text
0.5.1
```

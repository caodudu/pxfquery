# PxFquery

PxFquery asks natural-language questions against local perturbation data assets.

Example question:

```text
Which drugs activate apoptosis in A549 cells?
```

Expected answer shape:

```text
route type -> exact-hit / proxy-hit / no-hit / ambiguous-hit / context-missing
context    -> cell line, disease, direction, perturbation type
evidence   -> matrix/index sources used by the query
result     -> ranked perturbations or function scores
warnings   -> missing fields, disabled provider, ambiguous entities, fallback routes
```

## Install

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
python -m pip install pytest PyYAML
```

PxFquery is source-install first. Wheel installation is not the project workflow.

## Register Data

PxFquery does not hard-code one machine's data path. Register your local assets before querying.

Use a manifest when files can move:

```yaml
# assets.yaml
root: /path/to/pxfquery_assets
assets:
  matrix.cp_func_ad:
    path: matrices/cp_func_ad.h5ad
    role: compound perturbation function matrix
  matrix.sh_func_ad:
    path: matrices/sh_func_ad.h5ad
    role: shRNA perturbation function matrix
  matrix.xpr_func_ad:
    path: matrices/xpr_func_ad.h5ad
    role: overexpression perturbation function matrix
  index.drug_index:
    path: indexes/drug_index.json
    role: drug lookup index
  index.gene_index:
    path: indexes/gene_index.json
    role: gene lookup index
  index.cellline_index:
    path: indexes/cellline_index.json
    role: cell line lookup index
  index.function_index:
    path: indexes/function_index.json
    role: function lookup index
```

Then register it:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.register_assets(manifest="assets.yaml")
```

You can also register a folder that contains the standard filenames:

```python
pxf.register_assets(root="/path/to/standard_resources")
```

## Register LLM

Register an OpenAI-compatible provider before LLM-assisted parsing or route checks:

```python
pxf.register_llm_provider(
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

## Ask A Query

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.register_assets(manifest="assets.yaml")
pxf.register_llm_provider(
    "llm_gateway/deepseek-ai/deepseek-v4-flash",
    base_url="http://localhost:3000/v1",
    api_key_env="LLM_GATEWAY_API_KEY",
    model="deepseek-ai/deepseek-v4-flash",
    mode="real",
)

result = pxf.ask("Which drugs activate apoptosis in A549 cells?")
```

## Example Output

Current abridged output:

```json
{
  "route_type": "exact-hit",
  "query_context": {
    "cell_line": "A549",
    "cell_line_source": "exact",
    "tissue_lineage": "lung",
    "disease": "NSCLC",
    "perturbation_type": "compound",
    "direction": "reverse",
    "normalization_state": "PxFquery deterministic route"
  },
  "function_response": {
    "status": "OK",
    "matrix_source": "registered_assets",
    "scores": [
      {
        "pert_id": "BRD-K70401845",
        "cmap_name": "erlotinib",
        "score": 1.31,
        "rank": 1
      },
      {
        "pert_id": "BRD-K68045993",
        "cmap_name": "gefitinib",
        "score": 1.07,
        "rank": 2
      }
    ],
    "function_terms": [
      "activate apoptosis",
      "apoptosis",
      "MYC targets",
      "EGFR signaling",
      "KRAS signaling"
    ]
  },
  "confidence": "high",
  "diagnostics": {
    "warnings": [],
    "indexes_searched": [
      "drug_index.json",
      "gene_index.json",
      "function_index.json"
    ],
    "matrices_searched": [
      "cp_func_ad.h5ad",
      "sh_func_ad.h5ad",
      "xpr_func_ad.h5ad"
    ],
    "free_text_query": true
  },
  "asset_registry": {
    "registered_before_query": true,
    "keys": [
      "index.cellline_index",
      "index.drug_index",
      "index.function_index",
      "index.gene_index",
      "matrix.cp_func_ad",
      "matrix.sh_func_ad",
      "matrix.xpr_func_ad"
    ]
  },
  "schema_version": "2026-06-27"
}
```

## Current Limitation

Version `0.1.4` registers data assets and includes them in query output metadata. The remaining runtime work is to replace the current deterministic resolver internals with direct reads from the registered indexes and matrices.

In plain terms: the package now has the right public setup and output contract, but the next implementation step must make every route and score come from the registered data files rather than resolver placeholders.

## Test

```bash
python -m pytest -q tests
```

Current source test target:

```text
59 passed
```

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current version:

```text
0.1.4
```

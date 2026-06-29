# PxFquery

**PxFquery** is a natural-language query engine for perturbation biology. It converts biological questions into structured perturbation-function queries, searches **LINCS / Connectivity Map-style signature matrices**, and returns ranked evidence with tables, figures, reports, command-line output, and MCP-compatible responses.

## Core Idea

PxFquery treats a biological question as a query program:

```text
biological question
  -> LLM semantic parsing
  -> perturbation / function / context / direction / query-mode routing
  -> LINCS / CMap-style matrix evidence retrieval
  -> ranked biological answer, figures, report, and reusable evidence object
```

The language model is used to understand the question. The biological answer is produced from perturbation signature matrices, functional score matrices, metadata, and resource indexes.

## Traditional Lookup vs PxFquery

| If you use LINCS / CMap manually | If you use PxFquery |
| --- | --- |
| You translate the biological question into keywords by hand. | You ask the biological question directly. |
| You decide which compound, gene, cell line, and matrix to search. | PxFquery resolves entities, context, modality, and query direction. |
| You run separate steps for forward and reverse questions. | One interface handles perturbation-to-function and function-to-perturbation queries. |
| You compare tables and then make figures yourself. | PxFquery returns ranked answers, evidence tables, figures, and an HTML report. |
| You write a separate wrapper for scripts or AI tools. | The same result can be used from Python, CLI, chat, reports, or MCP. |

This design connects manuscript-style biological questions with computable perturbation-function evidence.

## Example Questions

**Forward: perturbation to function**

```text
For EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition, and are inflammatory or MAPK-related programs affected?
```

PxFquery resolves the perturbation, context, modality, and functional programs, then ranks matrix-backed functional responses.

**Reverse: function to perturbation**

```text
In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response and preservation of oxidative phosphorylation?
```

PxFquery resolves the desired functional state and searches perturbations associated with that profile.

## Outputs

PxFquery is designed to produce material a biological reader can inspect directly:

| Output | What it shows |
| --- | --- |
| Answer summary | The main biological pattern found for the question. |
| Ranked results | Perturbations or functional programs ordered by the matrix evidence. |
| Evidence table | Matched compounds, genes, contexts, routes, scores, and source fields. |
| Figures | Bar plots, bubble plots, heatmaps, and evidence-flow panels generated from the query result. |
| HTML report | A readable report with the question, interpreted query, ranked evidence, figures, and method overview. |
| Chat follow-up | Continued discussion over the same evidence object. |
| CLI and MCP | The same query engine exposed to terminals, pipelines, and external AI software. |

The Python API, command line, HTML report, chat interface, and MCP server all reuse the same parsed evidence object.

## Data Scope

PxFquery works with a resource pack built from perturbational signature resources:

- compound perturbation matrices
- shRNA/RNAi and overexpression-style genetic perturbation matrices
- functional gene-set score matrices
- perturbation, gene, compound, and cell-context metadata
- lookup indexes for biological names and aliases

Resource files are managed automatically. PxFquery uses a packaged Zenodo manifest and downloads the required matrices, metadata, and indexes into the user's cache when a query needs them.

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
print(pxf.resources.status())
```

Advanced users who maintain a local mirror can mount it explicitly with `pxf.resources.use("/path/to/pxfquery_resource_pack")`.

## Installation

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

PxFquery requires Python 3.10 or newer.

## Language Model Configuration

PxFquery uses a configured language-model endpoint for semantic query parsing and evidence-grounded follow-up discussion. The endpoint is not fixed to one provider.

Environment-variable configuration:

```bash
export PXFQUERY_LLM_API_KEY="..."
export PXFQUERY_LLM_BASE_URL="https://your-provider.example/v1"
export PXFQUERY_LLM_MODEL="your-model-name"
export PXFQUERY_LLM_PROVIDER="your-provider-name"
```

Python configuration:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.settings.register_llm_provider(
    name="my-provider",
    token="...",
    base_url="https://your-provider.example/v1",
    model="your-model-name",
    timeout=60,
)
```

For users who choose DeepSeek, a convenience helper is available:

```python
pxf.settings.use_deepseek(token="...", timeout=60)
```

## Quick Start

```python
from pxfquery import PxFQuery

pxf = PxFQuery()

forward = pxf.tl.parse(
    "In EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition, and are inflammatory or MAPK-related programs affected?",
    top_n=10,
)
pxf.tl.answer(forward)
forward_answer = pxf.get.answer(forward)

reverse = pxf.tl.parse(
    "In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response and preservation of oxidative phosphorylation?",
    top_n=10,
)
pxf.tl.answer(reverse)
reverse_answer = pxf.get.answer(reverse)

print(forward_answer.summary)
print(reverse_answer.biological_results[:5])
```

`pxf.tl.parse()` performs semantic parsing, route selection, matrix query execution, and evidence assembly. `pxf.tl.answer()` renders the assembled evidence for user-facing output.

## Python Output

```python
answer = pxf.ask(
    "For EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition?",
    mode="python",
)

print(answer.headline)
print(answer.summary)
print(answer.biological_results[:5])
```

The answer object contains:

- `summary`: biological interpretation
- `biological_results`: ranked functional programs or perturbation candidates
- `evidence`: matched context, evidence grade, route summary, and provenance fields
- `tables`: display-ready evidence tables
- `figures`: figure specifications used by HTML and file outputs

## Figures and HTML Reports

```python
q = pxf.tl.parse(
    "For a breast tumor context, which treatments are associated with reduced ERBB2 signaling and increased apoptosis?",
    top_n=10,
)
pxf.tl.answer(q)

pxf.tl.figures(q, output_dir="pxfquery_figures", format="png")
pxf.tl.figures(q, output_dir="pxfquery_figures_svg", format="svg")
pxf.tl.answer(q, mode="html", output="breast_tumor_erbb2_report.html")
```

HTML reports include the original question, interpreted biological question, ranked evidence table, process overview, figures, and evidence provenance.

## Follow-up Discussion

```python
q = pxf.tl.parse(
    "For EGFR-driven lung adenocarcinoma models, summarize perturbations that reduce MAPK-related programs and inflammatory signatures.",
    top_n=10,
)
pxf.tl.answer(q)

pxf.tl.chat(q, "Summarize the strongest biological patterns and the supporting evidence.")
print(pxf.get.chat(q))
```

Follow-up answers use the assembled PxFquery result and preserve the ranked programs, scores, candidates, and citations supplied by the evidence package.

## Command Line

```bash
pxfquery answer "In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response and preservation of oxidative phosphorylation?"

pxfquery answer \
  "In a lung cancer setting, find perturbations associated with lower inflammatory signaling and low proliferative signature." \
  --mode html \
  --output lung_cancer_inflammation_report.html

pxfquery figures \
  "For a breast tumor context, which treatments are associated with reduced ERBB2 signaling and increased apoptosis?" \
  --output-dir breast_tumor_erbb2_figures \
  --format png

pxfquery chat \
  "For EGFR-driven lung adenocarcinoma models, summarize perturbations that reduce MAPK-related programs and inflammatory signatures." \
  "Explain the main biological patterns and supporting evidence."
```

If configuration is stored in an environment file:

```bash
pxfquery --env-file .env answer "Which genetic perturbations may reduce MYC-related programs in a breast cancer context while preserving oxidative phosphorylation?"
```

## Optional Public Annotation

Additional public-database annotation can be attached after the primary matrix-backed result:

```python
q = pxf.tl.parse(
    "Which compounds are associated with suppression of interferon response in a lung cancer context?",
    top_n=10,
)
pxf.tl.anno(q, sources=("pubmed", "pubchem", "chembl"))

annotation = q.uns["annotation_evidence"]
```

## MCP Interface

PxFquery can be exposed as an MCP server for compatible external analysis environments:

```bash
python -m pxfquery.mcp_server --env-file .env
```

Available MCP tools:

- `pxfquery_parse_answer`: run a query and return the evidence-grounded answer payload
- `pxfquery_render_figures`: run a query and write figure files
- `pxfquery_l5_chat`: answer a follow-up question using the assembled evidence

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current package version:

```text
0.5.7.dev0
```

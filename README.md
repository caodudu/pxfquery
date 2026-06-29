# PxFquery

PxFquery is a Python package for querying perturbation-function evidence from natural-language biological questions. It is designed for exploratory analysis of LINCS / Connectivity Map-style perturbational signatures, especially questions that connect compounds, genetic perturbations, cell contexts, and functional gene-set programs.

The package supports two common query directions:

```text
Forward: In EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition, and are inflammatory or MAPK-related programs affected?

Reverse: In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response while avoiding strong MYC activation?
```

Both are returned as structured evidence reports with ranked functional results or perturbation candidates, route information, limitations, figures, and optional conversational follow-up.

## What PxFquery Provides

- Natural-language perturbation queries for drug and genetic perturbation settings.
- Forward queries: what functional programs change after a perturbation.
- Reverse queries: which perturbations are associated with a requested functional state.
- Matrix-backed evidence from LINCS / Connectivity Map-style perturbation resources.
- Compound, shRNA/RNAi, and overexpression-style perturbation modalities when the corresponding matrices are available.
- Optional public annotation from sources such as PubMed, PubChem, and ChEMBL.
- Python, command-line, HTML report, figure, and MCP interfaces.
- Publication-oriented visual outputs, including ranked score bars, bubble plots, heatmaps, evidence-path diagrams, and evidence-limit panels.

The output should be read as a structured summary of perturbational evidence: what was matched in the resource pack, which functional programs were ranked, where proxy evidence was used, and what limitations should accompany the interpretation.

## Installation

```bash
git clone git@github.com:caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

PxFquery requires Python 3.10 or newer.

## Configuration

PxFquery uses a configured language-model endpoint to interpret the user's question and to support evidence-constrained follow-up discussion. The endpoint is not fixed to one provider; any compatible provider can be registered through environment variables:

```bash
export PXFQUERY_LLM_API_KEY="..."
export PXFQUERY_LLM_BASE_URL="https://your-provider.example/v1"
export PXFQUERY_LLM_MODEL="your-model-name"
export PXFQUERY_LLM_PROVIDER="your-provider-name"
```

You can also configure a provider inside Python:

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

For users who choose DeepSeek, the convenience helper is:

```python
pxf.settings.use_deepseek(token="...", timeout=60)
```

Resource files are managed automatically. PxFquery uses a packaged Zenodo manifest and downloads the required LINCS / Connectivity Map-derived matrices, functional gene-set scores, metadata, and lookup indexes into the user's cache when a query needs them.

```python
print(pxf.resources.status())
```

Advanced users who maintain a local mirror of the resource pack can mount it explicitly with `pxf.resources.use("/path/to/pxfquery_resource_pack")`.

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
    "In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response while avoiding strong MYC activation?",
    top_n=10,
)
pxf.tl.answer(reverse)
reverse_answer = pxf.get.answer(reverse)

print(forward_answer.summary)
print(reverse_answer.biological_results[:5])
```

`pxf.tl.parse()` runs the evidence search. `pxf.tl.answer()` converts the evidence into a user-facing answer object without changing the underlying evidence.

## Python Output

The answer object contains:

- `summary`: a concise biological interpretation.
- `biological_results`: ranked functional programs or perturbation candidates.
- `evidence`: context, evidence grade, matched rows, and route status.
- `limitations`: evidence limits that should be reported with the result.
- `tables`: display-ready evidence tables.
- `figures`: figure specifications used by HTML and file outputs.

Forward-query example:

```python
answer = pxf.ask(
    "For EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition?",
    mode="python",
)

print(answer.headline)
print(answer.summary)
```

Reverse-query example:

```python
answer = pxf.ask(
    "Which perturbations suppress inflammatory response in a lung cancer context?",
    mode="python",
)

print(answer.headline)
print(answer.summary)
```

## Figures

PxFquery can write figure files directly from the evidence result:

```python
q = pxf.tl.parse(
    "For a breast tumor context, which treatments are associated with reduced ERBB2 signaling and increased apoptosis?",
    top_n=10,
)
pxf.tl.answer(q)

pxf.tl.figures(q, output_dir="pxfquery_figures", format="png")
pxf.tl.figures(q, output_dir="pxfquery_figures_svg", format="svg")
```

Current figure types include:

- ranked evidence score bar plot
- result magnitude bubble plot
- primary score heatmap
- query evidence path diagram
- evidence limits panel

These figures are designed for rapid biological review and manuscript-supporting exploratory reports, not as a substitute for independent statistical validation.

## HTML Report

HTML reports are intended for sharing a readable query result with collaborators:

```python
q = pxf.tl.parse(
    "In a lung cancer setting, find perturbations associated with lower inflammatory signaling without a strong proliferative signature.",
    top_n=10,
)
pxf.tl.answer(q, mode="html", output="lung_cancer_inflammation_report.html")
```

The report includes the original question, interpreted biological question, main evidence table, process overview, figures, and evidence limits. It avoids exposing internal package labels in the user-facing report.

## Follow-up Chat

After evidence is assembled, users can ask follow-up questions constrained to the same evidence:

```python
q = pxf.tl.parse(
    "For EGFR-driven lung adenocarcinoma models, summarize perturbations that reduce MAPK-related programs and report any evidence limitations.",
    top_n=10,
)
pxf.tl.answer(q)

pxf.tl.chat(q, "Summarize the strongest evidence and the main limitations.")
print(pxf.get.chat(q))
```

The chat interface is evidence-constrained. It is not allowed to add new candidates, change scores, invent citations, or upgrade weak evidence.

## Command Line

The command-line interface is useful for scripted queries and report generation:

```bash
pxfquery answer "In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response while avoiding strong MYC activation?"

pxfquery answer \
  "In a lung cancer setting, find perturbations associated with lower inflammatory signaling without a strong proliferative signature." \
  --mode html \
  --output lung_cancer_inflammation_report.html

pxfquery figures \
  "For a breast tumor context, which treatments are associated with reduced ERBB2 signaling and increased apoptosis?" \
  --output-dir breast_tumor_erbb2_figures \
  --format png

pxfquery chat \
  "For EGFR-driven lung adenocarcinoma models, summarize perturbations that reduce MAPK-related programs and report any evidence limitations." \
  "Explain the main evidence and limitations."
```

If configuration is stored in an environment file:

```bash
pxfquery --env-file .env answer "Which genetic perturbations may reduce MYC-related programs in a breast cancer context while preserving oxidative phosphorylation?"
```

## Optional Annotation

Additional public-database annotation can be attached after the primary evidence result:

```python
q = pxf.tl.parse(
    "Which compounds are associated with suppression of interferon response in a lung cancer context?",
    top_n=10,
)
pxf.tl.anno(q, sources=("pubmed", "pubchem", "chembl"))

annotation = q.uns["annotation_evidence"]
```

Annotation is optional. It supplements the matrix-backed result and does not replace the primary evidence route.

## MCP Interface

PxFquery can be exposed as an MCP server for compatible external analysis environments:

```bash
python -m pxfquery.mcp_server --env-file .env
```

Available MCP tools:

- `pxfquery_parse_answer`: run a query and return the evidence-grounded answer payload.
- `pxfquery_render_figures`: run a query and write figure files.
- `pxfquery_l5_chat`: answer a follow-up question using the assembled evidence.

The MCP interface returns structured evidence and display payloads. The calling application remains responsible for how it presents the result to the user.

## Example Questions

Forward perturbation questions:

```text
For EGFR-driven lung adenocarcinoma models, what functional programs are changed by EGFR inhibition?
For a breast tumor context, what functions go up or down after trastuzumab treatment?
In melanoma models, does MEK inhibition suppress MAPK-related programs and alter inflammatory signatures?
```

Reverse evidence questions:

```text
In a lung adenocarcinoma model, which perturbations are linked to suppression of inflammatory response while avoiding strong MYC activation?
Find compounds linked to increased oxidative phosphorylation in a cancer cell context.
Which genetic perturbations may reduce MYC-related programs in a breast cancer context while preserving oxidative phosphorylation?
```

## Interpreting Results

A PxFquery result should be read as an evidence summary from the configured LINCS / Connectivity Map-style resource pack:

- High-ranked rows indicate stronger matrix-backed associations within the available data.
- Functional programs are derived from perturbational signature scores, not from de novo pathway enrichment performed at query time.
- Proxy matches should be treated as weaker support than exact context or perturbation matches.
- Partial evidence should be reported with its limitations.
- Absence of evidence is not evidence of absence.
- Results are hypothesis-generating unless followed by independent biological validation.

## Version

```python
import pxfquery
print(pxfquery.__version__)
```

Current package version:

```text
0.5.7.dev0
```

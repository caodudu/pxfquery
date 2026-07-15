# PxFquery

PxFquery is a natural-language query and functional analysis tool for large-scale perturbation signatures. It supports two query directions:

- **Perturbation-to-function**: identify functional programs associated with a drug or genetic perturbation.
- **Function-to-perturbation**: retrieve drug or genetic perturbation candidates associated with a requested functional state.

Each query returns a readable answer and structured result tables, and can generate query-specific evidence figures and an HTML report.

![PxFquery query workflow](docs/pxfquery_core_idea.png)

Try the web interface: https://caodudu-pxfquery-web.hf.space/

## Installation

Python 3.10 or later is required.

```bash
git clone https://github.com/caodudu/pxfquery.git
cd pxfquery
python -m pip install -e .
```

## Configuration

Configure an LLM endpoint before running a query:

```bash
export PXFQUERY_LLM_API_KEY="..."
export PXFQUERY_LLM_BASE_URL="https://your-provider.example/v1"
export PXFQUERY_LLM_MODEL="your-model-name"
export PXFQUERY_LLM_PROVIDER="your-provider-name"
```

`DEEPSEEK_API_KEY`, `DEEPSEEK_API_BASE`, and `DEEPSEEK_MODEL` are also supported. When both sets of variables are present, `PXFQUERY_LLM_*` takes precedence.

## Run a query

After installation and configuration, run a query from the terminal:

```bash
pxfquery answer "In A549 lung cancer cells, what functional programs are changed by doxorubicin treatment?"
```

Or use Python:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
answer = pxf.ask(
    "In A549 lung cancer cells, what functional programs are changed by doxorubicin treatment?"
)
print(answer)
```

Both interfaces run the same query path. The `answer` object also retains structured results, tables, figures, and evidence fields for use in notebooks or downstream code.

## Resources and output

On the first query, PxFquery automatically downloads the required indexes and matrices from its bundled resource manifest into a local cache. External CSV files are normally not required.

To write files:

```bash
pxfquery answer "In A549 lung cancer cells, what functional programs are changed by doxorubicin treatment?" \
  --mode html --output result.html

pxfquery figures "In A549 lung cancer cells, what functional programs are changed by doxorubicin treatment?" \
  --output-dir figures --format pdf
```

## AI workflow integration (MCP)

PxFquery can run as a local MCP server for AI applications that support MCP. The package installation above already includes the MCP dependency.

The following OpenCode example uses an `.env` file containing the LLM configuration above. `/absolute/path/to/python` must be the Python interpreter in the environment where PxFquery is installed:

```json
{
  "mcp": {
    "pxfquery": {
      "type": "local",
      "enabled": true,
      "command": [
        "/absolute/path/to/python",
        "-m",
        "pxfquery.mcp_server",
        "--env-file",
        "/absolute/path/to/.env"
      ]
    }
  }
}
```

Once OpenCode starts, PxFquery is available as MCP tools for queries, figure generation, and follow-up questions over the current query result.

## Paper

For the methodological background and results, see the associated manuscript: *PxFquery: A Tool for Large Language Model–Assisted Functional Analysis of Large-Scale Perturbation Signatures*.

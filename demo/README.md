# PxFquery Demos

These notebooks are small, executed examples for the public GitHub repository.

Recommended reading order:

1. `01_forward_query.ipynb` - perturbation-to-function query.
2. `02_reverse_query.ipynb` - function-to-perturbation query.
3. `03_figures.ipynb` - figure generation and notebook preview.
4. `04_client_object.ipynb` - client API, answer object, and save/load.
5. `05_chat.ipynb` - evidence-grounded follow-up chat.
6. `06_mcp_placeholder.ipynb` - placeholder for a future MCP demo.

Before running the notebooks, install the package and configure an LLM provider:

```bash
python -m pip install -e .
export PXFQUERY_LLM_API_KEY="..."
export PXFQUERY_LLM_BASE_URL="https://your-provider.example/v1"
export PXFQUERY_LLM_MODEL="your-model-name"
export PXFQUERY_LLM_PROVIDER="your-provider-name"
```

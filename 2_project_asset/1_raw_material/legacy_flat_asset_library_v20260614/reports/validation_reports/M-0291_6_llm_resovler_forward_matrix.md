# 6_llm_resovler Forward Matrix Test

- Time: 2026-04-10 14:09:19
- Mode: mock hooks (deterministic)

| Query | Expected | Got | Found | Pass |
|------|----------|-----|-------|------|
| `CASE_EXACT_GENE` | `EXACT` | `EXACT` | `True` | `True` |
| `CASE_PROXY_PERT_GENE` | `PROXY_PERT` | `PROXY_PERT` | `True` | `True` |
| `CASE_PROXY_CELL_GENE_BY_DISEASE` | `PROXY_CELL` | `PROXY_CELL` | `True` | `True` |
| `CASE_UNKNOWN_CELL_INPUT` | `PROXY_CELL` | `PROXY_CELL` | `True` | `True` |
| `CASE_PROXY_BOTH_GENE` | `PROXY_BOTH` | `PROXY_BOTH` | `True` | `True` |
| `CASE_EXACT_DRUG` | `EXACT` | `EXACT` | `True` | `True` |
| `CASE_PROXY_PERT_DRUG` | `PROXY_PERT` | `PROXY_PERT` | `True` | `True` |
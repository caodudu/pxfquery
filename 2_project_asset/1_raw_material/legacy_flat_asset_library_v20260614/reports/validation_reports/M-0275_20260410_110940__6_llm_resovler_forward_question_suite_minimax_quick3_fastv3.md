# Forward Question Suite (minimax)

- Time: 2026-04-10 11:09:40
- Provider: minimax
- Model: MiniMax-M2.7
- Query Count: 3
- No Summary: True
- Suite Time (s): 0.825

| ID | Found | HitLevel | Source | Query |
|----|-------|----------|--------|-------|
| `Q1_exact_gene_cell` | `True` | `EXACT` | `sh` | In A549, what pathways are affected by EGFR knockdown? |
| `Q2_disease_not_cellname` | `True` | `PROXY_CELL` | `sh` | In non-small cell lung carcinoma, what happens if EGFR is suppressed? |
| `Q3_unknown_cell_label` | `True` | `PROXY_CELL` | `sh` | For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown? |

## Prompt Timing Total

```json
{}
```

## Detailed Results

### Q1_exact_gene_cell
- Query: `In A549, what pathways are affected by EGFR knockdown?`
- Found: `True`
- Hit Level: `EXACT`
- Selected Source: `sh`
- Composite Mode: `genetic_multi_source`
- Timing (s): `0.638`

Prompt Timing:
```json
{}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "EXACT",
  "pert_type": "sh",
  "pert_class": "genetic",
  "evidence_policy": {
    "max_forward_evidence": 15,
    "budget_exact": 1,
    "budget_proxy_pert": 4,
    "budget_proxy_cell": 4,
    "budget_proxy_both": 6
  },
  "cell_resolution_reason": "exact_cell_name",
  "requested_cell": "A549",
  "used_cell": "A549",
  "requested_perturbation": "EGFR",
  "used_perturbation": "EGFR",
  "proxy_cells_checked": [
    "H1299",
    "HCC827",
    "NCIH1437",
    "NCIH1563",
    "NCIH1573",
    "NCIH1781",
    "NCIH1975",
    "NCIH2073",
    "NCIH2110",
    "NCIH2172",
    "NCIH596",
    "NCIH838",
    "BEN",
    "HCC15",
    "HCC44",
    "HCC1588",
    "HCC95",
    "CORL23",
    "T3M10",
    "H1975"
  ],
  "proxy_perts_checked": [
    "EGF",
    "EREG",
    "AREG",
    "AR",
    "ERBB2",
    "ERBB4",
    "ERBB3",
    "HBEGF",
    "NRG1",
    "EPHA1",
    "GRB7",
    "AXL",
    "EGR1",
    "TLR4",
    "TGFA",
    "PDGFRA",
    "ADGRE5",
    "EPHB2",
    "FGFR2",
    "ERRFI1"
  ],
  "evidence_candidates": [
    {
      "hit_level": "EXACT",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "query_name": "EGFR"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "EGF",
      "query_name": "EGF"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "AR",
      "query_name": "AR"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "ERBB2",
      "query_name": "ERBB2"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "ERBB4",
      "query_name": "ERBB4"
    },
    {
      "hit_level": "PROXY_CELL",
      "used_cell": "HCC515",
      "used_perturbation": "EGFR",
      "query_name": "EGFR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "EGF",
      "query_name": "EGF"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "AR",
      "query_name": "AR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "ERBB2",
      "query_name": "ERBB2"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "ERBB4",
      "query_name": "ERBB4"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "ERBB3",
      "query_name": "ERBB3"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "NRG1",
      "query_name": "NRG1"
    }
  ],
  "composite_mode": "genetic_multi_source",
  "evidence_bundle": [
    {
      "pert_type": "xpr",
      "hit_level": "EXACT",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 5,
      "note": ""
    },
    {
      "pert_type": "sh",
      "hit_level": "EXACT",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 18,
      "note": ""
    }
  ],
  "selected_source": "sh"
}
```

Summary:

(empty)

### Q2_disease_not_cellname
- Query: `In non-small cell lung carcinoma, what happens if EGFR is suppressed?`
- Found: `True`
- Hit Level: `PROXY_CELL`
- Selected Source: `sh`
- Composite Mode: `genetic_multi_source`
- Timing (s): `0.098`

Prompt Timing:
```json
{}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "PROXY_CELL",
  "pert_type": "sh",
  "pert_class": "genetic",
  "evidence_policy": {
    "max_forward_evidence": 15,
    "budget_exact": 1,
    "budget_proxy_pert": 4,
    "budget_proxy_cell": 4,
    "budget_proxy_both": 6
  },
  "cell_resolution_reason": "bio_context_proxy",
  "requested_cell": null,
  "used_cell": "A549",
  "requested_perturbation": "EGFR",
  "used_perturbation": "EGFR",
  "proxy_cells_checked": [
    "H1299",
    "A549",
    "HCC827",
    "NCIH1437",
    "NCIH1563",
    "NCIH1573",
    "NCIH1781",
    "NCIH1975",
    "NCIH2073",
    "NCIH2110",
    "NCIH2172",
    "NCIH596",
    "NCIH838",
    "BEN",
    "HCC15",
    "HCC44",
    "HCC1588",
    "HCC95",
    "CORL23",
    "T3M10"
  ],
  "proxy_perts_checked": [
    "EGF",
    "EREG",
    "AREG",
    "AR",
    "ERBB2",
    "ERBB4",
    "ERBB3",
    "HBEGF",
    "NRG1",
    "EPHA1",
    "GRB7",
    "AXL",
    "EGR1",
    "TLR4",
    "TGFA",
    "PDGFRA",
    "ADGRE5",
    "EPHB2",
    "FGFR2",
    "ERRFI1"
  ],
  "evidence_candidates": [
    {
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "query_name": "EGFR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "EGF",
      "query_name": "EGF"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "AR",
      "query_name": "AR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB2",
      "query_name": "ERBB2"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB4",
      "query_name": "ERBB4"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB3",
      "query_name": "ERBB3"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "NRG1",
      "query_name": "NRG1"
    }
  ],
  "composite_mode": "genetic_multi_source",
  "evidence_bundle": [
    {
      "pert_type": "xpr",
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 5,
      "note": ""
    },
    {
      "pert_type": "sh",
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 18,
      "note": ""
    }
  ],
  "selected_source": "sh"
}
```

Summary:

(empty)

### Q3_unknown_cell_label
- Query: `For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?`
- Found: `True`
- Hit Level: `PROXY_CELL`
- Selected Source: `sh`
- Composite Mode: `genetic_multi_source`
- Timing (s): `0.089`

Prompt Timing:
```json
{}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "PROXY_CELL",
  "pert_type": "sh",
  "pert_class": "genetic",
  "evidence_policy": {
    "max_forward_evidence": 15,
    "budget_exact": 1,
    "budget_proxy_pert": 4,
    "budget_proxy_cell": 4,
    "budget_proxy_both": 6
  },
  "cell_resolution_reason": "bio_context_proxy",
  "requested_cell": null,
  "used_cell": "A549",
  "requested_perturbation": "EGFR",
  "used_perturbation": "EGFR",
  "proxy_cells_checked": [
    "H1299",
    "A549",
    "HCC827",
    "NCIH1437",
    "NCIH1563",
    "NCIH1573",
    "NCIH1781",
    "NCIH1975",
    "NCIH2073",
    "NCIH2110",
    "NCIH2172",
    "NCIH596",
    "NCIH838",
    "BEN",
    "HCC15",
    "HCC44",
    "HCC1588",
    "HCC95",
    "CORL23",
    "T3M10"
  ],
  "proxy_perts_checked": [
    "EGF",
    "EREG",
    "AREG",
    "AR",
    "ERBB2",
    "ERBB4",
    "ERBB3",
    "HBEGF",
    "NRG1",
    "EPHA1",
    "GRB7",
    "AXL",
    "EGR1",
    "TLR4",
    "TGFA",
    "PDGFRA",
    "ADGRE5",
    "EPHB2",
    "FGFR2",
    "ERRFI1"
  ],
  "evidence_candidates": [
    {
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "query_name": "EGFR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "EGF",
      "query_name": "EGF"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "AR",
      "query_name": "AR"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB2",
      "query_name": "ERBB2"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB4",
      "query_name": "ERBB4"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "ERBB3",
      "query_name": "ERBB3"
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "A549",
      "used_perturbation": "NRG1",
      "query_name": "NRG1"
    }
  ],
  "composite_mode": "genetic_multi_source",
  "evidence_bundle": [
    {
      "pert_type": "xpr",
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 5,
      "note": ""
    },
    {
      "pert_type": "sh",
      "hit_level": "PROXY_CELL",
      "used_cell": "A549",
      "used_perturbation": "EGFR",
      "found": true,
      "n_obs": 18,
      "note": ""
    }
  ],
  "selected_source": "sh"
}
```

Summary:

(empty)

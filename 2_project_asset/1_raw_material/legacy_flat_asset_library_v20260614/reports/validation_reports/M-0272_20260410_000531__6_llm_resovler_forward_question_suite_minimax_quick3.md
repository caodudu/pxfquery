# Forward Question Suite (minimax)

- Time: 2026-04-10 00:05:31
- Provider: minimax
- Model: MiniMax-M2.7
- Query Count: 3
- No Summary: True
- Suite Time (s): 71.26

| ID | Found | HitLevel | Source | Query |
|----|-------|----------|--------|-------|
| `Q1_exact_gene_cell` | `True` | `EXACT` | `sh` | In A549, what pathways are affected by EGFR knockdown? |
| `Q2_disease_not_cellname` | `False` | `NOT_FOUND` | `xpr` | In non-small cell lung carcinoma, what happens if EGFR is suppressed? |
| `Q3_unknown_cell_label` | `False` | `NOT_FOUND` | `xpr` | For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown? |

## Prompt Timing Total

```json
{
  "llm_map_cell_line": {
    "count": 6,
    "seconds": 33.697
  },
  "llm_parse_intent": {
    "count": 3,
    "seconds": 36.931
  }
}
```

## Detailed Results

### Q1_exact_gene_cell
- Query: `In A549, what pathways are affected by EGFR knockdown?`
- Found: `True`
- Hit Level: `EXACT`
- Selected Source: `sh`
- Composite Mode: `genetic_multi_source`
- Timing (s): `9.104`

Prompt Timing:
```json
{
  "llm_parse_intent": {
    "count": 1,
    "seconds": 8.474
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "EXACT",
  "pert_type": "sh",
  "pert_class": "genetic",
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
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "ERBB3",
      "query_name": "ERBB3"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "NRG1",
      "query_name": "NRG1"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "GRB7",
      "query_name": "GRB7"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "AXL",
      "query_name": "AXL"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "EGR1",
      "query_name": "EGR1"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "TLR4",
      "query_name": "TLR4"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "TGFA",
      "query_name": "TGFA"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "PDGFRA",
      "query_name": "PDGFRA"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "ADGRE5",
      "query_name": "ADGRE5"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "EPHB2",
      "query_name": "EPHB2"
    },
    {
      "hit_level": "PROXY_PERT",
      "used_cell": "A549",
      "used_perturbation": "FGFR2",
      "query_name": "FGFR2"
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
    },
    {
      "hit_level": "PROXY_BOTH",
      "used_cell": "HCC515",
      "used_perturbation": "GRB7",
      "query_name": "GRB7"
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
- Found: `False`
- Hit Level: `NOT_FOUND`
- Selected Source: `xpr`
- Composite Mode: `genetic_multi_source`
- Timing (s): `36.267`

Prompt Timing:
```json
{
  "llm_map_cell_line": {
    "count": 3,
    "seconds": 17.774
  },
  "llm_parse_intent": {
    "count": 1,
    "seconds": 18.492
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "NOT_FOUND",
  "pert_type": "xpr",
  "pert_class": "genetic",
  "cell_resolution_reason": "bio_context_proxy",
  "requested_cell": null,
  "used_cell": null,
  "requested_perturbation": "EGFR",
  "used_perturbation": null,
  "proxy_cells_checked": [
    "SKLU1",
    "DV90"
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
  "evidence_candidates": [],
  "composite_mode": "genetic_multi_source",
  "evidence_bundle": [
    {
      "pert_type": "xpr",
      "hit_level": "NOT_FOUND",
      "used_cell": null,
      "used_perturbation": null,
      "found": false,
      "n_obs": 0,
      "note": "No exact/proxy evidence found in current matrix for this (B, P) query."
    },
    {
      "pert_type": "sh",
      "hit_level": "NOT_FOUND",
      "used_cell": null,
      "used_perturbation": null,
      "found": false,
      "n_obs": 0,
      "note": "No exact/proxy evidence found in current matrix for this (B, P) query."
    }
  ],
  "selected_source": "xpr"
}
```

Summary:

(empty)

### Q3_unknown_cell_label
- Query: `For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?`
- Found: `False`
- Hit Level: `NOT_FOUND`
- Selected Source: `xpr`
- Composite Mode: `genetic_multi_source`
- Timing (s): `25.889`

Prompt Timing:
```json
{
  "llm_map_cell_line": {
    "count": 3,
    "seconds": 15.923
  },
  "llm_parse_intent": {
    "count": 1,
    "seconds": 9.965
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "NOT_FOUND",
  "pert_type": "xpr",
  "pert_class": "genetic",
  "cell_resolution_reason": "bio_context_proxy",
  "requested_cell": null,
  "used_cell": null,
  "requested_perturbation": "EGFR",
  "used_perturbation": null,
  "proxy_cells_checked": [
    "SKLU1",
    "DV90"
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
  "evidence_candidates": [],
  "composite_mode": "genetic_multi_source",
  "evidence_bundle": [
    {
      "pert_type": "xpr",
      "hit_level": "NOT_FOUND",
      "used_cell": null,
      "used_perturbation": null,
      "found": false,
      "n_obs": 0,
      "note": "No exact/proxy evidence found in current matrix for this (B, P) query."
    },
    {
      "pert_type": "sh",
      "hit_level": "NOT_FOUND",
      "used_cell": null,
      "used_perturbation": null,
      "found": false,
      "n_obs": 0,
      "note": "No exact/proxy evidence found in current matrix for this (B, P) query."
    }
  ],
  "selected_source": "xpr"
}
```

Summary:

(empty)

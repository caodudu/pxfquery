# Forward Question Suite (minimax)

- Time: 2026-04-10 11:38:54
- Provider: minimax
- Model: MiniMax-M2.7
- Query Count: 4
- Resolver Mode: always_llm
- No Summary: False
- Suite Time (s): 167.3

| ID | Found | HitLevel | Source | Query |
|----|-------|----------|--------|-------|
| `Q1_exact_gene_cell` | `True` | `EXACT` | `sh` | In A549, what pathways are affected by EGFR knockdown? |
| `Q2_disease_not_cellname` | `False` | `NOT_FOUND` | `xpr` | In non-small cell lung carcinoma, what happens if EGFR is suppressed? |
| `Q5_generic_drug_desc` | `False` | `NOT_FOUND` | `cp` | In A549, what pathways are affected by an EGFR inhibitor? |
| `Q13_nonexistent_drug` | `False` | `NOT_FOUND` | `xpr` | In PC3, estimate pathway response for l-theanine-like perturbation. |

## Prompt Timing Total

```json
{
  "llm_map_cell_line": {
    "count": 2,
    "seconds": 10.954
  },
  "llm_map_drug": {
    "count": 1,
    "seconds": 7.897
  },
  "llm_map_gene": {
    "count": 1,
    "seconds": 7.409
  },
  "llm_normalize_drug": {
    "count": 1,
    "seconds": 5.786
  },
  "llm_parse_intent": {
    "count": 4,
    "seconds": 117.142
  },
  "llm_summarize_forward": {
    "count": 4,
    "seconds": 17.08
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
- Timing (s): `61.716`

Prompt Timing:
```json
{
  "llm_parse_intent": {
    "count": 1,
    "seconds": 44.041
  },
  "llm_summarize_forward": {
    "count": 1,
    "seconds": 17.08
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "EXACT",
  "pert_type": "sh",
  "selected_source": "sh",
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
  "llm_call_stats": {
    "query": {
      "llm_parse_intent": {
        "count": 1,
        "seconds": 44.041
      },
      "llm_summarize_forward": {
        "count": 1,
        "seconds": 17.08
      }
    },
    "total": {
      "llm_parse_intent": {
        "count": 1,
        "seconds": 44.041
      },
      "llm_summarize_forward": {
        "count": 1,
        "seconds": 17.08
      }
    }
  }
}
```

LLM Call Stats:
```json
{
  "query": {
    "llm_parse_intent": {
      "count": 1,
      "seconds": 44.041
    },
    "llm_summarize_forward": {
      "count": 1,
      "seconds": 17.08
    }
  },
  "total": {
    "llm_parse_intent": {
      "count": 1,
      "seconds": 44.041
    },
    "llm_summarize_forward": {
      "count": 1,
      "seconds": 17.08
    }
  }
}
```

Summary:

Forward inference in A549 indicates EXACT evidence. Dominant activated programs include HALLMARK_MYOGENESIS, HALLMARK_KRAS_SIGNALING_DN, MP31 Alveolar, HALLMARK_APICAL_SURFACE, MP28 Oligo normal. Dominant suppressed programs include HALLMARK_OXIDATIVE_PHOSPHORYLATION, MP14 EMT-III , MP20 MYC, HALLMARK_MTORC1_SIGNALING, MP8 Proteasomal degradation. Interpretation should consider proxy usage and source evidence in resolver_meta.

### Q2_disease_not_cellname
- Query: `In non-small cell lung carcinoma, what happens if EGFR is suppressed?`
- Found: `False`
- Hit Level: `NOT_FOUND`
- Selected Source: `xpr`
- Composite Mode: `genetic_multi_source`
- Timing (s): `31.421`

Prompt Timing:
```json
{
  "llm_map_cell_line": {
    "count": 2,
    "seconds": 10.954
  },
  "llm_parse_intent": {
    "count": 1,
    "seconds": 20.466
  },
  "llm_summarize_forward": {
    "count": 1,
    "seconds": 0.0
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "NOT_FOUND",
  "pert_type": "xpr",
  "selected_source": "xpr",
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
  "used_cell": null,
  "requested_perturbation": "EGFR",
  "used_perturbation": null,
  "proxy_cells_checked": [
    "TC32",
    "A673",
    "SKES1"
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
  "llm_call_stats": {
    "query": {
      "llm_map_cell_line": {
        "count": 2,
        "seconds": 10.953
      },
      "llm_parse_intent": {
        "count": 1,
        "seconds": 20.466
      },
      "llm_summarize_forward": {
        "count": 1,
        "seconds": 0.0
      }
    },
    "total": {
      "llm_map_cell_line": {
        "count": 2,
        "seconds": 10.953
      },
      "llm_parse_intent": {
        "count": 2,
        "seconds": 64.507
      },
      "llm_summarize_forward": {
        "count": 2,
        "seconds": 17.08
      }
    }
  }
}
```

LLM Call Stats:
```json
{
  "query": {
    "llm_map_cell_line": {
      "count": 2,
      "seconds": 10.953
    },
    "llm_parse_intent": {
      "count": 1,
      "seconds": 20.466
    },
    "llm_summarize_forward": {
      "count": 1,
      "seconds": 0.0
    }
  },
  "total": {
    "llm_map_cell_line": {
      "count": 2,
      "seconds": 10.953
    },
    "llm_parse_intent": {
      "count": 2,
      "seconds": 64.507
    },
    "llm_summarize_forward": {
      "count": 2,
      "seconds": 17.08
    }
  }
}
```

Summary:

No result found. No exact/proxy evidence found in current matrix for this (B, P) query.

### Q5_generic_drug_desc
- Query: `In A549, what pathways are affected by an EGFR inhibitor?`
- Found: `False`
- Hit Level: `NOT_FOUND`
- Selected Source: `cp`
- Composite Mode: `None`
- Timing (s): `31.839`

Prompt Timing:
```json
{
  "llm_map_drug": {
    "count": 1,
    "seconds": 7.897
  },
  "llm_normalize_drug": {
    "count": 1,
    "seconds": 5.786
  },
  "llm_parse_intent": {
    "count": 1,
    "seconds": 17.802
  },
  "llm_summarize_forward": {
    "count": 1,
    "seconds": 0.0
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "NOT_FOUND",
  "pert_type": "cp",
  "selected_source": "cp",
  "pert_class": "drug",
  "evidence_policy": {
    "max_forward_evidence": 15,
    "budget_exact": 1,
    "budget_proxy_pert": 4,
    "budget_proxy_cell": 4,
    "budget_proxy_both": 6
  },
  "cell_resolution_reason": "exact_cell_name",
  "requested_cell": "A549",
  "used_cell": null,
  "requested_perturbation": "EGFR inhibitor",
  "used_perturbation": null,
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
  "proxy_perts_checked": [],
  "evidence_candidates": [],
  "llm_call_stats": {
    "query": {
      "llm_map_drug": {
        "count": 1,
        "seconds": 7.897
      },
      "llm_normalize_drug": {
        "count": 1,
        "seconds": 5.786
      },
      "llm_parse_intent": {
        "count": 1,
        "seconds": 17.802
      },
      "llm_summarize_forward": {
        "count": 1,
        "seconds": 0.0
      }
    },
    "total": {
      "llm_map_cell_line": {
        "count": 2,
        "seconds": 10.953
      },
      "llm_map_drug": {
        "count": 1,
        "seconds": 7.897
      },
      "llm_normalize_drug": {
        "count": 1,
        "seconds": 5.786
      },
      "llm_parse_intent": {
        "count": 3,
        "seconds": 82.309
      },
      "llm_summarize_forward": {
        "count": 3,
        "seconds": 17.08
      }
    }
  }
}
```

LLM Call Stats:
```json
{
  "query": {
    "llm_map_drug": {
      "count": 1,
      "seconds": 7.897
    },
    "llm_normalize_drug": {
      "count": 1,
      "seconds": 5.786
    },
    "llm_parse_intent": {
      "count": 1,
      "seconds": 17.802
    },
    "llm_summarize_forward": {
      "count": 1,
      "seconds": 0.0
    }
  },
  "total": {
    "llm_map_cell_line": {
      "count": 2,
      "seconds": 10.953
    },
    "llm_map_drug": {
      "count": 1,
      "seconds": 7.897
    },
    "llm_normalize_drug": {
      "count": 1,
      "seconds": 5.786
    },
    "llm_parse_intent": {
      "count": 3,
      "seconds": 82.309
    },
    "llm_summarize_forward": {
      "count": 3,
      "seconds": 17.08
    }
  }
}
```

Summary:

No result found. No exact/proxy evidence found in current matrix for this (B, P) query.

### Q13_nonexistent_drug
- Query: `In PC3, estimate pathway response for l-theanine-like perturbation.`
- Found: `False`
- Hit Level: `NOT_FOUND`
- Selected Source: `xpr`
- Composite Mode: `genetic_multi_source`
- Timing (s): `42.324`

Prompt Timing:
```json
{
  "llm_map_gene": {
    "count": 1,
    "seconds": 7.409
  },
  "llm_parse_intent": {
    "count": 1,
    "seconds": 34.833
  },
  "llm_summarize_forward": {
    "count": 1,
    "seconds": 0.0
  }
}
```

Resolver Meta:
```json
{
  "query_type": "forward",
  "hit_level": "NOT_FOUND",
  "pert_type": "xpr",
  "selected_source": "xpr",
  "pert_class": "genetic",
  "evidence_policy": {
    "max_forward_evidence": 15,
    "budget_exact": 1,
    "budget_proxy_pert": 4,
    "budget_proxy_cell": 4,
    "budget_proxy_both": 6
  },
  "cell_resolution_reason": "exact_cell_name",
  "requested_cell": "PC3",
  "used_cell": null,
  "requested_perturbation": "In PC3, estimate pathway response for l-theanine-like perturbation.",
  "used_perturbation": null,
  "proxy_cells_checked": [
    "VCAP",
    "22RV1",
    "DU145",
    "RWPE1",
    "LNCAP"
  ],
  "proxy_perts_checked": [],
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
  "llm_call_stats": {
    "query": {
      "llm_map_gene": {
        "count": 1,
        "seconds": 7.409
      },
      "llm_parse_intent": {
        "count": 1,
        "seconds": 34.833
      },
      "llm_summarize_forward": {
        "count": 1,
        "seconds": 0.0
      }
    },
    "total": {
      "llm_map_cell_line": {
        "count": 2,
        "seconds": 10.953
      },
      "llm_map_drug": {
        "count": 1,
        "seconds": 7.897
      },
      "llm_map_gene": {
        "count": 1,
        "seconds": 7.409
      },
      "llm_normalize_drug": {
        "count": 1,
        "seconds": 5.786
      },
      "llm_parse_intent": {
        "count": 4,
        "seconds": 117.142
      },
      "llm_summarize_forward": {
        "count": 4,
        "seconds": 17.08
      }
    }
  }
}
```

LLM Call Stats:
```json
{
  "query": {
    "llm_map_gene": {
      "count": 1,
      "seconds": 7.409
    },
    "llm_parse_intent": {
      "count": 1,
      "seconds": 34.833
    },
    "llm_summarize_forward": {
      "count": 1,
      "seconds": 0.0
    }
  },
  "total": {
    "llm_map_cell_line": {
      "count": 2,
      "seconds": 10.953
    },
    "llm_map_drug": {
      "count": 1,
      "seconds": 7.897
    },
    "llm_map_gene": {
      "count": 1,
      "seconds": 7.409
    },
    "llm_normalize_drug": {
      "count": 1,
      "seconds": 5.786
    },
    "llm_parse_intent": {
      "count": 4,
      "seconds": 117.142
    },
    "llm_summarize_forward": {
      "count": 4,
      "seconds": 17.08
    }
  }
}
```

Summary:

No result found. No exact/proxy evidence found in current matrix for this (B, P) query.

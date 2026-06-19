# LLM Stability Check

- Time: 2026-04-10T11:35:52
- Model: MiniMax-M2.7
- Success Rate: 6/9 = 0.667

```json
{
  "time": "2026-04-10T11:35:52",
  "model": "MiniMax-M2.7",
  "rounds": 3,
  "total": 9,
  "ok": 6,
  "success_rate": 0.667,
  "rows": [
    {
      "query": "In A549, what pathways are affected by EGFR knockdown?",
      "ok": true,
      "latency_sec": 29.176,
      "intent": {
        "query_type": "forward",
        "bio_context": "A549",
        "pert_desc": "EGFR knockdown",
        "pert_class": "genetic",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "In A549, what pathways are affected by an EGFR inhibitor?",
      "ok": false,
      "latency_sec": 36.287,
      "intent": {
        "query_type": null,
        "bio_context": null,
        "pert_desc": null,
        "pert_class": null,
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?",
      "ok": true,
      "latency_sec": 27.193,
      "intent": {
        "query_type": "forward",
        "bio_context": "NCI-H358-like NSCLC",
        "pert_desc": "EGFR knockdown",
        "pert_class": "genetic",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "In A549, what pathways are affected by EGFR knockdown?",
      "ok": true,
      "latency_sec": 34.572,
      "intent": {
        "query_type": "forward",
        "bio_context": "A549",
        "pert_desc": "EGFR knockdown",
        "pert_class": "genetic",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "In A549, what pathways are affected by an EGFR inhibitor?",
      "ok": false,
      "latency_sec": 40.126,
      "intent": {
        "query_type": null,
        "bio_context": null,
        "pert_desc": null,
        "pert_class": null,
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?",
      "ok": false,
      "latency_sec": 27.444,
      "intent": {
        "query_type": null,
        "bio_context": null,
        "pert_desc": null,
        "pert_class": null,
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "In A549, what pathways are affected by EGFR knockdown?",
      "ok": true,
      "latency_sec": 14.746,
      "intent": {
        "query_type": "forward",
        "bio_context": "A549",
        "pert_desc": "EGFR knockdown",
        "pert_class": "genetic",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "In A549, what pathways are affected by an EGFR inhibitor?",
      "ok": true,
      "latency_sec": 28.844,
      "intent": {
        "query_type": "forward",
        "bio_context": "A549",
        "pert_desc": "EGFR inhibitor",
        "pert_class": "drug",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    },
    {
      "query": "For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?",
      "ok": true,
      "latency_sec": 20.889,
      "intent": {
        "query_type": "forward",
        "bio_context": "NCI-H358-like NSCLC",
        "pert_desc": "EGFR knockdown",
        "pert_class": "genetic",
        "function_desc": null,
        "activate": [],
        "suppress": [],
        "top_n": null
      }
    }
  ]
}
```
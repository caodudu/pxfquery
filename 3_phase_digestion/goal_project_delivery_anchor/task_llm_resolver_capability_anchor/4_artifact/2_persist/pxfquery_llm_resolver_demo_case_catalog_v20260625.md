# PxFquery LLM/Resolver Demo Case Catalog

Generated: 2026-06-25  
Task: T-063 `llm_resolver_capability_anchor`

This catalog defines required future M3 acceptance case types. The examples are acceptance specifications, not current run results.

| Case ID | Case type | Example input shape | Required behavior | Required evidence | Failure labels |
|---|---|---|---|---|---|
| DEMO-EXACT-FWD-001 | Exact forward query | Natural language or semi-structured request for EGFR perturbation in A549/xpr context | Parse as forward query; normalize perturbation and context; dispatch exact route; return ranked activated/suppressed functions | Parse record; exact route status; source matrix/index reference; ranked result; metadata | `failed` if false entity; `evidence-insufficient` if no metadata |
| DEMO-EXACT-REV-001 | Exact reverse query | Request perturbations for apoptosis activation and/or MYC suppression in A549 | Parse as reverse query; normalize function target and direction; return ranked perturbation candidates | Parse record; function mapping; ranking; numeric sanity/warning review; metadata | `partial` if numeric warning unresolved; `blocked` if function index missing |
| DEMO-PROXY-FWD-001 | Proxy forward query | Forward query where exact cell line or perturbation is unavailable but approved neighbor evidence exists | Report exact miss; select approved proxy; return proxy-labeled functional response | Exact miss trigger; proxy source; similarity/hierarchy basis; limitations | `downgraded` if exact-only replaces required proxy; `failed` if proxy marked exact |
| DEMO-PROXY-REV-001 | Proxy reverse query | Reverse function query in a sparse context requiring cell/function proxy | Report exact miss or sparse coverage; use approved proxy basis; return proxy-labeled candidates | Function/context proxy metadata; candidate ranking; limitations | `blocked` if proxy index unavailable; `evidence-insufficient` if proxy basis hidden |
| DEMO-NOTFOUND-001 | Not-found query | Meaningless perturbation token in a valid context | Return no-hit/not-found and do not substitute nearest fuzzy token as found | Negative-control input; attempted routes; no false-positive confirmation; not-found reason | `failed` if a real perturbation is returned as found |
| DEMO-AMBIG-NL-001 | Ambiguous natural-language query | "What happens with an EGFR inhibitor in lung cancer?" | Expose ambiguity for perturbation identity, context, and modality; ask for clarification or use labeled low-confidence suggestions without dispatching as found | Ambiguity flags; missing fields; parse confidence; no unsafe dispatch | `failed` if ambiguity is silently resolved to a found result |
| DEMO-SEMI-STRUCT-001 | Semi-structured query | `{mode: forward, perturbation: EGFR, biological_context: A549, data_source_or_modality: xpr}` | Parse supplied fields deterministically; normalize fields; dispatch appropriate route | Structured input; normalized parse; route status; result metadata | `failed` if field mapping is wrong; `evidence-insufficient` if parse is not recorded |
| DEMO-LLM-FALLBACK-001 | LLM-service-unavailable fallback | Natural-language resolver query while configured AI service is unavailable | Record LLM failure; use deterministic parser or request structured fields; do not claim LLM primary path delivery | LLM failure trigger; fallback route; fallback-used flag; result or controlled blocked status | `blocked` if no fallback can operate; `downgraded` if fallback-only is accepted as primary without approval |
| DEMO-META-INSPECT-001 | Evidence metadata inspection | Any successful exact or proxy result | Show machine-readable metadata for route, evidence level, source, warnings, limitations, normalized entities, fallback, and LLM route | JSON/table metadata output; user-facing summary consistent with metadata | `evidence-insufficient` if only prose is available |

## Minimum Future Demo Set

A future M3 review must include at least one accepted example for every case type above. The examples should be run in the current milestone environment or explicitly inherit an accepted unchanged artifact. Historical reports and code presence alone do not satisfy the demo catalog.

## Case Selection Guidance

Use exact examples with known matrix/index support for the primary green path. Use separate negative and ambiguous examples to prove safety behavior. Use proxy examples only where the proxy basis is registered and inspectable. Use LLM fallback examples to prove resilience, not to replace primary LLM delivery.

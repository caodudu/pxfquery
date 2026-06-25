# T-063 Resolver Requirement Extraction

Generated: 2026-06-25

## Step Evidence

- Workspace and all 13 registered assets were present.
- CyHex API version was reachable at `http://localhost:47291/api/version` and returned app version `1.2.20`.
- No web search, package test, raw matrix read, implementation edit, or legacy source-root read was performed.

## Inherited Capability Rules

- T-062 is the package-level anchor. T-063 refines only the resolver/LLM layer.
- Resolver delivery is not satisfied by deterministic lookup alone when resolver behavior is in scope.
- LLM delivery is not satisfied by endpoint connectivity alone.
- Proxy delivery is not satisfied by exact-only lookup.
- Fallback is valid runtime behavior only when the trigger, route, evidence state, and limitation are explicit.
- Fallback-only acceptance of a required primary path is a downgrade unless explicitly user-approved.
- Status labels inherited for future review: `delivered`, `partial`, `blocked`, `failed`, `downgraded`, `deferred-user-approved`, `deferred-not-approved`, `out-of-scope`, `evidence-insufficient`.

## Resolver-Relevant Predecessor Facts

- T-007: Intended product supports forward and reverse query with exact-first and proxy evidence through cell-line hierarchy plus gene/drug neighbor indexes.
- T-007: LLMs may support parsing, mapping, normalization, and summarization; numerical retrieval remains deterministic and evidence-aware.
- T-007: Real LLM behavior was unstable and slow in historical evidence; claims should stay cautious.
- T-013: Exact forward EGFR/A549/xpr query passed.
- T-013: Reverse apoptosis/MYC/A549 ranking was partial because numeric stability warnings remained.
- T-013: Not-found safety failed because fuzzy fallback matched meaningless perturbation text to a real token.
- T-013: Natural-language resolver/proxy was blocked by current index naming and missing `function_index.json`.
- T-013: DeepSeek endpoint connectivity was shown, but resolver-level LLM parse/summary behavior was not delivered.
- T-061: `core.PxFquery` is the modern facade; `query.resolver.QueryResolver` is substantial but risk-bearing.
- T-061: Resolver evidence levels include `EXACT`, `PROXY_PERT`, `PROXY_CELL`, `PROXY_BOTH`, `FORCED_MATCH`, `FORCED_FALLBACK`, and `NOT_FOUND`.
- T-061: Forced fallback levels must not be treated as strong biological evidence.
- T-061: Index readers require exact JSON filenames and should be treated as readers/adapters, not index builders.

## M3 Anchor Implications

- M3 resolver acceptance must require user-facing query entry through natural language and semi-structured inputs.
- M3 must require parse output that records intent, direction, biological context, perturbation or target function, perturbation modality, normalized entities, confidence, ambiguity, and missing fields.
- M3 must require dispatch evidence for both forward and reverse resolver paths.
- M3 must require exact, proxy, and not-found routing evidence with transparent metadata.
- M3 must require the current CyHex-configured AI route, currently `deepseek-v4-pro`, for milestones that claim LLM-assisted resolver behavior unless a later task explicitly changes the route.
- M3 must include deterministic fallback evidence, but fallback evidence is not primary LLM/resolver delivery evidence.

# Changelog

## 0.5.3.dev2 - 2026-06-28

- Parallelized independent L2 route dimensions (`cell`, `perturbation`, and `function`) while preserving fixed `llm_calls` merge order and RoutePlan schema.
- Parallelized reverse three-pass function interpretation mapping while preserving fixed interpretation-set order.
- Added scheduler regression tests proving L2 parallel execution occurs without leaking demo answers or changing public handoff structure.

## 0.5.3.dev1 - 2026-06-28

- Fixed exact cell-line routing for surface forms such as `A549 cells` and `MCF7 cells`; these now canonicalize to valid cell IDs before LLM cell-tree traversal.
- Added regression coverage to ensure exact cell mentions with common suffixes do not route through proxy tree selection.

## 0.5.3.dev0 - 2026-06-28

- Completed the L2 resource-routing repair around `pxf.pp.route(qdata)`.
- Added resource-backed cell, drug, gene, function, and combination route plans with bounded candidates, rejected-candidate evidence, unresolved dimensions, and L3 handoff payloads.
- Added controlled DeepSeek-backed L2 routing for cell-tree traversal, drug/gene normalization, and function mapping; LLM outputs must validate against resource indexes.
- Added explicit `llm_unavailable` and `llm_output_invalid` states instead of demo or local fallback behavior.
- Validated with package tests, real DeepSeek L2 checks, T137 60-question L2 replay, and an additional 50-question L1+L2 generalization run.

## 0.5.1 - 2026-06-28

- Renamed the first business layer from `l1_nlu` to `l1_intent`; no compatibility alias is kept.
- Added a session-local LLM provider registry exposed through settings, with DiyGateway and official DeepSeek registration helpers.
- Added a small non-secret event logging system under `pxfquery.utils.events`; L1 now emits stage, warning, and error events for provider calls.
- Added spaced network retries, schema repair attempts, and chat restart attempts for L1 intent parsing.
- Added provider evidence capture for L1 calls: provider name, base URL, model, timestamps, attempts, response hash/excerpt, schema repair count, restart count, and final status.
- Kept L1 scope strict: provider output containing candidates, scores, route plans, citations, evidence, or biological answers is rejected.

## 0.5.0 - 2026-06-27

- Restored the original PxFquery functional core into the GitHub package: data loading, forward query, reverse query, resolver, index wrappers, and plotting.
- Reorganized implementation into five business layers plus package-level settings and utils helpers.
- Changed L1 intent contract to the original resolver-compatible schema: `query_type`, `bio_context`, `pert_desc`, `pert_class`, `function_desc`, `activate`, `suppress`, and `top_n`.
- Removed the degraded MS8 empty execution path from the scanpy-style chain.
- Kept L1 provider behavior honest: L1 requires a real configured LLM backend and does not contain local keyword/rule parsing.
- Moved CLI, client, workflow, settings, and version files out of `l5_presentation`; L5 now only contains answer, model, and plotting presentation code.

## 0.4.1 - 2026-06-27

- Replaced local L1 parsing with a real OpenAI-compatible LLM backend boundary.
- Added scanpy-style L1 provider configuration through `pxf.settings.use_diygateway(...)`.
- L1 now reports query task, perturbation type, perturbation action, regulation direction, extracted surface phrases, missing fields, and parser notes from the configured provider response.
- L1 remains honest: it does not resolve entities, query resources, create candidates, or score results.
- Reduced L1 testing to a single real DiyGateway contract path that fails if the provider is unavailable.

## 0.4.0 - 2026-06-27

- Current package source is organized as five inspectable internal folders: `l1_intent`, `l2_routing`, `l3_execution`, `l4_evidence`, and `l5_presentation`.
- `src/pxfquery/` root contains only thin entrypoints: `__init__.py` and `__main__.py`.
- `PxFQuery` is the only public top-level class.
- `PxFQuery` exposes a scanpy-style user interface: `read.query`, `pp.parse`, `pp.route`, `tl.execute`, `tl.assemble`, `get.result`, and `get.answer`.
- Biological results are not fabricated before resource-backed retrieval exists.

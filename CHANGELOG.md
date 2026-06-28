# Changelog

## 0.5.6.dev2 - 2026-06-29

- Added `pxf.tl.parse(text)` as a one-call L1-L4 pipeline entrypoint and `pxf.tl.anno(qdata, providers=[...])` as an optional real-provider annotation extension point.
- Kept `rejected_candidates` out of default L4 route evidence and exposed it only through hidden debug audit output when requested.
- Strengthened L4 LLM synthesis instructions so `exact_primary_with_proxy_support` is summarized as exact primary matrix evidence with proxy support, not as absent exact evidence.
- Filtered `CSS001*` control perturbations from sh/xpr reverse rankings before candidate ranking.
- Added L2 cell-tree robustness for deterministic single-option tree steps and empty-object LLM repair retries.

## 0.5.6.dev1 - 2026-06-29

- Published the T140 L4 package source to the GitHub export package.
- Fixed default resource-cache behavior so existing cached files are reused without repeated checksum scans, while newly downloaded files are still verified.
- Removed the obsolete `l2.gene_neighbors_simple` resource requirement.
- Materialized functional-score `.npz` matrices to reusable local `.npy` memmap files on first use instead of decompressing them on every query.

## 0.5.6.dev0 - 2026-06-28

- Added L4 `EvidenceDossier` assembly over `l3-matrix-execution/v1`, replacing the old `ForwardResult` / `ReverseResult` adapter path.
- Added renderer-neutral L4 sections: `claim_basis`, `evidence_layer`, `uncertainty_layer`, `rendering_hints`, and `audit_layer`.
- Wired `pxf.tl.assemble(qdata)` to consume L1 intent, L2 route plan, and L3 execution together, and added `pxf.get.evidence(qdata)`.
- Kept PubMed/literature as an optional channel that reports `disabled` without a provider, rather than inventing citations.
- Added optional real LLM synthesis through the configured provider when `synthesize=True`; default L4 assembly remains deterministic and reports synthesis as disabled.
- Verified L4 with resource-backed forward/reverse L3 execution and a real DeepSeek L1-L4 smoke run.

## 0.5.5.dev4 - 2026-06-28

- Added packaged default Zenodo resource manifest for record `21001791` and cache-first automatic resource download under `~/.cache/pxfquery/resources/v20260628`.
- Wired `pxf.pp.route(qdata)` to fetch L2 indexes and L3 `obs_min` metadata when using the default manifest, and `pxf.tl.execute(qdata)` to fetch only the L3 matrix resources needed by the selected route.
- Kept `pxf.resources.use(local_path)` as an explicit local resource-pack mode and fixed manifest/local switching so roots do not mix across modes.
- Reduced default route prefetch by making the currently unused `gene_neighbors_simple.json` optional rather than part of `l2_proxy_neighbors`.
- Verified an empty-cache default Zenodo route/execute path without passing an external resource directory.

## 0.5.5.dev3 - 2026-06-28

- Removed raw-query phrase-triggered L1 validators and kept L1 validation focused on schema, structure, layer boundaries, and payload consistency.
- Kept `constraints` and `forward_result_scope` as structured L1 fields while leaving natural-language semantics to the configured LLM.
- Added L3 reverse replicate aggregation by perturbation/cell and sign guards for reverse projection rankings.
- Verified current T139 package source with 20-question DeepSeek L1-L2-L3, 60-question L2-to-L3, and 50-question generalization L2-to-L3 validation artifacts.

## 0.5.5.dev2 - 2026-06-28

- Corrected genetic perturbation sign semantics: `xpr` is treated as CRISPR/loss-of-function evidence, not overexpression.
- Changed reverse ranking from cosine similarity to signed dot projection against the requested functional target vector.
- Added bidirectional genetic reverse outputs for loss-of-function perturbations and activation perturbations inferred from opposite LOF effects; compound reverse remains single-direction drug perturbation ranking.
- Added forward score orientation metadata so genetic activation-style queries can use `-LOF` inferred scores while preserving perturbation anchors.

## 0.5.5.dev1 - 2026-06-28

- Added stable L3 evidence labels for forward rankings and requested function records so downstream HTML/L4 readers do not lose function names.
- Integrated the L2 normal-lineage anchor downgrade patch: cancer-context routes that fall back to normal same-lineage data are explicitly marked as downgraded evidence.

## 0.5.5.dev0 - 2026-06-28

- Repaired L3 route-plan execution against the current L1/L2 contract without legacy compatibility shells.
- Replaced the old L3 loader/forward/reverse surface with resource-pack-backed matrix execution over L2 route plans.
- Kept L3 strict: unresolved route plans and missing matrix rows return structured failures rather than demo fallback values.
- Added tabbed HTML replay reports for the T137 60-question and 50-question L1/L2 validation sets with L3 execution details.
- Documented the lightweight resource-pack strategy for local paths plus future Zenodo download management.

## 0.5.3.dev3 - 2026-06-28

- Added shared `pxfquery.resources` resource manager from the T139 resource-layer design so L2 and L3 use the same resource root and `obs_min` discovery.
- Added L2 forward `pair_policy`: default `observed` filters top route candidates to real `(cell, perturbation)` pairs present in L3 `obs_min` metadata; explicit `global` keeps theoretical index-ranked candidates.
- Expanded internal cell and perturbation pools for observed pair search while keeping public `candidates`/`proxies` bounded.
- Preserved unspecified genetic modality as both `xpr` and `sh`; only explicit modality terms narrow the route.
- Added a final observed perturbation-anchor fallback when no routed cell-context pair exists; these routes are explicitly labeled as weak cell-context evidence instead of being treated as exact cell matches.
- Made reverse routes availability-aware for `sh`/`xpr` cell scope by filtering candidates against `obs_min` modality rows and labeling weak observed-modality anchor fallbacks.

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

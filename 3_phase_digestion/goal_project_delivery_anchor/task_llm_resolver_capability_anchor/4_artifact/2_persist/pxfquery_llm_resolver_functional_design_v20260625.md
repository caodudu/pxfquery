# PxFquery LLM/Resolver Functional Design Anchor

Generated: 2026-06-25  
Task: T-063 `llm_resolver_capability_anchor`

## Purpose

This document defines the user-facing resolver behavior expected for future PxFquery package milestones, especially M3-level resolver delivery. It is a design and acceptance anchor only. It does not claim that resolver code, current indexes, or LLM-assisted parsing were tested or repaired in T-063.

The anchor refines the T-062 algorithm-package delivery anchor. If a future milestone includes resolver capability, deterministic matrix lookup alone is not sufficient. The milestone must show that a user-facing natural-language or semi-structured query can be parsed, normalized, routed to forward or reverse query behavior, and returned with transparent exact/proxy/not-found metadata.

## Required User-Facing Behavior

M3 resolver delivery must support two entry styles:

1. Natural-language entry, such as a user asking for the functional response of a perturbation in a biological context or asking for perturbations that could activate or suppress a target function.
2. Semi-structured entry, where the user supplies fields such as `mode`, `perturbation`, `biological_context`, `function_target`, `desired_direction`, `data_source_or_modality`, and `proxy_allowed`.

The resolver must produce a structured parse before dispatch. Required parse fields include query id, raw input, entry type, intent, mode, perturbation, perturbation type, biological context, function target, desired direction, modality, missing fields, ambiguity flags, parse confidence, parse method, AI route used, and fallback status.

Forward queries must route from biological context plus perturbation to ranked or scored functional responses. Reverse queries must route from biological context plus desired functional target to ranked candidate perturbations. In both modes, the result must expose machine-readable evidence metadata rather than only a prose summary.

## AI Service Rule

Future milestones that claim LLM-assisted resolver behavior must route through the current CyHex-registered AI address. The current desired model route is `deepseek-v4-pro` unless a later task explicitly changes it.

Acceptable future evidence must show the configured route, the requested model or approved successor, a resolver parse or summary call, the structured result or user-facing summary, and latency/failure/fallback metadata. Endpoint connectivity alone is not enough to count as LLM-assisted resolver delivery.

LLM output may parse user text, normalize candidate names, explain ambiguity, and summarize deterministic evidence. It must not fabricate biological evidence, create matrix rows, convert low-confidence aliases into found results, or hide missing index/function/context coverage.

## Exact, Proxy, And Not-Found Routing

Exact routing is the first path. The resolver must try exact perturbation, function, and biological-context matches before proxy routes. Result metadata must label exact matches and cite the relevant source index or matrix reference.

Proxy routing is allowed after exact miss, sparse coverage, low coverage, or an explicit proxy-enabled request. Approved proxy bases include cell-line hierarchy or neighbors, disease/lineage/subtype context, gene neighbors, drug neighbors, and approved function aliases or function-index mappings. Proxy results must report the trigger, source, similarity or hierarchy basis, confidence, and limitation. Proxy results must never be reported as exact results.

Not-found routing is a required safety behavior. Unsupported perturbations, unsupported cell lines, unsupported functions, missing indexes, and low-confidence matches must return controlled no-hit, unsupported, blocked, or evidence-insufficient states. The resolver must not silently substitute the nearest fuzzy token as a found result.

## Fallback Semantics

Fallback is runtime behavior and review evidence, not proof that the primary resolver/LLM/proxy capability was delivered. A deterministic parser after LLM failure may be useful, but it cannot count as delivery of required LLM-assisted parsing unless the milestone explicitly accepts fallback-only scope with user approval.

Required fallback cases include unavailable LLM service, LLM parse failure, proxy failure, missing indexes, unsupported context, unsupported perturbation, unsupported function, and low-confidence match. Each fallback result must record its trigger, route, status label, evidence limitations, and whether primary behavior was skipped, failed, or unavailable.

If the resolver cannot start because required indexes are missing, the correct status is blocked. If a not-found case returns a false positive as found, the correct status is failed. If only endpoint connectivity is shown for an LLM-backed resolver milestone, the correct status is partial or evidence-insufficient, not delivered.

## Acceptance Evidence

Future M3 acceptance must include current run artifacts or accepted task artifacts covering exact forward, exact reverse, proxy forward, proxy reverse, not-found, ambiguous natural-language, semi-structured input, LLM-service-unavailable fallback, and evidence-metadata inspection cases.

Every accepted result must provide both functional behavior and metadata evidence: route status, evidence level, exact/proxy/not-found/fallback labels, normalized entities, source index or matrix reference, warnings, limitations, and LLM route when LLM assistance is claimed.

The allowed review labels are inherited from T-062: `delivered`, `partial`, `blocked`, `failed`, `downgraded`, `deferred-user-approved`, `deferred-not-approved`, `out-of-scope`, and `evidence-insufficient`.

## Disallowed Substitutes

The following cannot satisfy M3 resolver delivery when resolver/LLM/proxy behavior is in scope:

- Direct deterministic function calls in place of resolver-mediated user entry.
- Exact-only lookup in place of required proxy routing.
- Endpoint connectivity in place of LLM parse or summary behavior.
- Fallback-only behavior counted as primary delivery without explicit user approval.
- LLM-generated biological explanation without deterministic matrix/index evidence.
- A prose summary without inspectable route, source, warning, and limitation metadata.
- Historical report evidence presented as current implementation proof without accepted inheritance.

## Current Caveat

T-063 produced the design anchor and acceptance framework only. It did not run package workflows, inspect raw matrices, repair indexes, call LLM services, or validate resolver runtime behavior.

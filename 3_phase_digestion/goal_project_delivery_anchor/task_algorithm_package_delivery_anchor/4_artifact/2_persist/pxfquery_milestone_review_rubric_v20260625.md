# PxFquery Milestone Review Rubric

Generated: 2026-06-25

## Review Scope

Use this rubric after each algorithm-package milestone or whenever a task claims package capability delivery. The reviewer should classify each capability in the anchor, not only the easiest deterministic subset.

## Minimum Capability Review Set

| Capability | Review question | Acceptable evidence |
|---|---|---|
| Forward query | Can a perturbation plus biological context produce functional response output? | Current run/artifact with ranked or scored functional programs and status metadata |
| Reverse query | Can a functional target plus biological context produce ranked perturbation candidates? | Current run/artifact with candidate ranking, directionality, and numeric sanity check |
| Biological context | Does context affect retrieval or proxy selection? | Context filter/proxy evidence and exact/proxy context status |
| Exact routing | Are exact matches tried and labeled first? | Route metadata and source index/matrix reference |
| Proxy routing | Are sparse cases routed through approved proxy evidence when required? | Proxy trigger, source, similarity or hierarchy basis, and limitations |
| Not-found routing | Are unsupported inputs safely returned as no-hit/not-found? | Negative-control evidence with no false-positive substitution |
| Resolver entry | Can user-facing natural-language or semi-structured query entry dispatch correctly when required? | Resolver startup, parse result, dispatch result, and logs |
| LLM assist | Does the configured AI service perform required parse/summary behavior? | Backend evidence, prompt/call path, output, fallback metadata |
| Deterministic fallback | Is fallback explicit, safe, and labeled? | Triggered fallback evidence with route status |
| Evidence metadata | Do outputs expose status, route, source, warning, and limitation metadata? | Machine-readable output fields or report table |
| Standard resources | Is the package compatible with T-021 resources or an approved successor? | Load/parse evidence or accepted unchanged resource inheritance |

## Classification Rules

- `delivered`: Working behavior is demonstrated by current milestone evidence. Planned behavior, old reports, or code presence alone are insufficient.
- `partial`: The capability works only for a narrow subset, lacks robustness evidence, has unresolved warnings, or only part of the required path is shown.
- `blocked`: Evaluation or operation cannot proceed because a dependency, resource, configuration, account, or tool is unavailable.
- `failed`: The capability was attempted and returned incorrect, unsafe, or unusable behavior.
- `downgraded`: A required capability was removed, optionalized, or replaced by a weaker substitute.
- `deferred-user-approved`: Deferral is explicit and user-approved.
- `deferred-not-approved`: Deferral is proposed, implicit, or convenient but lacks explicit user approval.
- `out-of-scope`: The capability is truly outside the milestone contract, not merely inconvenient.
- `evidence-insufficient`: The claim may be plausible but lacks enough accepted evidence.

## Acceptance Thresholds

An algorithm-package milestone is not fully delivered unless the in-scope minimum capability set is classified as `delivered` or, where appropriate, `deferred-user-approved` for explicitly non-critical staged work. A milestone with missing forward query, unsafe not-found behavior, absent metadata, or incompatible standard resources cannot be accepted as a delivered package milestone.

Resolver, proxy, and LLM capabilities are scope-sensitive. They may be `out-of-scope` only if the milestone contract explicitly excludes them. If the milestone includes them, blocked or fallback-only evidence must remain visible and cannot be reclassified as delivered without matching primary-path evidence or explicit user-approved fallback-only scope.

## Evidence Hierarchy

1. Current task or milestone run artifacts with machine-readable outputs.
2. Current task review tables, logs, and reports that cite run artifacts.
3. Registered predecessor evidence when the milestone explicitly inherits it and no relevant state changed.
4. Code presence or historical legacy reports, which support planning but do not by themselves prove current delivery.
5. Planned behavior, which is never delivery evidence.

## Required Reviewer Notes

The review must record unresolved warnings, fallback paths, false-positive risks, missing assets, and any mismatch between manuscript claim language and development delivery scope. The review must also state whether every deferral or downgrade has explicit user approval.

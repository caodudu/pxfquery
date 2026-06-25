# Recommended Stress Test Milestone Tasks

Generated: 2026-06-24
Task: T-058 04_stress_test_development_handoff_pack
Sources: T-055, T-056, T-057, T-007

---

## Overview

The following 7 tasks constitute a recommended milestone for PxFquery stress-test development. Each task is grounded in predecessor digestion evidence (T-055 source map, T-056 scenario inventory, T-057 reuse boundary) and aligned with T-007 development state recommendations.

The task sequence assumes T-007 D001 (Establish Current Package Workspace) is the entry prerequisite — the stress-test milestone cannot begin until the package is importable in the current project.

---

## ST-M01: Establish Stress-Test Workspace and Asset Access

**Objective**: Create a current-project stress-test workspace with access to all reuse-ready assets and registered query indexes, without copying or modifying legacy flat library files.

**Estimated scope**: Small (1-2 sessions)
- Create a stress-test module or directory within the development phase
- Symlink or reference the migrated query indexes (`data/query_indexes/`) as read-only runtime indexes
- Symlink or reference the 10 direct-reference reports (M-0239, M-0291, M-0277, M-0275, M-0267, M-0243, M-0244, M-0290) for evidence reading
- Copy the resolver source code (`resolver.py`, `forward.py`, `reverse.py`) as canonical reference; do not modify
- Document which rewrite-needed scripts (Section 4 of handoff pack) are staged for porting
- Verify that `function_index.json` gap is noted and that placeholder handling is in place

**Predecessor dependency**: T-007 D001 (Current Package Workspace)
- The stress-test workspace must sit on top of an importable PxFquery package

**Rationale**: All 11 rewrite-needed scripts (T-057 §2.2) require a current-project workspace before porting can begin. T-007 Gap #4 documents that old workspace paths are the primary barrier. This task creates the clean target workspace without touching the flat library.

**Anchoring evidence**:
- T-057 §3.1: "Every script uses old workspace paths"
- T-007 Gap #1: "Package runnability not verified"
- Handoff pack Section 4: 11 rewrite-needed scripts require workspace first

---

## ST-M02: Rebuild Function Index

**Objective**: Recover or rebuild the missing `function_index.json` runtime asset from its builder script, and register it as a current index asset.

**Estimated scope**: Medium (2-3 sessions)
- Port `M-0373_build_function_index.py` (rewrite needed, T-057) to the current workspace with updated paths
- Locate the source xpr_func_ad.h5ad functional matrix and verify its var_names contain the expected 91 functions
- Run the builder; compare output (function count, alias count) against M-0252 report (91 functions, 243 aliases)
- Register the rebuilt `function_index.json` as a current asset
- Verify `FunctionIndex` class loads from the rebuilt JSON
- If h5ad is unavailable: document the blocker and escalate; do NOT fabricate a placeholder index

**Predecessor dependency**: ST-M01 (Stress-Test Workspace)
- Requires workspace paths and function matrix access

**Rationale**: This is the single highest-priority gap. T-055 (§2.4 Notable gap), T-056 (SC-027), T-057 (§3.4), and T-007 (Gap #2) all independently identify `function_index.json` as missing. Reverse query scenarios (SC-002, SC-023, SC-027) depend on it. The builder script (M-0373) is the only known recovery path.

**Anchoring evidence**:
- T-055 §2.4 Notable gap: "No function_index.json was found"
- T-057 §2.2: "M-0373 HIGH PRIORITY for rewrite"
- T-007 Gap #2: "function_index.json is missing from migrated runtime query indexes"
- Handoff pack Section 5: Ranked as #1 priority gap

---

## ST-M03: Port Deterministic Query Regression Suite

**Objective**: Port the 7-case deterministic forward matrix test and minimal smoke test into the current workspace, and produce a fresh current-project deterministic regression run.

**Estimated scope**: Medium (2-4 sessions)
- Port `M-0386_test_forward_matrix.py` (rewrite needed, T-057) with mock hooks and current package imports
- Port `M-0387_test_resolver_smoke.py` (rewrite needed) with mock provider as default, not real LLM
- Run the 7-case matrix covering: EXACT gene, EXACT drug, PROXY_PERT gene, PROXY_PERT drug, PROXY_CELL, PROXY_BOTH gene, and unknown-cell case
- Compare results against M-0291 evidence: expected 7/7 pass across all hit levels
- Document any divergence from legacy results
- Register the ported scripts as current-artifact test assets

**Predecessor dependency**: ST-M01 (workspace), ST-M02 (function index — needed if any test exercises function resolution)
- Mock tests with prompt hooks may run without function index; verify

**Rationale**: The deterministic matrix test (M-0291, 7/7 pass) is the strongest existing validation evidence in the entire corpus (T-057 §2.1). M-0386's mock hook architecture (query_intents, parse_intent_hook, map_cell_hook) is the preferred approach for deterministic resolver testing. T-007 D003 recommends running "direct forward/reverse without LLM first." The 29-scenario inventory anchors 5 scenarios (SC-004, SC-005, SC-017, SC-018, SC-019) to this evidence.

**Anchoring evidence**:
- T-057 §2.2: "M-0386 should be the first test ported after resolver package migration"
- T-057 §2.1: M-0291 "is the single strongest piece of validation evidence"
- T-007 D003: "Verify deterministic direct forward/reverse query without LLM first"
- Handoff pack Section 3 asset #2: M-0291 direct reference
- T-055 §5.2: "Use the deterministic forward matrix test as the primary regression test"

---

## ST-M04: Execute Resolver Mode Behavior Suite

**Objective**: Port the question suite runner and execute a controlled cross-mode test covering deterministic, hybrid_fast, and (optionally) always_llm modes.

**Estimated scope**: Medium-Large (3-5 sessions)
- Port `M-0385_run_forward_question_suite.py` (rewrite needed, T-057) with the 14-question bank, switching default to hybrid_fast
- Port `M-0389_verify_resolver_cases.py` (rewrite needed) with hybrid_fast default and output archiving
- Run a subset of the 29 T-056 scenarios that are executable post-ST-M02 and ST-M03:
  - Strict queries: SC-004 (KRAS/A549), SC-005 (erlotinib/A549)
  - Proxy/exact: SC-017 (EGFR/A549 EXACT), SC-018 (PROXY_CELL), SC-019 (PROXY_BOTH), SC-020 (PROXY_PERT drug)
  - Boundary: SC-007 (unknown cell), SC-008 (fake drug), SC-009 (empty string), SC-010 (typo cell)
  - No-hit: SC-011 (EGFR inhibitor generic), SC-012 (NSCLC free text)
  - LLM cross-check: SC-024 (mode divergence), SC-026 (deterministic vs hybrid_fast consistency)
- Cross-reference results against: M-0291 (deterministic 7/7), M-0275 (hybrid_fast 0.825s/3q), M-0277 (always_llm latency), M-0267 (stability 6/9)
- Do NOT run always_llm at scale (SC-025); run 1-2 smoke cases only to confirm mode divergence
- Register the ported scripts and result artifacts

**Predecessor dependency**: ST-M01, ST-M02, ST-M03
- Requires deterministic baseline, function index, and workspace

**Rationale**: This is the core stress-test execution task. T-056 defines 29 scenarios across 9 dimensions; this task exercises the subset that is executable after foundation tasks. T-057 identifies M-0385 as the "most comprehensive validation script" and M-0389 as a valuable regression template. T-007 D004 recommends "small hybrid_fast question suite with no summary first."

The deliberately conservative scope (14-18 scenarios, not all 29) respects T-056's risk flags: SC-001 (multi-gene) and SC-003 (drug+gene combined) are expected FAIL and may require resolver changes before testing is meaningful. SC-022 (multi-drug multi-context) is FAIL. These high-risk scenarios should be deferred to ST-M07.

**Anchoring evidence**:
- T-057 §2.2: M-0385 "14-question bank covers good scenario diversity"
- T-056: 29 scenarios defined with rationale and source anchors
- T-007 D004: "Run deterministic matrix tests or mock-hook tests"
- Handoff pack Section 2: Complete scenario-to-asset cross-walk
- M-0275: 0.825s baseline for hybrid_fast; M-0277: 167s baseline for always_llm

---

## ST-M05: Port LLM Stability Evaluator (Optional, External-Dependency)

**Objective**: Port the LLM stability checker as an optional off-CI test, and produce a fresh stability measurement with the current LLM provider.

**Estimated scope**: Small-Medium (1-3 sessions)
- Port `M-0377_check_llm_stability.py` (rewrite needed, T-057) with:
  - Current LLM provider configuration
  - 3-5 cases (not just 3) to improve statistical resolution
  - 3 rounds per case
  - Output archiving (this script produces no output in its current form)
- Run against SC-011 (EGFR inhibitor), SC-012 (NSCLC), SC-024 (mode divergence case), plus 1-2 well-behaved exact cases as controls
- Document stability rate and compare against M-0267 baseline (6/9)
- If stability degrades (e.g., <50%): flag as escalating risk
- If stability improves (e.g., >80%): document but DO NOT upgrade manuscript claims without further validation
- Do NOT include in CI; this is an optional manual test requiring LLM API access

**Predecessor dependency**: ST-M01, ST-M02, ST-M03 (optional: can run after ST-M01 if mock deterministic tests pass)
- Requires LLM API credentials configured in current workspace

**Rationale**: LLM stability is the most consistently documented risk across all predecessors: T-055 §5.3, T-056 SC-011/SC-012/SC-024, T-057 §2.1 (M-0267), T-007 Gap #3. M-0267's 6/9 stability represents the only formal measurement. T-007's safer claims recommend "deterministic retrieval is the scientific foundation" — a fresh stability measurement confirms or updates that posture. The optional/external-dependency designation reflects T-057's recommendation: "do not include in CI."

**Anchoring evidence**:
- T-057 §2.2: M-0377 "Port as optional external-dependency test"
- T-007 Gap #3: "LLM path unstable and slow; use hybrid_fast as default"
- M-0267: 6/9 baseline for comparison
- Handoff pack Section 4 risk: "Real LLM dependency (no mock fallback) — medium"

---

## ST-M06: Reverse Query Stress-Test Extension

**Objective**: Extend stress-test coverage to reverse-query scenarios, addressing the known imbalance where forward-query testing dominates.

**Estimated scope**: Medium (2-4 sessions)
- Verify reverse query works with rebuilt function index (post-ST-M02)
- Execute the four reverse-query scenarios from T-056:
  - SC-002: Multi-function reverse (activate apoptosis + suppress MYC + suppress BCL2 / A549)
  - SC-006: Strict reverse with proxy disallowed (activate apoptosis / A549)
  - SC-015: Pan-cancer broad context reverse (activate apoptosis / "cancer")
  - SC-027: Reverse with function not in 91-function index (activate autophagy / A549)
- Compare results against Act-1 legacy evidence (M-0255, with M-0239 caveat)
- Do NOT create new scenarios beyond the four T-056 defines
- Document: (a) which scenarios pass with EXACT matches, (b) which fall to proxy, (c) which correctly return NOT_FOUND, (d) whether function_index.json rebuild was sufficient

**Predecessor dependency**: ST-M02 (must have function index), ST-M01 (workspace)
- Can run independently of ST-M03/M-04 if direct reverse query code path is importable

**Rationale**: T-007 Gap #7 identifies reverse query as "under-validated." T-057 §3.5 notes "test coverage is good for forward query, sparse for reverse." Only Act-1 (M-0255) provides reverse evidence, and that report carries mixed authority per M-0239. T-056 defines 3 reverse scenarios plus 1 reverse-boundary scenario (SC-027 for missing function index). This task fills a coverage gap using existing scenario definitions — no invention needed.

**Anchoring evidence**:
- T-007 Gap #7: "Reverse query is implemented but less deeply validated"
- T-057 §3.5: "Reverse testing should be expanded in future development"
- T-056: SC-002, SC-006, SC-015, SC-027 (4 reverse scenarios)
- Handoff pack Section 5: Gap #5 (reverse under-validated, medium priority)

---

## ST-M07: Stress-Driven Case Study and Risk Register

**Objective**: Synthesize all stress-test milestone results into a consolidated case-study demo and an updated risk register for carry-forward into manuscript-phase tasks.

**Estimated scope**: Medium (2-4 sessions)
- Select one well-supported forward case with clean evidence (recommended: SC-004/SC-017 — EGFR or KRAS in A549, EXACT, with deterministic match)
- Select one reverse case (recommended: SC-006 — activate apoptosis in A549, with proxy disallowed) if ST-M06 produced usable results
- Produce a minimal demo walkthrough: input → resolver path → hit level → top N functional programs / perturbation candidates → evidence bundle metadata
- Run the high-risk scenarios that were deferred from ST-M04 to confirm expected failure behavior:
  - SC-001 (multi-gene forward) — expected FAIL
  - SC-003 (drug+gene combined) — expected FAIL
  - SC-011 (generic drug) — expected INCONSISTENT (mode-dependent)
  - SC-022 (multi-drug multi-context) — expected FAIL
  - SC-025 (always_llm latency) — expected LATENCY_ISSUE
- Document each failure with: what was expected, what actually happened, which risk gap it maps to
- Update the risk register from T-007 A-008 with fresh evidence:
  - Was function_index.json rebuild successful → resolve Gap #2
  - Was deterministic matrix result reproduced → confirm Gap #1 resolution or escalate
  - Is LLM stability better/worse than 6/9 → update Gap #3
  - Is drug generic-query still inconsistent → update Gap #8
- Register all result artifacts (demo outputs, risk register v2) as current-project assets

**Predecessor dependency**: ST-M01 through ST-M06
- Consolidates results from all previous tasks

**Rationale**: T-007 D005 recommends selecting "a narrow biological demonstration that is easy to explain" for a Genes-style case study. T-056's scenario inventory provides the candidate pool — the scenarios that passed (SC-004, SC-005, SC-017) are naturally the right demo content. The expected-failure scenarios (SC-001, SC-003, SC-011, SC-022, SC-025) should be run not to "fix" but to produce honest risk evidence that a manuscript can frame as "known limitations."

The risk register update creates a clean carry-forward bridge from this stress-test milestone to the next development or manuscript phase.

**Anchoring evidence**:
- T-007 D005: "Select one concrete Genes-style case study"
- T-056: 29 scenarios including 6 expected to FAIL
- T-007 A-008: Gap and risk list v1 to be updated with stress-test evidence
- M-0243 known_risks: 6 risks to re-verify post-stress-test
- Handoff pack Section 5: 19 gaps consolidated; Section 6: T-007 alignment

---

## Task Sequence Summary

```
T-007 D001 (prerequisite: establish current package workspace)
    │
    ▼
ST-M01: Establish Stress-Test Workspace and Asset Access
    │
    ├──────────────────────┐
    ▼                      ▼
ST-M02: Rebuild        ST-M03: Port Deterministic
Function Index          Query Regression Suite
    │                      │
    ├──────────────────────┤
    ▼                      ▼
ST-M04: Execute Resolver Mode Behavior Suite
    │
    ├──────────────────────┐
    ▼                      ▼
ST-M05: Port LLM        ST-M06: Reverse Query
Stability Evaluator     Stress-Test Extension
    │                      │
    ├──────────────────────┘
    ▼
ST-M07: Stress-Driven Case Study
        and Risk Register
```

### Task dependency rationale

| Task | Depends on | Why |
|---|---|---|
| ST-M01 | T-007 D001 | Stress-test workspace needs importable package |
| ST-M02 | ST-M01 | Builder needs workspace paths and h5ad access |
| ST-M03 | ST-M01, ST-M02* | Mock tests may pass without function index; verify |
| ST-M04 | ST-M01, ST-M02, ST-M03 | Needs deterministic baseline and function index |
| ST-M05 | ST-M01, ST-M03 | Needs workspace; can run independent of ST-M04 |
| ST-M06 | ST-M01, ST-M02 | Needs function index; independent of forward tests |
| ST-M07 | ST-M01..ST-M06 | Consolidates all milestone results |

*ST-M03 may run without ST-M02 if deterministic mock tests use prompt hooks that bypass function index. Verify during ST-M03 scoping.

### Constraints (from T-058 protocol, applied to all ST-Mxx tasks)

- Do not implement or run stress tests in this digestion task (T-058). These are recommendations for future tasks.
- Do not modify predecessor task outputs (T-055, T-056, T-057, T-007).
- Do not read raw legacy assets or scan unregistered directories.
- Do not prescribe implementation details (specific code changes, class names, database schemas).
- If function_index.json cannot be rebuilt, escalate honestly rather than fabricating a placeholder.

### Approximate milestone scope

| Task | Sessions | Risk level | LLM needed? |
|---|---|---|---|
| ST-M01 | 1-2 | Low | No |
| ST-M02 | 2-3 | Medium (h5ad dependency) | No |
| ST-M03 | 2-4 | Low-Medium | No (mock) |
| ST-M04 | 3-5 | Medium | Optional (always_llm smoke only) |
| ST-M05 | 1-3 | Medium | Yes (manual, off-CI) |
| ST-M06 | 2-4 | Medium | No |
| ST-M07 | 2-4 | Low | No |
| **Total** | **13-25** | | |
# T-062 Step List And Extraction Notes

Generated: 2026-06-25

## Step Discipline

| Step | Sub-goal | Operation | Expected evidence/output | Dependency |
|---|---|---|---|---|
| 1 | Confirm task structure and selected assets only | Inspect task-local folders and registered symlink assets | Asset paths present and no new discovery needed | None |
| 2 | Extract capability and risk facts | Read A-001 through A-007 and only inspect A-008 names/guide-level metadata if needed | This extraction note | Step 1 |
| 3 | Draft deliverables | Create anchor YAML, matrix CSV, downgrade rules, rubric, vocabulary, Chinese MD/HTML summary | Files under `4_artifact/` | Step 2 |
| 4 | Validate deliverables | Parse YAML/CSV and check required files are non-empty | Validation evidence in completion/report | Step 3 |
| 5 | Register and report | Update `4_artifact/registry.yaml`, write completion and required HTML reports | Registry and reports | Step 4 |

## Extracted Authority Points

- T-003 records that the current project protocol was rewritten from migrated context instead of preserving legacy protocol shells. The active identity is a LINCS-based perturbation-to-function workflow/tool, with legacy roots treated as read-only historical sources.
- T-007 defines intended product behavior as forward query `(biological context, perturbation) -> functional response`, reverse query `(biological context, desired functional program) -> candidate perturbations`, exact match first, then proxy evidence through cell-line hierarchy and gene/drug neighbor indexes.
- T-007 states LLMs should assist parsing, mapping, and summarization while numerical retrieval remains deterministic and evidence-aware.
- T-007 warns against claiming stable broad AI-agent behavior, stable natural-language resolver performance across domains, current-project manuscript-ready validation, or complete distribution/download support.
- T-013 required MVP behavior includes local functional matrix reading, controlled forward and reverse queries, serializable table/JSON outputs, and found/not-found status.
- T-013 current evidence shows forward exact query passed, reverse query is partial due to numeric warning, not-found handling failed due to fuzzy false-positive risk, resolver/proxy is blocked by index naming and missing function index in that run, and DeepSeek endpoint connectivity passed as a gated backend check.
- T-021 standard resources provide three float32 h5ad functional matrices, ten JSON query indexes including rebuilt `function_index.json`, five CSV metadata tables, and a data description file. The guide says these are Python-verified and package-compatible.

## Anchor Implications

- Deterministic lookup alone is insufficient for a milestone that includes user-facing resolver, LLM-assisted parsing/summarization, proxy routing, transfer behavior, or transparent fallback.
- Runtime fallback is acceptable behavior only when the primary path is attempted or explicitly scoped, reported, and evidenced. It cannot be counted as delivery of a removed primary capability.
- Missing, blocked, deferred, or downgraded capabilities must remain visible in future milestone reviews. Required capability removal, optionalization, or deferral needs explicit user approval.
- Manuscript claim restraint limits external claims; it does not reduce development acceptance criteria for package milestones.

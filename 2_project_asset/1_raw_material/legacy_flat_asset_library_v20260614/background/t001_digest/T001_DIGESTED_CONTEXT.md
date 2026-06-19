# T001 Digested Context

This file replaces the need to migrate old protocol/navigation shells.

## Project Background
# Project Background Extraction

## What PxFquery Is

- **PxFquery** is a Python bioinformatics tool for perturbation-to-function analysis using LINCS (Library of Integrated Network-based Cellular Signatures) data
- Core class `pxfquery` provides methods: `load_pxf`, `load_llm`, `load_anno`, `pert2func`, `func2pert`
- Integrates single-cell expression data (AnnData/h5ad), compound metadata, and LLM-based analysis
- Uses LiteLLM as provider-agnostic LLM access layer
- Built on CMAP (Connectivity Map) perturbation datasets, specifically Alzheimer's Disease (AD) studies

## Why It Exists

- **Academic requirement**: First-author tool paper for graduation (master's/PhD)
- **Target journal**: MDPI *Genes* — not a top-tier journal, chosen for realistic acceptance
- **Strategic angle**: LINCS-based perturbation-to-function workflow with biological case study
- **Minimal viable submission**: Avoid over-engineering; understand *Genes* acceptance ecology first
- **Author constraints**: Graduation timeline, health limitations, limited time → must be pragmatic

## Academic/Submission Goal

- **Primary**: Publish a tool paper in MDPI *Genes* describing PxFquery as a bioinformatics workflow
- **Narrative**: "LINCS-based perturbation-to-function workflow with biological case study"
- **Scope**: Minimal results to close the loop for the *Genes* use case (Phase C)
- **Risk posture**: Understand *Genes* acceptance criteria before building full tool (Phase A)
- **Four-phase strategy**:
  - **Phase A**: Understand *Genes* journal requirements and submission ecology
  - **Phase B**: Position PxFquery to match *Genes* expectations
  - **Phase C**: Produce minimal results to close the loop
  - **Phase D**: Write manuscript and package submission

## Constraints That Shape It

- **Engineering**:
  - Development in VSCode + Obsidian vault
  - Four-stage overlay structure (10_, 20_, 30_, 40_ phases)
  - Archive directory (90_archive) for frozen pre-restructure files
  - Checkpoint policy for reproducibility and rollback
  - AI-assisted development via OpenCode on HPC with custom glibc/proxy
- **Submission**:
  - Target *Genes* journal — not a high-impact journal
  - "Fast manuscript" mode — minimal viable submission
  - No over-engineering; no exaggeration of AI agent capabilities
- **Collaboration**:
  - Chinese primary communication language
  - Pragmatic naming conventions
  - AI must respect personal constraints when suggesting tasks
- **Data**:
  - CMAP datasets (AD-specific): `cmap_cp_ad.h5ad`, `cmap_sh_ad.h5ad`, `cmap_xpr_ad.h5ad`
  - Compound metadata: `cp_meta_unique.csv` (BRD → drug name mapping)
  - Cell line metadata: `cellline_meta_sub.csv`
  - Gene sets: `merged.gmt` (MSigDB Hallmark sets)
  - Gene attribute matrix: `gene_attribute_matrix_standardized.txt.gz` (1.1 GB)

## Narrative Direction from Old Assets

- **Primary narrative**: LINCS-based perturbation-to-function workflow → biological case study → *Genes* submission
- **Supporting technologies**:
  - MCP (Model Context Protocol) for AI-tool integration
  - LangChain for agent patterns
  - LiteLLM for multi-provider LLM access
  - Local Ollama for inference
- **Key strategic documents**:
  - `PROJECT_BRIEF.md`: Core strategic intent and phase plan
  - `ROADMAP.md`: Four-stage submission strategy
  - `DECISIONS.md`: Organizational history and restructuring rationale
  - `DIRECTORY_MAP.md`: Phase-based workflow logic
  - `MD_SYSTEM_GUIDE.md`: Navigation and maintenance conventions
- **Personal context**:
  - Author profile: graduation requirement, first-author paper, limited time
  - Constraints: submission target, engineering tools, health considerations
  - Preferences: Chinese communication, pragmatic scope, no over-engineering
- **Phase-specific direction**:
  - Phase A: Understand *Genes* acceptance ecology (completed)
  - Phase B: Position PxFquery to match *Genes* (code scaffold exists)
  - Phase C: Minimal results (scope defined, results navigation exists)
  - Phase D: Manuscript writing and submission (structure defined, narrative set)


## Old Asset Structure Understanding
# Old Asset Structure Understanding

## Project Overview

The legacy project is organized as a **four-stage overlay structure** built on top of an older mixed directory layout. The current structure was a deliberate reorganization decision documented in `00_meta/DECISIONS.md`.

## Core Organizational Layers

### 1. Meta Layer (`00_meta/`) — Project Control Hub
- **Purpose**: Central governance, decision records, and navigation
- **Contains**:
  - Decision logs (`DECISIONS.md`)
  - Directory maps (`DIRECTORY_MAP.md`)
  - System guides (`MD_SYSTEM_GUIDE.md`)
  - Project briefs and dashboards (`PROJECT_BRIEF.md`, `PROJECT_DASHBOARD.md`)
  - Roadmaps (`ROADMAP.md`)
  - Personal constraints and preferences (`personal/`)
  - AI prompt templates (`prompts/`)

### 2. Phase Directories (`10_phase_A_`, `20_phase_B_`, `30_phase_C_`, `40_phase_D_`)
- **Purpose**: Workflow stages for journal submission strategy
- **Phase A** (`10_phase_A_understand_genes/`): Journal understanding and submission strategy
  - Contains: analysis, references, notes, prompts
  - Key files: `MOC_phase_A.md`, journal analysis READMEs
- **Phases B-D**: Defined but not fully populated in the snapshot

### 3. Archive Layer (`90_archive/`)
- **Purpose**: Historical snapshots and frozen old workspace
- **Contains**:
  - Pre-restructure workspace (`20260429_pre_restructure/`)
  - Claude workspace with full 4t protocol implementation
  - Checkpoint system with rollback capability

## Where the Real Operational Core Lives

### Active Code & Data (in Archive Workspace)
- **Code**: `90_archive/.../workspace/script/PxFquery/`
  - Core modules: `core.py`, `loader.py`, `forward.py`, `reverse.py`, `resolver.py`
  - Resolver scripts: `workspace/script/word_new/6_llm_resovler/`
- **Data Assets** (read-only inputs):
  - `workspace/input/`: Cell line metadata, compound info, gene annotations
  - `workspace/input/cmap/`: Connectivity Map beta data
  - `workspace/input/genePT/`: Precomputed gene embeddings (large binary files)
  - `workspace/input/genesets/`: MSigDB hallmark gene sets
- **Processed Outputs**:
  - `workspace/output/store/genePT/`: Filtered gene embeddings
  - `workspace/output/store/gsea_anndata/`: GSEA-ready AnnData files
- **Reports & Evidence**:
  - `workspace/report/`: Resolver runs, step documentation, indexes

### Context & Navigation System
- **Context Layer**: `workspace/context/`
  - `context_manifest.yaml`: Reading order and constraints
  - `INDEX.md`: L0/L1/L2 reading hierarchy
  - `module_cards/`: Architecture, data, resolver, reports, risks
  - `deep_dive/`: Canonical design documents
  - `governance/`: Content governance policies
  - `task_playbooks/`: Audit checklists

## Where Strategy Lives

### Strategic Documents (Canonical Sources)
1. **`00_meta/ROADMAP.md`**: Four-stage submission strategy targeting MDPI Genes
2. **`00_meta/PROJECT_BRIEF.md`**: Core strategic intent and phase plan
3. **`00_meta/PROJECT_DASHBOARD.md`**: Current one-sentence goal and priorities
4. **`00_meta/personal/constraints.md`**: Submission target (Genes), engineering constraints
5. **`00_meta/prompts/task/phase_A_genes_understanding.md`**: Journal-specific strategy
6. **`10_phase_A_understand_genes/analysis/journal_analysis/README.md`**: Strategic conclusions about Genes

### Design Documents (Architecture)
1. **`workspace/context/deep_dive/01_project_design_workspace.md`**: Project goals, method narrative, risks
2. **`workspace/context/deep_dive/02_code_design_workspace.md`**: Package structure, resolver architecture
3. **`workspace/context/deep_dive/source_archive/PxFquery_project.source.md`**: Project overview with phases
4. **`workspace/context/deep_dive/source_archive/PxFquery_code.source.md`**: Code design guide

## What Parts Are Overlays or Archive Noise

### Overlays (Structural Artifacts, Not Core Content)
- **`00_meta/MOC_meta.md`**: Navigation index — useful but replaceable
- **`00_meta/SYSTEM_PROMPT_DRAFT.md`**: Pointer file, no unique content
- **`10_phase_A_understand_genes/notes/README.md`**: Navigation rules, not substantive
- **`10_phase_A_understand_genes/references/legacy_reference_workspace/README.md`**: Directory map only
- **`workspace/context/module_cards/40_reports_and_evidence.md`**: Navigation aid, not primary data
- **`workspace/context/task_playbooks/project_audit.md`**: Procedural checklist

### Archive Noise (Historical, Low Reuse Value)
- **Checkpoint templates** (`checkpoint_entry_template.md`): Outdated format
- **Old `.gitignore` files**: Workspace-specific, not reusable
- **Draft prompts** (`SYSTEM_PROMPT_DRAFT.md`): Superseded by canonical versions
- **Empty or placeholder files**: Any file with only structural content and no unique data

### Preserved but Frozen (Historical Record)
- **`90_archive/20260429_pre_restructure/`**: Complete snapshot of old workspace
  - Contains all code, data, and context from before restructuring
  - Useful for reference but not for active development
  - Checkpoint system provides rollback history

## Key Structural Observations

1. **Dual Organization**: The project has both a phase-based overlay (10/20/30/40) and a workspace-based operational layer (input/output/report/context) — these are not fully synchronized.

2. **Redundant Navigation**: Multiple MOC files, READMEs, and indexes create overlapping navigation paths (e.g., `MOC_meta.md`, `INDEX.md`, `context_manifest.yaml`).

3. **Scattered Strategy**: Strategic intent is distributed across `00_meta/`, phase directories, and workspace context — no single source of truth.

4. **Data Asset Registry**: `workspace/input/description.yaml` is the only consolidated data catalog, but it's buried in the archive.

5. **Prompt System**: AI interaction protocols are well-defined but split across `00_meta/prompts/` and `workspace/context/` — need consolidation.


## Authoritative Source Priority
# Authoritative Sources Map

## Source Priority

### Priority A: operational truth

- `legacy_4t_workspace/START_HERE.md`
- `legacy_4t_workspace/AI_READ_PROTOCOL.md`
- `legacy_4t_workspace/context/INDEX.md`
- `legacy_4t_workspace/context/deep_dive/01_project_design_workspace.md`
- `legacy_4t_workspace/context/deep_dive/02_code_design_workspace.md`
- `legacy_4t_workspace/report/00_index/latest_reports_index.md`
- `legacy_4t_workspace/report/03_resolver/06_suite_runs/`

Use these first when the question is about:

- what the system actually did
- where current technical evidence lives
- which report is valid
- how the old package was organized

### Priority B: strategic manuscript framing

- `legacy_genes_timing_results/pxfquery_fast_genes_strategy.md`
- `legacy_genes_timing_results/pxfquery_genes_submission_assessment.md`
- `legacy_genes_timing_results/timing_analysis.md`

Use these when the question is about:

- Genes suitability
- workflow framing
- fast-submission strategy

### Priority C: later project overlay

- `legacy_project_root/00_meta/`
- `legacy_project_root/10_phase_A_understand_genes/`
- `legacy_project_root/20_phase_B_position_pxfquery/`

Use these when the question is about:

- later planning logic
- stage decomposition
- user-facing project navigation

## Non-authoritative or lower-priority zones

- old chat transcripts unless they point to a file that became canonical
- duplicated markdown drafts when a workspace canonical file exists
- report folders not endorsed by `latest_reports_index.md`

## Rule for future tasks

Any future task that reads legacy material should first declare which priority layer it is using and why.


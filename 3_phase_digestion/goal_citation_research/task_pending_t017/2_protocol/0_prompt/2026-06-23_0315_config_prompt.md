# Configuration Prompt
Generated: 2026-06-23 03:15

## 1. Mandatory CyHex Protocol Read
Before any configuration work:

1. Call `GET http://localhost:47291/api/version`.
2. Read `cyhex_protocol.md` from the returned `protocol_path`.
3. Treat that file as the only source of CyHex workflow rules.
4. Do not rely on memory or on any CyHex summary in this prompt.

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/cyhex_protocol.md

## 2. Configuration Assignment
You are configuring this one CyHex task. You are not executing it.

Your required output is file changes, not a writing plan:
1. Write or revise current task `protocol.md`.
2. Write or revise current task `asset_rule.yaml`.
3. Register or explicitly identify required/missing assets when needed.
4. Give a short evidence report after writing: files read, assets selected/missing, files changed, blockers if any.

Do not explain human-facing app concepts. They are not part of your assignment.

## 3. Project Reads
Project: PxFquery (P-012)
Phase: development | Status: active

Read project protocol:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/0_overview.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/1_goal.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/2_rule.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/3_environment.md

Read project state:
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/state.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/current_state.md

Browse project asset source candidates. Start from directories, README files, and registries; do not load large files until needed:
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/README.md
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/README.md
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/background
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/background/project_context
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/background/t001_digest
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/analysis_scripts
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/design_docs
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/README.md
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/data
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/data/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/index
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/index/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/llm
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/llm/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/prompt
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/prompt/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/viz
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/viz/__pycache__
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/cmap_ad_matrices
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/functional_matrices
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/genept_embeddings
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/metadata_tables
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/query_indexes
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/history
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/history/design_traces
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/manuscript
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/manuscript/genes_strategy
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/manuscript/manuscript_assets
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/manuscript/reference_articles
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/manuscript/submission_context
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/redacted_secrets
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/digested_context
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/results
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/results/figures
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/results/gsea_pickles
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/results/gsea_tables
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/wxy投稿文件
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/2_bibliography
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/2_bibliography/README.md
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/3_ref_example
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/3_ref_example/README.md

## 4. Current Task Intent
ID: T-017 | Name: Pending T-017
Status: active | Executor: hybrid
Objective: 搜一下mdpi的写作引用格式上哪一种。
可以结合网络搜索，

参考范文的引用区域。

以及wjy的word

但是最后要确定是具体哪一种，因为我需要在zenoto里用

如果是常规模式，我在zenoto里插入

如果不是，帮我搜到下载相关引用格式文件。我忘记一般引用是什么格式文件了
Notes / User Natural-Language Intent: mdpi引用格式
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017

This objective/intent may be informal. Convert it into task protocol and asset rules after reading the required paths.

## 5. Current Task Reads
Read current task files:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/1_asset/registration.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/2_protocol_split/protocol.md
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/3_asset_rule/asset_rule.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/0_prompt

Use these files to decide whether this is a blank pending task or an existing configuration that needs validation and revision.

## 6. Required Predecessor Reads
The human selected the following predecessor tasks/goals as required context. They are not optional background. Read them first, then decide which assets or deliverables should be reused for the current task.

### Reference Task 1: T-015 MDPI submission package and guide
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide
Human-selected reason: this task/goal was selected as required predecessor context for the current task.

Read these files before configuring current task:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/1_asset/registration.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/2_protocol/2_protocol_split/protocol.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/2_protocol/3_asset_rule/asset_rule.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/4_artifact/registry.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_submission_rules/task_mdpi_submission_package_and_guide/5_report/completion.md

### Reference Task 2: T-008 MDPI cross-journal affiliation and PUMCH publication landscape
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape
Human-selected reason: this task/goal was selected as required predecessor context for the current task.

Read these files before configuring current task:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/1_asset/registration.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/2_protocol/2_protocol_split/protocol.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/2_protocol/3_asset_rule/asset_rule.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/4_artifact/registry.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_magazine_research/task_mdpi_cross_journal_affiliation_landscape/5_report/completion.md

### Reference Task 3: T-016 Digest WXY Genes template paper package
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper
Human-selected reason: this task/goal was selected as required predecessor context for the current task.

Read these files before configuring current task:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/1_asset/registration.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/2_protocol/2_protocol_split/protocol.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/2_protocol/3_asset_rule/asset_rule.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/4_artifact/registry.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_digest_wxy_genes_template_paper/5_report/completion.md


## 7. Asset Configuration Work
Asset selection is the core of this stage.

Use only the following scoped sources unless a missing asset must be acquired:
1. Current task asset registry: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/1_asset/registration.yaml`
2. Project asset candidates under: `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`
3. Required predecessor task asset registries and artifact registries listed above
4. External web/search/download only if the task needs an asset that is not present locally

Do not conclude "no assets" just because the current task registry is empty. Empty registry means you must inspect the scoped candidate sources and decide what should be registered.

## 8. Files To Write
Write or revise:
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/2_protocol_split/protocol.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/2_protocol/3_asset_rule/asset_rule.yaml`

If assets must be registered, update:
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017/1_asset/registration.yaml`

If name/objective is empty or clearly wrong, propose the correction in your final evidence report. Do not create a duplicate task name.

After writing configuration files, call this API to generate the downstream action prompt and verify it exists:
- `POST http://localhost:47291/api/projects/12_PxFquery/tasks/goal_citation_research/task_pending_t017/prompt/generate`

## 9. Final Evidence Report
After writing files, output a concise report with:
1. Files actually read.
2. Predecessor tasks actually read.
3. Assets selected, registered, missing, or intentionally not used.
4. Files written or revised.
5. Generated action prompt path, if generation succeeded.
6. Blockers, if configuration cannot be completed.

End with exactly one of:
- `配置完成。请确认：配置通过 / 提出修改意见`
- `配置无法完成。需要补充：...`

## Hard Stops
- 不执行任务本体
- 不写 4_artifact/ 交付物
- 不把 task 标记为 done
- 不跳过人类配置确认点
- 不把 CyHex 协议内容复制进任务协议；任务协议只写当前任务本体

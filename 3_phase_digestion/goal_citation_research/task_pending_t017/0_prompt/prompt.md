# Configuration Prompt
Generated: 2026-06-23 01:47

## CyHex Protocol
CyHex protocol v2.11 loaded from /Applications/CyHex.app/Contents/Frameworks/cyhex_protocol.md

## Task Info
- Task ID: T-017
- Task Name: Pending T-017
- Project: P-012 (PxFquery)
- Phase: digestion
- Goal: goal_citation_research
- Status: active
- Sub Status: configuring
- Executor: hybrid

## Objective
确定 MDPI/Genes 期刊的引用格式。具体来说：MDPI 使用的是编号制引用格式（numbered citation style），Zotero 中的官方对应样式名称为 "Multidisciplinary Digital Publishing Institute"。该 CSL 文件存在于 Zotero 官方样式仓库中，可直接在 Zotero 偏好设置中搜索安装。CSL 文件的原始下载地址为：
https://raw.githubusercontent.com/citation-style-language/styles/master/multidisciplinary-digital-publishing-institute.csl

## Assets
- A-001: T-015 MDPI submission rules outputs (deliverable, local) — 提供 MDPI 投稿规则上下文，交叉验证引用格式规则。
- A-002: WXY manuscript_v8.docx (raw, local) — Genes 期刊已投稿论文，检验实际使用的引用格式（编号制 [1], [2]）。
- A-003: MDPI Reference List and Citations Style Guide (reference, url) — https://www.mdpi.com/authors/references — MDPI 官方引用格式指南。
- A-004: MDPI CSL file (reference, url) — https://raw.githubusercontent.com/citation-style-language/styles/master/multidisciplinary-digital-publishing-institute.csl — 官方 CSL 样式文件。
- A-005: Zotero Style Repository page (reference, url) — https://www.zotero.org/styles/?q=id%3Amultidisciplinary-digital-publishing-institute — Zotero 官方仓库确认该样式可安装。
- A-006: Alternative MDPI Zotero style repo (other, url) — 非官方替代样式，仅供参考。

## Asset Rules
- Required: A-001, A-002, A-003, A-004, A-005
- Optional: A-006
- Forbidden to modify: ../../../2_project_asset/1_raw_material/wxy投稿文件/, ../../6_project_deliverable/
- Modifiable: 3_execution/, 4_artifact/, 5_report/
- Non-modifiable: 1_asset/, 2_protocol/, wxy投稿文件/

## Protocol Summary
1. 读取 MDPI 官方引用指南 (A-003)，确认官方引用格式要求。
2. 检查 WXY 论文 (A-002) 的文中引用格式和参考文献列表，确认实际使用的格式。
3. 通过网络搜索确认 Zotero CSL 样式名称："Multidisciplinary Digital Publishing Institute"。
4. 定位并下载官方 CSL 文件 (A-004)，保存到 4_artifact/6_archive/。
5. 记录在 Zotero 中安装该样式的方法。
6. 生成 Markdown 格式的调查结果报告。

## Deliverables
- MDPI citation format investigation report: 4_artifact/2_persist/mdpi_citation_format_findings_v20260623.md
- Downloaded MDPI CSL file (if needed): 4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl

## Hard Stops
- 不修改 WXY 原始投稿文件。
- 不把 task 标记为 done（需人类验收）。
- 不写 6_project_deliverable/。
- 不将 CyHex 协议内容复制进任务输出。
- 执行完成时生成 execution_report 和 result_report 两份 HTML 报告。

## Project Context
PxFquery is targeting MDPI Genes for manuscript submission. MDPI uses the "Multidisciplinary Digital Publishing Institute" Zotero style, a numbered (ACS-based) citation format using [1], [2] bracket numbering in text. This style is a standard Zotero repository style — no manual CSL file download is required. In Zotero: Preferences → Cite → Styles → Get additional styles → search "Multidisciplinary Digital Publishing Institute" → install.
# Protocol: 生信查询网站交付可行性调研

## Objective
调研 PxFquery 生信查询工具的网站交付方案：包括托管平台选择（GitHub Pages 等）、LLM API 集成可行性、从制作到部署的全流程，以及低成本前后端方案（含价格对比）。按四个独立子任务交付。

## Inputs
- A-001: T-007 PxFquery development state digest — 了解当前 PxFquery 的技术架构（Python 包、索引查询逻辑、LLM 集成现状），作为网站方案设计的参考背景。
- A-002: PxFquery 项目协议 — 提供项目定位（Genes 投稿导向、轻量实用工具）边界，约束网站方案不偏离项目目标。
- A-003: 外部网络资源 — 通过浏览器搜索获取的在线资料、论文链接、GitHub Pages 案例、云服务定价页面等。此资产为动态获取，不预先存在本地。

## Steps
1. 阅读 T-007 核心报告（A-001）和项目协议（A-002），明确 PxFquery 当前技术形态和项目边界。
2. **子任务 1 — GitHub Pages 调研：** 搜索确认 github.io 是否可作为学术论文配套网站；搜索至少 3 篇已将工具网站托管在 github.io 并正式发表的生物信息学/计算生物学论文，提供论文标题、链接、网站 URL。
3. **子任务 2 — LLM API 集成可行性调研：** 调研 GitHub Pages（纯静态托管）是否能对接大模型 API；分析 PxFquery 的 LLM 功能（自然语言→查询转译）在纯静态站点 vs 需要后台服务器的技术边界；给出可行的集成方案（如客户端直接调 API、Serverless 函数、轻量后端等）。
4. **子任务 3 — 生信网站全流程报告：** 输出一份从网站制作到挂出上线的完整流程，覆盖域名、托管、部署、维护等环节，并说明对分析型网站的特殊要求（如 Python 后端运行环境、数据文件托管）。
5. **子任务 4 — 低成本前后端方案调研与价格登记：** 调研并对比至少 3 种方案（如 GitHub Pages + Vercel/Netlify Functions、Railway、Fly.io、阿里云轻量服务器等），登记每种方案的预估年费（1-2 年）、免费额度、优势与限制。
6. 将四个子任务结果分别写入 `4_artifact/2_persist/` 下的独立 markdown 文件。
7. 整合所有调研结果，在 `4_artifact/3_document/` 下生成两份 HTML 报告：`execution_report_v{YYYYMMDD}.html`（执行情况）和 `result_report_v{YYYYMMDD}.html`（面向人类读者的成果展示）。
8. 编写 `5_report/completion.md`，登记交付物到 `4_artifact/registry.yaml`。

## Constraints
- 这是调研任务，不是实施任务。不搭建实际网站，不购买服务，不注册域名。
- 搜索结果必须给出真实可访问的 URL 和可验证的论文信息，不得编造。
- 涉及外部网络搜索的子步骤必须使用浏览器搜索工具，不得仅凭训练数据记忆。
- 价格信息需注明信息来源（URL）和查询日期。
- 不修改项目代码、迁移资产库或已有任务交付物。

## Deliverables
- `4_artifact/2_persist/github_pages_academic_hosting_research.md` — 子任务 1 成果
- `4_artifact/2_persist/llm_api_static_site_feasibility.md` — 子任务 2 成果
- `4_artifact/2_persist/bioinfo_website_deployment_guide.md` — 子任务 3 成果
- `4_artifact/2_persist/low_cost_fullstack_hosting_comparison.md` — 子任务 4 成果
- `4_artifact/3_document/execution_report_vYYYYMMDD.html`
- `4_artifact/3_document/result_report_vYYYYMMDD.html`

## Acceptance
- 每个子任务都有独立的、内容充实的交付文档。
- 论文案例真实可查，每条均有 URL。
- 价格方案覆盖至少 3 个选项，标注来源和查询日期。
- 全流程报告覆盖从代码到上线的完整环节。
- LLM API 集成分析能区分静态站点能做什么、不能做什么，并给出可行的技术路径。
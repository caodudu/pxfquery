I see this is a **checking stage** prompt, not a configuration stage prompt. I was previously executing the configuration prompt. Let me now execute the checking prompt. Let me first read the current task
I notice the configuration stage already produced files but the previous turn ended abnormally (no evidence report was emitted). The current stage is **checking**. The check prompt notes that an action prompt (`{latest_action_prompt.md}`) is missing — but the prompt file I see is the check prompt itself, indicating the execution action prompt hasn't been generated yet.

Let me check the file structure and proceed with the checking stage work.
Now let me also check the predecessor tasks. The user previously selected T-024 and T-013 as predecessors. Let me check their assets and artifacts for
Now I have enough context. Let me also look at the legacy LLM module to understand what's expected, and check `notes.jsonl`/`history.jsonl` for context:
Good. Now I have a thorough understanding. Let me perform the checking:

**Key findings:**

1. **Status**: `active` with `sub_status: checking` — correct, no PATCH needed.
2. **Assets**: `registration.yaml` is empty (`assets: []`), `asset_rule.yaml` has all empty lists. Protocol references no concrete assets. But the task's objective (DeepSeek v4 flash adapter using CyHex llm_gateway) is self-contained code generation — it needs **project environment info** and **legacy LLM code reference** as assets.
3. **Protocol Steps**: Steps are vague ("Use the current CyHex/OpenCode default model configuration", "Implement graceful fallback", "Run a small endpoint/config smoke check") — no concrete steps or paths.
4. **Deliverables**: Listed but not concretely specified with paths.
5. **No action prompt generated** — the prompt path is missing.
6. **`3_execution/` is empty** — ok for checking stage.

The protocol needs concrete steps and deliverables with paths. The registration needs environment and legacy LLM code as assets. Let me fix
Good. Now I understand the legacy LLM module pattern. T-024 produced `pxfquery-T-024` workspace. Now let me check if T-024's workspace has an LLM module:
Good. The T-024 workspace has the legacy LLM module as a reference. Now I have all the context. Let me proceed with the checking-stage repairs:

**Repair Plan:**
1. Revise `protocol.md` to add concrete Steps, deliverable paths, and acceptance criteria.
2. Populate `registration.yaml` with required assets (project environment, project protocol, legacy LLM module reference, T-024 workspace LLM module, CyHex API endpoint).
3. Populate `asset_rule.yaml` making those assets required.
4. Regenerate the action prompt.

Let me make the repairs:
Now let me regenerate the action prompt:
Action prompt generated successfully at `2_protocol/0_prompt/2026-06-23_0727_action_prompt.md` and is consistent with the repaired protocol and asset rule. Let me verify the file is there:
Action prompt is in place. Now delivering the evidence report:

---

## 检查与修复报告

### 一、我准备如何遵守 CyHex
- **实际文件和目录**：本 task 工作目录 `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1/task_llm_flash_adapter_v1/`；使用 CyHex 本地 API `http://localhost:47291`；`3_execution/` 存放 smoke 脚本和 llm_gateway 快照；`4_artifact/` 存放 adapter 代码、smoke 记录、文档和 HTML 报告。
- **需要的 API**：`GET /api/version`（llm_gateway snapshot），`POST .../prompt/generate`（已调用），`POST .../artifacts/auto_register` 或直接写 `4_artifact/registry.yaml`（执行阶段）。
- **禁止目录/行为**：不修改 `2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/`；不修改 T-024 的 `4_artifact/`；不翻转 CyHex llm_gateway 默认模型；不自行 PATCH task 为 done。
- **阻断触发条件**：4 个 required 资产全部不可读；`pxfquery` conda 环境无法启动；上游 T-024 交付物被删除或损坏。

### 二、我准备如何达成任务目标
- **用自己的话复述**：在 T-024 workspace 基础上，做一个可选的 DeepSeek v4 flash adapter 层。它和 legacy `LLMClient` 保持相同接口，端点不可用时优雅降级（返回结构化的 `ok: false`），并且写清楚 `导入适配器→端点不可用→管线照常运作` 的降级路径。不修改 T-024 的文件。
- **执行计划（9 步）**：记录 CyHex api/version 快照 → 读取 T-024 workspace LLM 模块 interface → 写 `DeepSeekFlashAdapter` → 更新 task 自身目录下的 `__init__.py` → 写 `pyproject.toml` → 跑 import / py_compile smoke → 运行 smoke endpoint script → 写两个 HTML 报告和文档 → 写 completion。
- **输出**：位于 `4_artifact/2_persist/workspace/src/pxfquery/llm/adapter/` 和 `4_artifact/2_persist/` 下；报告在 `4_artifact/3_document/` 下。
- **为什么可执行**：所有 required 资产均存在且可读；T-024 workspace 提供 `LLMClient` 接口参照；CyHex API 可用并已生成 action prompt；pyproject 环境和 `pxfquery` conda 环境在 T-024 已验证。

### 三、检查与修复
- **问题 1**：`registration.yaml` 为空（`assets: []`）。**已修复** — 登记 A-001~A-004 共 4 个资产。
- **问题 2**：`asset_rule.yaml` 全部字段为空。**已修复** — required 登记 A-001~A-004，forbidden 登记上游目录，modifiable 登记 A-004。
- **问题 3**：`protocol.md` 的 Steps 模糊（"Use the current CyHex/OpenCode default..."），交付物缺路径。**已修复** — 重写为 9 个具体 Step，每个 Step 含具体命令、目标文件和验证方式；每项 Deliverable 都有精确路径。
- **问题 4**：缺少 action prompt。**已修复** — `POST .../prompt/generate` 返回成功，action prompt 落盘到 `2_protocol/0_prompt/2026-06-23_0727_action_prompt.md`，内容与 protocol、assets、asset_rules 一致。
- **无阻断问题**：所有 required 资产路径均为 readable path；无空壳资产；协议步骤可通过现有能力完成。
- **检查的状态检查**：task `status: active, sub_status: checking`，无需 PATCH。
- **4_artifact/ 空模板**：检查通过 — 各子目录结构已就位（由 CyHex 初始化创建），不包含交付物（执行阶段写入）。

---

检查完成。请确认：检查通过，开始执行 / 提出修改意见

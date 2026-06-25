This is a repair prompt — the task went into `config_interrupted` state and needs validation. Let me verify the current configuration is complete and consistent.
Now let me check that the symlinks exist in `1_asset/` and verify the latest generated
The symlinks are missing. The registration.yaml says `symlink: true` for all 4 assets but the actual symlink files were never created in the `1_asset/` directory. This is the inconsistency that needs repair — registration says they should be symlinks but they don't exist on disk.

Let me fix this by creating the sym
All 4 symlinks created and resolve to real files. Now let me regenerate the action prompt since the asset registration was fixed (symlinks were missing, which could affect the prompt's ability to reference asset
配置完成。任务目标：从 T-021 标准资源包创建包含 7 个 resolver 兼容 JSON 符号链接的 `pxfquery-T-027` 运行时查询索引目录，并交付 schema 报告。提示词路径：`2_protocol/0_prompt/2026-06-23_0803_action_prompt.md`。

**本次修复内容**：`registration.yaml` 中 4 个资产（A-001 ~ A-004）均标记 `symlink: true` 但实际符号链接未创建，导致前次配置为 config_interrupted 状态。已在 `1_asset/` 下创建 4 个符号链接：
- `T-021 standard_resources bundle (D-004)` → T-021 D-004 目录
- `T-025 resource manifest (D-006).yaml` → T-025 manifest
- `T-025 schema summary (D-007).md` → T-025 schema summary
- `T-021 artifact registry.yaml` → T-021 artifact registry

所有链接可解析到实际文件。协议、资产规则、资产登记均保持之前版本，内容一致无需修改。提示词已重新生成。

配置通过 / 提出修改意见

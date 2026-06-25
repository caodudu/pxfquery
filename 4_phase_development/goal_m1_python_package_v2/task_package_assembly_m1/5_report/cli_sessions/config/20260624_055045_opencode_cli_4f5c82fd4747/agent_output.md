Let me inspect the actual package structures from the predecessor tasks
Now I'll write all three configuration files.
## Final Evidence Report

**1. Verdict:** `green_config`

**2. Files actually read:**
- `meta.yaml` for all 3 predecessor tasks (T-044, T-059, T-060)
- `handoff_ai_use.md` for all 3 predecessor tasks
- `4_artifact/registry.yaml` for all 3 predecessor tasks
- T-044 skeleton package files: `pyproject.toml`, `pxfquery/cli/__init__.py`, `pxfquery/cli/__main__.py`, `pxfquery/query/forward.py`, `pxfquery/query/reverse.py`
- T-059 package files: `src/pxfquery/core.py`, `src/pxfquery/__init__.py`, `src/pxfquery/cli/__init__.py`, `src/pxfquery/cli/main.py`, `src/pxfquery/query/forward.py`, `src/pxfquery/query/reverse.py`
- T-060 fixture: `reverse_repair_manifest_m1_1.yaml`, directory listing for `4_artifact/1_package/pxfquery` (confirmed symlink)
- T-059 fixture: `forward_repair_manifest_m1_1.yaml`
- CyHex API version (confirmed v1.2.19)

**3. Predecessor tasks actually read:**
- T-044 `package_skeleton_m1` — skeleton with stub modules
- T-059 `forward_query_core_repair_m1` — forward+reverse query implementations
- T-060 `reverse_query_core_repair_m1` — reverse repair fixture (D-001 is symlink to T-044, not accepted as task-local code)

**4. Assets selected / registered / missing / planned-web:**
- 15 assets registered (A-001 through A-015)
- Key assets: T-044 CLI wiring (A-002, A-003), T-059 forward+reverse query logic (A-004, A-005), T-059 core.py reference (A-010, requires func2pert rewiring), T-059 forward fixture (A-011), T-060 reverse fixture (A-013)
- T-060/D-001 (package code) explicitly NOT selected — is a symlink to T-044, not accepted as standalone reverse code
- `query/reverse.py` from T-059 (A-005) selected as authoritative reverse implementation instead
- No planned-web assets

**5. Files written or revised:**
- `1_asset/registration.yaml` — 15 assets registered
- `2_protocol/2_protocol_split/protocol.md` — full protocol with objective, steps, constraints, deliverables
- `2_protocol/3_asset_rule/asset_rule.yaml` — required/optional/forbidden/output/modifiable rules

**6. Confirmation that no downstream prompt endpoint was called:** Confirmed. Only `GET /api/version` was called.

**7. Blockers:** None. Configuration is complete.

---

**Key architectural finding:** T-059's package includes both `query/forward.py` and `query/reverse.py` with full implementations. T-059's `core.py` returns `NotImplemented` for `func2pert()`, so the assembly must create a new `core.py` that wires both. T-059's `cli/__init__.py` only has `forward` command; T-044's `cli/__init__.py` has `forward` + `reverse` + `info` — use T-044's CLI init. T-060 contributes only the reverse repair fixture (A-013), not package code.

配置完成。请确认：配置通过 / 提出修改意见
配置完成。三个文件已写入：

1. **`1_asset/registration.yaml`** — 15 个资产注册 (A-001 ~ A-015)，覆盖 T-044 骨架 CLI、T-059 前向/反向实现、T-060 反向 fixture
2. **`2_protocol/2_protocol_split/protocol.md`** — 完整协议：组装步骤（建目录→复制模块→接线 core.py→安装→烟测→forward demo→reverse demo→收集证据）、约束、交付物、接受标准
3. **`2_protocol/3_asset_rule/asset_rule.yaml`** — 必需的输入资产、可选资产、禁止项（2_project_asset/、T024-T040、T-048/T-049）、输出目录

关键发现：T-059 的 `query/reverse.py` 已有完整反向实现，但 `core.py` 中 `func2pert()` 返回 `NotImplemented`；组装时需新写 `core.py` 完成接线（不改查询逻辑）。T-060 只贡献反向 fixtue，不贡献包代码。

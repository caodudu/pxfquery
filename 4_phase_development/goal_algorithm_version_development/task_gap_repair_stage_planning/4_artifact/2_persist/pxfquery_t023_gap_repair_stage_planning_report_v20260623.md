# PxFquery 缺口修复阶段规划报告

生成时间: 2026-06-23
来源任务: T-023 gap_repair_stage_planning
基于证据: T-013 (MVP走查) + T-007 (开发状态理解) + T-012 (Genes论文模式分析)

---

## 一、缺口总览与优先级

### 1.1 修复优先级判断

T-013 审查发现 4 个需要修复的缺口。按阻塞关系和论文路径排序：

| 优先级 | 缺口 | 状态 | 阻塞影响 |
|--------|------|------|----------|
| P0 | CAP-03 索引不可用 | fail | 阻断 resolver/NL/全部自然语言入口 |
| P0 | CAP-07 NL resolver 阻断 | blocked | 阻断自然语言查询链路，论文无法描述 |
| P1 | CAP-05 未命中误报 | fail | 无意义输入返回假阳性结果，论文可信度受损 |
| P2 | CAP-06 反向查询数值warning | partial | 影响论文定量展示的可信度 |

修复阶段逻辑：
- **第1阶段**（P0）：CAP-03 + CAP-07 必须一起修复，因为索引修复是 resolver 启动的前置条件。
- **第2阶段**（P1）：CAP-05 需要在 resolver 基础可用后修复 fuzzy/no-hit 逻辑。
- **第3阶段**（P2）：CAP-06 在核心检索稳定后进行数值稳健性改善和论文级打磨。

---

## 二、逐缺口技术诊断

### 2.1 CAP-03：查询索引不可直接被 resolver 使用

**T-013 证据:**
- T013-ASSET-002, T013-MVP-005, T013-MVP-006
- 迁移索引文件带 M-前缀（如 M-0202_cellline_index.json），resolver 期望无前缀文件名
- function_index.json 未迁移

**技术根因:**
- resolver.py 第92-104行硬编码了索引文件名：
  - `cellline_index.json`, `cellline_neighbors.json`
  - `gene_index_simple.json`, `gene_neighbors_simple.json`
  - `drug_index.json`, `drug_neighbors.json`
  - `function_index.json`
- 迁移时 T-002 保留了原始文件名（含 M-编号前缀）作为 provenance 标记
- function_index.json 由 build_function_index.py 从 h5ad 的 var_names 构建，需要 h5ad 源文件读取 91 个功能列名，但该文件在迁移资产中不可用

**T-013 禁止的修复方式:**
- 不能在 T-013 内静默修改索引文件名
- 不能生成或修复 function_index.json

**代码层面确认:**
- resolver.py: `QueryResolver.__init__` 通过 `self.index_dir / "cellline_index.json"` 等方式加载
- 迁移索引目录 `data/query_indexes/` 中：9 个文件，均无 function_index.json
- build_function_index.py 需要访问 `output/store/gsea_anndata/xpr_func_ad.h5ad`（该文件未在迁移资产中）

**修复方向:**
- 去前缀：将 9 个索引文件从 M-编号前缀改为 resolver 期望的无前缀名
- 重建 function_index.json：需要找到 h5ad 源或从包代码中推断 91 个功能列的 var_names

---

### 2.2 CAP-07：自然语言 resolver / proxy 检索阻断

**T-013 证据:**
- T013-MVP-005, T013-MVP-006
- 当前索引命名和 function_index 缺口阻止 resolver 完整启动

**技术根因:**
- CAP-03 的索引问题直接导致 QueryResolver 初始化失败
- resolver 需要 4 个索引（CellLine, Drug, Gene, Function）全部可用才能实例化
- CellLineIndex 需 2 个文件、FunctionIndex 需 1 个文件——缺少任一个都会报 FileNotFoundError

**依赖性:**
- 完全依赖 CAP-03 修复
- 不需要代码修改，仅需要索引文件到位

**修复方向:**
- 完成 CAP-03 的索引修复后，resolver 即可启动
- 用 hybrid_fast 模式（无 LLM 调用）先行验证 retrieval 链路
- 有 DeepSeek API key 后再加 LLM 解析/总结

---

### 2.3 CAP-05：未命中查询误报

**T-013 证据:**
- T013-MVP-002
- fuzzy fallback 对无意义扰动名给出相近 token，误匹配为真实基因名

**技术根因:**
- resolver.py 的 `_force_forward_evidence` 方法（第500-555行）
- 当 must_answer=True 且 EXACT/PROXY_PERT/PROXY_CELL/PROXY_BOTH 全未命中时触发
- `_name_similarity` 使用 SequenceMatcher 做字符相似度计算（第490-498行）
- 对无意义输入如 "ZZZ999" 仍可能匹配到短基因名如 "ZIC2"
- 当前没有相似度阈值门控——只要 best_score > 0 就返回 FORCED_FALLBACK
- 返回的 hit_level 为 "FORCED_FALLBACK"，但结果不标注 confidence

**代码层面确认:**
- `_force_forward_evidence`: must_answer_token_match → must_answer_similarity 两级 fallback
- `_name_similarity`: 做字母数字规范化后计算 SequenceMatcher 比值
- 没有最小相似度阈值，没有 no-hit 截断

**修复方向:**
- 为 `_force_forward_evidence` 加相似度阈值（例如 0.6），低于阈值返回 NOT_FOUND 而非 FORCED_FALLBACK
- 或者在返回后由上层标注 "low_confidence" 标记，由调用方决定是否展示
- 为 resolver_meta 增加 confidence_score 字段

---

### 2.4 CAP-06：反向查询数值稳健性警告

**T-013 证据:**
- T013-MVP-003
- A549 中凋亡激活/MYC 抑制可以产生候选排序，但出现矩阵相似度数值 warning

**技术根因:**
- 警告来自 reverse.py 中的余弦相似度计算（用于 ranking 扰动和功能目标之间的相似度）
- 可能原因：零范数向量、NaN 值、或极端稀疏导致余弦相似度不稳定
- reverse.py 使用 scipy 或 numpy 的余弦距离/相似度计算

**修复方向:**
- 检查 reverse.py 中的 similarity 计算是否有 NaN guard
- 加入零范数向量跳过逻辑（跳过而非崩溃）
- 在 ranking 结果中标注计算稳定性信息

---

## 三、分阶段 G-006 任务建议

### 第1阶段：基础层恢复（P0）

#### 任务建议 G-006-T1：索引目录修复与 function_index 重建

**目标:** 让 resolver 可以初始化并运行 hybrid_fast 模式

**具体工作:**
1. 在 G-006 workspace 下创建受控的当前索引目录（不修改迁移资产）
2. 将 9 个迁移索引文件去 M-前缀后复制到当前索引目录
3. 重建 function_index.json：
   - 方案A（优先）：从 h5ad 矩阵的 var_names 提取 91 列名，使用 build_function_index.py 逻辑重建
   - 方案B（降级）：从 function_index.py 的文档和 curated aliases 反向推断 var_names 列表，手工构建
4. 验证 CellLineIndex、DrugIndex、GeneIndex、FunctionIndex 全部可实例化

**验收标准:**
- resolver 初始化不报 FileNotFoundError
- function_index 有 91 个条目、包含 hallmark 和 3ca_mps 两类
- aliases 表包含 curated 缩写（emt, apoptosis, myc 等）
- 所有索引文件在当前索引目录下，迁移资产未修改

**依赖:** 无（是 G-006 的起点任务）
**需要人类决策:** 方案A 需要找到 xpr_func_ad.h5ad 文件位置；如不可用，使用方案B
**完成后解锁:** CAP-07 自动修复；G-006-T2 可执行

---

#### 任务建议 G-006-T2：resolver hybrid_fast 验证

**目标:** 验证 resolver 在确定性模式下（无 LLM）可正确完成检索链路

**具体工作:**
1. 使用 T-013 已运行的测试用例（EGFR/A549 forward、A549 apoptosis reverse）重跑
2. 配置 use_fast_path=True，避免 LLM 调用
3. 验证四层命中（EXACT/ PROXY_PERT/ PROXY_CELL/ PROXY_BOTH）正常
4. 验证 NOT_FOUND 案例正常返回

**验收标准:**
- EGFR/A549 forward 查询返回 ForwardResult 且 found=True
- A549 apoptosis/MYC 反向查询返回候选排序
- 至少一个 NOT_FOUND 案例返回且不崩溃
- resolver_meta 包含 hit_level、used_cell、used_perturbation

**依赖:** G-006-T1（索引目录修复）
**需要人类决策:** 是否需要配置 DeepSeek key 开始 LLM 测试
**完成后解锁:** 可以声明 resolver 基础链路可用；G-006-T3 可执行

---

### 第2阶段：行为正确性修复（P1）

#### 任务建议 G-006-T3：解决未命中查询误报

**目标:** fuzzy fallback 不再对无意义输入返回假阳性结果

**具体工作:**
1. 在 `_force_forward_evidence` 中增加相似度阈值参数（默认 0.6）
2. 低于阈值的匹配返回 NOT_FOUND 而非 FORCED_FALLBACK
3. 在 resolver_meta 中增加 confidence_score 字段（0-1浮点数）
4. 为 NOT_FOUND 结果写明确的中文提示

**验收标准:**
- 无意义输入 "ZZZ999" 返回 NOT_FOUND（或至少不返回假基因名）
- 正常输入 EGFR/A549 仍返回正确结果
- T-013 原测试用例 T013-MVP-002 场景不再误报
- confidence_score 在所有结果中可用

**依赖:** G-006-T2（resolver hybrid_fast 验证通过）
**需要人类决策:** 阈值的合理值可由人类在验收时调整
**完成后解锁:** 论文可声称 "查询对未支持输入安全返回 not-found 状态"

---

### 第3阶段：数值稳健性与论文打磨（P2）

#### 任务建议 G-006-T4：反向查询数值稳健性修复

**目标:** 消除矩阵相似度警告，确保排名结果数值稳定

**具体工作:**
1. 在 reverse.py 中定位 cosine similarity 计算
2. 加入 NaN/Inf guard 和零范数向量跳过
3. 在 ranking 输出中标注 "数值稳健" 或 "含低质量向量"
4. 写 unit-like smoke test：固定输入产生固定输出

**验收标准:**
- T-013 相同用例重跑后无相似度 warning
- 零范数向量被跳过且记录在日志/元数据中
- ranking 输出可复现

**依赖:** G-006-T3（行为正确性修复完成）
**需要人类决策:** 无
**完成后解锁:** 可进入论文案例选择（G-006-T5）

---

## 四、阶段间依赖关系

```
G-006-T1 (索引修复)
    └── G-006-T2 (resolver hybrid_fast 验证)
            └── G-006-T3 (未命中误报修复)
                    └── G-006-T4 (反向查询稳健性修复)
                            └── G-006-T5 (Genes 案例选择与论文级验证)
```

所有任务都可以在同一 goal (G-006) 下作为独立 CyHex task 注册。

## 五、需要人类决策的阻塞点

1. **function_index.json 重建方案:** 需要确认 xpr_func_ad.h5ad 或等效的 91 列 h5ad 文件可从哪里获取。如果无法获取，同意使用方案B（从 function_index.py 和 build_function_index.py 推断重构）。
2. **索引目录位置:** 同意在 G-006 workspace 下创建新的当前索引目录（不修改迁移资产）。
3. **DeepSeek LLM 时间:** 是否需要与基础检索修复同步进行 LLM 测试，还是等基础链路验证稳定后再加。

## 六、Genes 论文措辞对齐

当各阶段完成后，论文中对应能力的推荐措辞：

- **第1阶段完成后:** "PxFquery uses pre-built query indexes for cell lines, genes, drugs, and gene set functions to support rapid, deterministic retrieval."（参考 software_package_or_tool 措辞模式）
- **第2阶段完成后:** "For unsupported queries, the system returns a clear not-found status rather than a spurious match."（弱点承认模式，Genes 论文常见）
- **第3阶段完成后:** "Reverse query ranks candidate perturbations by cosine similarity to the target functional profile, with numerical stability checks applied."（算法方法描述模式）

详细措辞对照见 `pxfquery_t023_repair_genes_wording_v20260623.md`。

---

*本报告基于 T-013 的 4 个缺口证据、T-007 的开发状态理解、以及迁移包代码/设计文档/索引目录的只读检查。不包含任何代码执行或资产修改。*
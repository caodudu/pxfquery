# TODO List (Resolver / LLM)

更新时间：2026-04-10

## 本轮完成（logger 重构）
- [x] 新增统一 logger 配置模块（模块名/级别/格式/开关统一）。
- [x] 新增 `verbosity`：`quiet` / `normal` / `debug`。
- [x] 新增 `log_llm_io` 开关（默认关闭，debug 下可开启）。
- [x] 新增按日期文件日志输出：`pxfquery_YYYY-MM-DD.log`。
- [x] resolver 日志加入 `query_id`，并同步写入 `resolver_meta.query_id`。
- [x] 保留 `resolver_meta.llm_call_stats` 并在完成日志中输出查询级统计。
- [x] 最小验证完成：`compileall` + `test_forward_matrix.py` + 文件日志落盘检查。

## 已完成
- [x] 单条性能定位：确认旧慢点来自 LLM 延迟 + 证据收集全表扫描。
- [x] Resolver 证据匹配加速：增加 `(cell, pert)->query_name` 缓存，替代重复布尔筛选。
- [x] 证据预算落地：EXACT/PROXY 分层预算 + 总预算（默认 15）。
- [x] `run_forward_question_suite.py` 增强：`--limit/--ids/--no-summary/--output-tag` + 分项计时。
- [x] 外部 API demo 跑通：PubChem + Cellosaurus 报告已生成。
- [x] cellline stepwise 多场景 demo 已补充。
- [x] LLM 轻任务默认关闭推理模式；summary 保留推理模式。
- [x] 加入意图与映射缓存（同进程重复问答可接近 0 延迟）。
- [x] 加入快速本地解析与快速层级选择（LLM 兜底），典型 forward 查询压到 < 1s（no-summary）。

## 进行中
- [ ] 质量守护：快速路径与 LLM 路径的一致性回归（避免“快但语义偏移”）。
- [ ] 疾病上下文到 proxy cell 的选择策略解释文档（便于论文写法）。

## 下一步
- [ ] 增加 `--force-llm` 开关：强制全 LLM 路径用于对照实验。
- [ ] 增加“5 秒预算模式”配置：超时后自动降级到快速路径 + 证据说明。
- [ ] 为 summary 增加两档：`fast`（无推理）/`quality`（有推理）。

## 本轮新增完成
- [x] 修复 stepwise demo 与生产 resolver 逻辑不一致（trace 增加 source）。
- [x] 修复 NSCLC / colorectal 快速选择偏差。
- [x] 修复 drug/genetic 快速判定，药物 query 正确进入 `cp`。
- [x] 增加 MiniMax 临时 5xx 重试机制。
- [x] 增加可复现实验脚本 `verify_resolver_cases.py`。
- [x] suite 结果按时间戳归档到统一目录并生成索引。

## 本轮收尾
- [x] 增加 `always_llm` / `hybrid_fast` 双模式说明与实现。
- [x] `hybrid_fast` 下 LLM失败 warning + 自动降级。
- [x] 增加查询级真实 LLM 调用统计（非估算）。
- [x] 增加 `Resolver_Workbench.ipynb` 供分 block 验证。
- [x] 增加 `check_llm_stability.py`。
- [x] 更新 6_llm_resovler README 与 suite 输出规范。
- [x] 实测中国区 highspeed 可用性并记录结论。

# Code Design (Workspace Canonical)

来源：
- `markdown/PxFquery_code.md`
- `workspace/script/PxFquery/*` 当前实现
- `workspace/report/01_status/core_modules_and_tests.md`

本文件是工作区内“代码架构与模块职责”的主文档。

## 1. 包结构主线

- 入口：`workspace/script/PxFquery/core.py`
- 数据：`workspace/script/PxFquery/data/loader.py`
- 查询：
  - `workspace/script/PxFquery/query/forward.py`
  - `workspace/script/PxFquery/query/reverse.py`
  - `workspace/script/PxFquery/query/resolver.py`
- 索引：`workspace/script/PxFquery/index/*.py`
- LLM：`workspace/script/PxFquery/llm/prompts.py`

## 2. resolver 架构

- 意图解析：`llm_parse_intent`
- B 定位：cellline index + 树遍历
- P 定位：gene/drug index + 邻域代理
- 四层命中：`EXACT / PROXY_PERT / PROXY_CELL / PROXY_BOTH`
- 证据预算：避免无限候选堆积
- 查询模式：`always_llm` / `hybrid_fast`

## 3. 当前实现状态（以代码为准）

- `index/`：已实现并接入 resolver
- `query/resolver.py`：已实现并在套件中验证
- `llm/prompts.py`：resolver 主用
- `llm/client.py`：兼容保留（非 resolver 主路径）

## 4. 脚本与验证

主脚本目录：`workspace/script/word_new/6_llm_resovler/`

核心脚本：
- `run_forward_question_suite.py`
- `verify_resolver_cases.py`
- `test_forward_matrix.py`
- `check_llm_stability.py`

## 5. 后续扩展点

1. resolver 输出统一 run_id（md/json/log 贯通）
2. summary 双档（fast/quality）标准化
3. 异常与 fallback 行为统一可配置
4. 统一 legacy 报告清退策略（保留不删除，弱化入口）

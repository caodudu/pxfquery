# Architecture Card

## 核心主线

- 入口：`workspace/script/PxFquery/core.py`
- 数据加载：`workspace/script/PxFquery/data/loader.py`
- 基础查询：
  - 正向：`workspace/script/PxFquery/query/forward.py`
  - 反向：`workspace/script/PxFquery/query/reverse.py`
- 解析器：`workspace/script/PxFquery/query/resolver.py`

## 当前状态

- resolver 主链路已启用。
- 模式：`always_llm`（叙事）+ `hybrid_fast`（容灾/速度）。

## 进入深读

- `workspace/report/01_status/core_modules_and_tests.md`
- `workspace/markdown/PxFquery_code.md`

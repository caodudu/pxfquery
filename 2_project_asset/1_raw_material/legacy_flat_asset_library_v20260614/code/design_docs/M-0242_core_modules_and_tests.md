# 核心模块职责与测试脚本用途

## 核心模块职责

- `workspace/script/PxFquery/core.py`：包入口，统一加载/查询/可视化/resolver。
- `workspace/script/PxFquery/data/loader.py`：xpr/sh/cp h5ad 数据加载。
- `workspace/script/PxFquery/query/forward.py`：正向查询（pert -> func）。
- `workspace/script/PxFquery/query/reverse.py`：反向查询（func -> pert）。
- `workspace/script/PxFquery/query/resolver.py`：自然语言解析、索引映射、四层命中、证据预算。
- `workspace/script/PxFquery/index/*.py`：细胞系/基因/药物/功能索引封装。
- `workspace/script/PxFquery/llm/prompts.py`：当前 resolver 主用 LLM prompt 层。
- `workspace/script/PxFquery/llm/client.py`：旧接口兼容层（非 resolver 主路径）。

## 测试脚本用途

- `run_forward_question_suite.py`：主套件（命中/耗时/prompt计时/llm_call_stats）。
- `verify_resolver_cases.py`：快速检查分流与命中级别范围。
- `test_forward_matrix.py`：mock hooks 下四层命中确定性验证。
- `test_resolver_smoke.py`：初始化与基础正反向冒烟测试。
- `validate_act1.py`：端到端双 case 验证。
- `check_llm_stability.py`：LLM intent 解析稳定性测试。
- `demo_*.py`：演示脚本（不作为主回归证据）。

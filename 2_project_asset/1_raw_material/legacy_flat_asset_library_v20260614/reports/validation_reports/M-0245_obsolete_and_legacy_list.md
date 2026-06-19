# 过时与遗留文件清单（建议保留，不建议删除）

## 遗留目录

1. `workspace/script/PxFquery_old/`
2. `workspace/script/script_old/`

## 历史机制

1. `workspace/report/report.yaml`
- 已标记历史遗留。

## 历史报告副本

1. `workspace/report/03_resolver/03_suite_legacy/*.md`
- 作为过渡期副本保留。
- 当前有效结论优先看 `workspace/report/03_resolver/06_suite_runs/`。

2. `workspace/output/store/resolver_demo/forward_question_suite_*.json`（非时间戳）
- 与 `output/store/resolver_demo/suite_runs/*.json` 重复。
- 本次未触碰 output，仅记录。

## 兼容入口

1. `workspace/report/6_llm_resovler_suite_runs/README.md`
- 旧路径兼容说明，不再存放主报告。

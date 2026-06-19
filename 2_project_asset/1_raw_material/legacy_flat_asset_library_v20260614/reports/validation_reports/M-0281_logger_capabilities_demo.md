# Logger Capabilities Demo (Real Run)

- Time: 2026-04-10 14:22:04
- Scope: resolver logger (mock provider + real local data/index).
- Query used in all cases: `logger demo` (hooked intent -> A549 + EGFR).

## 1) 设计总览

1. 统一入口：`script/PxFquery/logging_utils.py` 提供 `configure_logger()`。
2. verbosity：`quiet`(WARNING+) / `normal`(INFO+) / `debug`(DEBUG+)。
3. query trace：每次 query 生成 `query_id`，写入日志与 `resolver_meta.query_id`。
4. LLM I/O：`log_llm_io=True` 时在 debug 级输出输入/输出摘要。
5. 文件日志：`log_to_file=True` 时写 `prefix_YYYY-MM-DD.log`。
6. 人类可读模式：`log_human_readable=True` 时采用简化格式。

## 2) 从简单到复杂的真实测试

### Case 1: Normal + Technical format

- verbosity: `normal`
- human_readable: `False`
- log_llm_io: `False`
- query_id: `q20260410-142135-0001`
- hit_level: `EXACT`
- llm_call_stats.query: `{}`
- log file: `D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\logs\loggerdemo_01_normal_technical_2026-04-10.log`

日志尾部样例：
```text
2026-04-10 14:21:35 | INFO | pxfquery.resolver | qid=q20260410-142135-0001 | Step 1/3 Start resolve | summarize=True | user_input=logger demo
2026-04-10 14:21:35 | INFO | pxfquery.resolver | qid=q20260410-142135-0001 | Step 2/3 Intent parsed | query_type=forward pert_class=genetic bio_context=A549 pert_desc=EGFR
2026-04-10 14:21:36 | INFO | pxfquery.resolver | qid=q20260410-142135-0001 | Step 3/3 Forward query done | found=True hit=EXACT pert_type=xpr | llm_calls={}
```

### Case 2: Quiet (minimum logs)

- verbosity: `quiet`
- human_readable: `False`
- log_llm_io: `False`
- query_id: `q20260410-142138-0001`
- hit_level: `EXACT`
- llm_call_stats.query: `{}`
- log file: `D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\logs\loggerdemo_02_quiet_minimal_2026-04-10.log`

日志尾部样例：
```text
(empty)
```

### Case 3: Debug + LLM I/O visible

- verbosity: `debug`
- human_readable: `False`
- log_llm_io: `True`
- query_id: `q20260410-142140-0001`
- hit_level: `EXACT`
- llm_call_stats.query: `{}`
- log file: `D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\logs\loggerdemo_03_debug_with_io_2026-04-10.log`

日志尾部样例：
```text
2026-04-10 14:21:40 | INFO | pxfquery.resolver | qid=q20260410-142140-0001 | Step 1/3 Start resolve | summarize=True | user_input=logger demo
2026-04-10 14:21:40 | DEBUG | pxfquery.resolver | qid=q20260410-142140-0001 | LLM hook input | name=llm_parse_intent | args=('logger demo',) | kwargs={}
2026-04-10 14:21:40 | DEBUG | pxfquery.resolver | qid=q20260410-142140-0001 | LLM hook output | name=llm_parse_intent | out={'query_type': 'forward', 'bio_context': 'A549', 'pert_desc': 'EGFR', 'pert_class': 'genetic', 'function_desc': None, 'activate': [], 'suppress': [], 'top_n': 5}
2026-04-10 14:21:40 | INFO | pxfquery.resolver | qid=q20260410-142140-0001 | Step 2/3 Intent parsed | query_type=forward pert_class=genetic bio_context=A549 pert_desc=EGFR
2026-04-10 14:21:40 | DEBUG | pxfquery.resolver | qid=q20260410-142140-0001 | LLM hook input | name=llm_summarize_forward | args=(ForwardResult(perturbation='EGFR', cell_line='A549', n_obs=5, top_activated=5, top_suppressed=5),) | kwargs={'include_numbers': False}
2026-04-10 14:21:40 | DEBUG | pxfquery.resolver | qid=q20260410-142140-0001 | LLM hook output | name=llm_summarize_forward | out='mock summary'
2026-04-10 14:21:40 | INFO | pxfquery.resolver | qid=q20260410-142140-0001 | Step 3/3 Forward query done | found=True hit=EXACT pert_type=xpr | llm_calls={}
```

### Case 4: Normal + Human-readable format

- verbosity: `normal`
- human_readable: `True`
- log_llm_io: `False`
- query_id: `q20260410-142142-0001`
- hit_level: `EXACT`
- llm_call_stats.query: `{}`
- log file: `D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\logs\loggerdemo_04_normal_human_2026-04-10.log`

日志尾部样例：
```text
2026-04-10 14:21:42 | INFO | Step 1/3 Start resolve | summarize=True | user_input=logger demo | qid=q20260410-142142-0001
2026-04-10 14:21:42 | INFO | Step 2/3 Intent parsed | query_type=forward pert_class=genetic bio_context=A549 pert_desc=EGFR | qid=q20260410-142142-0001
2026-04-10 14:21:42 | INFO | Step 3/3 Forward query done | found=True hit=EXACT pert_type=xpr | llm_calls={} | qid=q20260410-142142-0001
```

### Case 5: Real LLM call (MiniMax)

- verbosity: `normal`
- human_readable: `False`
- log_llm_io: `False`
- query_id: `q20260410-142144-0001`
- hit_level: `EXACT`
- llm_call_stats.query: `{'llm_parse_intent': {'count': 1, 'seconds': 19.513}}`
- log file: `D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\logs\loggerdemo_05_live_llm_2026-04-10.log`

日志尾部样例：
```text
2026-04-10 14:21:44 | INFO | pxfquery.resolver | qid=q20260410-142144-0001 | Step 1/3 Start resolve | summarize=False | user_input=In A549, what pathways are affected by EGFR knockdown?
2026-04-10 14:22:04 | INFO | pxfquery.resolver | qid=q20260410-142144-0001 | Step 2/3 Intent parsed | query_type=forward pert_class=genetic bio_context=A549 pert_desc=EGFR knockdown
2026-04-10 14:22:04 | INFO | pxfquery.resolver | qid=q20260410-142144-0001 | Step 3/3 Forward query done | found=True hit=EXACT pert_type=xpr | llm_calls={'llm_parse_intent': {'count': 1, 'seconds': 19.513}}
```

## 3) 结论（人类可读 vs AI 可读）

1. `quiet`：最简，只保留 warning/error，适合只看是否出错。
2. `normal + human_readable=True`：最适合人读，保留关键步骤与状态。
3. `normal + technical`：兼顾追踪，适合开发日常。
4. `debug + log_llm_io=True`：最适合定位复杂问题（信息最多）。

## 4) 推荐配置（你提到的“人类优先”）

```python
pxf.enable_resolver(
    ...,
    verbosity="normal",
    log_human_readable=True,
    log_to_file=True,
    log_dir="report/04_management/logs",
    log_llm_io=False,
)
```
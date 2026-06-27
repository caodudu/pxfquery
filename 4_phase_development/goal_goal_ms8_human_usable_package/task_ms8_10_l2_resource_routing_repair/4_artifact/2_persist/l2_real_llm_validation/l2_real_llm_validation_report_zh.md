# T138 L2 真实 LLM 路由验证报告

- 生成时间：2026-06-27T22:08:04.470272+00:00
- 模型：deepseek-v4-flash
- Base URL：https://api.deepseek.com/v1
- 资源目录：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources`
- 总结果：通过

## 场景结果

### S1_exact_cell_noncoding_gene_function
- 目的：exact A549 + exact MALAT1 lncRNA + exact apoptosis；验证非编码基因 proxy 不是占位。
- 结果：通过
- route_status：routed
- 检查项：
  - cell_resolved: True
  - gene_malat1_lnrna: True
  - function_apoptosis: True
- LLM 调用：
- 路由摘要：
  - cell: ['A549'] candidates=6
  - perturbation: [{'symbol': 'MALAT1', 'gene_type': 'lncRNA', 'in_matrix': False, 'role': 'exact', 'rank': 1}]
  - function: [{'var_name': 'HALLMARK_APOPTOSIS', 'label': 'Apoptosis', 'source': 'hallmark', 'direction': 'target', 'input': 'apoptosis', 'rank': 1}]

### S2_llm_cell_tree_context
- 目的：模糊细胞语境进入真实 LLM cell tree selection。
- 结果：通过
- route_status：routed
- 检查项：
  - cell_llm_call_ok: True
  - cell_candidates_limited: True
- LLM 调用：
  - cell_tree_lineage / ok / deepseek / deepseek-v4-flash / temp=0 / hash=303552cd44f87e204becd8da6e9711b195dd5c48710908cee2c36e02c39b0f04
  - cell_tree_disease / ok / deepseek / deepseek-v4-flash / temp=0 / hash=fcb240861ec4b84bbbc9f81aba75c4ea9f75c5c193e6ed36c2d52f2bd49580c3
  - cell_tree_subtype / ok / deepseek / deepseek-v4-flash / temp=0 / hash=2d274c6ca55924665a102dee293753b2a42859b24eeb3607c7af1c82612697b0
- 路由摘要：
  - cell: ['BEN'] candidates=2
  - perturbation: [{'symbol': 'MALAT1', 'gene_type': 'lncRNA', 'in_matrix': False, 'role': 'exact', 'rank': 1}]
  - function: [{'var_name': 'HALLMARK_APOPTOSIS', 'label': 'Apoptosis', 'source': 'hallmark', 'direction': 'target', 'input': 'apoptosis', 'rank': 1}]

### S3_llm_drug_typo_normalization
- 目的：药物 typo 先召回 top candidates，再由真实 LLM 选择/假设并回索引校验。
- 结果：通过
- route_status：routed
- 检查项：
  - drug_llm_call_ok: True
  - drug_resolved: True
- LLM 调用：
  - drug_normalization / ok / deepseek / deepseek-v4-flash / temp=0 / hash=7f166aa27a77c43880c1c75183b8905fb3f5c2744a374f8e9339a2a295ffaca6
- 路由摘要：
  - cell: ['A549'] candidates=6
  - perturbation: [{'id': 'BRD-K70401845', 'alias': 'erlotinib', 'role': 'llm-normalized', 'rank': 1}]
  - function: [{'var_name': 'HALLMARK_APOPTOSIS', 'label': 'Apoptosis', 'source': 'hallmark', 'direction': 'target', 'input': 'apoptosis', 'rank': 1}]

### S4_llm_gene_descriptive_normalization
- 目的：描述性基因名不直接匹配索引时，由真实 LLM 规范化后回索引校验。
- 结果：通过
- route_status：routed
- 检查项：
  - gene_llm_call_ok: True
  - gene_resolved: True
- LLM 调用：
  - gene_normalization / ok / deepseek / deepseek-v4-flash / temp=0 / hash=57cc7d0ca8fdbebf3a652d763688f26ec0925b69f2dc1e407f4c7309b78afa2b
- 路由摘要：
  - cell: ['A549'] candidates=6
  - perturbation: [{'symbol': 'TP53', 'gene_type': 'protein_coding', 'in_matrix': True, 'role': 'llm-normalized', 'rank': 1}]
  - function: [{'var_name': 'HALLMARK_APOPTOSIS', 'label': 'Apoptosis', 'source': 'hallmark', 'direction': 'target', 'input': 'apoptosis', 'rank': 1}]

### S5_llm_forward_function_mapping
- 目的：模糊功能词由真实 LLM 从固定 91 项 function_index 中选择，不能自由生成。
- 结果：通过
- route_status：routed
- 检查项：
  - function_llm_call_ok: True
  - function_resolved: True
- LLM 调用：
  - function_mapping / ok / deepseek / deepseek-v4-flash / temp=0 / hash=212a942f28f6b901d43e13e19363dc8ee36c2bfd7cffe320f9e40f5b17d06b81
- 路由摘要：
  - cell: ['A549'] candidates=6
  - perturbation: [{'symbol': 'MALAT1', 'gene_type': 'lncRNA', 'in_matrix': False, 'role': 'exact', 'rank': 1}]
  - function: [{'var_name': 'HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION', 'label': 'Epithelial Mesenchymal Transition', 'source': 'hallmark', 'direction': 'target', 'input': 'llm-mapped', 'rank': 1}, {'var_name': 'MP12 EMT-I', 'label': 'EMT-I', 'source': '3ca_mps', 'direction': 'target', 'input': 'llm-mapped', 'rank': 2}, {'var_name': 'MP13 EMT-II', 'label': 'EMT-II', 'source': '3ca_mps', 'direction': 'target', 'input': 'llm-mapped', 'rank': 3}, {'var_name': 'MP14 EMT-III ', 'label': 'EMT-III ', 'source': '3ca_mps', 'direction': 'target', 'input': 'llm-mapped', 'rank': 4}, {'var_name': 'MP15 EMT IV', 'label': 'EMT IV', 'source': '3ca_mps', 'direction': 'target', 'input': 'llm-mapped', 'rank': 5}]

### S6_llm_reverse_three_pass_function_mapping
- 目的：反向查询对模糊功能做三次独立真实 LLM 映射，每次结果都必须回 91 项索引校验。
- 结果：通过
- route_status：routed
- 检查项：
  - reverse_three_sets: True
  - reverse_llm_calls_ok: True
  - reverse_convergence_recorded: True
- LLM 调用：
  - cell_tree_lineage / ok / deepseek / deepseek-v4-flash / temp=0 / hash=339bb7ab19c2baccfb893a247b2af6ef366dc2aa5379ca497b23998b9d48d949
  - cell_tree_disease / ok / deepseek / deepseek-v4-flash / temp=0 / hash=1cba7372c8e898672ccb9c6edc043ef830f067db4488c007dd340e938bf8ab0c
  - cell_tree_subtype / ok / deepseek / deepseek-v4-flash / temp=0 / hash=e47245426c63cab3cb5242e96914863b1c9c9a18feee7f43b6c73a894a9ffb5f
  - function_reverse_mapping_direct_pathway / ok / deepseek / deepseek-v4-flash / temp=0.0 / hash=8e8ca3bfdf22218aaba9a5adcf694783ca7bda2be270bc15651336c707c234c0
  - function_reverse_mapping_mechanism_or_program / ok / deepseek / deepseek-v4-flash / temp=0.35 / hash=8e8ca3bfdf22218aaba9a5adcf694783ca7bda2be270bc15651336c707c234c0
  - function_reverse_mapping_phenotype_or_state / ok / deepseek / deepseek-v4-flash / temp=0.7 / hash=8e8ca3bfdf22218aaba9a5adcf694783ca7bda2be270bc15651336c707c234c0
- 路由摘要：
  - cell: ['BT20'] candidates=6
  - perturbation: []
  - function: [{'var_name': 'HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION', 'label': 'Epithelial Mesenchymal Transition', 'source': 'hallmark', 'direction': 'target', 'input': 'llm-mapped', 'rank': 1}, {'var_name': 'HALLMARK_E2F_TARGETS', 'label': 'E2F Targets', 'source': 'hallmark', 'direction': 'target', 'input': 'llm-mapped', 'rank': 2}, {'var_name': 'HALLMARK_G2M_CHECKPOINT', 'label': 'G2M Checkpoint', 'source': 'hallmark', 'direction': 'target', 'input': 'llm-mapped', 'rank': 3}]
  - reverse interpretation sets: 3
  - reverse convergence: complete_convergence

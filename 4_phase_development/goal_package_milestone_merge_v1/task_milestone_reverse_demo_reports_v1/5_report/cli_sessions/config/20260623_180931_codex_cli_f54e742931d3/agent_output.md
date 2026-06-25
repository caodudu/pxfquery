我会先读取本机 CyHex 协议入口和项目/前置任务配置，只做当前任务的配置文件，不执行任务本体。
CyHex API 可用；我现在按它返回的 `protocol_path` 读取协议，再读取当前任务和四个指定前置任务的配置/产物登记信息。
项目层协议确认了当前工作边界：只在 `12_PxFquery` 内配置，优先使用已迁移资产和前置任务登记，不回到旧源目录。下一步我会读取 CyHex 格式参考和前置任务产物登记，确定该 milestone 分支应消费哪些上游交付。
格式参考已经读取；资产规则可用最小 `version/required/optional/forbidden/modifiable/output/notes` 格式。现在我会集中读取 T-038 当前配置和 T-030/T-032/T-035/T-036 的 registry/completion，以免把未指定的 T-040 或旧 T-037 混进依赖。

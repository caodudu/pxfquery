# task_llm_flash_adapter_v1

## Orchestration Input

- This waiting task is optional and must not block the deterministic package milestone or T-037.
- Despite the historical task name, use the current CyHex/OpenCode llm_gateway default requested for this run: DeepSeek v4 pro. Do not switch the project back to flash.
- Deliver graceful fallback behavior and endpoint/config documentation as `pxfquery-T-034`. If the LLM endpoint is unavailable, record the failure and keep the deterministic package path usable.
- Acceptance requires a small endpoint/config smoke check or a clear unavailable-result record; no downstream task should depend on this for core forward/reverse functionality.

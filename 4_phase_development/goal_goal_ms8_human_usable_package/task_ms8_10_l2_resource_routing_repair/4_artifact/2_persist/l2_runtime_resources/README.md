# T138 L2 Runtime Resources

日期：2026-06-28

本目录存放 T138 L2 实现直接消费的资源文件。

## function_index.json 决策

T138 不做多种 `function_index.json` schema 兼容。运行时只消费本目录下的：

```text
function_index.json
```

该文件从 T021 `standard_resources/function_index.json` 字节复制而来，sha256：

```text
2b23be5b413021f0c2ebd7d684b4d47ca30949325513efb3c113f88d392a658f
```

固定 schema：

```json
{
  "var_names": ["..."],
  "meta": {
    "<var_name>": {
      "source": "hallmark | 3ca_mps",
      "label": "<human readable label>"
    }
  },
  "aliases": {
    "<lowercase_alias>": "<var_name>"
  }
}
```

选择理由：

- 该 schema 直接支持 L2 的 `alias -> var_name` lookup。
- 当前 `FunctionIndex` reader 已按该 schema 工作。
- legacy original 是旧 `{functions, note, score_note}` schema，不作为 T138 运行时 schema。

后续 L2 代码应只引用这个 runtime file 或同 schema 文件。

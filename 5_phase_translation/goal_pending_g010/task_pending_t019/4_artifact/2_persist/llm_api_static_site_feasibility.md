# GitHub Pages 搭建 LLM API 静态站点可行性分析

## 1. GitHub Pages 的静态本质

GitHub Pages 提供的是**纯静态托管服务**，其核心特性与限制如下：

| 特性 | 说明 |
|------|------|
| **托管内容** | 仅支持 HTML、CSS、JavaScript 等静态文件 |
| **无服务端运行时** | 不能运行 Python、Node.js、Java、Go、PHP 等后端代码 |
| **无数据库** | 没有 MySQL、PostgreSQL、MongoDB 等持久化存储 |
| **无后台进程** | 没有定时任务、WebSocket 服务端、消息队列 |
| **无文件写入** | 构建后无法在服务端写入或修改文件 |

这意味着任何需要后端处理的功能（矩阵计算、文件解析、数据库查询）都无法直接在 GitHub Pages 上完成。

## 2. GitHub Pages 能否对接 LLM API

**可以，但有限制。**

### 2.1 直接调用方式

通过客户端 JavaScript 直接调用 OpenAI / Anthropic 等公开 REST API：

```javascript
// 示例：前端直接调用 OpenAI API
const response = await fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({ model: "gpt-4", messages: [...] }),
});
```

### 2.2 关键限制

| 限制 | 说明 |
|------|------|
| **CORS 策略** | 大部分 LLM API 不允许浏览器跨域请求，直接调用会报 CORS 错误 |
| **API Key 泄露** | 前端代码完全公开，API Key 若硬编码则所有人可见，易被滥用 |
| **请求体积** | 大模型上下文较长时，前端 HTTP 请求可能超时或被浏览器限制 |

### 2.3 CORS 规避方案

#### 方案 A：Cloudflare Workers（推荐，免费）

```javascript
// Cloudflare Worker 代理（免费额度：10 万请求/天）
export default {
  async fetch(request) {
    const body = await request.json();
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + API_KEY, // 密钥在 Worker 端，不暴露
      },
      body: JSON.stringify(body),
    });
    return new Response(response.body, {
      headers: { "Access-Control-Allow-Origin": "*" },
    });
  },
};
```

#### 方案 B：Vercel / Netlify Functions（免费额度充足）

- Vercel Functions：Hobby 计划每月 100 小时运行时长，足够轻量 API 代理
- Netlify Functions：免费计划每月 125,000 次调用
- 可将 API Key 保存在环境变量中，前端无法读取

#### 方案 C：AWS Lambda + API Gateway

- 免费套餐：每月 100 万次请求
- 配置略复杂，但可靠性最高

### 2.4 推荐的 CORS + 安全架构

```
浏览器 (GitHub Pages) → Cloudflare Worker (API 代理) → OpenAI / Anthropic API
                             ↑
                         环境变量中存储 API Key（安全）
```

## 3. 针对 PxFquery 的分析

### 3.1 PxFquery 中 LLM 的角色

根据 PxFquery 的设计，LLM 承担的是**自然语言理解与解释层**，而不是计算引擎：

| 职责 | 说明 |
|------|------|
| 理解自然语言问题 | 将用户用自然语言描述的分析意图结构化 |
| 标准化术语映射 | 将非专业表述映射到标准生信分析术语 |
| 生成可读功能解释 | 对分析结果输出人类可读的解释性文本 |

LLM **不负责**：矩阵计算、索引检索、h5ad 文件解析等重计算任务。

### 3.2 两种模式可行性判断

#### 模式 A：纯对话界面（可行 ✅）

架构：`GitHub Pages + Cloudflare Worker 代理`

```
用户输入问题 → 前端 JS 发送请求 → Cloudflare Worker → OpenAI API
   ↑                                                          │
   └──────── 返回 LLM 回答 ←──────────────────────────┘
```

- 所需资源：零后端服务器
- 成本：Cloudflare Workers 免费额度足够
- 适合场景：论文展示页上的"体验 LLM 问答"Demo

#### 模式 B：完整 PxFquery 流程（不可行 ❌）

```
用户输入问题 → LLM 理解 → 翻译为标准查询 → 加载 h5ad 矩阵 → 矩阵计算
  → 索引检索 → LLM 解释结果 → 返回用户
```

**关键瓶颈**：
- h5ad 文件（单细胞矩阵）通常几百 MB 到数 GB，无法在前端加载
- 矩阵运算（稀疏矩阵、PCA、聚类）需要 Python 生态（numpy、scipy、anndata）
- 索引检索需要服务端数据库或搜索引擎

### 3.3 纯静态站支持"微型在线分析"的限度

| 可做 ✅ | 不可做 ❌ |
|--------|----------|
| 预计算结果的表格搜索与展示 | 实时加载 h5ad 文件 |
| LLM API 调用结果渲染 | 服务端矩阵运算 |
| 静态图表（预生成热图、UMAP） | 动态聚类或降维计算 |
| 交互式筛选（前端 JS 处理小数据集） | 大规模索引检索 |
| API 返回数据的可视化 | 文件上传并解析（超大型文件） |

## 4. 三种可行性方案对比

| 方案 | 后端需求 | 维护成本 | 适合场景 |
|------|---------|---------|---------|
| **纯静态站 + LLM API 代理** | 无（代理层免费，如 Cloudflare Workers） | 极低 | 仅展示预计算结果 + LLM 对话 Demo |
| **静态站 + Serverless 函数** | 无服务器函数（Vercel Functions / AWS Lambda） | 低 | 调用 Python 临时计算（如小规模矩阵运算） |
| **完整前后端** | 需要后台服务器（Django / FastAPI + 数据库） | 中-高 | 实时矩阵查询 + 索引检索 + 完整 PxFquery 流程 |

### 方案详解

#### 方案一：纯静态站 + LLM API 代理（推荐论文初期）

```
GitHub Pages (Jekyll/Hugo) ─→ Cloudflare Worker ─→ LLM API
  ├─ 工具介绍页面          (纯 HTML)
  ├─ 使用文档              (Markdown 生成)
  ├─ 预计算结果案例         (预生成 JSON 数据)
  └─ 交互式 LLM 问答 Demo   (前端 JS 调用 API)
```

- 优点：零服务器运维，仅域名成本，快速上线
- 缺点：功能有限，无法实时分析

#### 方案二：静态站 + Serverless 函数

```
GitHub Pages (前端) ─→ Vercel Functions (Python) ─→ 外部资源
                        ├─ 轻量计算
                        ├─ 小文件处理
                        └─ 数据格式转换
```

- 优点：可执行轻量 Python 逻辑，Vercel 免费额度充足
- 缺点：Vercel Functions 有冷启动（约 1-5 秒），执行时长限制（Hobby 计划 10 秒/次）
- 适用：调用 Python 做小规模矩阵子集提取、格式转换等

#### 方案三：完整前后端（生产环境）

```
Nginx / CDN (前端) ─→ FastAPI / Django (后端) ─→ 数据库 + 对象存储
                                              ├─ 实时矩阵查询
                                              ├─ 索引检索 (Elasticsearch)
                                              └─ LLM API 调用（服务端）
```

- 优点：功能完整，性能可控
- 缺点：需要服务器运维，成本高
- 适用：PxFquery 正式线上服务

## 5. 结论与建议

### 论文初期（推荐方案）

使用 **方案一**：GitHub Pages + Cloudflare Workers 代理 LLM API。

**展示内容**：
- 工具介绍与背景
- 详细使用文档
- 预计算结果的案例分析页面（预生成图表 + 描述文本）
- 交互式案例 Demo：用户输入预设问题 → 前端调 LLM API → 展示回答（作为 PxFquery LLM 能力的示例）

**完整分析功能**：放在 GitHub 仓库中，用户通过 README 指引在本地运行 PxFquery。

### 中期过渡

若需增强用户互动，可引入 **方案二**（Vercel Functions），增加：
- 小规模数据在线预览
- 查询结果导出功能

### 长期规划

当 PxFquery 用户量增长、需要提供完整在线分析服务时，过渡到 **方案三**（完整前后端），可基于：
- 前端：React / Vue 3
- 后端：FastAPI（Python，与 PxFquery 生态一致）
- 数据库：PostgreSQL + 对象存储（S3/MinIO）
- 部署：Docker + 云服务器 / Kubernetes
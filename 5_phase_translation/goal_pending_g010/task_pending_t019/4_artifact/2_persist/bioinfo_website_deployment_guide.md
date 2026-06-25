# 生物信息查询网站部署上手指南：从代码到上线

## 1 前期准备（代码和数据）

在部署之前，需要先准备好三部分内容：

| 组件 | 技术选型示例 | 说明 |
|------|-------------|------|
| 前端 | HTML + CSS + JavaScript（或 React/Vue） | 用户看到的页面，查询表单、结果展示 |
| 后端 | Python Flask / FastAPI | 处理查询逻辑、读取数据、返回结果 |
| 数据 | h5ad 矩阵、JSON 索引、CSV 注释表 | 存放基因表达量、细胞注释等 |

**代码管理**：将所有代码推送到 GitHub 仓库，这是后续所有部署方式的基础。

```bash
git init
git add .
git commit -m "init"
git remote add origin https://github.com/你的用户名/你的仓库.git
git push -u origin main
```

> 数据文件（尤其是 h5ad 几十 MB 到几百 MB）**不要直接放进 Git 仓库**，应使用 `.gitignore` 排除，改用 GitHub Releases 或云存储托管。

---

## 2 域名选择

### 2.1 免费方案（推荐起步）

| 平台 | 默认域名 |
|------|---------|
| GitHub Pages | `你的用户名.github.io/仓库名` |
| Vercel | `项目名.vercel.app` |
| Netlify | `项目名.netlify.app` |

完全免费，无需购买域名，HTTPS 自动配置，适合原型验证和学术分享。

### 2.2 自定义域名

如果需要专业形象（如 `bioinfo-lab.cn`），需购买域名：

| 注册商 | 价格参考 | 特点 |
|--------|---------|------|
| GoDaddy | 约 50-100 元/年 | 国际主流，.com 稳定 |
| Namecheap | 约 50-100 元/年 | 免费 WhoisGuard 隐私保护 |
| 阿里云 | 约 30-150 元/年 | 国内备案方便，.cn 首选 |
| Cloudflare | 成本价 | 不加价，DNS 管理优秀 |

### 2.3 域名后缀选择

| 后缀 | 适用场景 | 注意 |
|------|---------|------|
| `.com` | 通用首选，最权威 | 好的名字往往被占 |
| `.io` | 科技/开源项目常用 | 较贵（约 200-400 元/年） |
| `.cn` | 面向国内用户 | 需实名备案 |
| `.org` | 学术/非盈利项目 | 可信度好 |
| `.bio` | 生物信息学专业 | 小众，约 150-250 元/年 |

> 建议：国内用户选 `.cn`（阿里云）+ 备案；国际用户选 `.com`（Namecheap）+ Cloudflare DNS。

---

## 3 纯静态站 —— GitHub Pages

如果你的网站**纯前端**（查询逻辑通过 JavaScript 加载本地 JSON 或调用公开 API），GitHub Pages 是最优解。

### 3.1 部署步骤

1. 创建 GitHub 仓库（公开）
2. 将前端代码推送到仓库
3. 进入仓库 **Settings → Pages**
4. 在 **Branch** 下拉选择 `main`（或 `gh-pages`），目录选择 `/root`
5. 点击 **Save**
6. 等待 1-2 分钟，访问 `https://你的用户名.github.io/仓库名`

### 3.2 绑定自定义域名

1. 在域名 DNS 管理面板添加 CNAME 记录：
   - 记录类型：`CNAME`
   - 主机记录：`www`（或 `@`）
   - 记录值：`你的用户名.github.io`
2. 在 GitHub Pages 设置页填入自定义域名
3. 勾选 **Enforce HTTPS**
4. 在仓库根目录创建 `CNAME` 文件（GitHub 会自动生成）：

```
你的域名.com
```

### 3.3 自动部署

每次推送到 `main` 分支，GitHub Actions 会自动触发重新部署。也可以在仓库添加 `.github/workflows/` 自定义构建流程。

> 优点：完全免费、自动 HTTPS、无需维护服务器
> 局限：**不能运行 Python 后端**，纯前端 JavaScript 无法读取 h5ad 文件（除非预转为 JSON）

---

## 4 有后端的网站部署

如果网站需要 Python 后端处理查询（例如接收基因名 → 后端从 h5ad 读取表达量 → 返回计算结果），GitHub Pages 无法满足需求，需要以下方案。

### 4.1 方案 A：Vercel / Netlify（前端免费 + Serverless 函数）

适合：前端为主，后端逻辑较轻的场景。

**Vercel 部署步骤：**

1. 在 GitHub 创建仓库，包含前端代码 + `api/` 目录（Python Serverless Functions）
2. 访问 [vercel.com](https://vercel.com)，用 GitHub 登录
3. 点击 **Add New → Project**，导入仓库
4. 构建设置：
   - Framework Preset：选择 `Other`
   - Build Command：留空
   - Output Directory：前端构建后的目录
5. 点击 **Deploy**
6. 在 `vercel.json` 中配置路由（可选）：

```json
{
  "functions": {
    "api/**/*.py": {
      "maxDuration": 10
    }
  }
}
```

**重要限制：**
- Vercel Serverless Functions 默认执行超时 **10 秒**（Pro 版 60 秒/900 秒）
- 单个函数响应体限制 **4.5 MB**
- 不适用于载入大 h5ad 文件（几百 MB 内存不可行）

**Netlify 类似**，使用 Netlify Functions（基于 AWS Lambda），超时同样是 10 秒。

### 4.2 方案 B：Railway 一键部署

适合：后端较重、需要完整运行环境的场景。

**部署步骤：**

1. 访问 [railway.app](https://railway.app)，GitHub 登录
2. 点击 **New Project → Deploy from GitHub repo**
3. 选择仓库
4. Railway 自动检测语言（如检测到 `requirements.txt` 则启动 Python 环境）
5. 设置启动命令（在 Railway Dashboard → Settings → Deploy）：

```
gunicorn app:app
```

6. Railway 会自动分配域名 `你的项目.up.railway.app`

**免费额度：**
- 每月 **$5 或 500 小时**（2025 年政策），适合轻量使用
- 支持自定义域名
- 支持持久卷（Persistent Volume）缓存大文件

**优势：** 比 Vercel 更适合 Python 后端，运行环境更完整。

### 4.3 方案 C：Fly.io

适合：需要精细控制部署配置的用户。

**部署步骤：**

1. 安装 flyctl：`curl -L https://fly.io/install.sh | sh`
2. `fly auth login`
3. 在项目目录下 `fly launch`，自动生成 `fly.toml`
4. 编辑 `fly.toml` 配置机器规格：

```toml
[services]
  internal_port = 8080
  concurrency = { hard_limit = 25 }

[[vm]]
  memory = "1gb"
  cpu_kind = "shared"
  cpus = 1
```

5. `fly deploy` 推送部署

**费用：** 按需付费，最低约 **$2-3/月**（共享 CPU + 256MB 内存）。免费额度需绑卡。

**优势：** 全球多地域、支持大内存（可选 4GB/8GB）、支持持久卷。

### 4.4 方案 D：阿里云轻量应用服务器

适合：生产环境、数据量大、面向国内用户。

| 配置 | 价格（1 年） | 适合场景 |
|------|-------------|---------|
| 2 核 2G + 60GB SSD | 约 500-600 元 | 小型查询网站 |
| 2 核 4G + 80GB SSD | 约 800-1000 元 | 含 h5ad 加载 |

**部署步骤：**

1. 购买轻量应用服务器（选择 Ubuntu 22.04）
2. SSH 登录：

```bash
ssh root@你的服务器IP
```

3. 安装依赖：

```bash
apt update && apt install -y nginx python3-pip
pip install flask gunicorn scanpy anndata
```

4. 从 GitHub clone 代码：

```bash
git clone https://github.com/你的用户名/你的仓库.git /var/www/app
```

5. 配置 Nginx 反向代理：

```nginx
server {
    listen 80;
    server_name 你的域名.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
    }
}
```

6. 使用 Supervisor 或 Systemd 保持后端运行：

```bash
# /etc/systemd/system/bioinfo.service
[Unit]
Description=Bioinfo Query App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/app
ExecStart=/usr/local/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

7. 启动：`systemctl enable --now bioinfo`
8. 配置域名解析 A 记录指向服务器 IP
9. 申请 SSL 证书：`apt install certbot python3-certbot-nginx && certbot --nginx`

**优缺点：**
- ✅ 完全控制环境，可加载大 h5ad 文件
- ✅ 无超时限制，适合长计算
- ✅ 国内访问速度快
- ❌ 需要维护服务器（安全更新、备份）
- ❌ 需要域名备案（使用大陆服务器必备）

---

## 5 分析型网站的特殊要求

### 5.1 Python 运行环境

生物信息查询网站的特点决定了**不能仅靠静态站**：

- 处理用户查询需要 Python 库（scanpy、anndata、numpy、pandas）
- 浏览器 JavaScript 不具备读取 `.h5ad` 文件的能力
- 预转为 JSON 只适合小规模数据（数千细胞 × 数百基因）

### 5.2 大文件数据托管

| 方案 | 适合场景 | 实现方式 |
|------|---------|---------|
| GitHub Releases | 公开数据集 | `gh release upload v1.0 data.h5ad`，通过 URL 下载 |
| Hugging Face Datasets | 大型共享数据 | 上传到 Hugging Face，服务器下载 |
| AWS S3 / 阿里云 OSS | 企业级 | 后端从 S3 下载到本地，缓存后提供服务 |
| 服务器本地磁盘 | 数据固定 | scp/rsync 上传到服务器，应用直接读取 |

### 5.3 计算超时限制

| 平台 | 单次执行超时 | 建议 |
|------|-------------|------|
| Vercel Hobby | 10s | 不适合复杂查询 |
| Netlify Free | 10s | 同上 |
| Railway | 无硬性限制 | 适合中等计算 |
| Fly.io | 无硬性限制 | 适合中等计算 |
| 自建服务器 | 自行配置 | 无限制 |

**应对策略：**
- 对耗时操作设置超时熔断（`signal.alarm()` 或 `asyncio.wait_for`）
- 返回 503 + 提示"计算超时，请简化查询条件"
- 在查询结果中缓存热门基因表达量

### 5.4 异步任务方案

当计算时间超过平台限制（如全基因集差异分析、GSEA 富集分析），需要引入异步任务队列：

| 方案 | 说明 | 适用平台 |
|------|------|---------|
| Celery + Redis | 经典任务队列 | 自建服务器 |
| Dramatiq | 轻量替代 Celery | 自建服务器 |
| Vercel Queue | Vercel 原生方案 | Vercel Pro |
| 前端轮询 | 提交任务后定时查询状态 | 所有平台 |

**基本流程：**
```
用户提交查询 → 任务入队 → 返回 task_id
                  ↓
           后端 Worker 处理（可能数分钟）
                  ↓
           结果写入 Redis/数据库
                  ↓
用户通过 task_id 轮询获取结果
```

---

## 6 上线后的维护

### 6.1 更新内容

```bash
# 推送到 GitHub，自动触发 CI/CD 部署
git add .
git commit -m "add new gene search feature"
git push
```

对于自建服务器，可配合 GitHub Webhook：

```bash
# 服务器上的 post-receive hook 自动拉取最新代码
cd /var/www/app && git pull && systemctl restart bioinfo
```

### 6.2 监控

| 服务 | 免费额度 | 功能 |
|------|---------|------|
| UptimeRobot | 50 个监控器 | 每 5 分钟检查一次，宕机邮件/短信告警 |
| Better Uptime | 3 个监控器 | 心跳检测 + 状态页 |
| Grafana + Prometheus | 自建 | 完整性能监控（适合自建服务器） |

**UptimeRobot 配置（免费、零代码）：**

1. 访问 [uptimerobot.com](https://uptimerobot.com)，注册
2. 点击 **Add New Monitor**
3. Monitor Type 选择 **HTTP(s)**
4. URL 填入网站地址
5. 选择告警方式（默认邮件免费）
6. 点击 **Create Monitor**

当网站宕机时，5 分钟内会收到邮件通知。

### 6.3 SSL 证书

**GitHub Pages：** 自动申请和续期 Let's Encrypt 证书，无需手动操作。

**自定义域名 + 自建服务器：**

```bash
# 首次申请（推荐使用 Certbot + Nginx）
certbot --nginx -d 你的域名.com

# 证书自动续期（Certbot 默认通过 systemd timer 自动进行）
certbot renew --dry-run
```

**Cloudflare 代理：** 如果 DNS 使用 Cloudflare，开启 Proxy（橙色云朵）即可自动获得 SSL 证书，后端只需监听 HTTP。

---

## 总结：部署方案决策树

```
网站是否需要 Python 后端？
├── 否 → GitHub Pages（最简单、免费、零维护）
│         └── 需要自定义域名？→ DNS CNAME 绑定
│
└── 是 → 后端计算量有多大？
          ├── 轻量（<10s 响应）→ Vercel / Netlify
          ├── 中等（<60s 响应）→ Railway
          ├── 较重（几分钟） → Fly.io 或 AWS/阿里云
          └── 很重（大 h5ad 加载） → 阿里云轻量服务器（国内）或 VPS（海外）
```

对于大多数生物信息学查询网站，推荐的最佳实践是：

1. **原型阶段：** Railway（快速部署，验证核心功能）
2. **小规模使用：** Fly.io（配置灵活，按需付费）  
3. **正式上线（面向国内用户）：** 阿里云轻量服务器（稳定、快速、可备案）
4. **静态文档/结果展示页：** GitHub Pages（始终免费，适合配套页面）
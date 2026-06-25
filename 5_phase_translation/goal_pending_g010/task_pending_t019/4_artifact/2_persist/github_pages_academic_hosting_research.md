# GitHub Pages 学术生物信息学论文配套网站托管调研报告

## 1. GitHub Pages（github.io）作为学术论文配套网站的合法性

### 1.1 是否被期刊接受

**是的，GitHub Pages 被学术界和期刊广泛接受，作为学术论文配套网站（companion website）的托管平台。**

期刊的核心关注点是：
- 论文内容的学术质量和同行评审
- 配套材料/工具的可用性（availability）和可访问性（accessibility）
- 数据和方法是否符合 FAIR 原则（Findable, Accessible, Interoperable, Reusable）

期刊**不限制**使用何种托管平台来提供工具访问或补充材料。GitHub Pages 作为一种广泛使用、免费、稳定且支持 HTTPS 的静态网站托管服务，完全满足学术出版的要求。

### 1.2 MDPI Genes 期刊的政策

MDPI 旗下的《Genes》期刊（Impact Factor 3.1, Scopus CiteScore 5.9）在其**作者指南**中要求：

- **Data Availability Statement**：作者必须在论文中提供"数据可用性声明"，说明支持研究结果的公开归档数据集或工具的访问链接。
- **参考文献格式**：MDPI 明确接受 URL 链接作为参考文献格式之一（参见其参考文献格式第 9 类："Title of Site. Available online: URL (accessed on Day Month Year)."），**对 URL 的域名或其是否为 github.io 不做任何限制**。
- **补充材料**：MDPI 允许任何格式的补充材料，并鼓励使用非专有的通用格式。

因此，**MDPI Genes 完全接受使用 GitHub Pages（github.io）作为论文配套工具的托管平台**，只要链接持续可访问即可。

### 1.3 NAR Web Server Issue 和 Bioinformatics 期刊

- **Nucleic Acids Research (NAR) Web Server Issue**：该特刊专门发表生物信息学 web 工具。在投稿要求中明确要求提供工具的 URL（tool availability URL），而 **github.io 域名已被大量收录于该特刊中**（如 EDGE 工具：`lanl-bioinformatics.github.io/EDGE/`）。
- **Bioinformatics（Oxford）**：同样接受 github.io 作为工具的可用性链接。

---

## 2. GitHub Pages 功能特性

| 特性 | 说明 |
|------|------|
| **免费** | 公开仓库免费使用；私有仓库在 GitHub Free 计划中也可使用 Pages |
| **自定义域名** | 支持绑定自定义域名（如 `tool.example.com`），支持 Apex 域名和 www 子域名 |
| **HTTPS/TLS** | 自动为 `*.github.io` 域名及绑定的自定义域名提供 TLS 证书（通过 Let's Encrypt） |
| **静态网站托管** | 从仓库分支直接发布 HTML/CSS/JS 静态内容 |
| **Jekyll 支持** | 内建 Jekyll 静态站点生成器，可自动将 Markdown 转换为 HTML 网站；也支持自定义 GitHub Actions 构建流程 |
| **带宽（软限制）** | 100 GB/月（soft limit），超过后 GitHub 会联系用户建议优化 |

---

## 3. GitHub Pages 限制

| 限制项 | 具体数值 | 备注 |
|--------|----------|------|
| **仓库文件总大小** | 推荐 ≤ 1 GB | 对超大文件有单独限制（单个文件 ≤ 100 MB） |
| **发布站点大小** | ≤ 1 GB | 编译后的静态网站内容 |
| **月带宽（软限制）** | 100 GB/月 | soft limit，超限后可能无法提供服务，GitHub 会发送邮件提醒 |
| **构建频率** | 10 次构建/小时 | **仅适用于默认的 Jekyll 构建**；使用自定义 GitHub Actions 构建流程无此限制 |
| **部署超时** | 10 分钟 | 构建超过 10 分钟将被终止 |
| **站点数量** | 每个账户仅能创建 1 个用户/组织站点 | 项目站点（project sites）无数量限制 |

**对学术用途的适用性分析**：
- 生物信息学工具配套网站通常小于 1 GB；1 GB 的限制对大多数静态文档和下载页面完全足够（大型数据集应托管在专门的数据库如 Zenodo、Figshare、NCBI 等）。
- 100 GB/月的带宽足以支撑中等规模的学术工具访问（相当于每月数十万次页面浏览）。
- 10 次构建/小时对于学术网站通常无影响；如有更高更新频率需求，可启用自定义 GitHub Actions 工作流。

---

## 4. 真实案例：使用 github.io 作为配套网站并发表于同行评审期刊的生物信息学工具

### 案例 1：EDGE — 微生物 NGS 分析平台

| 项目 | 内容 |
|------|------|
| **工具名称** | EDGE (Empowering the Development of Genomics Expertise) |
| **GitHub Pages URL** | `https://lanl-bioinformatics.github.io/EDGE/` |
| **论文标题** | *Enabling the democratization of the genomics revolution with a fully integrated web-based bioinformatics platform* |
| **DOI** | [10.1093/nar/gkw1027](https://doi.org/10.1093/nar/gkw1027) |
| **期刊** | *Nucleic Acids Research* (NAR), 2016 |
| **简介** | EDGE 由洛斯阿拉莫斯国家实验室（LANL）开发，为生物学家提供完整的 NGS 数据分析流程，包括质控、组装、注释、分类、系统发育分析等。其官网托管于 GitHub Pages，并被多篇 NAR、Bioinformatics 等高影响力期刊论文引用。EDGE 还在 Nature 新闻中被报道（*"How bioinformatics tools are bringing genetic analysis to the masses"*, Nature, 2017）。 |

### 案例 2：GET_HOMOLOGUES — 泛基因组分析工具

| 项目 | 内容 |
|------|------|
| **工具名称** | GET_HOMOLOGUES / GET_HOMOLOGUES-EST |
| **GitHub Pages URL** | `https://eead-csic-compbio.github.io/get_homologues/manual/` |
| **论文标题** | *GET_HOMOLOGUES, a Versatile Software Package for Scalable and Robust Microbial Pangenome Analysis* |
| **DOI** | [10.1128/AEM.02411-13](https://doi.org/10.1128/AEM.02411-13) |
| **期刊** | *Applied and Environmental Microbiology*, 2013 |
| **额外论文** | *GET_HOMOLOGUES-EST: A versatile and robust tool for computing pangenome and transcriptome sequence clusters* — *Frontiers in Plant Science*, 2017, DOI: [10.3389/fpls.2017.00184](https://doi.org/10.3389/fpls.2017.00184) |
| **简介** | GET_HOMOLOGUES 由西班牙国家研究委员会（EEAD-CSIC）开发，是国际上广泛使用的泛基因组分析工具（128 GitHub stars, 26 forks, 被 Google Scholar 追踪的数百篇论文引用）。其完整文档（包括 HTML 手册、教程、植物泛基因组分析协议）托管于 `eead-csic-compbio.github.io`。该工具已被 bioconda 收录，并被 ELIXIR 欧洲生物信息学基础设施认可。 |

### 案例 3：BioBuntu — 一体化生物信息学平台

| 项目 | 内容 |
|------|------|
| **工具名称** | BioBuntu |
| **GitHub Pages URL** | `https://biobuntu.github.io/` |
| **论文标题** | *BioBuntu: A Comprehensive Platform for Genomic Analysis with CLI, GUI, and Web Interfaces* |
| **预印本** | [Research Square, rs-7861003/v1](https://www.researchsquare.com/article/rs-7861003/v1) |
| **简介** | BioBuntu 提供 CLI、桌面 GUI（BioBuntu Studio）和 Web Dashboard 三种界面，支持 RNA-seq、变异检测、宏基因组学等分析流程。集成 FastQC、BWA、GATK、HISAT2、Samtools 等主流工具。配套网站 biobuntu.github.io 提供完整文档、安装指南和社区资源。 |

### 案例 4：Picard Tools — Broad Institute（补充案例）

| 项目 | 内容 |
|------|------|
| **工具名称** | Picard Tools |
| **GitHub Pages URL** | `https://broadinstitute.github.io/picard/` |
| **简介** | 由 Broad Institute 维护的 NGS 数据处理工具集，被 GATK 工作流程广泛使用。其 GitHub Pages 站点是工具的官方文档门户。虽然 Picard 本身作为工具集被引用而非以单一论文发表，但它是全球引用量最大的生物信息学基础设施之一，其 github.io 的部署模式证明了该平台在学术/研究基础设施中的成熟应用。 |

### 使用 github.io 作为学术实验室主页的广泛实践

除工具配套网站外，大量学术实验室和课题组使用 `*.github.io` 作为其实验室主页和出版物门户：

- **Shi Lab, Monash University** — `https://github.com/ShiLab-Bioinformatics/ShiLab-Bioinformatics.github.io`
- **Huttenhower Lab (Harvard)** — 其 bioBakery 工具套件（MetaPhlAn、HUMAnN 等）均托管于 GitHub 并大量使用 github.io 作为文档站
- **Ifremer Bioinformatics** (法国海洋研究所) — `https://ifremer-bioinformatics.github.io/`

这些都表明 GitHub Pages 已成为生物信息学领域学术展示和工具发布的**事实标准平台**。

---

## 5. 学术出版中使用 GitHub Pages 的政策总结

### 5.1 总体政策

**GitHub Pages 完全可接受作为学术论文的配套网站托管平台。** 主要理由：

1. **期刊不审查托管平台**：期刊的同行评审关注科学内容，不审查工具/文档是托管在 AWS、GitHub Pages、自有服务器还是大学服务器上。
2. **只要链接持续可访问**：GitHub Pages 作为微软旗下的免费服务，自 2008 年推出以来持续运行，具备长期稳定性。即使 GitHub Pages 未来停运，静态网站也可轻松迁移至其他托管服务。
3. **与学术开源精神一致**：GitHub 已成为全球生物信息学开源代码的标准托管平台，使用 GitHub Pages 作为配套网站是自然的延伸。

### 5.2 MDPI 期刊的具体政策

- MDPI（包括《Genes》）的投稿指南中，**Data Availability Statement**部分要求作者提供数据访问链接，**不限制链接的域名类型**。
- MDPI 的参考文献格式指南明确列出 URL 作为合法引用格式，示例为 "Available online: URL (accessed on ...)"。
- MDPI 鼓励使用稳定的持久标识符（如 DOI），但也接受 URL 作为数据/工具的访问途径。

### 5.3 建议

为增强链接的长期稳定性，建议：

1. **同时使用 DOI**：将代码在 Zenodo 归档以生成 DOI，同时在论文中同时引用 DOI 和 github.io URL。
2. **在 Data Availability Statement 中明确说明**：如 "The companion website of this tool is available at `https://xxx.github.io/yyy/`."
3. **版本标记**：使用 Git tag 和 GitHub Release 功能标记发布版本，并在 Zenodo 中对发布版进行归档。

---

## 参考资料

1. GitHub Pages 官方文档 — Limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
2. Li P-E, Lo C-C, Anderson JJ, et al. "Enabling the democratization of the genomics revolution with a fully integrated web-based bioinformatics platform." *Nucleic Acids Research*, 2016. DOI: [10.1093/nar/gkw1027](https://doi.org/10.1093/nar/gkw1027)
3. Contreras-Moreira B, Vinuesa P. "GET_HOMOLOGUES, a Versatile Software Package for Scalable and Robust Microbial Pangenome Analysis." *Applied and Environmental Microbiology*, 2013. DOI: [10.1128/AEM.02411-13](https://doi.org/10.1128/AEM.02411-13)
4. Contreras-Moreira B, Cantalapiedra CP, et al. "Analysis of Plant Pan-Genomes and Transcriptomes with GET_HOMOLOGUES-EST." *Frontiers in Plant Science*, 2017. DOI: [10.3389/fpls.2017.00184](https://doi.org/10.3389/fpls.2017.00184)
5. BioBuntu — Research Square Preprint: https://www.researchsquare.com/article/rs-7861003/v1
6. Picard Tools — Broad Institute: https://broadinstitute.github.io/picard/
7. EDGE Bioinformatics: https://lanl-bioinformatics.github.io/EDGE/
8. GET_HOMOLOGUES Manual: https://eead-csic-compbio.github.io/get_homologues/manual/
9. MDPI Genes — Instructions for Authors: https://www.mdpi.com/journal/genes/instructions
10. GitHub Terms of Service (Pages policies): https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
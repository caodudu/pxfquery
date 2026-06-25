# MDPI Citation Format Investigation Report

**Generated:** 2026-06-23  
**Task:** T-017 — mdpi引用格式  
**Source:** Official MDPI documentation + WXY manuscript practical verification

---

## 1. Conclusion (TL;DR)

MDPI uses the **"Multidisciplinary Digital Publishing Institute"** Zotero citation style, which is a **numbered (ACS-based) citation format** using `[1]`, `[2]` bracket numbering in text. This is a **standard Zotero repository style** — no manual CSL file download is required.

### How to install in Zotero
1. Open Zotero → **Preferences** (or **Settings**)
2. Go to **Cite** → **Styles**
3. Click **Get additional styles...**
4. Search **"Multidisciplinary Digital Publishing Institute"**
5. Click to install

---

## 2. Official MDPI Citation Rules

Per the official [MDPI Reference List and Citations Style Guide](https://www.mdpi.com/authors/references):

- **In-text citations:** Numbered in brackets `[1]`, `[2]`, `[3]` in order of appearance.
- **Reference list:** Numbered list at the end of the manuscript, ordered by first appearance in text.
- **Recommended software:** MDPI explicitly recommends Zotero (free), EndNote, ReferenceManager, or Mendeley.
- **EndNote users:** Download the MDPI.ens file from `http://endnote.com/downloads/style/mdpi`.

### Journal article reference format
```
Author1, A.B.; Author2, C.D.; Author3, E.F. Title of the article. Abbreviated Journal Name. Year, Volume, Page Range.
```
Example: `Malik, V.S.; Schulze, M.B.; Hu, F.B. Intake of sugar-sweetened beverages and weight gain: A systematic review. Am. J. Clin. Nutr. 2006, 84, 274–288.`

The official MDPI CSL style ID is `multidisciplinary-digital-publishing-institute`.

The CSL file is maintained in the official [citation-style-language/styles](https://github.com/citation-style-language/styles) GitHub repository.

---

## 3. Practical Verification: WXY Manuscript (Genes Journal)

Inspecting the WXY manuscript_v8.docx (a successfully published Genes submission):

**In-text citation format:** Numbered brackets `[1]`, `[2]`, `[3]` ... used throughout.

**Reference list format (sampled):**
```
[1] Claussnitzer, M.; Cho, J.H.; Collins, R.; et al. A brief history of human disease genetics. ...
[2] Landrum, M.J.; Chitipiralla, S.; Brown, G.R.; et al. ClinVar: improvements to accessing data. Nucleic Acids Res. 2020, 48, D835-D844, ...
[5] Bergoug, M.; Doudeau, M.; Godin, F.; et al. Neurofibromin Structure, Functions and Regulation. Cells 2020, 9, doi:10.3390/cells9112365.
```

This matches the official MDPI style exactly:
- Numbered list `[1]`, `[2]`, `[3]`...
- Authors separated by semicolons, initials with periods
- Year in bold (when formatted)
- Journal abbreviated, volume in italics
- DOI included at end

---

## 4. CSL File Details

- **Style ID:** `http://www.zotero.org/styles/multidisciplinary-digital-publishing-institute`
- **Citation format:** `numeric` (collapsed citation-number)
- **Category:** science
- **Based on:** American Chemical Society (ACS) style
- **Zotero repo page:** https://www.zotero.org/styles/?q=id%3Amultidisciplinary-digital-publishing-institute
- **Raw CSL download:** https://raw.githubusercontent.com/citation-style-language/styles/master/multidisciplinary-digital-publishing-institute.csl
- **Local copy:** `4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl` (9,534 bytes)

---

## 5. Zotero Installation Guide

### Method 1: From Within Zotero (Recommended)
Since this is a standard Zotero repository style, the easiest way is:
1. Open Zotero desktop app
2. **Edit** → **Preferences** (macOS: **Zotero** → **Preferences**)
3. Select the **Cite** tab
4. Under "Style Manager", click **Get additional styles...**
5. Search for **"Multidisciplinary Digital Publishing Institute"**
6. Click on the style, then **Install**

### Method 2: Manual CSL File Installation
If the above method fails or you need offline install:
1. Download the CSL file from: https://raw.githubusercontent.com/citation-style-language/styles/master/multidisciplinary-digital-publishing-institute.csl
2. Open Zotero → **Preferences** → **Cite** → **Styles**
3. Click the **"+"** button (Add style)
4. Select the downloaded `.csl` file
5. The style will be added to your Zotero

### Note on the "Zenoto" Reference in the Task
The task mentioned "zenoto" — this likely refers to **Zotero**. The MDPI style is directly installable in Zotero as described above.

---

## 6. Evidence Sources

| Source | Tier | URL / Path |
|--------|------|-----------|
| MDPI Official Reference Guide | Official (A-003) | https://www.mdpi.com/authors/references |
| MDPI CSL File | Official (A-004) | https://raw.githubusercontent.com/citation-style-language/styles/master/multidisciplinary-digital-publishing-institute.csl |
| Zotero Style Repository | Official (A-005) | https://www.zotero.org/styles/?q=id%3Amultidisciplinary-digital-publishing-institute |
| WXY Manuscript (Genes) | Practical Example (A-002) | Local: WXY manuscript_v8.docx |
| MDPI Submission Rules (T-015) | Context (A-001) | Local: T-015 delivery artifacts |

---

## 7. Answer to the User's Questions

**Q: MDPI的写作引用格式是哪种？**
A: MDPI使用**编号制引用格式**（numbered citation），Zotero中对应的官方样式名称是 **"Multidisciplinary Digital Publishing Institute"**。

**Q: 是常规模式吗？我能在Zotero里直接插入吗？**
A: **是的，这是Zotero官方仓库中的标准样式**。在Zotero中通过 Preferences → Cite → Get additional styles，搜索 "Multidisciplinary Digital Publishing Institute" 即可直接安装，无需下载CSL文件。安装后在Zotero里直接插入引用即可。

**Q: 如果不是常规模式，帮忙下载文件。**
A: 该样式**已是常规模式**（Zotero官方仓库样式），不需要手动下载。但为了方便，CSL文件已下载到本地：`4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl`。
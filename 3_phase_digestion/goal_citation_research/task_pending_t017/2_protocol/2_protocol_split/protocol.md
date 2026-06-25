# Protocol: MDPI Citation Format Investigation

## Objective
Determine the exact citation/reference format used by MDPI and Genes journal, confirm it is a standard format directly installable in Zotero, and identify the official CSL file and download location. If it is not a standard Zotero-supported style, locate and download the required citation format file.

## Inputs
- A-001: T-015 MDPI submission rules outputs — Prior MDPI submission rules summary; use to cross-reference citation rules mentioned in the official MDPI author guide.
- A-002: WXY manuscript_v8.docx — Published/reviewed Genes submission example; inspect its in-text citation format and reference list to confirm the style used in practice.
- A-003: MDPI Reference List and Citations Style Guide (official) — The authoritative source for MDPI's official citation format. Identifies "Multidisciplinary Digital Publishing Institute" as the Zotero style.
- A-004: MDPI CSL file — The official CSL definition file for the MDPI citation style. Use to verify style details and make the file available for local download if needed.
- A-005: Zotero Style Repository page for MDPI — Confirms the CSL style is in the official Zotero repository and directly installable.
- A-006: Web search results — Supplementary evidence to cross-validate the Zotero style name and CSL download source.

## Steps
1. Read the official MDPI reference/citation guide (A-003) to identify the official citation style requirements: in-text citation format, reference list format, and the recommended Zotero style name.
2. Inspect the WXY manuscript (A-002) reference section and in-text citations to confirm the practical citation format used in a real Genes submission.
3. Search online to confirm the Zotero CSL style name: "Multidisciplinary Digital Publishing Institute".
4. Locate and verify the official CSL file (A-004) from the citation-style-language GitHub repository. Download a local copy to `4_artifact/6_archive/` for offline access.
5. Document the exact steps to install the MDPI citation style in Zotero.
6. Produce a concise findings report in Markdown format.

## Constraints
- Do not modify the original WXY manuscript file.
- Distinguish between official MDPI rules (from mdpi.com/authors/references) and practical observations from the example manuscript.
- The CSL file must be the official version from the citation-style-language/styles repository, not a user-modified fork.
- If the style is a standard Zotero repository style, the answer should be: "MDPI uses the 'Multidisciplinary Digital Publishing Institute' style, which is a numbered (ACS-based) citation style. In Zotero, go to Preferences → Cite → Styles → Get additional styles, search 'Multidisciplinary Digital Publishing Institute', and install. It uses [1], [2] bracket numbering in text."

## Deliverables
- MDPI citation format investigation report: `{taskPath}/4_artifact/2_persist/mdpi_citation_format_findings_v20260623.md`
- Downloaded MDPI CSL file (if needed for offline install): `{taskPath}/4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl`

## Acceptance
- The report clearly states the exact Zotero style name.
- The in-text citation format (numbered brackets [1], [2]) and reference list format are documented.
- The method to install the style in Zotero is explicitly described.
- The WXY manuscript reference format serves as a practical confirmation example.
# External API Demo (PubChem + Cellosaurus)

- Time: 2026-04-10T00:02:51

## PubChem

```json
{
  "erlotinib": {
    "smiles": "COCCOC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC=CC(=C3)C#C)OCCOC",
    "inchikey": "AAKJLRGGTJKAMG-UHFFFAOYSA-N"
  },
  "tarceva": {
    "smiles": "COCCOC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC=CC(=C3)C#C)OCCOC.Cl",
    "inchikey": "GTTBEUCJPZQMDZ-UHFFFAOYSA-N"
  },
  "not_a_real_drug_name_xyz": {
    "error": "HTTPError: HTTP Error 404: PUGREST.NotFound"
  }
}
```

## Cellosaurus

```json
{
  "HAP1": {
    "site": "Bone marrow",
    "disease": "Chronic myelogenous leukemia, BCR-ABL1 positive",
    "category": "Cancer cell line"
  },
  "HEK293T": {
    "site": "Fetal kidney",
    "disease": "",
    "category": "Transformed cell line"
  },
  "NCI-H358": {
    "site": "Lung",
    "disease": "Minimally invasive lung adenocarcinoma",
    "category": "Cancer cell line"
  },
  "MCLF1234": null
}
```
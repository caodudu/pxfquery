# Cellline Stepwise Selection Demo

- Time: 2026-04-10T11:08:05
- Model: MiniMax-M2.7
- Demo Count: 4

## Step Traces

### Context: `triple-negative breast cancer`
- Step 1 (lineage): selected `breast` from ['bone', 'breast', 'central_nervous_system', 'cervix', 'endometrium', 'haematopoietic_and_lymphoid_tissue', 'kidney', 'large_intestine', 'liver', 'lung', 'normal_other', 'ovary', 'pancreas', 'prostate', 'skin', 'soft_tissue', 'stomach', 'upper_aerodigestive_tract', 'urinary_tract'] (source=fast_rule)
- Step 2 (disease): selected `breast cancer` from ['breast cancer', 'normal breast sample', 'unknown'] (source=fast_rule)
- Step 3 (subtype): selected `carcinoma` from ['carcinoma', 'adenocarcinoma'] (source=llm)
- Resolved Cells: `['BT20', 'BT474', 'HS578T', 'MCF10A', 'T47D', 'ZR751']`

### Context: `non-small cell lung carcinoma`
- Step 1 (lineage): selected `lung` from ['bone', 'breast', 'central_nervous_system', 'cervix', 'endometrium', 'haematopoietic_and_lymphoid_tissue', 'kidney', 'large_intestine', 'liver', 'lung', 'normal_other', 'ovary', 'pancreas', 'prostate', 'skin', 'soft_tissue', 'stomach', 'upper_aerodigestive_tract', 'urinary_tract'] (source=fast_rule)
- Step 2 (disease): selected `lung cancer` from ['lung cancer', 'normal lung sample'] (source=fast_rule)
- Step 3 (subtype): selected `non-small cell lung carcinoma` from ['non-small cell lung carcinoma', 'carcinoma', 'small cell lung carcinoma', 'adenocarcinoma'] (source=fast_rule)
- Resolved Cells: `['H1299', 'A549', 'HCC827', 'NCIH1437', 'NCIH1563', 'NCIH1573', 'NCIH1781', 'NCIH1975', 'NCIH2073', 'NCIH2110', 'NCIH2172', 'NCIH596', 'NCIH838', 'BEN', 'HCC15', 'HCC44', 'HCC1588', 'HCC95', 'CORL23', 'T3M10']`

### Context: `colorectal adenocarcinoma`
- Step 1 (lineage): selected `large_intestine` from ['bone', 'breast', 'central_nervous_system', 'cervix', 'endometrium', 'haematopoietic_and_lymphoid_tissue', 'kidney', 'large_intestine', 'liver', 'lung', 'normal_other', 'ovary', 'pancreas', 'prostate', 'skin', 'soft_tissue', 'stomach', 'upper_aerodigestive_tract', 'urinary_tract'] (source=fast_rule)
- Step 2 (subtype): selected `adenocarcinoma` from ['adenocarcinoma', 'carcinoma'] (source=fast_rule)
- Resolved Cells: `['DLD1', 'HT29', 'LOVO', 'NCIH508', 'NCIH716', 'RKO', 'SW480', 'SW620', 'SW948', 'CL34', 'SNUC4', 'SNUC5', 'GP2D']`

### Context: `NCI-H358-like NSCLC context`
- Step 1 (lineage): selected `lung` from ['bone', 'breast', 'central_nervous_system', 'cervix', 'endometrium', 'haematopoietic_and_lymphoid_tissue', 'kidney', 'large_intestine', 'liver', 'lung', 'normal_other', 'ovary', 'pancreas', 'prostate', 'skin', 'soft_tissue', 'stomach', 'upper_aerodigestive_tract', 'urinary_tract'] (source=fast_rule)
- Step 2 (disease): selected `lung cancer` from ['lung cancer', 'normal lung sample'] (source=fast_rule)
- Step 3 (subtype): selected `non-small cell lung carcinoma` from ['non-small cell lung carcinoma', 'carcinoma', 'small cell lung carcinoma', 'adenocarcinoma'] (source=fast_rule)
- Resolved Cells: `['H1299', 'A549', 'HCC827', 'NCIH1437', 'NCIH1563', 'NCIH1573', 'NCIH1781', 'NCIH1975', 'NCIH2073', 'NCIH2110', 'NCIH2172', 'NCIH596', 'NCIH838', 'BEN', 'HCC15', 'HCC44', 'HCC1588', 'HCC95', 'CORL23', 'T3M10']`

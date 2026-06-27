# PxFquery Demo Notebooks

These notebooks are the current GitHub-facing observation surface for PxFquery.

They show how a biomedical researcher should interact with the package through natural-language questions and `PxFQuery().ask(...)`, while keeping structured output available for inspection.

## Scenarios

| Notebook | Scene | Question |
|---|---|---|
| `01_drug_forward.ipynb` | Drug + forward | How does erlotinib change functional programs in A549 lung cancer cells? |
| `02_drug_reverse.ipynb` | Drug + reverse | Which drugs activate apoptosis in A549 cells? |
| `03_genetic_forward.ipynb` | Genetic + forward | What happens to functional programs if I knock down KRAS in A549 lung cancer cells? |
| `04_genetic_reverse.ipynb` | Genetic + reverse | What genetic perturbations suppress MYC expression in A549 cells? |

## Current Status

The notebooks show the MS8 user-facing answer shape and are intended to evolve into manuscript application examples. The current package still uses a placeholder query kernel, so these are interface and workflow demos rather than final resource-pack-backed biological analyses.

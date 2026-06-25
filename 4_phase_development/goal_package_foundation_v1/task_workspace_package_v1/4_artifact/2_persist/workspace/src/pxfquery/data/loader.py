"""
loader.py — Load and cache GSEA score matrices for PxFquery.

Supports loading from local h5ad (AnnData) files.
Future: download from Zenodo by DOI.

Matrix orientation after loading
---------------------------------
Internal representation follows AnnData convention:
  - obs  (rows)   : perturbation experiments (~201k)
  - var  (columns): functional terms / gene sets (91)
  - obs fields    : sig_id, project_code, cell_iname,
                    pert_id, cmap_name, pert_dose, pert_time
"""

from __future__ import annotations
from pathlib import Path
from typing import Dict, Optional, List
import warnings


# Supported perturbation types
PERT_TYPES = ("xpr", "sh", "cp")


class DataLoader:
    """
    Load and manage GSEA score matrices.

    Parameters
    ----------
    cache_dir : str or Path, optional
        Directory to look for local h5ad files.
        Defaults to the package's bundled data directory.

    Examples
    --------
    >>> loader = DataLoader()
    >>> loader.load_local("xpr", "/path/to/xpr_func_ad.h5ad")
    >>> ad = loader.get("xpr")
    """

    def __init__(self, cache_dir: Optional[str | Path] = None):
        self._data: Dict[str, "AnnData"] = {}
        self.cache_dir = Path(cache_dir) if cache_dir else None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def load_local(self, pert_type: str, path: str | Path) -> None:
        """
        Load a single h5ad matrix from a local path.

        Parameters
        ----------
        pert_type : str
            One of 'xpr', 'sh', 'cp'.
        path : str or Path
            Path to the .h5ad file.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        ValueError
            If pert_type is not recognized.
        """
        pert_type = _validate_pert_type(pert_type)
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        import anndata as ad
        self._data[pert_type] = ad.read_h5ad(path)
        print(f"[loader] Loaded '{pert_type}' — {self._data[pert_type].shape}")

    def load_all_local(self, directory: str | Path) -> None:
        """
        Load all three matrices from a directory.

        Expects files named: xpr_func_ad.h5ad, sh_func_ad.h5ad, cp_func_ad.h5ad

        Parameters
        ----------
        directory : str or Path
        """
        directory = Path(directory)
        for pert_type in PERT_TYPES:
            fpath = directory / f"{pert_type}_func_ad.h5ad"
            if fpath.exists():
                self.load_local(pert_type, fpath)
            else:
                warnings.warn(f"[loader] Not found, skipping: {fpath}")

    def get(self, pert_type: str) -> "AnnData":
        """
        Retrieve a loaded AnnData matrix.

        Parameters
        ----------
        pert_type : str
            One of 'xpr', 'sh', 'cp'.

        Returns
        -------
        AnnData

        Raises
        ------
        KeyError
            If the matrix has not been loaded yet.
        """
        pert_type = _validate_pert_type(pert_type)
        if pert_type not in self._data:
            raise KeyError(
                f"'{pert_type}' matrix not loaded. "
                f"Call load_local('{pert_type}', path) first."
            )
        return self._data[pert_type]

    def list_loaded(self) -> List[str]:
        """Return list of currently loaded perturbation types."""
        return list(self._data.keys())

    @property
    def term_names(self) -> List[str]:
        """
        Return functional term names (var_names) from any loaded matrix.
        All matrices share the same terms.
        """
        if not self._data:
            raise RuntimeError("No matrix loaded yet.")
        return list(next(iter(self._data.values())).var_names)

    # ------------------------------------------------------------------
    # Future: Zenodo download
    # ------------------------------------------------------------------

    def download_zenodo(self, doi: str, pert_type: str) -> None:
        """
        Download a matrix from Zenodo by DOI. (Not yet implemented)

        Parameters
        ----------
        doi : str
            Zenodo DOI string, e.g. "10.5281/zenodo.1234567".
        pert_type : str
            One of 'xpr', 'sh', 'cp'.
        """
        raise NotImplementedError(
            "Zenodo download not implemented yet. "
            "Use load_local() with a local file path."
        )


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _validate_pert_type(pert_type: str) -> str:
    pt = pert_type.lower().strip()
    if pt not in PERT_TYPES:
        raise ValueError(
            f"Unknown pert_type '{pert_type}'. Must be one of: {PERT_TYPES}"
        )
    return pt

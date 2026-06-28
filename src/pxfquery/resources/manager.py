from __future__ import annotations

import hashlib
import json
import os
import shutil
import time
import urllib.request
from dataclasses import asdict, dataclass, field
from importlib import resources as importlib_resources
from pathlib import Path
from typing import Any

from tqdm.auto import tqdm

from pxfquery.l3_execution.assets import AssetRegistry


DEFAULT_CACHE_DIR = Path.home() / ".cache" / "pxfquery" / "resources"
DEFAULT_MANIFEST_PACKAGE = "pxfquery.resources.manifests"
DEFAULT_MANIFEST_FILE = "zenodo_21001791_v20260628.json"
MODALITIES = ("cp", "sh", "xpr")
L3_MATRIX_PATTERNS = (
    "{modality}_X_dense_thr0.1_round2_float16_compressed.npz",
    "{modality}_X_dense_thr0.1_round2_float16.npz",
    "{modality}_X_round2_float16_compressed.npz",
)


@dataclass
class ResourceFile:
    key: str
    path: str
    exists: bool
    group: str | None = None
    modality: str | None = None
    bytes: int | None = None
    sha256: str | None = None
    url: str | None = None
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ResourceStatus:
    configured: bool
    available: bool
    source: str = "unconfigured"
    version: str | None = None
    root: str | None = None
    available_files: dict[str, str] = field(default_factory=dict)
    missing_files: list[str] = field(default_factory=list)
    optional_missing_files: list[str] = field(default_factory=list)
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class ResourceManager:
    """Resource-pack manager shared by L2/L3/L4.

    It owns paths, downloads, checksums, and lightweight resource discovery only.
    It does not parse user intent, route entities, execute matrices, or assemble
    biological evidence.
    """

    def __init__(self, client: Any | None = None, *, cache_dir: str | Path | None = None, verify_checksums: bool | None = None) -> None:
        self._client = client
        self._root: Path | None = None
        self._manifest: dict[str, Any] = {}
        self._version: str | None = None
        self.verify_checksums = _default_checksum_verification() if verify_checksums is None else bool(verify_checksums)
        self._functional_matrix_cache: dict[str, Any] = {}
        env_root = os.environ.get("PXFQUERY_RESOURCE_DIR")
        if env_root:
            self._root = Path(env_root).expanduser().resolve()
        self._cache_dir = Path(cache_dir).expanduser().resolve() if cache_dir else DEFAULT_CACHE_DIR
        if self._root is None and _default_resources_enabled():
            self.use_manifest(default_manifest(), strict=False)

    @property
    def root(self) -> Path | None:
        return self._root

    def use(self, path: str | Path, *, strict: bool = True, version: str | None = None) -> ResourceStatus:
        self._root = Path(path).expanduser().resolve()
        self._manifest = {}
        self._version = version
        self._functional_matrix_cache.clear()
        if self._client is not None:
            self._client.assets = AssetRegistry.from_root(self._root, strict=strict)
            self._client._index_dir = self._root
        return self.status()

    def use_manifest(self, manifest: str | Path | dict[str, Any], *, strict: bool = True, version: str | None = None) -> ResourceStatus:
        payload = _load_manifest(manifest)
        self._manifest = payload
        self._version = version or payload.get("version") or payload.get("resource_version")
        self._root = None
        self._functional_matrix_cache.clear()
        root = payload.get("root")
        if root:
            root_path = Path(root).expanduser()
            if not root_path.is_absolute() and isinstance(manifest, (str, Path)):
                root_path = Path(manifest).expanduser().resolve().parent / root_path
            self._root = root_path.resolve()
        elif isinstance(manifest, (str, Path)):
            self._root = Path(manifest).expanduser().resolve().parent
        if self._client is not None:
            self._refresh_client_assets(strict=strict)
            self._client._index_dir = self._root
        return self.status()

    def status(self) -> ResourceStatus:
        files = self._discover_files()
        available = {key: item.path for key, item in files.items() if item.exists}
        missing_required = [key for key, item in files.items() if not item.exists and item.group not in OPTIONAL_RESOURCE_GROUPS]
        missing_optional = [key for key, item in files.items() if not item.exists and item.group in OPTIONAL_RESOURCE_GROUPS]
        configured = self._root is not None or bool(self._manifest)
        return ResourceStatus(
            configured=configured,
            available=configured and not missing_required,
            source="manifest" if self._manifest else ("local_resource_pack" if self._root else "unconfigured"),
            version=self._version,
            root=str(self._root) if self._root is not None else None,
            available_files=available,
            missing_files=missing_required,
            optional_missing_files=missing_optional,
            message="PxFquery resources are configured." if configured else "No PxFquery resource pack is configured.",
        )

    def manifest(self) -> dict[str, Any]:
        if self._manifest:
            return dict(self._manifest)
        if self._client is not None and getattr(self._client, "assets", None) is not None:
            return self._client.assets.to_dict()
        return {}

    def download(
        self,
        group: str | None = None,
        *,
        modalities: list[str] | tuple[str, ...] | None = None,
        kinds: list[str] | tuple[str, ...] | None = None,
    ) -> ResourceStatus:
        if group is not None:
            return self.ensure(group, modalities=modalities, kinds=kinds, auto_download=True)
        for name in ("l2_core_indexes", "l2_proxy_neighbors"):
            self.ensure(name, auto_download=True)
        self.ensure("l3_functional_scores", modalities=modalities, kinds=kinds, auto_download=True)
        return self.status()

    def path(self, group: str, *, modality: str | None = None, kind: str | None = None) -> Path:
        item = self._resource_file(group=group, modality=modality, kind=kind)
        if not item.exists:
            raise FileNotFoundError(f"resource missing: {item.key} at {item.path}")
        return Path(item.path)

    def ensure(
        self,
        group: str,
        *,
        modalities: list[str] | tuple[str, ...] | None = None,
        kinds: list[str] | tuple[str, ...] | None = None,
        auto_download: bool = True,
    ) -> ResourceStatus:
        required = self._required_files(group=group, modalities=modalities, kinds=kinds)
        missing = [item for item in required if not item.exists]
        if missing and auto_download:
            for item in missing:
                self._download_file(item)
            self._refresh_client_assets(strict=False)
            required = self._required_files(group=group, modalities=modalities, kinds=kinds)
            missing = [item for item in required if not item.exists]
        return ResourceStatus(
            configured=self._root is not None or bool(self._manifest),
            available=not missing,
            source="manifest" if self._manifest else "local_resource_pack",
            version=self._version,
            root=str(self._root) if self._root else None,
            available_files={item.key: item.path for item in required if item.exists},
            missing_files=[item.key for item in missing],
            message="resources available" if not missing else "resources missing",
        )

    def _required_files(
        self,
        *,
        group: str,
        modalities: list[str] | tuple[str, ...] | None = None,
        kinds: list[str] | tuple[str, ...] | None = None,
    ) -> list[ResourceFile]:
        if group == "l3_functional_scores":
            mods = modalities or MODALITIES
            ks = kinds or ("matrix", "obs", "var")
            return [self._resource_file(group=group, modality=m, kind=k) for m in mods for k in ks]
        return [item for item in self._discover_files().values() if item.group == group]

    def _resource_file(self, *, group: str, modality: str | None, kind: str | None) -> ResourceFile:
        key = ".".join(part for part in [group, modality, kind] if part)
        manifest_item = self._manifest_file(key)
        if manifest_item is not None:
            return manifest_item
        if group == "l3_functional_scores" and modality:
            return self._local_l3_file(modality, kind or "matrix")
        raise KeyError(f"unknown resource key: {key}")

    def _discover_files(self) -> dict[str, ResourceFile]:
        out: dict[str, ResourceFile] = {}
        for modality in MODALITIES:
            for kind in ("matrix", "obs", "var"):
                item = self._resource_file(group="l3_functional_scores", modality=modality, kind=kind)
                out[item.key] = item
        for key, filename in L2_INDEX_FILES.items():
            item = self._manifest_file(key)
            if item is None:
                item = self._local_file(key, filename, group=L2_INDEX_GROUPS[key])
            out[item.key] = item
        return out

    def _local_l3_file(self, modality: str, kind: str) -> ResourceFile:
        if kind == "matrix":
            candidates = [pattern.format(modality=modality) for pattern in L3_MATRIX_PATTERNS]
        elif kind == "obs":
            candidates = [f"{modality}_obs_min.parquet", f"{modality}_obs_min.csv"]
        elif kind == "var":
            candidates = [f"{modality}_var_names.json", "var_names.json"]
        else:
            raise KeyError(kind)
        path = _find_first(self._root, candidates)
        fallback = (self._root or self._cache_dir) / candidates[0]
        return ResourceFile(
            key=f"l3_functional_scores.{modality}.{kind}",
            path=str(path or fallback),
            exists=path is not None,
            group="l3_functional_scores",
            modality=modality,
        )

    def _local_file(self, key: str, filename: str, *, group: str) -> ResourceFile:
        path = _find_first(self._root, [filename])
        fallback = (self._root or self._cache_dir) / filename
        return ResourceFile(key=key, path=str(path or fallback), exists=path is not None, group=group)

    def _manifest_file(self, key: str) -> ResourceFile | None:
        files = self._manifest.get("files") or self._manifest.get("resources") or {}
        payload = files.get(key)
        if payload is None:
            return None
        rel = payload.get("path") or payload.get("filename") or Path(payload.get("url", key)).name
        root = self._root or self._cache_dir / str(self._version or "default")
        if self._root is None and self._manifest.get("cache_subdir"):
            root = self._cache_dir / str(self._manifest["cache_subdir"])
        path = Path(rel).expanduser()
        if not path.is_absolute():
            path = root / path
        exists = path.exists() and _manifest_file_ok(path, payload, verify_checksum=self.verify_checksums)
        return ResourceFile(
            key=key,
            path=str(path),
            exists=exists,
            group=payload.get("group"),
            modality=payload.get("modality"),
            bytes=payload.get("bytes"),
            sha256=payload.get("sha256"),
            url=payload.get("url"),
        )

    def _download_file(self, item: ResourceFile) -> None:
        if not item.url:
            raise FileNotFoundError(f"resource missing and no download URL configured: {item.key}")
        target = Path(item.path)
        target.parent.mkdir(parents=True, exist_ok=True)
        part = target.with_suffix(target.suffix + ".part")
        lock = target.with_suffix(target.suffix + ".lock")
        _acquire_lock(lock)
        try:
            if target.exists() and _checksum_ok(target, item.sha256):
                return
            if part.exists():
                if item.bytes and part.stat().st_size == item.bytes and _checksum_ok(part, item.sha256):
                    shutil.move(str(part), str(target))
                    return
                part.unlink(missing_ok=True)
            with urllib.request.urlopen(item.url) as response:
                total = int(response.headers.get("Content-Length") or item.bytes or 0)
                with part.open("wb") as handle, tqdm(total=total, unit="B", unit_scale=True, desc=item.key) as bar:
                    while True:
                        chunk = response.read(1024 * 1024)
                        if not chunk:
                            break
                        handle.write(chunk)
                        bar.update(len(chunk))
            if item.sha256 and _sha256(part) != item.sha256:
                part.unlink(missing_ok=True)
                raise RuntimeError(f"checksum_failed for {item.key}")
            shutil.move(str(part), str(target))
        finally:
            lock.unlink(missing_ok=True)

    def _refresh_client_assets(self, *, strict: bool) -> None:
        if self._client is None or not self._manifest:
            return
        base_dir = self._root
        if base_dir is None:
            base_dir = self._cache_dir / str(self._manifest.get("cache_subdir") or self._version or "default")
        self._client.assets = AssetRegistry.from_manifest(self._manifest, strict=strict, base_dir=base_dir)


L2_INDEX_FILES = {
    "l2.cellline_index": "cellline_index.json",
    "l2.cellline_neighbors": "cellline_neighbors.json",
    "l2.cellline_tree": "cellline_tree.json",
    "l2.drug_index": "drug_index.json",
    "l2.drug_neighbors": "drug_neighbors.json",
    "l2.gene_index": "gene_index.json",
    "l2.gene_index_simple": "gene_index_simple.json",
    "l2.gene_neighbors": "gene_neighbors.json",
    "l2.function_index": "function_index.json",
}

L2_INDEX_GROUPS = {
    "l2.cellline_index": "l2_core_indexes",
    "l2.cellline_neighbors": "l2_proxy_neighbors",
    "l2.cellline_tree": "l2_core_indexes",
    "l2.drug_index": "l2_core_indexes",
    "l2.drug_neighbors": "l2_proxy_neighbors",
    "l2.gene_index": "l2_core_indexes",
    "l2.gene_index_simple": "l2_core_indexes",
    "l2.gene_neighbors": "l2_proxy_neighbors",
    "l2.function_index": "l2_core_indexes",
}

OPTIONAL_RESOURCE_GROUPS: set[str] = set()


def _find_first(root: Path | None, names: list[str]) -> Path | None:
    if root is None:
        return None
    for name in names:
        direct = root / name
        if direct.exists():
            return direct.resolve()
        matches = sorted(root.rglob(name))
        if matches:
            return matches[0].resolve()
    return None


def _load_manifest(manifest: str | Path | dict[str, Any]) -> dict[str, Any]:
    if isinstance(manifest, dict):
        return dict(manifest)
    path = Path(manifest).expanduser()
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        import yaml

        payload = yaml.safe_load(text)
    else:
        payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("resource manifest must be a mapping")
    return payload


def default_manifest() -> dict[str, Any]:
    text = importlib_resources.files(DEFAULT_MANIFEST_PACKAGE).joinpath(DEFAULT_MANIFEST_FILE).read_text(encoding="utf-8")
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("default resource manifest must be a mapping")
    return payload


def _default_resources_enabled() -> bool:
    value = os.environ.get("PXFQUERY_AUTO_RESOURCES", "1").strip().lower()
    return value not in {"0", "false", "no", "off"}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _checksum_ok(path: Path, expected: str | None) -> bool:
    return True if not expected else _sha256(path) == expected


def _size_ok(path: Path, expected: int | None) -> bool:
    return True if expected is None else path.stat().st_size == expected


def _manifest_file_ok(path: Path, payload: dict[str, Any], *, verify_checksum: bool) -> bool:
    if not path.exists() or not _size_ok(path, payload.get("bytes")):
        return False
    if verify_checksum:
        return _checksum_ok(path, payload.get("sha256"))
    return True


def _default_checksum_verification() -> bool:
    value = os.environ.get("PXFQUERY_VERIFY_CHECKSUMS", "0").strip().lower()
    return value in {"1", "true", "yes", "on"}


def _acquire_lock(path: Path, *, timeout: float = 900.0, poll: float = 0.25) -> None:
    started = time.time()
    while True:
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(str(os.getpid()))
            return
        except FileExistsError:
            if time.time() - started > timeout:
                raise TimeoutError(f"timed out waiting for resource download lock: {path}")
            time.sleep(poll)

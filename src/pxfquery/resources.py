from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from pxfquery.assets import AssetRegistry


@dataclass
class ResourceStatus:
    configured: bool
    available: bool
    source: str = "unconfigured"
    version: str | None = None
    path: str | None = None
    asset_count: int = 0
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class ResourceManager:
    """User-facing resource-pack manager.

    The current implementation wraps local standard_resources registration. A later
    MS8 task will add official archive download, cache verification, and resource
    pack version manifests.
    """

    def __init__(self, client) -> None:
        self._client = client
        self._pack_path: Path | None = None
        self._version: str | None = None

    def status(self) -> ResourceStatus:
        registry = self._client.assets
        if registry is None:
            return ResourceStatus(
                configured=False,
                available=False,
                message="No PxFquery resource pack is configured. Use resources.use(...) or resources.download(...).",
            )
        keys = registry.keys()
        return ResourceStatus(
            configured=True,
            available=all(registry.get(key).exists for key in keys),
            source="local_resource_pack",
            version=self._version,
            path=str(self._pack_path) if self._pack_path is not None else None,
            asset_count=len(keys),
            message="PxFquery resource pack is configured.",
        )

    def use(self, path: str | Path, *, strict: bool = True, version: str | None = None) -> ResourceStatus:
        self._pack_path = Path(path).expanduser().resolve()
        self._version = version
        self._client.assets = AssetRegistry.from_root(self._pack_path, strict=strict)
        return self.status()

    def use_manifest(self, manifest: str | Path | dict[str, Any], *, strict: bool = True, version: str | None = None) -> ResourceStatus:
        self._version = version
        self._client.assets = AssetRegistry.from_manifest(manifest, strict=strict)
        self._pack_path = _manifest_root(manifest)
        return self.status()

    def download(self, url: str | None = None, *, cache_dir: str | Path | None = None, force: bool = False) -> ResourceStatus:
        _ = (cache_dir, force)
        if not url:
            return ResourceStatus(
                configured=False,
                available=False,
                source="download_not_configured",
                message="Official resource-pack download is not configured in this version. Provide a local pack with resources.use(...).",
            )
        return ResourceStatus(
            configured=False,
            available=False,
            source="download_planned",
            message=f"Download support is planned for a later MS8 task; requested URL was {url}.",
        )

    def manifest(self) -> dict[str, dict[str, Any]]:
        if self._client.assets is None:
            return {}
        return self._client.assets.to_dict()


def _manifest_root(manifest: str | Path | dict[str, Any]) -> Path | None:
    if isinstance(manifest, (str, Path)):
        return Path(manifest).expanduser().resolve().parent
    root = manifest.get("root")
    return Path(root).expanduser().resolve() if root else None

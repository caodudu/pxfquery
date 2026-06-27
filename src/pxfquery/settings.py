from __future__ import annotations

from pxfquery.l1_nlu import DEFAULT_L1_BASE_URL, DEFAULT_L1_MODEL, OpenAICompatibleNLUBackend, backend_from_env


class SettingsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def set_l1_backend(
        self,
        *,
        token: str,
        base_url: str = DEFAULT_L1_BASE_URL,
        model: str = DEFAULT_L1_MODEL,
        timeout: float = 30.0,
    ) -> None:
        self._client.nlu_backend = OpenAICompatibleNLUBackend(
            base_url=base_url,
            api_key=token,
            model=model,
            timeout=timeout,
        )

    def use_diygateway(self, *, token: str | None = None, timeout: float = 30.0) -> None:
        if token is not None:
            self.set_l1_backend(token=token, timeout=timeout)
            return
        backend = backend_from_env(required=True)
        backend.timeout = timeout
        self._client.nlu_backend = backend

    def enable_resolver(
        self,
        *,
        index_dir: str,
        token: str | None = None,
        base_url: str = DEFAULT_L1_BASE_URL,
        model: str = DEFAULT_L1_MODEL,
        default_top_n: int = 20,
    ) -> None:
        self._client.enable_resolver(
            index_dir=index_dir,
            api_key=token,
            base_url=base_url,
            model=model,
            default_top_n=default_top_n,
        )

    def l1_backend_status(self) -> dict:
        backend = self._client.nlu_backend
        if backend is None:
            return {"configured": False}
        return {
            "configured": True,
            "base_url": backend.base_url,
            "model": backend.model,
            "timeout": backend.timeout,
        }

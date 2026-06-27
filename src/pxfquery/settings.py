from __future__ import annotations

from pxfquery.l1_intent import (
    DEFAULT_PROVIDER,
    DIYGATEWAY_BASE_URL,
    DIYGATEWAY_MODEL,
    OFFICIAL_DEEPSEEK_BASE_URL,
    OFFICIAL_DEEPSEEK_MODEL,
    LLMProviderConfig,
    provider_from_env,
)


class SettingsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def register_llm_provider(
        self,
        *,
        name: str = DEFAULT_PROVIDER,
        token: str,
        base_url: str = OFFICIAL_DEEPSEEK_BASE_URL,
        model: str = OFFICIAL_DEEPSEEK_MODEL,
        timeout: float = 30.0,
        max_network_attempts: int = 3,
        network_retry_sleep: float = 2.0,
        default: bool = True,
    ) -> None:
        self._client.llm_providers.register(
            LLMProviderConfig(
                name=name,
                base_url=base_url,
                api_key=token,
                model=model,
                timeout=timeout,
                max_network_attempts=max_network_attempts,
                network_retry_sleep=network_retry_sleep,
            ),
            default=default,
        )

    def set_l1_provider(
        self,
        *,
        token: str,
        base_url: str = DIYGATEWAY_BASE_URL,
        model: str = DIYGATEWAY_MODEL,
        timeout: float = 30.0,
    ) -> None:
        self.register_llm_provider(
            name="l1",
            base_url=base_url,
            token=token,
            model=model,
            timeout=timeout,
        )

    def use_diygateway(self, *, token: str | None = None, timeout: float = 30.0) -> None:
        if token is not None:
            self.register_llm_provider(
                name="diygateway",
                token=token,
                base_url=DIYGATEWAY_BASE_URL,
                model=DIYGATEWAY_MODEL,
                timeout=timeout,
            )
            return
        provider = provider_from_env(required=True)
        provider.config.timeout = timeout
        self._client.llm_providers.register(provider.config, default=True)

    def use_deepseek(self, *, token: str, timeout: float = 60.0) -> None:
        self.register_llm_provider(
            name="deepseek",
            token=token,
            base_url=OFFICIAL_DEEPSEEK_BASE_URL,
            model=OFFICIAL_DEEPSEEK_MODEL,
            timeout=timeout,
        )

    def enable_resolver(
        self,
        *,
        index_dir: str,
        token: str | None = None,
        base_url: str = DIYGATEWAY_BASE_URL,
        model: str = DIYGATEWAY_MODEL,
        default_top_n: int = 20,
    ) -> None:
        self._client.enable_resolver(
            index_dir=index_dir,
            api_key=token,
            base_url=base_url,
            model=model,
            default_top_n=default_top_n,
        )

    def llm_provider_status(self) -> dict:
        return self._client.llm_providers.status()

    def l1_provider_status(self) -> dict:
        provider = self._client.llm_providers.get()
        if provider is None:
            return {"configured": False}
        return {
            "configured": True,
            "base_url": provider.config.base_url,
            "model": provider.config.model,
            "timeout": provider.config.timeout,
        }

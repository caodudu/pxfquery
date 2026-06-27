from pxfquery import PxFQuery, __version__, get_llm_provider, list_llm_providers, register_llm_provider


def test_version_is_public():
    assert __version__ == "0.1.0"


def test_client_query_api():
    client = PxFQuery()
    result = client.query("What happens to KRAS knockdown in A549?")
    assert result["route_type"] == "exact-hit"
    assert result["intent"]["perturbation_identity"] == "KRAS"


def test_register_llm_provider():
    register_llm_provider(
        "local/test-model",
        base_url="http://localhost:3000/v1",
        api_key_env="PXFQUERY_TEST_KEY",
        model="test-model",
    )
    provider = get_llm_provider("local/test-model")
    assert provider.base_url == "http://localhost:3000/v1"
    assert provider.api_key_env == "PXFQUERY_TEST_KEY"
    assert "local/test-model" in list_llm_providers()


def test_client_registers_default_provider_when_unset():
    client = PxFQuery()
    client.register_llm_provider("local/instance-model", base_url="http://localhost:3000/v1")
    assert client.provider == "local/instance-model"

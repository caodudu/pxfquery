import pxfquery
from pxfquery import PxFQuery


def test_version_is_public():
    assert pxfquery.__version__ == "0.1.3"
    assert PxFQuery().version == "0.1.3"


def test_only_class_is_exported_at_top_level():
    assert pxfquery.__all__ == ["PxFQuery"]


def test_client_query_api():
    client = PxFQuery()
    result = client.query("What happens to KRAS knockdown in A549?")
    assert result["route_type"] == "exact-hit"
    assert result["intent"]["perturbation_identity"] == "KRAS"


def test_register_llm_provider():
    client = PxFQuery()
    client.settings.register_llm(
        "local/test-model",
        base_url="http://localhost:3000/v1",
        api_key_env="PXFQUERY_TEST_KEY",
        model="test-model",
        mode="real",
    )
    provider = client.get_llm_provider("local/test-model")
    assert provider.base_url == "http://localhost:3000/v1"
    assert provider.api_key_env == "PXFQUERY_TEST_KEY"
    assert "local/test-model" in client.list_llm_providers()


def test_client_registers_default_provider_when_unset():
    client = PxFQuery()
    client.register_llm_provider("local/instance-model", base_url="http://localhost:3000/v1")
    assert client.provider == "local/instance-model"


def test_scverse_style_workflow_registers_provider_before_query():
    client = PxFQuery()
    client.settings.register_llm(
        "local/workflow-model",
        base_url="http://localhost:3000/v1",
        api_key_env="PXFQUERY_TEST_KEY",
        model="workflow-model",
        mode="real",
    )

    qdata = client.read.query("Run with registered llm_gateway/deepseek-ai/deepseek-v4-flash and record prompt.")
    client.pp.parse(qdata)
    client.tl.resolve(qdata)
    result = client.get.result(qdata)

    assert client.provider == "local/workflow-model"
    assert qdata.uns["provider"]["registered_before_parse"] is True
    assert result["provider"]["name"] == "local/workflow-model"
    assert result["provider"]["registered_before_query"] is True
    assert result["provider"]["mode"] == "real"

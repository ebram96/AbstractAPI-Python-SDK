import pytest

from abstract_api.core.bases.json_response import (
    JSONResponse,
    JSONResponseMeta
)


class TestJSONResponseMeta:
    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"key": "value"})],
        indirect=["content_response"]
    )
    def test_initialization(self, content_response):
        assert JSONResponseMeta(content_response).body_json == content_response.json()

    def test_initialization_with_no_content(self, blank_response):
        assert JSONResponseMeta(blank_response).body_json is None


class TestJSONResponse:
    @pytest.fixture
    def response_fields(self):
        return frozenset(["wanted1", "wanted2", "wanted3"])

    def test__init_response_field(self, blank_response):
        field = "some_key"
        value = "some_value"

        instance = JSONResponse(blank_response, frozenset())
        instance._init_response_field(field, value)

        assert getattr(instance, f"_{field}") == value

    def test_initialization_meta(self, blank_response, response_fields):
        instance = JSONResponse(blank_response, response_fields)
        assert isinstance(instance.meta, JSONResponseMeta)

    def test_initialization_blank_response(
        self, blank_response, response_fields
    ):
        instance = JSONResponse(blank_response, response_fields)

        assert instance.meta.body_json is None
        assert instance._response_fields == response_fields

    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"wanted1": "value1", "wanted2": "value2", "unwanted": "value3"})],
        indirect=True
    )
    def test_initialization_content_response(
        self, content_response, response_fields
    ):
        instance = JSONResponse(content_response, response_fields)

        assert instance._wanted1 == "value1"
        assert instance._wanted2 == "value2"
        assert not hasattr(instance, "wanted3")
        assert not hasattr(instance, "unwanted")

    @pytest.mark.parametrize(
        "content_response",
        [dict(data=[{"key1": "value1", "key2": "value2"}, {"key1": "value1", "key2": "value2"}])],
        indirect=True
    )
    def test_initialization_content_list_response(self, content_response):
        response_fields = frozenset(["nested_entities"])

        instance = JSONResponse(
            content_response, response_fields, list_response=True
        )

        assert instance._nested_entities == instance.meta.body_json

    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"wanted1": "value1", "wanted2": "value2", "unwanted": "value3"})],
        indirect=True
    )
    def test__get_response_field(self, content_response, response_fields):
        instance = JSONResponse(content_response, response_fields)

        assert instance._get_response_field("wanted1") == instance._wanted1
        assert instance._get_response_field("wanted2") == instance._wanted2
        with pytest.raises(AttributeError):
            instance._get_response_field("unwanted")

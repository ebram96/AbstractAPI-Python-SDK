import pytest

from abstract_api.core.bases.json_response import (
    JSONResponse,
    JSONResponseMeta
)
from tests.common_assertions import assert_unchangeable_fields


class TestJSONResponseMeta:
    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"key": "value"})],
        indirect=["content_response"]
    )
    def test_initialization(self, content_response):
        # When
        json = JSONResponseMeta(content_response).response_json

        # Then
        assert json == content_response.json()

    def test_initialization_with_no_content(self, blank_response):
        # When
        json = JSONResponseMeta(blank_response).response_json

        # Then
        assert json is None


class TestJSONResponse:
    @pytest.fixture
    def response_fields(self):
        return frozenset(["wanted1", "wanted2", "wanted3"])

    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"wanted1": "value1", "wanted2": "value2", "unwanted": "value3"})],
        indirect=True
    )
    def test_setattr(self, response_fields, content_response):
        # When
        instance = JSONResponse(content_response, response_fields)

        # Then
        assert_unchangeable_fields(instance, ["wanted1", "wanted2", "_response_fields"])
        instance.new_random_attr = "value"

    def test__init_response_field(self, blank_response):
        # Given
        field = "some_key"
        value = "some_value"

        # When
        instance = JSONResponse(blank_response, frozenset())
        instance._init_response_field(field, value)

        # Then
        assert getattr(instance, f"_{field}") == value

    def test_initialization_meta(self, response_fields, blank_response):
        # When
        instance = JSONResponse(blank_response, response_fields)

        # Then
        assert isinstance(instance.meta, JSONResponseMeta)

    def test_initialization_blank_response(
        self, response_fields, blank_response
    ):
        # When
        instance = JSONResponse(blank_response, response_fields)

        # Then
        assert instance.meta.response_json is None
        assert instance._response_fields == response_fields

    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"wanted1": "value1", "wanted2": "value2", "unwanted": "value3"})],
        indirect=True
    )
    def test_initialization_content_response(
        self, response_fields, content_response
    ):
        # When
        instance = JSONResponse(content_response, response_fields)

        # Then
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
        # Given
        response_fields = frozenset(["nested_entities"])

        # When
        instance = JSONResponse(
            content_response, response_fields, list_response=True
        )

        # Then
        assert instance._nested_entities == instance.meta.response_json

    @pytest.mark.parametrize(
        "content_response",
        [dict(data={"wanted1": "value1", "wanted2": "value2", "unwanted": "value3"})],
        indirect=True
    )
    def test__get_response_field(self, response_fields, content_response):
        # When
        instance = JSONResponse(content_response, response_fields)

        # Then
        assert instance._get_response_field("wanted1") == instance._wanted1
        assert instance._get_response_field("wanted2") == instance._wanted2
        with pytest.raises(AttributeError):
            instance._get_response_field("unwanted")

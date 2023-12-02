import pytest

from abstract_api.core.exceptions import ClientRequestError
from abstract_api.core.mixins import ResponseFieldsMixin


class ConcreteExample(ResponseFieldsMixin):
    _response_fields = frozenset(["field1", "field2"])


class TestResponseFieldsMixin:
    @pytest.fixture
    def instance(self):
        return ConcreteExample()

    def test_initialization_no_response_fields(self, instance):
        assert instance.response_fields == ConcreteExample._response_fields

    def test_initialization_with_response_fields(self):
        response_fields = ["field1"]

        instance = ConcreteExample(response_fields=response_fields)

        assert instance.response_fields == frozenset(response_fields)

    def test__validate_response_fields(self, instance):
        with pytest.raises(ClientRequestError):
            instance._validate_response_fields(["not_expected_field"])

    def test_response_fields_setter(self, instance):
        response_fields = ["field2"]
        instance.response_fields = response_fields

        assert instance.response_fields == frozenset(response_fields)

    def test__response_fields_as_param(self, instance):
        assert instance._response_fields_as_param(instance.response_fields) ==\
            ",".join(instance.response_fields)

    def test__prepare_selected_fields_with_fields(self, instance, mocker):
        response_fields = ["field2"]
        mocked__validate_response_fields = mocker.patch.object(
            instance,
            "_validate_response_fields",
            wraps=instance._validate_response_fields
        )

        prepared_fields = instance._prepare_selected_fields(response_fields)

        mocked__validate_response_fields.assert_called_with(response_fields)
        assert isinstance(prepared_fields, frozenset)

    def test__prepare_selected_fields_no_fields(self, instance, mocker):
        mocked__validate_response_fields = mocker.patch.object(
            instance,
            "_validate_response_fields",
            wraps=instance._validate_response_fields
        )

        prepared_fields = instance._prepare_selected_fields()

        assert mocked__validate_response_fields.call_count == 0
        assert prepared_fields is instance.response_fields

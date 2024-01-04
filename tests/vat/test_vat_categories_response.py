import pytest

from abstract_api.core.bases import JSONResponse
from abstract_api.vat import VATCategoriesResponse
from abstract_api.vat._response_fields import CATEGORIES_RESPONSE_FIELDS
from abstract_api.vat.vat_categories_response import Category
from tests.utils import generate_response


class TestVATCategoriesResponse:
    def test__init_response_field(self, vat_categories_sample):
        # Given
        response = generate_response(vat_categories_sample)
        instance = VATCategoriesResponse(response)

        # When
        instance._init_response_field("categories", vat_categories_sample)

        # Then
        assert isinstance(instance.categories, tuple)
        assert len(instance.categories) == len(vat_categories_sample)
        for h in instance.categories:
            assert isinstance(h, Category)

    def test_initialization_super_call(self, blank_response, mocker):
        # Given
        mocked_init = mocker.patch.object(
            JSONResponse,
            "__init__",
            wraps=JSONResponse.__init__
        )
        mocked_init.return_value = None

        # When
        VATCategoriesResponse(blank_response)

        # Then
        mocked_init.assert_called_once_with(
            blank_response, CATEGORIES_RESPONSE_FIELDS, list_response=True
        )

    def test_initialization(self, vat_categories_sample, mocker):
        # Given
        response = generate_response(vat_categories_sample)

        # When
        instance = VATCategoriesResponse(response)

        # Then
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        assert len(instance.categories) == len(vat_categories_sample)
        mocked__get_response_field.assert_called_with("categories")
        assert mocked__get_response_field.call_count == 1
        with pytest.raises(AttributeError):
            setattr(instance, "categories", "changed")

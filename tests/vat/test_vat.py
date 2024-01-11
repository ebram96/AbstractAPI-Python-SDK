import pytest

from abstract_api import VAT
from abstract_api.core.validators import numerical
from abstract_api.vat import (
    VATCalculationResponse,
    VATCategoriesResponse,
    VATValidationResponse
)


class TestVAT:
    @pytest.fixture
    def service(self):
        return VAT(api_key="no-api-key")

    @pytest.fixture
    def service_url(self, base_url, service):
        return base_url.format(subdomain=service._subdomain)

    def test_check(
        self,
        service,
        service_url,
        vat_validation_sample,
        mocker,
        requests_mock
    ):
        # Given
        vat_number = vat_validation_sample["vat_number"]
        action = "validate"
        requests_mock.get(service_url + action, json=vat_validation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.check(vat_number)

        # Then
        assert isinstance(response, VATValidationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=VATValidationResponse,
            _action=action,
            vat_number=vat_number
        )

    def test_calculate(
        self,
        service,
        service_url,
        vat_calculation_sample,
        mocker,
        requests_mock
    ):
        # Given
        amount = float(vat_calculation_sample["amount_excluding_vat"])
        country_code = vat_calculation_sample["country"]["code"]
        action = "calculate"
        requests_mock.get(service_url + action, json=vat_calculation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked_greater_or_equal = mocker.patch.object(
            numerical, "greater_or_equal", wraps=numerical.greater_or_equal
        )

        # When
        response = service.calculate(amount, country_code)

        # Then
        assert isinstance(response, VATCalculationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=VATCalculationResponse,
            _action=action,
            amount=amount,
            country_code=country_code,
            is_vat_incl=None,
            vat_category=None
        )
        mocked_greater_or_equal.assert_called_once_with("amount", amount, 0)

    def test_lookup(
        self,
        service,
        service_url,
        vat_categories_sample,
        mocker,
        requests_mock
    ):
        # Given
        country_code = vat_categories_sample[0]["country_code"]
        action = "categories"
        requests_mock.get(service_url + action, json=vat_categories_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.categories(country_code)

        # Then
        assert isinstance(response, VATCategoriesResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=VATCategoriesResponse,
            _action=action,
            country_code=country_code,
        )

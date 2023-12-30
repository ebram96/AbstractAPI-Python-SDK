from abstract_api import IBANValidation
from abstract_api.iban_validation import IBANValidationResponse


class TestIBANValidation:
    """IBANValidation service tests."""
    def test_check(
        self,
        iban_validation_sample,
        base_url,
        requests_mock,
        mocker
    ):
        service = IBANValidation(api_key="no-api-key")
        url = base_url.format(subdomain=IBANValidation._subdomain)
        requests_mock.get(url, json=iban_validation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        response = service.check(iban_validation_sample["iban"])

        assert isinstance(response, IBANValidationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=IBANValidationResponse,
            iban=iban_validation_sample["iban"],
        )

from abstract_api import PhoneValidation
from abstract_api.phone_validation import PhoneValidationResponse


class TestPhoneValidation:
    def test_check(self, phone_validation_sample, base_url, requests_mock, mocker):
        # Given
        service = PhoneValidation(api_key="no-api-key")
        url = base_url.format(subdomain=PhoneValidation._subdomain)
        requests_mock.get(url, json=phone_validation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.check(phone=phone_validation_sample["phone"])

        # Then
        assert isinstance(response, PhoneValidationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=PhoneValidationResponse,
            phone=phone_validation_sample["phone"]
        )

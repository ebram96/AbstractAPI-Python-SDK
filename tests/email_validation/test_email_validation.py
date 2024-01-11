from abstract_api import EmailValidation
from abstract_api.email_validation import EmailValidationResponse


class TestEmailValidation:
    def test_check(self, email_validation_sample, base_url, requests_mock, mocker):
        # Given
        service = EmailValidation(api_key="no-api-key")
        url = base_url.format(subdomain=EmailValidation._subdomain)
        requests_mock.get(url, json=email_validation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.check(email=email_validation_sample["email"])

        # Then
        assert isinstance(response, EmailValidationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=EmailValidationResponse,
            email=email_validation_sample["email"],
            auto_correct=False
        )

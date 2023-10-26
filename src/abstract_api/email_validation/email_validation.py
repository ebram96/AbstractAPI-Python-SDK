from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .email_validation_response import EmailValidationResponse


class EmailValidation(BaseService):
    """AbstractAPI email validation and verification service.

    Used to validate and verify an email address.

    Attributes:
        _subdomain: Email validation service subdomain.
    """
    _subdomain: str = "emailvalidation"

    def check(
        self,
        email: str,
        auto_correct: bool | None = False
    ) -> EmailValidationResponse:
        """Validates and verifies an email address.

        Args:
            email: An email address to be validated and verified.
            auto_correct: Whether the given email address should be
                autocorrected and returned in API response.

        Returns:
            EmailValidationResponse representing API call response.
        """
        response = self._service_request(
            email=email,
            auto_correct=auto_correct
        )

        try:
            email_validation_response = EmailValidationResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as EmailValidationResponse"
            ) from e

        return email_validation_response

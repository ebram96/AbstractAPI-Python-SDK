from ..bases import BaseService
from .email_validation_response import EmailValidationResponse


class EmailValidation(BaseService[EmailValidationResponse]):
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
        return self._service_request(
            _response_class=EmailValidationResponse,
            email=email,
            auto_correct=auto_correct
        )

from typing import Any

from _base_service import _BaseService


class EmailValidation(_BaseService):
    """AbstractAPI email validation and verification service

    Used to validate and verify and email address.

    Attributes:
        _subdomain: Email validation service subdomain.
    """
    _subdomain: str = "emailvalidation"

    def check(self, email: str, auto_correct: bool | None = False) -> dict[str, Any]:
        """Validates and verifies an email address.

        Args:
            email: An email address to be validated and verified.
            auto_correct: Whether the given email address should be
                autocorrected and returned in API response.

        Returns:
            A dict that contains the response to API call.
        """
        result = self._service_request(email=email, auto_correct=auto_correct)
        return result

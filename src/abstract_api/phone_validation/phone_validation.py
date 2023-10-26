from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .phone_validation_response import PhoneValidationResponse


class PhoneValidation(BaseService):
    """AbstractAPI phone validation and verification service.

    Used to validate and verify a phone number.

    Attributes:
        _subdomain: Phone validation service subdomain.
    """
    _subdomain: str = "phonevalidation"

    def check(self, phone: str) -> PhoneValidationResponse:
        """Validates and verifies a phone number.

        Args:
            phone: An phone number to be validated and verified.

        Returns:
            PhoneValidationResponse representing API call response.
        """
        response = self._service_request(phone=phone)

        # TODO: Move to parent
        try:
            phone_validation_response = PhoneValidationResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as PhoneValidationResponse"
            ) from e

        return phone_validation_response

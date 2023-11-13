from typing import ClassVar

from ..core.bases import BaseService
from .phone_validation_response import PhoneValidationResponse


class PhoneValidation(BaseService[PhoneValidationResponse]):
    """AbstractAPI phone validation and verification service.

    Used to validate and verify a phone number.

    Attributes:
        _subdomain: Phone validation service subdomain.
    """
    _subdomain = "phonevalidation"
    _service_name_env_var: ClassVar[str] = "PHONE_VALIDATION"

    def check(self, phone: str) -> PhoneValidationResponse:
        """Validates and verifies a phone number.

        Args:
            phone: An phone number to be validated and verified.

        Returns:
            PhoneValidationResponse representing API call response.
        """
        return self._service_request(
            _response_class=PhoneValidationResponse,
            phone=phone
        )

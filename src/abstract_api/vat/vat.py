from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .vat_validation_response import VATValidationResponse


class VAT(BaseService):
    """AbstractAPI VAT categories, validation, and calculation service.

    Used to validate and calculate VAT numbers and also to inquery about
    VAT categories.

    Attributes:
        _subdomain: VAT service subdomain.
    """
    _subdomain: str = "vat"

    @property
    def _service_url(self):
        """Builds and returns an API URL for a service using its subdomain.

        Returns:
            A str that can be used to make API calls to a service.
        """
        return super()._service_url + "validate"

    def check(self, vat_number: str) -> VATValidationResponse:
        """Validates a VAT number.

        Args:
            vat_number: The VAT number to validate.

        Returns:
            VATValidationResponse representing API call response.
        """
        response = self._service_request(vat_number=vat_number)

        try:
            vat_validation_response = VATValidationResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as VATValidationResponse"
            ) from e

        return vat_validation_response

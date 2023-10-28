from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .iban_validation_response import IBANValidationResponse


class IBANValidation(BaseService):
    """AbstractAPI IBAN validation and verification service.

    Used to validate and verify a IBAN number.

    Attributes:
        _subdomain: IBAN validation service subdomain.
    """
    _subdomain: str = "ibanvalidation"

    def check(self, iban: str) -> IBANValidationResponse:
        """Validates an IBAN.

        Args:
            iban: The IBAN to validate. Note that the API will accept white
                spaces, so BE71 0961 2345 6769 is considered as valid
                as BE71096123456769.

        Returns:
            IBANValidationResponse representing API call response.
        """
        response = self._service_request(iban=iban)

        # TODO: Move to parent
        try:
            iban_validation_response = IBANValidationResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as IBANValidationResponse"
            ) from e

        return iban_validation_response

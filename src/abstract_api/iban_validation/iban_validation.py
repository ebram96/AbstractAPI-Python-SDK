from ..core.bases import BaseService
from .iban_validation_response import IBANValidationResponse


class IBANValidation(BaseService[IBANValidationResponse]):
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
        return self._service_request(
            _response_class=IBANValidationResponse,
            iban=iban
        )

import requests

from ..core.bases import JSONResponse
from .response_fields import RESPONSE_FIELDS


class IBANValidationResponse(JSONResponse):
    """IBAN validation service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new IBANValidationResponse."""
        super().__init__(response, RESPONSE_FIELDS)

    @property
    def iban(self) -> str:
        """The IBAN submitted for validation."""
        return self._get_response_field("iban")

    @property
    def is_valid(self) -> bool:
        """Whether the IBAN submitted is valid."""
        return self._get_response_field("is_valid")

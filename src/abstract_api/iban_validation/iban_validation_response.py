from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields import RESPONSE_FIELDS


class IBANValidationResponse(JSONResponse):
    """IBAN validation service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new IBANValidationResponse."""
        super().__init__(response)
        self._response_fields = RESPONSE_FIELDS
        for field in RESPONSE_FIELDS:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field)
            # TODO: Move to parent class
            setattr(self, f"_{field}", value)

    @property
    def iban(self) -> str:
        """The IBAN submitted for validation."""
        return self._get_response_field("iban")

    @property
    def is_valid(self) -> bool:
        """Whether the IBAN submitted is valid."""
        return self._get_response_field("is_valid")

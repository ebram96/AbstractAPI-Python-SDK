from typing import TYPE_CHECKING

import requests.models

from abstract_api.bases import JSONResponse


class CompanyEnrichmentResponse(JSONResponse):
    """Company enrichment service response."""

    def __init__(
        self,
        response: requests.models.Response,
        response_fields: frozenset[str]
    ) -> None:
        """Initializes a new CompanyEnrichmentResponse."""
        super().__init__(response)
        self._response_fields = response_fields
        not_in_response = object()
        for field in response_fields:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                setattr(self, f"_{field}", value)

    @property
    def name(self) -> str | None:
        """The name of the company."""
        return self._get_response_field("name")

    @property
    def domain(self) -> str | None:
        """The domain the company website is hosted on."""
        return self._get_response_field("domain")

    @property
    def year_founded(self) -> int | None:
        """The year the company was founded."""
        return self._get_response_field("year_founded")

    @property
    def industry(self) -> str | None:
        """The industry the company is operating in."""
        return self._get_response_field("industry")

    @property
    def employees_count(self) -> str | None:
        """The approximate number of employees of the company."""
        return self._get_response_field("employees_count")

    @property
    def locality(self) -> str | None:
        """The city or region he company headquarter is based in."""
        return self._get_response_field("locality")

    @property
    def country(self) -> str | None:
        """The country the company is based in."""
        return self._get_response_field("country")

    @property
    def linkedin_url(self) -> str | None:
        """The LinkedIn URL of the company."""
        return self._get_response_field("linkedin_url")

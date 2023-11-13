from functools import cached_property

from ..core.bases import JSONResponse


class CompanyEnrichmentResponse(JSONResponse):
    """Company enrichment service response."""

    @cached_property
    def name(self) -> str | None:
        """The name of the company."""
        return self._get_response_field("name")

    @cached_property
    def domain(self) -> str | None:
        """The domain the company website is hosted on."""
        return self._get_response_field("domain")

    @cached_property
    def year_founded(self) -> int | None:
        """The year the company was founded."""
        return self._get_response_field("year_founded")

    @cached_property
    def industry(self) -> str | None:
        """The industry the company is operating in."""
        return self._get_response_field("industry")

    @cached_property
    def employees_count(self) -> str | None:
        """The approximate number of employees of the company."""
        return self._get_response_field("employees_count")

    @cached_property
    def locality(self) -> str | None:
        """The city or region the company headquarter is based in."""
        return self._get_response_field("locality")

    @cached_property
    def country(self) -> str | None:
        """The country the company is based in."""
        return self._get_response_field("country")

    @cached_property
    def linkedin_url(self) -> str | None:
        """The LinkedIn URL of the company."""
        return self._get_response_field("linkedin_url")

from typing import Iterable

from ..bases import BaseService
from ..mixins import ResponseFieldsMixin
from .company_enrichment_response import CompanyEnrichmentResponse


class CompanyEnrichment(
    ResponseFieldsMixin,
    BaseService[CompanyEnrichmentResponse]
):
    """AbstractAPI company enrichment service.

    Used to find a company's details using its domain.

    Attributes:
        _subdomain: Company enrichment service subdomain.
    """
    _subdomain: str = "companyenrichment"
    _response_fields = frozenset({
        "name",
        "domain",
        "year_founded",
        "industry",
        "employees_count",
        "locality",
        "country",
        "linkedin_url"
    })

    def check(
        self,
        domain: str,
        fields: Iterable[str] | None = None
    ) -> CompanyEnrichmentResponse:
        """Finds a company's details using its domain.

        Args:
            domain: The domain of the company you want to get data from.
            fields: Selected response fields.

        Returns:
            CompanyEnrichmentResponse representing API call response.
        """
        if fields:
            self._validate_response_fields(fields)
            response_fields = frozenset(fields)
        else:
            response_fields = self.response_fields

        return self._service_request(
            _response_class=CompanyEnrichmentResponse,
            _response_class_kwargs={"response_fields": response_fields},
            domain=domain,
            fields=self._response_fields_as_param(response_fields)
        )

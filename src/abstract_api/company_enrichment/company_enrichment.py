from typing import ClassVar, Iterable, Optional

from ..core.bases import BaseService
from ..core.mixins import ResponseFieldsMixin
from ._response_fields import RESPONSE_FIELDS
from .company_enrichment_response import CompanyEnrichmentResponse


class CompanyEnrichment(
    ResponseFieldsMixin,
    BaseService[CompanyEnrichmentResponse]
):
    """AbstractAPI company enrichment service.

    Used to find a company's details using its domain.

    Attributes:
        _subdomain: Company enrichment service subdomain.
        _response_fields: API response fields.
    """
    _subdomain = "companyenrichment"
    _response_fields = RESPONSE_FIELDS
    _service_name_env_var: ClassVar[str] = "COMPANY_ENRICHMENT"

    def check(
        self,
        domain: str,
        fields: Optional[Iterable[str]] = None
    ) -> CompanyEnrichmentResponse:
        """Finds a company's details using its domain.

        Args:
            domain: The domain of the company you want to get data for.
            fields: Selected response fields (optional).

        Returns:
            CompanyEnrichmentResponse representing API call response.
        """
        selected_fields = self._prepare_selected_fields(fields)

        return self._service_request(
            _response_class=CompanyEnrichmentResponse,
            _response_class_kwargs={"response_fields": selected_fields},
            domain=domain,
            fields=self._response_fields_as_param(selected_fields)
        )

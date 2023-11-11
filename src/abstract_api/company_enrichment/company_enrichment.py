from typing import Iterable

from abstract_api.bases import BaseService
from abstract_api.exceptions import ClientRequestError

from .company_enrichment_response import CompanyEnrichmentResponse
from .response_fields import RESPONSE_FIELDS


class CompanyEnrichment(BaseService[CompanyEnrichmentResponse]):
    """AbstractAPI company enrichment service.

    Used to find a company's details using its domain.

    Attributes:
        _subdomain: Company enrichment service subdomain.
    """
    _subdomain: str = "companyenrichment"

    def __init__(
        self,
        *,
        response_fields: Iterable[str] | None = None,
        **kwargs
    ) -> None:
        """Constructs a CompanyEnrichment.

        Args:
            response_fields: Selected response fields.
        """
        super().__init__(**kwargs)
        if response_fields is not None:
            self.response_fields = frozenset(response_fields)
        else:
            self.response_fields = RESPONSE_FIELDS

    @staticmethod
    def _validate_response_fields(response_fields: Iterable[str]) -> None:
        """Validates whether all the given fields are acceptable.

        Args:
            response_fields: Selected response fields.
        """
        for field in response_fields:
            if field not in RESPONSE_FIELDS:
                raise ClientRequestError(
                    f"Field '{field}' is not a valid response field for "
                    f"Company Enrichment service."
                )

    @property
    def response_fields(self) -> frozenset[str]:
        """Gets selected response fields."""
        if self._response_fields:
            return self._response_fields
        return RESPONSE_FIELDS

    @response_fields.setter
    def response_fields(self, fields: Iterable[str]) -> None:
        """Sets selected response fields."""
        self._validate_response_fields(fields)
        self._response_fields = frozenset(fields)

    @staticmethod
    def _response_fields_as_param(response_fields: Iterable[str]) -> str:
        """Builds 'fields' URL query parameter.

         Builds a string that contains selected response fields to be used
         as a URL query parameter.

        Args:
            response_fields: Selected response fields.

        Returns:
            Comma-separated string with all selected response fields.
        """
        return ",".join(response_fields)

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

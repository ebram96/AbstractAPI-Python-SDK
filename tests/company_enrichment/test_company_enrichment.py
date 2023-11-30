import pytest
import requests

from abstract_api import CompanyEnrichment
from abstract_api.company_enrichment import CompanyEnrichmentResponse


class TestCompanyEnrichment:
    """CompanyEnrichment service tests."""
    @pytest.fixture
    def service(self) -> CompanyEnrichment:
        return CompanyEnrichment(api_key="no-api-key")

    @pytest.fixture
    def domain(self):
        return "google.com"

    def test_check(
        self, service, domain, company_enrichment_sample, base_url, requests_mock
    ):
        url = base_url.format(subdomain=CompanyEnrichment._subdomain)
        requests_mock.get(url, json=company_enrichment_sample)

        response = service.check(domain=domain)

        assert response.meta.http_status == requests.codes.OK
        assert isinstance(response, CompanyEnrichmentResponse)
        for field in service.response_fields:
            assert company_enrichment_sample[field] == getattr(response, field)

    @pytest.mark.parametrize(
        "service", [
            CompanyEnrichment(api_key="no-api-key"),
            CompanyEnrichment(
                api_key="no-api-key",
                response_fields=["name", "domain", "country"]
            )
        ]
    )
    def test_check_with_response_fields(
        self, service, domain, company_enrichment_sample, base_url, requests_mock
    ):
        url = base_url.format(subdomain=CompanyEnrichment._subdomain)
        sample_for_fields = {
            "name": "Google",
            "domain": "google.com"
        }
        requests_mock.get(url, json=sample_for_fields)

        response = service.check(
            domain=domain,
            fields=list(sample_for_fields.keys())
        )

        assert response.meta.http_status == requests.codes.OK
        assert isinstance(response, CompanyEnrichmentResponse)
        assert response.name == sample_for_fields["name"]
        assert response.domain == sample_for_fields["domain"]
        for field in service.response_fields:
            if field in sample_for_fields:
                continue
            with pytest.raises(AttributeError):
                assert company_enrichment_sample[field] == getattr(response, field)

import pytest

from abstract_api import CompanyEnrichment
from abstract_api.company_enrichment import CompanyEnrichmentResponse


class TestCompanyEnrichment:
    """CompanyEnrichment service tests."""
    @pytest.fixture
    def service(self) -> CompanyEnrichment:
        return CompanyEnrichment(api_key="no-api-key")

    def test_check(
        self,
        service,
        company_enrichment_sample,
        base_url,
        requests_mock,
        mocker
    ):
        url = base_url.format(subdomain=CompanyEnrichment._subdomain)
        requests_mock.get(url, json=company_enrichment_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        response = service.check(domain=company_enrichment_sample["domain"])

        assert isinstance(response, CompanyEnrichmentResponse)
        for field in service.response_fields:
            assert company_enrichment_sample[field] == getattr(response, field)
        mocked__service_request.assert_called_once_with(
            _response_class=CompanyEnrichmentResponse,
            _response_class_kwargs={"response_fields": service.response_fields},
            domain=company_enrichment_sample["domain"],
            fields=service._response_fields_as_param(service.response_fields)
        )

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
        self,
        service,
        company_enrichment_sample,
        base_url,
        requests_mock,
        mocker
    ):
        url = base_url.format(subdomain=CompanyEnrichment._subdomain)
        sample_for_fields = {
            "name": "Google",
            "domain": "google.com"
        }
        selected_fields = service._prepare_selected_fields(sample_for_fields.keys())
        requests_mock.get(url, json=sample_for_fields)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        response = service.check(
            domain=company_enrichment_sample["domain"],
            fields=selected_fields
        )

        assert isinstance(response, CompanyEnrichmentResponse)
        assert response.name == sample_for_fields["name"]
        assert response.domain == sample_for_fields["domain"]
        for field in service.response_fields:
            if field in sample_for_fields:
                continue
            with pytest.raises(AttributeError):
                assert company_enrichment_sample[field] == getattr(response, field)
        mocked__service_request.assert_called_once_with(
            _response_class=CompanyEnrichmentResponse,
            _response_class_kwargs={"response_fields": selected_fields},
            domain=company_enrichment_sample["domain"],
            fields=service._response_fields_as_param(selected_fields)
        )

from abstract_api.company_enrichment import CompanyEnrichmentResponse
from abstract_api.company_enrichment.response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestCompanyEnrichmentResponse:
    def test_instance(self, company_enrichment_sample, mocker):
        response = generate_response(company_enrichment_sample)

        instance = CompanyEnrichmentResponse(response, RESPONSE_FIELDS)

        assert_response_fields(
            instance, RESPONSE_FIELDS, company_enrichment_sample, mocker
        )

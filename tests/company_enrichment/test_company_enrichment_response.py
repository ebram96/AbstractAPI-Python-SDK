from abstract_api.company_enrichment import CompanyEnrichmentResponse
from abstract_api.company_enrichment.response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_unchangeable_fields
from tests.utils import generate_response


class TestCompanyEnrichmentResponse:
    def test_instance(self, company_enrichment_sample, mocker):
        response = generate_response(company_enrichment_sample)

        instance = CompanyEnrichmentResponse(response, RESPONSE_FIELDS)

        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field in RESPONSE_FIELDS:
            assert getattr(instance, field) == company_enrichment_sample[field]
            mocked__get_response_field.assert_called_with(field)
        assert mocked__get_response_field.call_count == len(RESPONSE_FIELDS)
        assert_unchangeable_fields(instance, RESPONSE_FIELDS)

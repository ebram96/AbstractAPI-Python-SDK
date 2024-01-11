import pytest

from abstract_api import IPGeolocation
from abstract_api.ip_geolocation import IPGeolocationResponse
from abstract_api.ip_geolocation._response_fields import RESPONSE_FIELDS
from abstract_api.ip_geolocation.ip_geolocation_response import Timezone


class TestIPGeolocation:
    """IPGeolocation service tests."""
    @pytest.fixture
    def service(self) -> IPGeolocation:
        return IPGeolocation(api_key="no-api-key")

    @pytest.fixture
    def service_url(self, base_url, service):
        return base_url.format(subdomain=service._subdomain)

    def test_check(
        self,
        service,
        service_url,
        ip_geolocation_sample,
        requests_mock,
        mocker
    ):
        # Given
        requests_mock.get(service_url, json=ip_geolocation_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.check(ip=ip_geolocation_sample["ip_address"])

        # Then
        assert isinstance(response, IPGeolocationResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=IPGeolocationResponse,
            _response_class_kwargs={"response_fields": RESPONSE_FIELDS},
            ip_address=ip_geolocation_sample["ip_address"],
            fields=service._response_fields_as_param(RESPONSE_FIELDS)
        )

    @pytest.mark.parametrize(
        "service", [
            IPGeolocation(api_key="no-api-key"),
            IPGeolocation(
                api_key="no-api-key",
                response_fields=["ip_address", "city", "timezone"]
            )
        ]
    )
    def test_check_with_response_fields(
        self,
        service,
        service_url,
        ip_geolocation_sample,
        requests_mock,
        mocker
    ):
        # Given
        sample_for_fields = {
            "ip_address": ip_geolocation_sample["ip_address"],
            "city": ip_geolocation_sample["city"],
            "timezone": ip_geolocation_sample["timezone"]
        }
        selected_fields = service._prepare_selected_fields(sample_for_fields.keys())
        requests_mock.get(service_url, json=sample_for_fields)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.check(
            ip=ip_geolocation_sample["ip_address"],
            fields=selected_fields
        )

        # Then
        assert isinstance(response, IPGeolocationResponse)
        assert response.ip_address == sample_for_fields["ip_address"]
        assert response.city == sample_for_fields["city"]
        assert isinstance(response.timezone, Timezone)
        for field in service.response_fields:
            if field in sample_for_fields:
                continue
            with pytest.raises(AttributeError):
                assert ip_geolocation_sample[field] == getattr(response, field)
        mocked__service_request.assert_called_once_with(
            _response_class=IPGeolocationResponse,
            _response_class_kwargs={"response_fields": selected_fields},
            ip_address=ip_geolocation_sample["ip_address"],
            fields=service._response_fields_as_param(selected_fields)
        )

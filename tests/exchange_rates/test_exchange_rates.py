import pytest

from abstract_api import ExchangeRates
from abstract_api.core.validators import numerical
from abstract_api.exchange_rates import (
    ExchangeRatesConversionResponse,
    HistoricalExchangeRatesResponse,
    LiveExchangeRatesResponse
)


class TestExchangeRates:
    @pytest.fixture
    def service(self):
        return ExchangeRates(api_key="no-api-key")

    @pytest.fixture
    def service_url(self, base_url, service):
        return base_url.format(subdomain=service._subdomain)

    @pytest.mark.parametrize(
        ["target", "expected"],
        [
            [None, None],
            [["t1", "t2"], "t1,t2"]
        ]
    )
    def test__target_as_param(self, target, expected):
        # Then
        assert ExchangeRates._target_as_param(target) == expected

    def test_live(
        self,
        service,
        service_url,
        exchange_rates_live_sample,
        mocker,
        requests_mock
    ):
        # Given
        base = exchange_rates_live_sample["base"]
        target = None
        action = "live"
        requests_mock.get(service_url + action, json=exchange_rates_live_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.live(base, target)

        # Then
        assert isinstance(response, LiveExchangeRatesResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=LiveExchangeRatesResponse,
            _action=action,
            base=base,
            target=service._target_as_param(target),
        )

    def test_convert(
        self,
        service,
        service_url,
        exchange_rates_conversion_sample,
        mocker,
        requests_mock
    ):
        # Given
        base = exchange_rates_conversion_sample["base"]
        target = exchange_rates_conversion_sample["target"]
        base_amount = exchange_rates_conversion_sample["base_amount"]
        action = "convert"
        requests_mock.get(service_url + action, json=exchange_rates_conversion_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked_greater_or_equal = mocker.patch.object(
            numerical, "greater_or_equal", wraps=numerical.greater_or_equal
        )

        # When
        response = service.convert(base, target, base_amount=base_amount)

        # Then
        assert isinstance(response, ExchangeRatesConversionResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=ExchangeRatesConversionResponse,
            _response_class_kwargs={"date_included_in_request": False},
            _action=action,
            base=base,
            target=target,
            date=None,
            base_amount=base_amount
        )
        mocked_greater_or_equal.assert_called_once_with(
            "base_amount", base_amount, 0
        )

    def test_historical(
        self,
        service,
        service_url,
        exchange_rates_historical_sample,
        mocker,
        requests_mock
    ):
        # Given
        base = exchange_rates_historical_sample["base"]
        target = None
        date = exchange_rates_historical_sample["date"]
        action = "historical"
        requests_mock.get(service_url + action, json=exchange_rates_historical_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )

        # When
        response = service.historical(base, date)

        # Then
        assert isinstance(response, HistoricalExchangeRatesResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=HistoricalExchangeRatesResponse,
            _action=action,
            base=base,
            target=service._target_as_param(target),
            date=date
        )

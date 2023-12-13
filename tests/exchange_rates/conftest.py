import pytest


@pytest.fixture
def exchange_rates_historical_sample():
    return {
        "base": "USD",
        "date": "2023-12-09",
        "exchange_rates": {
            "EUR": 0.927902,
            "JPY": 144.3166,
            "BGN": 1.814791,
            "CZK": 22.598126,
            "DKK": 6.918252,
            "GBP": 0.795119,
            "HUF": 354.365779,
            "PLN": 4.019486,
            "RON": 4.610096,
            "SEK": 10.427763,
            "CHF": 0.875754,
            "ISK": 139.278092,
            "NOK": 10.881507,
            "TRY": 28.982091,
            "AUD": 1.514986,
            "BRL": 4.911664,
            "CAD": 1.357242,
            "CNY": 7.161455,
            "HKD": 7.812007,
            "IDR": 15513.603044,
            "ILS": 3.709938,
            "INR": 83.406792,
            "KRW": 1310.967802,
            "MXN": 17.437413,
            "MYR": 4.664471,
            "NZD": 1.626798,
            "PHP": 55.449569,
            "SGD": 1.338591,
            "THB": 35.350283,
            "ZAR": 18.897374
        }
    }


@pytest.fixture
def exchange_rates_conversion_sample():
    return {
      "base": "USD",
      "target": "EUR",
      "base_amount": 1,
      "converted_amount": 0.925583,
      "exchange_rate": 0.925583,
      "last_updated": 1702300500
    }

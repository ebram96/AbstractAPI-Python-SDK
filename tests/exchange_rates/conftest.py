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


@pytest.fixture
def exchange_rates_live_sample():
    return {
        "base": "USD",
        "last_updated": 1702425599,
        "exchange_rates": {
            "EUR": 0.925583,
            "JPY": 145.168456,
            "BGN": 1.810255,
            "CZK": 22.60274,
            "DKK": 6.901981,
            "GBP": 0.795335,
            "HUF": 353.387634,
            "PLN": 4.016383,
            "RON": 4.60311,
            "SEK": 10.441966,
            "CHF": 0.874028,
            "ISK": 139.855609,
            "NOK": 10.901518,
            "HRK": 7.06591,
            "RUB": 104.99999999999999,
            "TRY": 29.041559,
            "AUD": 1.517771,
            "BRL": 4.935857,
            "CAD": 1.356535,
            "CNY": 7.168364,
            "HKD": 7.809793,
            "IDR": 15582.247316,
            "ILS": 3.706405,
            "INR": 83.373288,
            "KRW": 1309.894484,
            "MXN": 17.347186,
            "MYR": 4.684469,
            "NZD": 1.626527,
            "PHP": 55.630322,
            "SGD": 1.340152,
            "THB": 35.67475,
            "ZAR": 18.909385,
            "ARS": 75.269373,
            "DZD": 124.445887,
            "MAD": 8.83269,
            "TWD": 27.466513,
            "BTC": 0.000024,
            "ETH": 0.000453,
            "BNB": 0.003919,
            "DOGE": 10.749394,
            "XRP": 1.617959,
            "BCH": 0.004346,
            "LTC": 0.013847
        }
    }

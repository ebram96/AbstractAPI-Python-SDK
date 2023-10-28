from typing import Final

from .avatars import Avatars
from .email_validation import EmailValidation
from .exchange_rates import ExchangeRates
from .holidays import Holidays
from .iban_validation import IBANValidation
from .ip_geolocation import IPGeolocation
from .phone_validation import PhoneValidation
from .vat import VAT

__all__: Final[list[str]] = [
    "Avatars",
    "EmailValidation",
    "ExchangeRates",
    "Holidays",
    "IBANValidation",
    "IPGeolocation",
    "PhoneValidation",
    "VAT"
]

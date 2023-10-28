from typing import Final

from .avatars import Avatars
from .email_validation import EmailValidation
from .iban_validation import IBANValidation
from .ip_geolocation import IPGeolocation
from .phone_validation import PhoneValidation
from .vat import VAT

__all__: Final[list[str]] = [
    "Avatars",
    "EmailValidation",
    "IBANValidation",
    "IPGeolocation",
    "PhoneValidation",
    "VAT"
]

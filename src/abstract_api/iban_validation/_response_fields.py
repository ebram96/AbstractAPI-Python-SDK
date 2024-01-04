"""Response fields of IBAN validation service endpoint."""


RESPONSE_FIELDS: frozenset[str] = frozenset({
    "iban",
    "is_valid"
})

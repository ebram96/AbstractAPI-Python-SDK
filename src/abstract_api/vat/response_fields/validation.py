"""Response fields of phone validation service endpoint."""


VALIDATION_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "vat_number",
    "valid",
    "company",
    "country"
})

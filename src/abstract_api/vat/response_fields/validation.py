"""Response fields of VAT validation service endpoint."""


VALIDATION_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "vat_number",
    "valid",
    "company",
    "country"
})

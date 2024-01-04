"""Response fields of VAT calculation service endpoint."""


CALCULATION_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "amount_excluding_vat",
    "amount_including_vat",
    "vat_amount",
    "vat_category",
    "vat_rate",
    "country"
})

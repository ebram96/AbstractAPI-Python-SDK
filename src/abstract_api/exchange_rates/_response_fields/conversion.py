"""Response fields of exchange rates conversion service endpoint."""


CONVERSION_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "base",
    "target",
    "date",
    "base_amount",
    "converted_amount",
    "exchange_rate",
    "last_updated"
})

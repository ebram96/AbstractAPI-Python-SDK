"""Response fields of historical exchange rates service endpoint."""


HISTORICAL_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "base",
    "date",
    "exchange_rates"
})

"""Response fields of Live exchange rates service endpoint."""


LIVE_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "base",
    "last_updated",
    "exchange_rates"
})

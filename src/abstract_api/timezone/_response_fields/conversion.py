"""Response fields of timezone conversion service endpoint."""


CONVERSION_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "base_location",
    "target_location"
})

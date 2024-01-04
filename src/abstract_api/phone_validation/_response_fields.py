"""Response fields of phone validation service endpoint."""


RESPONSE_FIELDS: frozenset[str] = frozenset({
    "phone",
    "valid",
    "format",
    "country",
    "location",
    "type",
    "carrier"
})

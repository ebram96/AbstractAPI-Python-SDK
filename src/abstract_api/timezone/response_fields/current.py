"""Response fields of current timezone service endpoint."""


CURRENT_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "datetime",
    "timezone_name",
    "timezone_location",
    "timezone_abbreviation",
    "gmt_offset",
    "is_dst",
    "requested_location",
    "latitude",
    "longitude"
})

"""Response fields of IP geolocation service endpoint."""


ACCEPTABLE_FIELDS: frozenset[str] = frozenset({
    "ip_address",
    "city",
    "city_geoname_id",
    "region",
    "region_iso_code",
    "region_geoname_id",
    "postal_code",
    "country",
    "country_code",
    "country_geoname_id",
    "country_is_eu",
    "continent",
    "continent_code",
    "continent_geoname_id",
    "longitude",
    "latitude",
    "security",
    "timezone",
    "flag",
    "currency",
    "connection"
})

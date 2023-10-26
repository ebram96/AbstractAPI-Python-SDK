from typing import Type

import requests.models

from abstract_api.bases import JSONResponse


class Security:
    """Security entity in IP Geolocation response."""

    def __init__(self, is_vpn: bool) -> None:
        """Initializes a new Security."""
        self._is_vpn = is_vpn

    # TODO: type hint
    @property
    def is_vpn(self) -> bool | None:
        """Whether the IP address is using from a VPN or using a proxy."""
        return self._is_vpn


class Timezone:
    """Timezone entity in IP Geolocation response."""

    def __init__(
        self,
        name: str,
        abbreviation: str,
        gmt_offset: int,
        current_time: str,
        is_dst: bool
    ):
        """Initializes a new Timezone."""
        self._name = name
        self._abbreviation = abbreviation
        self._gmt_offset = gmt_offset
        self._current_time = current_time
        self._is_dst = is_dst

    @property
    def name(self) -> str | None:
        """Timezone’s name from the IANA Time Zone Database."""
        return self._name

    @property
    def abbreviation(self) -> str | None:
        """Timezone’s abbreviation, also from the IANA Time Zone Database."""
        return self._abbreviation

    @property
    def gmt_offset(self) -> int | None:
        """Timezone’s offset from Greenwich Mean Time (GMT)."""
        return self._gmt_offset

    @property
    def current_time(self) -> str | None:
        """Current time in the local time zone."""
        return self._current_time

    @property
    def is_dst(self) -> bool | None:
        """True if the location is currently in Daylight Savings Time (DST)."""
        return self._is_dst


class Flag:
    """Flag entity in IP Geolocation response."""

    def __init__(self, emoji: str, unicode: str, png: str, svg: str) -> None:
        """Initializes a new Flag."""
        self._emoji = emoji
        self._unicode = unicode
        self._png = png
        self._svg = svg

    @property
    def emoji(self) -> str | None:
        """Country’s flag as an emoji."""
        return self._emoji

    @property
    def unicode(self) -> str | None:
        """Country’s flag in unicode."""
        return self._unicode

    @property
    def png(self) -> str | None:
        """Link to a hosted version of the country’s flag in PNG format."""
        return self._png

    @property
    def svg(self) -> str | None:
        """Link to a hosted version of the country’s flag in SVG format."""
        return self._svg


class Currency:
    """Currency entity in IP Geolocation response."""

    def __init__(self, currency_name: str, currency_code: str) -> None:
        """Initializes a new Currency."""
        self._currency_name = currency_name
        self._currency_code = currency_code

    @property
    def currency_name(self) -> str | None:
        """The currency’s name."""
        return self._currency_name

    @property
    def currency_code(self) -> str | None:
        """The currency’s code in ISO 4217 format."""
        return self._currency_code


class Connection:
    """Connection entity in IP Geolocation response."""

    def __init__(
        self,
        autonomous_system_number: int,
        autonomous_system_organization: str,
        connection_type: str,
        isp_name: str,
        organization_name: str
    ):
        """Initializes a new Connection."""
        self._autonomous_system_number = autonomous_system_number
        self._autonomous_system_organization = autonomous_system_organization
        self._connection_type = connection_type
        self._isp_name = isp_name
        self._organization_name = organization_name

    @property
    def autonomous_system_number(self) -> int | None:
        """Autonomous System number."""
        return self._autonomous_system_number

    @property
    def autonomous_system_organization(self) -> str | None:
        """Autonomous System Organization name."""
        return self._autonomous_system_organization

    @property
    def connection_type(self) -> str | None:
        """Network connection type: Dialup, Cable/DSL, Cellular, Corporate."""
        return self._connection_type

    @property
    def isp_name(self) -> str | None:
        """Internet Service Provider (ISP) name."""
        return self._isp_name

    @property
    def organization_name(self) -> str | None:
        """Organization name."""
        return self._organization_name


class IPGeolocationResponse(JSONResponse):
    """IP Geolocation service response."""
    _nested_entities: dict[str, Type] = {
        "security": Security,
        "timezone": Timezone,
        "flag": Flag,
        "currency": Currency,
        "connection": Connection
    }

    def __init__(
        self,
        response: requests.models.Response,
        response_fields: frozenset[str]
    ) -> None:
        """Initializes a new IPGeolocationResponse."""
        super().__init__(response)
        self._response_fields = response_fields
        not_in_response = object()
        for field in response_fields:
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                setattr(
                    self,
                    f"_{field}",
                    value if field not in self._nested_entities
                    else self._nested_entities[field](**value)
                )

    @property
    def ip_address(self) -> str | None:
        """The IP address submitted for geolocation."""
        return self._get_response_field("ip_address")

    @property
    def city(self) -> str | None:
        """City’s name."""
        return self._get_response_field("city")

    @property
    def city_geoname_id(self) -> int | None:
        """City’s geoname ID."""
        return self._get_response_field("city_geoname_id")

    @property
    def region(self) -> str | None:
        """State or province in which the city is located."""
        return self._get_response_field("region")

    @property
    def region_iso_code(self) -> str | None:
        """State or province’s ISO 3166-2 code."""
        return self._get_response_field("region_iso_code")

    @property
    def region_geoname_id(self) -> int | None:
        """State or province’s geoname ID."""
        return self._get_response_field("region_geoname_id")

    @property
    def postal_code(self) -> str | None:
        """ZIP or postal code."""
        return self._get_response_field("postal_code")

    @property
    def country(self) -> str | None:
        """Country’s name."""
        return self._get_response_field("country")

    @property
    def country_code(self) -> str | None:
        """Country’s ISO 3166-1 alpha-2 code."""
        return self._get_response_field("country_code")

    @property
    def country_geoname_id(self) -> int | None:
        """Country’s geoname ID."""
        return self._get_response_field("country_geoname_id")

    @property
    def country_is_eu(self) -> bool | None:
        """True if the country is in the EU, false if it is not."""
        return self._get_response_field("country_is_eu")

    @property
    def continent(self) -> str | None:
        """Continent’s name."""
        return self._get_response_field("continent")

    @property
    def continent_code(self) -> str | None:
        """2 letter continent code: AF, AS, EU, NA, OC, SA, AN."""
        return self._get_response_field("continent_code")

    @property
    def continent_geoname_id(self) -> int | None:
        """Continent’s geoname ID."""
        return self._get_response_field("continent_geoname_id")

    @property
    def longitude(self) -> float | None:
        """Decimal of the longitude."""
        return self._get_response_field("longitude")

    @property
    def latitude(self) -> float | None:
        """Decimal of the latitude."""
        return self._get_response_field("latitude")

    @property
    def security(self) -> Security | None:
        """Whether the IP address is using from a VPN or using a proxy."""
        return self._get_response_field("security")

    @property
    def timezone(self) -> Timezone | None:
        """Timezone details."""
        return self._get_response_field("timezone")

    @property
    def flag(self) -> Flag | None:
        """Flag details."""
        return self._get_response_field("flag")

    @property
    def currency(self) -> Currency | None:
        """Currency details."""
        return self._get_response_field("currency")

    @property
    def connection(self) -> Connection | None:
        """Connection details."""
        return self._get_response_field("connection")

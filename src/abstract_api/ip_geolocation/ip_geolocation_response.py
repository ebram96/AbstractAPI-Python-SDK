from functools import cached_property
from typing import Optional

from ..core.bases import JSONResponse
from ..core.mixins import NestedEntitiesMixin


class Security:
    """Security entity in IP Geolocation response."""

    def __init__(self, is_vpn: bool) -> None:
        """Initializes a new Security."""
        self._is_vpn = is_vpn

    @property
    def is_vpn(self) -> Optional[bool]:
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
    ) -> None:
        """Initializes a new Timezone."""
        self._name = name
        self._abbreviation = abbreviation
        self._gmt_offset = gmt_offset
        self._current_time = current_time
        self._is_dst = is_dst

    @property
    def name(self) -> Optional[str]:
        """Timezone's name from the IANA Time Zone Database."""
        return self._name

    @property
    def abbreviation(self) -> Optional[str]:
        """Timezone's abbreviation, also from the IANA Time Zone Database."""
        return self._abbreviation

    @property
    def gmt_offset(self) -> Optional[int]:
        """Timezone's offset from Greenwich Mean Time (GMT)."""
        return self._gmt_offset

    @property
    def current_time(self) -> Optional[str]:
        """Current time in the local time zone."""
        return self._current_time

    @property
    def is_dst(self) -> Optional[bool]:
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
    def emoji(self) -> Optional[str]:
        """Country's flag as an emoji."""
        return self._emoji

    @property
    def unicode(self) -> Optional[str]:
        """Country's flag in unicode."""
        return self._unicode

    @property
    def png(self) -> Optional[str]:
        """Link to a hosted version of the country's flag in PNG format."""
        return self._png

    @property
    def svg(self) -> Optional[str]:
        """Link to a hosted version of the country's flag in SVG format."""
        return self._svg


class Currency:
    """Currency entity in IP Geolocation response."""

    def __init__(self, currency_name: str, currency_code: str) -> None:
        """Initializes a new Currency."""
        self._currency_name = currency_name
        self._currency_code = currency_code

    @property
    def currency_name(self) -> Optional[str]:
        """The currency's name."""
        return self._currency_name

    @property
    def currency_code(self) -> Optional[str]:
        """The currency's code in ISO 4217 format."""
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
    ) -> None:
        """Initializes a new Connection."""
        self._autonomous_system_number = autonomous_system_number
        self._autonomous_system_organization = autonomous_system_organization
        self._connection_type = connection_type
        self._isp_name = isp_name
        self._organization_name = organization_name

    @property
    def autonomous_system_number(self) -> Optional[int]:
        """Autonomous System number."""
        return self._autonomous_system_number

    @property
    def autonomous_system_organization(self) -> Optional[str]:
        """Autonomous System Organization name."""
        return self._autonomous_system_organization

    @property
    def connection_type(self) -> Optional[str]:
        """Network connection type: Dialup, Cable/DSL, Cellular, Corporate."""
        return self._connection_type

    @property
    def isp_name(self) -> Optional[str]:
        """Internet Service Provider (ISP) name."""
        return self._isp_name

    @property
    def organization_name(self) -> Optional[str]:
        """Organization name."""
        return self._organization_name


class IPGeolocationResponse(NestedEntitiesMixin, JSONResponse):
    """IP Geolocation service response."""
    _nested_entities = {
        "security": Security,
        "timezone": Timezone,
        "flag": Flag,
        "currency": Currency,
        "connection": Connection
    }

    @cached_property
    def ip_address(self) -> Optional[str]:
        """The IP address submitted for geolocation."""
        return self._get_response_field("ip_address")

    @cached_property
    def city(self) -> Optional[str]:
        """City's name."""
        return self._get_response_field("city")

    @cached_property
    def city_geoname_id(self) -> Optional[int]:
        """City's geoname ID."""
        return self._get_response_field("city_geoname_id")

    @cached_property
    def region(self) -> Optional[str]:
        """State or province in which the city is located."""
        return self._get_response_field("region")

    @cached_property
    def region_iso_code(self) -> Optional[str]:
        """State or province's ISO 3166-2 code."""
        return self._get_response_field("region_iso_code")

    @cached_property
    def region_geoname_id(self) -> Optional[int]:
        """State or province's geoname ID."""
        return self._get_response_field("region_geoname_id")

    @cached_property
    def postal_code(self) -> Optional[str]:
        """ZIP or postal code."""
        return self._get_response_field("postal_code")

    @cached_property
    def country(self) -> Optional[str]:
        """Country's name."""
        return self._get_response_field("country")

    @cached_property
    def country_code(self) -> Optional[str]:
        """Country's ISO 3166-1 alpha-2 code."""
        return self._get_response_field("country_code")

    @cached_property
    def country_geoname_id(self) -> Optional[int]:
        """Country's geoname ID."""
        return self._get_response_field("country_geoname_id")

    @cached_property
    def country_is_eu(self) -> Optional[bool]:
        """True if the country is in the EU, false if it is not."""
        return self._get_response_field("country_is_eu")

    @cached_property
    def continent(self) -> Optional[str]:
        """Continent's name."""
        return self._get_response_field("continent")

    @cached_property
    def continent_code(self) -> Optional[str]:
        """2 letter continent code: AF, AS, EU, NA, OC, SA, AN."""
        return self._get_response_field("continent_code")

    @cached_property
    def continent_geoname_id(self) -> Optional[int]:
        """Continent's geoname ID."""
        return self._get_response_field("continent_geoname_id")

    @cached_property
    def longitude(self) -> Optional[float]:
        """Decimal of the longitude."""
        return self._get_response_field("longitude")

    @cached_property
    def latitude(self) -> Optional[float]:
        """Decimal of the latitude."""
        return self._get_response_field("latitude")

    @cached_property
    def security(self) -> Optional[Security]:
        """Whether the IP address is using from a VPN or using a proxy."""
        return self._get_response_field("security")

    @cached_property
    def timezone(self) -> Optional[Timezone]:
        """Timezone details."""
        return self._get_response_field("timezone")

    @cached_property
    def flag(self) -> Optional[Flag]:
        """Flag details."""
        return self._get_response_field("flag")

    @cached_property
    def currency(self) -> Optional[Currency]:
        """Currency details."""
        return self._get_response_field("currency")

    @cached_property
    def connection(self) -> Optional[Connection]:
        """Connection details."""
        return self._get_response_field("connection")

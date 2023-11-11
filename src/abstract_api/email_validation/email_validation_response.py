from typing import Any, ClassVar

import requests

from ..bases import JSONResponse
from .response_fields import RESPONSE_FIELDS


class EmailValidationResponse(JSONResponse):
    """Email validation service response."""

    _complex_bool_fields: ClassVar[frozenset[str]] = frozenset({
        "is_valid_format",
        "is_free_email",
        "is_disposable_email",
        "is_role_email",
        "is_catchall_email",
        "is_mx_found",
        "is_smtp_valid"
    })

    def _init_response_field(self, field: str, value: Any) -> None:
        """TODO."""
        setattr(
            self,
            f"_{field}",
            value if field not in self._complex_bool_fields
            else value["value"]
        )

    def __init__(
        self,
        response: requests.models.Response
    ) -> None:
        """Initializes a new EmailValidationResponse."""
        super().__init__(response, RESPONSE_FIELDS)

    @property
    def email(self) -> str | None:
        """The value for “email” that was entered into the request."""
        return self._get_response_field("email")

    @property
    def autocorrect(self) -> str | None:
        """The auto corrected email.

        If a typo has been detected then a suggestion of the correct
        email (e.g., johnsmith@gmial.com => johnsmith@gmail.com) is returned.
        If no typo is detected then this is empty.
        Auto correction doesn't happen if 'auto_correct' parameter was set
        to false.
        """
        return self._get_response_field("autocorrect")

    @property
    def deliverability(self) -> str | None:
        """Abstract’s evaluation of the deliverability of the email.

        Possible values are: DELIVERABLE, UNDELIVERABLE, and UNKNOWN.
        """
        return self._get_response_field("deliverability")

    @property
    def quality_score(self) -> float | None:
        """Decimal score for quality and deliverability of the submitted email.

        It is between 0.01 and 0.99 reflecting AbstractAPI’s confidence in the
        quality and deliverability of the submitted email.
        """
        return self._get_response_field("quality_score")

    @property
    def is_valid_format(self) -> bool | None:
        """Whether the email follows the format of “address @ domain . TLD”.

        If any of those elements are missing or if they contain extra or
        incorrect special characters, then it returns false.
        """
        return self._get_response_field("is_valid_format")

    @property
    def is_free_email(self) -> bool | None:
        """Whether email’s domain is a free to use email.

        True if email domain is found among Abstract’s list of free email
        providers (Gmail, Yahoo, etc.).
        """
        return self._get_response_field("is_free_email")

    @property
    def is_disposable_email(self) -> bool | None:
        """Whether the email is disposable.

        True if the email’s domain is found among Abstract’s list of disposable
        email providers (e.g., Mailinator, Yopmail, etc.).
        """
        return self._get_response_field("is_disposable_email")

    @property
    def is_role_email(self) -> bool | None:
        """Whether the email represents a role and not an individual.

        True if the email’s local part (e.g., the “to” part) appears to be for
        a role rather than individual.
        Examples of this include “team@”, “sales@”, “info@”, etc.
        """
        return self._get_response_field("is_role_email")

    @property
    def is_catchall_email(self) -> bool | None:
        """Whether the domain is configured to catch all email."""
        return self._get_response_field("is_catchall_email")

    @property
    def is_mx_found(self) -> bool | None:
        """Whether MX Records for the domain can be found.

        Only available on AbstractAPI paid plans. Will return null and UNKNOWN
        on free plans.
        """
        return self._get_response_field("is_mx_found")

    @property
    def is_smtp_valid(self) -> bool | None:
        """Whether the SMTP check of the email was successful.

        If the check fails, but other checks are valid, the email will be
        returned as UNKNOWN. AbstractAPI recommends not blocking signups or
        form submissions when an SMTP check fails.
        """
        return self._get_response_field("is_smtp_valid")

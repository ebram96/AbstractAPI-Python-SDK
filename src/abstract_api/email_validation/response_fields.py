"""Response fields of Email validation service endpoint."""


RESPONSE_FIELDS: frozenset[str] = frozenset({
    "email",
    "autocorrect",
    "deliverability",
    "quality_score",
    "is_valid_format",
    "is_free_email",
    "is_disposable_email",
    "is_role_email",
    "is_catchall_email",
    "is_mx_found",
    "is_smtp_valid"
})

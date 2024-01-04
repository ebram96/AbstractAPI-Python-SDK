"""Response fields of company enrichment service endpoint."""


RESPONSE_FIELDS: frozenset[str] = frozenset({
    "name",
    "domain",
    "year_founded",
    "industry",
    "employees_count",
    "locality",
    "country",
    "linkedin_url"
})

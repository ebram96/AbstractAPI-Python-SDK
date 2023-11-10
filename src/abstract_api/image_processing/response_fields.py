"""Response fields of image processing service endpoints."""


RESPONSE_FIELDS: frozenset[str] = frozenset({
    "original_size",
    "original_height",
    "original_width",
    "final_size",
    "bytes_saved",
    "final_height",
    "final_width",
    "url"
})

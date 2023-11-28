from io import BytesIO

import pytest

from abstract_api.core.bases.json_response import JSONResponseMeta


class TestJSONResponseMeta:
    @pytest.mark.parametrize(
        "content_response",
        [dict(raw=BytesIO(b'{"key":"value"}'))],
        indirect=["content_response"]
    )
    def test_initialization(self, content_response):
        assert JSONResponseMeta(content_response).body_json == content_response.json()

    def test_initialization_with_no_content(self, blank_response):
        assert JSONResponseMeta(blank_response).body_json is None

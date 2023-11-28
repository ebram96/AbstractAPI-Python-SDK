from io import BytesIO

import requests

from abstract_api.core.bases import FileResponse
from abstract_api.core.bases.file_response import FileResponseMeta


class TestFileResponse:
    def test_instance(self):
        response = requests.Response()
        response.raw = BytesIO(b'some-raw-response-content')

        instance = FileResponse(response)

        assert instance.content == response.content
        assert isinstance(instance.meta, FileResponseMeta)

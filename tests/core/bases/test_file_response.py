from abstract_api.core.bases import FileResponse
from abstract_api.core.bases.file_response import FileResponseMeta


class TestFileResponse:
    def test_initialization(self, content_response):
        instance = FileResponse(content_response)

        assert instance.content == content_response.content
        assert isinstance(instance.meta, FileResponseMeta)

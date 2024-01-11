from abstract_api.core.bases._base_response import (
    BaseResponse,
    BaseResponseMeta
)


class TestBaseResponseMeta:
    def test_instance(self, content_response):
        # When
        meta = BaseResponseMeta(content_response)

        # Then
        assert meta.http_status == content_response.status_code
        assert meta.body == content_response.content


class TestBaseResponse:
    def test_instance(self, blank_response, mocker):
        # Given
        mocker.patch.object(
            BaseResponse, "_meta_class", BaseResponseMeta, create=True
        )

        # When
        base_response = BaseResponse(blank_response)

        # Then
        assert isinstance(base_response.meta, BaseResponseMeta)

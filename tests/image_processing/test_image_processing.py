import json
from io import BytesIO

import pytest

from abstract_api import ImageProcessing
from abstract_api.core.validators import numerical
from abstract_api.image_processing import ImageProcessingResponse


class TestImageProcessing:
    @pytest.fixture
    def service(self):
        return ImageProcessing(api_key="no-api-key")

    @pytest.fixture
    def service_url(self, base_url, service):
        return base_url.format(subdomain=service._subdomain)

    @pytest.fixture
    def image_file(self):
        return BytesIO(b"some-image-content")

    @pytest.fixture
    def image_url(self):
        return "https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png"

    def test_check(
        self,
        service,
        service_url,
        image_file,
        image_processing_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "upload/"
        requests_mock.post(service_url + action, json=image_processing_sample)
        mocked__process = mocker.patch.object(
            service, "_process", wraps=service._process
        )

        # When
        response = service.upload(image_file)

        # Then
        assert isinstance(response, ImageProcessingResponse)
        mocked__process.assert_called_once_with(
            image=image_file,
            lossy=None,
            quality=None,
            resize=None
        )

    def test_url(
        self,
        service,
        service_url,
        image_url,
        image_processing_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "url/"
        requests_mock.post(service_url + action, json=image_processing_sample)
        mocked__process = mocker.patch.object(
            service, "_process", wraps=service._process
        )

        # When
        response = service.url(image_url)

        # Then
        assert isinstance(response, ImageProcessingResponse)
        mocked__process.assert_called_once_with(
            url=image_url,
            lossy=None,
            quality=None,
            resize=None
        )

    def test__process_no_url_no_image(self, service):
        # Then
        with pytest.raises(ValueError):
            # When
            service._process()

    def test__process_for_image(
        self,
        service,
        service_url,
        image_file,
        image_processing_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "upload/"
        requests_mock.post(service_url + action, json=image_processing_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked_between = mocker.patch.object(
            numerical, "between", wraps=numerical.between
        )

        # When
        response = service._process(image=image_file)

        # Then
        assert isinstance(response, ImageProcessingResponse)
        mocked_between.assert_called_once_with("quality", None, 0, 100)
        mocked__service_request.assert_called_once_with(
            _response_class=ImageProcessingResponse,
            _action=action,
            _method="POST",
            _files={
                "image": image_file,
                "data": (None, json.dumps({"api_key": service._api_key}))
            }
        )

    def test__process_for_url(
        self,
        service,
        service_url,
        image_url,
        image_processing_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "url/"
        requests_mock.post(service_url + action, json=image_processing_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked_between = mocker.patch.object(
            numerical, "between", wraps=numerical.between
        )

        # When
        response = service.url(image_url)

        # Then
        assert isinstance(response, ImageProcessingResponse)
        mocked_between.assert_called_once_with("quality", None, 0, 100)
        mocked__service_request.assert_called_once_with(
            _response_class=ImageProcessingResponse,
            _action=action,
            _method="POST",
            _body={
                "api_key": service._api_key,
                "url": image_url
            }
        )

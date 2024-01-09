from abstract_api.image_processing import ImageProcessingResponse
from abstract_api.image_processing._response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestImageProcessingResponse:
    def test_instance(self, image_processing_sample, mocker):
        # Given
        response = generate_response(image_processing_sample)

        # When
        instance = ImageProcessingResponse(response)

        # Then
        assert_response_fields(
            instance, RESPONSE_FIELDS, image_processing_sample, mocker
        )

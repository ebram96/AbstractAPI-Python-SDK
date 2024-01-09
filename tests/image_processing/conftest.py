import pytest


@pytest.fixture
def image_processing_sample():
    return {
        'original_size': 15829,
        'original_height': 183,
        'original_width': 200,
        'final_size': 6647,
        'bytes_saved': 9182,
        'final_height': 100,
        'final_width': 109,
        'url': 'https://abstractapi-images.s3.amazonaws.com/2d51df80db614b2c84a920e455751c9c_Wikipedia-logo-v2.png'
    }

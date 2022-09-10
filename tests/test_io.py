import pytest
from src.ervision.io import io
import numpy as np

@pytest.fixture
def image_files():
    data = {
        'jpg': {
            '1c': 'assets/1c_jpg_file.jpg',
            '3c': 'assets/3c_jpg_file.jpg',
        },
        'png': {
            '3c': 'assets/3c_png_file.png',
            '4c': 'assets/4c_png_file.png',
        }
    }
    return data


def test_imread_opencv_png_rgb(image_files):
    jpg1c = image_files['png']['3c']
    img = io.imread(jpg1c, engine=io.OPENCV_ENGINE)
    assert type(img) == np.ndarray
    assert len(img.shape) == 3
    assert img.shape[2] == 3

def test_imread_opencv_jpg_rgb(image_files):
    jpg1c = image_files['jpg']['3c']
    img = io.imread(jpg1c, engine=io.OPENCV_ENGINE)
    assert type(img) == np.ndarray
    assert len(img.shape) == 3
    assert img.shape[2] == 3

def test_imread_opencv_jpg_gray(image_files):
    jpg3c = image_files['jpg']['1c']
    img = io.imread(jpg3c, engine=io.OPENCV_ENGINE)
    assert type(img) == np.ndarray
    assert len(img.shape) == 2
    

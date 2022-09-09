from typing import Union
import numpy as np
import PIL.Image as PILImage
from . import functional as F


__all__ = ['imread']


def imread(impath: str, engine='opencv', mode='RGB')->Union[np.ndarray, PILImage.Image]:
    assert impath.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'))
    if engine == 'opencv':
        return F.opencv_imread(impath, mode=mode)
    elif engine == 'pillow':
        return F.pillow_imread(impath, mode=mode)
    else:
        raise ValueError("engine must be one of ['opencv', 'pillow']")
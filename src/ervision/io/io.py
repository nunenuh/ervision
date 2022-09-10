from pathlib import Path
from typing import Union
import numpy as np
from PIL.Image import Image as PILImage
from . import functional as F


__all__ = ['imread', 'OPENCV_ENGINE', 'PILLOW_ENGINE']


OPENCV_ENGINE = 'opencv'
PILLOW_ENGINE = 'pillow'

def imread(impath: str, engine=OPENCV_ENGINE)->Union[np.ndarray, PILImage]:
    if engine == OPENCV_ENGINE:
        img = F.opencv_imread(impath)
    elif engine == PILLOW_ENGINE:
        img = F.pillow_imread(impath)
    else:
        raise ValueError("engine must be one of ['opencv', 'pillow']")
    return img

def to_pil(img:np.ndarray)->PILImage:
    if type(img)==np.ndarray:
        return F.npimage_to_pillow(img)
    return img   

def to_cv(img:PILImage)->np.ndarray:
    return F.pillow_to_npimage(img)
   
    
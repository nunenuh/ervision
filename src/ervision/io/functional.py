import cv2 as cv
import PIL.Image as Image
import numpy as np
from pathlib import Path

__all__ = ['opencv_imread', 'pillow_imread']

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

def safe_load_image_file_path(impath: str):
    impath = Path(impath)
    if impath.exists() and impath.is_file():
        if impath.suffix in image_extensions:
            return impath
        else:
            raise ValueError("File extension must be one of {}".format(image_extensions))
    else:
        raise FileNotFoundError(f'File {impath} not found')

def opencv_imread(impath: str)->np.ndarray:
    impath = safe_load_image_file_path(impath)
    img = cv.imread(str(impath), cv.IMREAD_UNCHANGED)
    if len(img.shape) == 3 and img.shape[2] == 3:  # RGB
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    elif len(img.shape) == 3 and img.shape[2] == 4: #RGBA
        img = cv.cvtColor(img, cv.COLOR_BGRA2RGBA)
    return img

def pillow_imread(impath: str)->Image.Image:
    impath = safe_load_image_file_path(impath)
    img = Image.open(str(impath))
    return img

def pillow_to_npimage(image: Image.Image)->np.ndarray:
    return np.array(image)

def npimage_to_pillow(image: np.ndarray)->Image.Image:
    return Image.fromarray(image)
    

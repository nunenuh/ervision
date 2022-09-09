import cv2 as cv
import PIL.Image as Image
import numpy as np

__all__ = ['opencv_imread', 'pillow_imread']

def opencv_imread(impath: str, mode="RGB")->np.ndarray:
    img = cv.imread(impath)
    if img is not None:
        h,w,c = img.shape
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img

def pillow_imread(impath: str)->Image.Image:
    img = Image.open(impath)
    if img is not None:
        img = img.convert("RGB")
    
    return img

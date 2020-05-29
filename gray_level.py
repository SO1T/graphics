from PIL import Image
from pylab import array
import numpy as np


def clamp(arr, min_, max_):
    return np.asarray(arr / 255 * (max_ - min_) + min_).astype(np.uint8)


def gray_level_transformation(path, min_, max_):
    img = Image.open(path)
    clamped = clamp(array(img), min_, max_)
    new_path = path.rsplit(".", 1)[0] + f"_gray_level_{min_}_{max_}_transformed.png"
    Image.fromarray(clamped).save(new_path)


path = "img/car.png"

gray_level_transformation(path, 0, 100)
gray_level_transformation(path, 155, 255)
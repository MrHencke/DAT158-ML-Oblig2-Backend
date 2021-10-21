import numpy as np
from PIL import Image, ImageOps


def prepareImage(img):
    return np.array(ImageOps.invert(Image.open(img).convert(
        'L').resize((28, 28)))).reshape(1, 28, 28) / 255.0


def toImagePreviewArray(img):
    return np.array(ImageOps.invert(Image.open(img).convert('L').resize((28, 28)))).tolist()

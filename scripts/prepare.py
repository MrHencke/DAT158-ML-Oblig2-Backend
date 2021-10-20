import numpy as np
from PIL import Image, ImageOps


def prepareImage(img):
    newimg = Image.open(img).convert('L').resize((28, 28))
    newimg = ImageOps.invert(newimg)
    mnist = np.array(newimg).reshape(1, 28, 28)
    return mnist / 255.0

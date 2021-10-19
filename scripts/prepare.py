import numpy as np
from PIL import Image, ImageOps


def prepareImage(img, test=False):
    newimg = Image.open(img).convert('L').resize((28, 28))
    newimg = ImageOps.invert(newimg)
    mnist = toMNIST_IMG(newimg)
    if test:
        newimg.save("./test-images/scaled.png")
    else:
        return mnist / 255.0


def toMNIST_IMG(img):
    data_array = np.array(img)
    return data_array

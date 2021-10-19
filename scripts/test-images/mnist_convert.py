from PIL import Image
import numpy as np


def toMNIST_IMG(img):
    data_array = np.array(img)
    return data_array


def toMNIST_PATH(img):
    Im = Image.open(img)
    data_array = np.array(Im)
    return data_array


if __name__ == "__main__":
    imgpath = "./test-images/scaled.png"
    savepath = "./test-images/"
    toMNIST_PATH(imgpath)

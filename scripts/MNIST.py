from PIL import Image
from array import *
from random import shuffle


def toMNIST_PATH(img):
    data_image = array('B')

    Im = Image.open(img)
    pixel = Im.load()
    width, height = Im.size
    for x in range(0, width):
        for y in range(0, height):
            data_image.append(pixel[y, x])

    outputFile(data_image)
    return data_image


def toMNIST_IMG(img):
    data_image = array('B')

    Im = img
    pixel = Im.load()
    width, height = Im.size
    for x in range(0, width):
        for y in range(0, height):
            data_image.append(pixel[y, x])

    #outputFile(data_image)
    return data_image


def outputFile(file):
    output_file = open('./test-images/image-idx3-ubyte', 'wb')
    file.tofile(output_file)
    output_file.close()


if __name__ == "__main__":
    path = "./test-images/scaled.png"
    toMNIST_PATH(path)

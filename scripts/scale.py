from PIL import Image, ImageOps
from mnist_convert import toMNIST_IMG


def scaleImage(img, test=False):
    newimg = Image.open(img).convert('L').resize((28, 28))
    newimg = ImageOps.invert(newimg)
    mnist = toMNIST_IMG(newimg)
    if test:
        newimg.save("./test-images/scaled.png")
    else:
        return mnist / 255.0


if __name__ == "__main__":
    img = "./test-images/ts.png"
    scaleImage(img, True)

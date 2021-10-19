from PIL import Image
from scripts.mnist_convert import toMNIST_IMG


def scaleImage(img, test=False):
    newimg = Image.open(img).convert('L')
    newimg = newimg.resize((28, 28))
    mnist = toMNIST_IMG(newimg)

    if test:
        newimg.save("./test-images/scaled.png")
    else:
        return mnist


if __name__ == "__main__":
    img = "./test-images/ts.png"
    scaleImage(img, True)

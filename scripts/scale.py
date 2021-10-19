from PIL import Image
from MNIST import toMNIST_IMG, toMNIST_PATH


def scaleImage(img, test):
    newimg = Image.open(img).convert('L')
    newimg = newimg.resize((28, 28))
    if test:
        newimg.save("./test-images/scaled.png")
        mnist = toMNIST_IMG(newimg)
        print(mnist)


if __name__ == "__main__":
    img = "./test-images/ts.png"
    scaleImage(img, True)

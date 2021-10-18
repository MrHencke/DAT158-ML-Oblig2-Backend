from PIL import Image


def scaleImage(img, test):
    newimg = Image.open(img).convert('L')
    newimg = newimg.resize((28, 28))
    if test:
        newimg.save("./test-images/scaled.png")


if __name__ == "__main__":
    img = "./test-images/ts.png"
    scaleImage(img, True)

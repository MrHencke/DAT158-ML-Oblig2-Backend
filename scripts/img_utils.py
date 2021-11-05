import numpy as np
from io import BytesIO
import base64
from PIL import Image, ImageOps


def prepareImage(img):
    return np.array(ImageOps.invert(Image.open(img).convert(
        'L').resize((28, 28)))).reshape(1, 28, 28) / 255.0

def flipImage(img):
    return Image.open(img).transpose(Image.FLIP_LEFT_RIGHT)

def toBase64String(img):
    return imgToB64(ImageOps.invert(Image.open(img).convert('L').resize((28, 28))))


def imgToB64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
    return img_str.decode("utf-8")

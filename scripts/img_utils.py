import numpy as np
from io import BytesIO
import base64
from PIL import Image, ImageOps


def prepareImage(img):
    """
    Converts a given raster image to the MNIST-format

    Args:
        img (JPG | JFIF | PNG): A raster image

    Returns:
        (Numpy Array): A MNIST-compliant grayscaled image
    """
    return np.array(ImageOps.invert(Image.open(img).convert(
        'L').resize((28, 28)))).reshape(1, 28, 28, 1) / 255.0


def prepareFlip(img):
    """
    Flips, then converts a given raster image to the MNIST-format

    Args:
        img (JPG | JFIF | PNG): A raster image

    Returns:
        (Numpy Array): A MNIST-compliant grayscaled image
    """
    return np.array(ImageOps.invert(Image.open(img).transpose(Image.FLIP_LEFT_RIGHT)
                                    .convert('L').resize((28, 28)))).reshape(1, 28, 28, 1) / 255.0


def toBase64String(img):
    """
    Converts an image to the MNIST-format, then transform it into a base64 string.

    Args:
        img (JPG | JFIF | PNG): A raster image

    Returns:
        (String): A base64 encoded string of a MNIST-compliant image.
    """
    return imgToB64(ImageOps.invert(Image.open(img).convert('L').resize((28, 28))))


def imgToB64(image):
    """
    Converts an image to a base64 string.

    Args:
        image (JPG | JFIF | PNG): A raster image

    Returns:
        (string): A utf-8 and base64 encoded string of an image.
    """
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
    return img_str.decode("utf-8")

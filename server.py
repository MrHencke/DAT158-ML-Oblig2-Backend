# Imports
# Used for allowing cross origin requests
from flask_cors import CORS, cross_origin
# Scripts for image preparation
from scripts.img_utils import prepareImage, toBase64String, prepareFlip
from scripts.prediction import Prediction  # JSON-compliant serializer class
# Used for basic REST-server functionality
from flask import Flask, request, jsonify, Response
import numpy as np  # Used for arrays and array-functions
from tensorflow import keras  # Used for the machine learning model
import fleep  # Used for checking headers of uploaded files

# Importing the model, from our models folder.
model = keras.models.load_model("./model/cnn")

# Boilerplate flask app initialization.
app = Flask(__name__)

# Enabling CORS, needed as backend and frontend is split.
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    """
    Runs our model on a given image, sent from the frontend.

    Args:
        File (JPG | PNG | JFIF): A raster image, from the request.

    Returns:
        if legal input:
            Response (JSON): Returns 6 objects. Objects prefixed with f or o are mirrored.
                        o_top_prediction (String): Gives top prediction for the original picture.
                        f_top_prediction (String): Gives top prediction for the flipped picture.
                        top_prediction (String): Gives the top overall prediction between the original and flipped image.
                        o_certainties (Numpy): Gives an array with percantage certainties for what the original image is.
                        f_certainties (Numpy): Gives an array with percantage certainties for what the flipped image is.
                        processed_image (String): A base64 encoded string with the image data of the processed image.
        else:
            Response (JSON): Returns two objects
                response.text (String): An error message.
                response.status (number): Standard bad request number.
    """
    file = request.files['file']
    info = fleep.get(file.read(128))
    if info.type_matches("raster-image"):
        prepared_file = toBase64String(file)
        o_predicted = predict(file)
        f_predicted = predictFlipped(file)
        o_top_prediction = labels[np.argmax(o_predicted)]
        f_top_prediction = labels[np.argmax(f_predicted)]
        top_prediction = o_top_prediction if np.amax(
            o_predicted) > np.amax(f_predicted) else f_top_prediction
        o_formatted = format(o_predicted)
        f_formatted = format(f_predicted)
        if (np.abs(100*(np.amax(o_predicted) - np.amax(f_predicted)) < 3) and o_top_prediction == f_top_prediction):
            return jsonify(top_prediction=top_prediction, o_certainties=o_formatted, processed_image=prepared_file)
        else:
            return jsonify(o_top_prediction=o_top_prediction, f_top_prediction=f_top_prediction, top_prediction=top_prediction, o_certainties=o_formatted, f_certainties=f_formatted, processed_image=prepared_file)
    else:
        return Response(
            "Nice try, but that is not an image",
            status=400,
        )


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    """
    Returns a "u"-string to signify that the backend is up. It is the least demanding check we could think of to test the up-status of the backend.

    Returns:
        Response (String): The letter "u".
    """
    return "u"


def predict(file):
    """
    Prepares the image, then uses the ML-model to predict on the original raster image.

    Args:
        file (File-Stream): A File-Stream of a Raster Image

    Returns:
        result[0] (numpy array): A numpy array containing the certainties for an image being a specific object.
    """
    prepared_file = prepareImage(file)
    result = model.predict(prepared_file)
    return result[0]


def predictFlipped(file):
    """
    Prepares and flips the image, then uses the ML-model to predict on the flipped raster image.

    Args:
        file (File-Stream): A File-Stream of a Raster Image

    Returns:
        result[0] (numpy array): A numpy array containing the certainties for an image being a specific object.
    """
    prepared_file = prepareFlip(file)
    result = model.predict(prepared_file)
    return result[0]


def format(arr):
    """
    Formats the array, drops low values and labels the items.

    Args:
        arr (numpy array): An array of certainties ranging from 0 to 1.

    Returns:
        output (list): A list of all certainties over 1%, with corresponding labels.
    """
    decimals = map(lambda x: round((x * 100), 2), arr)
    output = []

    for key, data in zip(labels, decimals):
        if data > 1:
            output.append(Prediction(key, data).serialize())
    return output


# A list of labels, corresponding to the indexes used by the model.
labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Instructions if the app is ran directly.
if __name__ == '__main__':
    app.run(debug=True)

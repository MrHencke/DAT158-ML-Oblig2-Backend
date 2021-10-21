from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage, toImagePreviewArray
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("./model/keras")


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    file = request.files['file']
    prepared_file = toImagePreviewArray(file)
    predicted = predict(file)
    top_prediction = labels[np.argmax(predicted)]
    formatted = format(predicted)
    return jsonify(top_prediction=top_prediction, certainties=formatted, processed_image=prepared_file)


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    return "u"


def predict(file):
    prepared_file = prepareImage(file)

    result = model.predict(prepared_file)

    output = result[0]

    return output


def format(arr):
    decimals = map(lambda x: x * 100, arr)
    percentages = map(lambda x: "{:2.2f}%".format(x), decimals)
    output = dict(zip(labels, percentages))
    return output


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

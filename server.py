from flask_cors import CORS, cross_origin
from scripts.img_utils import prepareImage, toBase64String, prepareFlip
from scripts.prediction import Prediction
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
    prepared_file = toBase64String(file)
    o_predicted = predict(file)
    f_predicted = predictFlipped(file)
    o_top_prediction = labels[np.argmax(o_predicted)]
    f_top_prediction = labels[np.argmax(f_predicted)]
    o_formatted = format(o_predicted)
    f_formatted = format(f_predicted)
    return jsonify(o_top_prediction=o_top_prediction, f_top_prediction=f_top_prediction, o_certainties=o_formatted, f_certainties=f_formatted, processed_image=prepared_file)


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    return "u"


def predict(file):
    prepared_file = prepareImage(file)
    result = model.predict(prepared_file)
    return result[0]

def predictFlipped(file):
    prepared_file = prepareFlip(file)
    result = model.predict(prepared_file)
    return result[0]


def format(arr):
    decimals = map(lambda x: round((x * 100), 2), arr)
    output = []
    
    for key, data in zip(labels, decimals):
        if data > 1:
            output.append(Prediction(key, data).serialize())
    return output

labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

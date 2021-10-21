from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage, toBase64String
from scripts import prediction
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
    print(prepared_file)
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
    decimals = map(lambda x: round((x * 100), 2), arr)
    output = []
    
    for label, value in zip(labels, decimals):
        output.append(prediction(label, value))
    
    return output


def format2(arr):
    decimals = map(lambda x: round(x * 100), arr)
    output = dict(zip(labels, decimals))
    return output


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage
from flask import Flask, request
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("./model/keras")


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    print(request.files)
    file = request.files['file']
    print(file)
    predicted = predict(file)
    formatted = format(predicted)
    print(formatted)
    preProcessedFile = prepareImage(file)
    results = placeholderModel(preProcessedFile)
    #result = "%s with a %.2f certainty" % labels[results[0]], results[1]
    return "{} {}".format(results[0], results[1])  # results


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
    output = []
    
    decimals = map(lambda x: x * 100, arr)
    percentages = map(lambda x : "{:2.2f}%".format(x), decimals)
    
    
    
    for i in range(len(arr)):
        output.append(zip(percentages, labels))
    
    return output

def placeholderModel(pf):
    if pf is None:
        status = "something"
        certainty = "100%"
    else:
        status = "a picture"
        certainty = "99.99%"

    return [status, certainty]  # {np.argmax(predictions[0]), certainty}


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

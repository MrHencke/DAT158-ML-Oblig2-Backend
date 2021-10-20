from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage
from flask import Flask, request
import numpy as np
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    print(request.files)
    file = request.files['file']
    print(file)
    preProcessedFile = prepareImage(file)
    print(preProcessedFile.shape)
    print(type(preProcessedFile))
    results = placeholderModel(preProcessedFile)
    print(results)
    # results
    return "%s with a %s certainty" % results[0], results[1]


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    return "u"


def placeholderModel(pf):
    if pf is None:
        status = "something"
        certainty = "100%"
    else:
        status = "a picture"
        certainty = "99.99%"

    return [status, certainty]


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

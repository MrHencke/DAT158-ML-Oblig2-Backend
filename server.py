from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage
from scripts.rwutils import readModel
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
    results = placeholderModel(preProcessedFile)
    print(results)
    return "%s with a %.2f certainty" % labels[results[0]], results[1] # results


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    return "u"


def placeholderModel(pf):
    clf = readModel("knn.pkl")
    if pf is None:
        status = "something"
        certainty = "100%"
    else:
        status = "a picture"
        certainty = "99.99%"
        predictions = clf.predict(pf)

    return {np.argmax(predictions[0]), certainty}


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

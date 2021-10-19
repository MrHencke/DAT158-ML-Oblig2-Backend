from flask_cors import CORS, cross_origin
from scripts.prepare import prepareImage
from flask import Flask, request
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    file = request.files['file']
    print(file)
    preProcessedFile = prepareImage(file)
    print(preProcessedFile.shape)
    results = placeholderModel(preProcessedFile)
    print(results)
    return "Something"  # results


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

    return {status, certainty}


labels = ["T-shirt/top", "Trouser", "Pullover", "Dress",
          "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

if __name__ == '__main__':
    app.run(debug=True)

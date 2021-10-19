from flask import Flask, request
from scripts.scale import scaleImage
app = Flask(__name__)


@app.route('/api/ml', methods=['POST'])
def runModel():
    f = request.files['file']
    #scaled = scaleImage(f)
    #prediction = model.predict(scaled)
    # return prediction
    return "placeholder"
    # Use route to process image, and return response.


@app.route('/api/up')
def isUpText():
    return "The server is up"
    # Use route to check backend is up

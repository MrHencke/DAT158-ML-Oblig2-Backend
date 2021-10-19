from flask import Flask, request
from scripts.scale import scaleImage
app = Flask(__name__)


@app.route('/api/ml')
def runModel():
    f = request.files['file']
    scaled = scaleImage(f)
    #prediction = model.predict(scaled)
    # return prediction
    return "placeholder"


@app.route('/api/up')
def isUp():
    return True

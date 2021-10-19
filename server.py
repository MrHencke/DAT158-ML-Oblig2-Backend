from flask import Flask, request
#from scripts.scale import scaleImage
app = Flask(__name__)


@app.route('/api/ml', method='POST')
def runModel():
    f = request.files['file']
    #scaled = scaleImage(f)
    #prediction = model.predict(scaled)
    # return prediction
    return "placeholder"


@app.route('/api/up', method='GET')
def isUp():
    return True


@app.route('/api/up-text', method='GET')
def isUpText():
    return "The server is up"

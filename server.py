from flask_cors import CORS, cross_origin
from scripts.scale import scaleImage
from flask import Flask
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/ml', methods=['POST'])
@cross_origin(origin='*')
def runModel():
    return "placeholder"


@app.route('/api/up', methods=['GET'])
@cross_origin(origin='*')
def isUp():
    return "up"


if __name__ == '__main__':
    app.run(debug=True)

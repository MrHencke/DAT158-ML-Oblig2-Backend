from flask_cors import CORS
from scripts.scale import scaleImage
from flask import Flask
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}},
     methods=['GET', 'POST', 'PUT', 'DELETE'])


@app.route('/api/ml', methods=['POST'])
def runModel():
    return "placeholder"


@app.route('/api/up', methods=['GET'])
def isUpText():
    return "The server is up"


if __name__ == '__main__':
    app.run(debug=True)

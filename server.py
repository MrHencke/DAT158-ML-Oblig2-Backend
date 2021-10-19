from flask import Flask, request
#from scripts.scale import scaleImage
#from flask_cors import CORS

app = Flask(__name__)

#CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/ml', methods=['POST'])
def runModel():
    f = request.files['file']
    #scaled = scaleImage(f)
    #prediction = model.predict(scaled)
    # return prediction
    return "placeholder"


@app.route('/api/up')
def isUpText():
    return "The server is up"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/api/ml', methods=['POST'])
def runModel():

    return "placeholder"


@app.route('/api/up')
def isUpText():
    return "The server is up"


if __name__ == '__main__':
    app.run(debug=True)

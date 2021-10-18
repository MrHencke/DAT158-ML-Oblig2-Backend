from flask import Flask
app = Flask(__name__)


@app.route('/api/ml')
def runModel():
    arg = request.args.get('arg')
    return "placeholder"


def scaleImage(img):
    return "placeholder"

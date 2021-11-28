# Server Flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "E:/Dev/python/projects/env2/pythonflask/uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return "<p>MI primera Web en Flask!</p>"

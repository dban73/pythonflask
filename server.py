# Server Flask
from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = "E:/Dev/python/projects/env2/pythonflask/uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return "<p>MI primera Web en Flask!</p>"

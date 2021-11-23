#Server Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>MI primera Web en Flask!</p>"
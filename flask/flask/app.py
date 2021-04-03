from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
@app.route("/home")
def hello():
    return f"<h1>{app.config['GREETING']}<h1>"


@app.route("/about")
def about():
    return "<h1>About page</h1>"


@app.route("/item/<id>")
def item(id):
    return f"<h1>Item {id} show page"



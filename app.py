from  flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello wlecom ot my site web"

@app.route("/bonjour/<string:name>")
def bonjour(name : str):
    return f"bonjour {name}"
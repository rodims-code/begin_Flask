from  flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello wlecom ot my site web"
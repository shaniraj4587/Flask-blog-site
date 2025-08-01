from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/index")
def index():
    return render_template("index.html", name = "shani raj")

app.run(debug=True) 
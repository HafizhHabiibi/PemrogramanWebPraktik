# import flask
from flask import Flask

# main app
app = Flask(__name__)

# set route untuk /
@app.route("/")
def index():
    return "Hello World!"

if __name__ == "main":
    app.run(debug=True)

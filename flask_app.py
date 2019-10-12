from flask import Flask

### Flask ###
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello world!"
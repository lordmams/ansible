from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello, World </p>"

app.run('0.0.0.0', 5000)

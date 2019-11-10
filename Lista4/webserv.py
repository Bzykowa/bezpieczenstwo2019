#!/usr/bin/python
import os
from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hacked")
def hacking():
    return render_template("hacked.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, ssl_context=('certA.crt', 'privkeyA.pem'))

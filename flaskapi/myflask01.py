#!/usr/bin/python3

""" Simple Flask server """

from flask import Flask

# Flask constructor takes the name of the current
# module (__name__) as argument
app = Flask(__name__)

# rount() function fo the Flask class is a
# decorator, tells the applicaiton which URL
# should call the associated function

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/other")
def other():
    return "Something Else"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

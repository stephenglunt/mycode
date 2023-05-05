#!/usr/bin/env python3

"""Using Flask to host an Avatar API"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

# import JSON into program
with open("avatars.json", "r") as file:
    data = json.load(file)

app = Flask(__name__)

def get_random_character():
#    return random.choice(data)
    mylist = []
    for i in range(4):
        mylist.append(random.choice(data))
    return render_template("index.html", charList=mylist)

@app.route('/')
def landingPage():
    return get_random_character()

@app.route('/affiliation=<friends>')
def affiliations(friends):
    affiliates = []
    for character in data:
        if character['affiliation'].contains(friends):
            affiliates.append(character)

    return affiliates

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug = True)

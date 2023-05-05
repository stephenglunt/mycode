#!/usr/bin/python3

from flask import Flask, request, redirect, jsonify

import json

app = Flask(__name__)

herodata= [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
              ]
             }]

@app.route("/", methods["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            name = data["name"]
            realName = data["realName"]
            since = data["since"]
            powers = data['poers']
            herodata.append({'name': name, 'realName': realName, 'since': since, "powers": powers})

    return jsonify(herodata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

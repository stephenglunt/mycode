#!/usr/bin/env python3

"""Using Flask to host an Avatar API"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

# import JSON into program
with open("avatars.json", "r") as file:
    data = json.load(file)

with open("avatarSymbols.json", "r") as myfile:
    symbols = json.load(myfile)

app = Flask(__name__)

@app.route('/random')
def get_random_character():
#    return random.choice(data)
    return random.choice(data)


@app.route('/character/<_id>')
def characterPage(_id):
    for character in data:
        if character['_id'] == _id:
            symbol_imgs = []
            if "affiliation" in character:
                print("\n\n", character["affiliation"])
                for key in symbols.keys():
                    if key in character["affiliation"]:
                        symbol_imgs.append(symbols[key])
            return render_template('character.html', character=character, symbol_imgs = symbol_imgs)

    redirect('/')

@app.route('/')
def landingPage():
    mylist = []
    for i in range(4):
        mylist.append(get_random_character())



    return render_template("index.html", charList=mylist)

@app.route('/affiliation=<friends>')
def affiliations(friends):
    affiliates = []
    for character in data:
        if 'affiliation' in character:
            if friends in character['affiliation']:
                affiliates.append(character)

    

    return affiliates

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug = True)

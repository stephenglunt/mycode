#!/usr/bin/env python3
"""showing off how to use Flask | Wheel of Time Quote API | Chad Feeser, data by Stephen Glunt"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request

# gotta pull in all that JSON so we can serve it to our clients!
with open("stephen_glunt_wot_quotes.json", "r") as foo:
    data= json.load(foo)

# this object represents our website!
app= Flask(__name__)


def quote_from_title(titlestr):
    """returns a randomly selected quote from the given book title"""
    while True:
        random.shuffle(data)
        for eachdict in data:
            # go through each quote's book title and see if it matches
            if titlestr.lower() in eachdict["title"].lower():
                # if so, return that quote dictionary
                return eachdict

        # if for loop ends without having returned a quote, return this instead:
        return "Sorry, no titles match your selection!"

@app.route("/choice")
def landingpage():
    return render_template("titleposter.html")

@app.route("/bookchoice", methods=["POST"])
def bookchoice():
    if request.form["nm"]:
        # if a value was posted, grab that value and put it in a variable
        title= request.form["nm"]
    else:
        # if no value was posted, pick Chad's favorite book in the series
        title= "The Shadow Rising"

    # send the title to a separate function which will find and return a match (if one exists)
    quote= quote_from_title(title)

    return quote

@app.route("/<derpnum>")
def redirectexample(derpnum):
    """route for redirecting users who don't follow instructions-
    it's /quotes/<num>, NOT /<num>"""
    return redirect(url_for("randomquote", num= derpnum) )

@app.route("/quotes/<num>")
def randomquote(num):
    """returns a random selection of quotes from any book"""
    quotelist= []

    # repeats code according to number above; quotes are added to empty list
    for everynum in range(int(num)):
        randomquote= random.choice(data)
        quotelist.append(randomquote)

    return quotelist

if __name__ == "__main__":
    # debug=True is really nice for testing; whenever you save the file 
    # the flask API automatically restarts
    app.run(host="0.0.0.0", port=2224, debug=True)

#!/usr/bin/python3

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/sucess/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/") # user can land at '/'
@app.route('/start') # or user can land at'/start'
def start():
    return render_template("postmaker.html") #look for templates/postmaker.html

# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come form a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get('nm'): # if nm was assigned via the POST
            user = request.form.get('nm') # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"

    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with value for name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application

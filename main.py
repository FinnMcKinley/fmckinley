import os
import sys
from flask import Flask, render_template
# Imports libraries

DEBUG = True # Sets whether code is in development stage or not

def log(s):
    """ Prints debug log (s) to screen"""
    if DEBUG:
        print(s)
        
# # # # # # # # #
# Flask Section #
# # # # # # # # #

app = Flask(__name__) # Starts Flask app

@app.route("/") # Homepage
def homepage():
    return render_template("home.html", page_title="Home")

@app.route("/projects") # Projects page
def projects():
    return render_template("projects.html", page_title="Projects")

if __name__ == "__main__":    # Starts App
    app.run(debug=True, host="0.0.0.0", port=5000)
#!/usr/bin/env python3
"""0-Basic Flask app"""


from flask import Flask, render_template


# Create an instance of Flask
app = Flask(__name__)


# Create a route for the index page
# that renders the index.html template
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """renders index.html
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()

#!/usr/bin/env python3
"""Mock a logging in user"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


# Create a Config class
class Config:
    """
        COnfiguration class for Bable
        It confugures the default language to be English,
        and the default timezone to be UTC

        it has a languages class attributes equal to ["en", "fr"]
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create a get_locale function that uses request.accept_languages
# and returns the best match with our supported languages
def get_locale():
    """returns the best match with our supported languages
    """

    return request.accept_languages.best_match(app.config["LANGUAGES"])


# mock database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Create an instance of Flask
app = Flask(__name__)
# Create an instance of Babel
babel = Babel(app)
# Configure the app with the Config class
app.config.from_object(Config)
# Initialize Babel with the app and the get_locale function
babel.init_app(app, locale_selector=get_locale)


# Create a get_user function that returns a user dictionary or None
def get_user():
    """returns a user dictionary or None if the ID cannot be found or
    """

    login_id = request.args.get("login_as")
    if login_id is None:
        return None
    return users.get(int(login_id))


# Create a before_request function that finds a user if any
# and set it as a global on flask.g.user
@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user
    """

    g.user = get_user()


# Create a route for the index page
# that renders the index.html template
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """renders index.html
    """

    return render_template("5-index.html")


# Run the app only if this file is called directly
if __name__ == "__main__":
    app.run()

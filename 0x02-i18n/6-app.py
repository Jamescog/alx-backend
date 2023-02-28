#!/usr/bin/env python3
"""Use user locale"""


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
# if it is supported, use the locale from the user settings

def get_locale():
    """returns the best match with our supported languages
    """

    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    
    header_locale = request.headers.get("locale")
    if header_locale and header_locale in app.config["LANGUAGES"]:
        return header_locale
    
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
@app.before_request
def before_request():
    """finds a user if any
    """

    g.user = get_user()


# Create a root route that returns the rendered index.html template
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """returns the rendered index.html template
    """

    return render_template("6-index.html")


# Run the app if and only if this file is called as a script
if __name__ == "__main__":
    app.run()
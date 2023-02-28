"""Infer appropriate time zone from request headers"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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


# Create get_timezone function that uses request.args.get("timezone")
# and return the babel timezone object
def get_timezone():
    """ Determines best match for supported timezones """
    # check if there is a timezone parameter/query string
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    # check if there is a timezone in an existing user's profile
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    # default to return as a failsafe
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

# Create an instance of Flask
app = Flask(__name__)
# Create an instance of Babel
babel = Babel(app)
# Configure the app with the Config class
app.config.from_object(Config)
# Use the get_locale function to set the locale
babel.init_app(app, locale_selector=get_locale)
# Use the get_timezone function to set the timezone
babel.init_app(app, timezone_selector=get_timezone)


# Create a before_request function that sets the user
# from the users dictionary if the user_id is in the dictionary
@app.before_request
def before_request():
    """sets the user from the users dictionary
    """

    user_id = request.args.get("login_as")
    if user_id:
        g.user = users.get(int(user_id))
    else:
        g.user = None


# Create a route that renders 7-index.html
@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """renders 7-index.html
    """

    return render_template("7-index.html")


# Run the app only if this file is called directly
if __name__ == "__main__":
    app.run()

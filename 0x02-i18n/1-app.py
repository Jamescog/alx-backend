"""1-Basic Babel Setup"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)



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
app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """renders index.html
    """

    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
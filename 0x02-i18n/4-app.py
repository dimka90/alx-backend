#!/usr/bin/env python3
"""
Localization module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """localization app configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index() -> str:
    """ Route the index page """
    return render_template('1-index.html',)


@babel.localeselector
def get_locale() -> str:
    """
    Get Locallangauge set
    """
    local_lang = request.args.get('locale')
    if local_lang in app.config["LANGUAGES"]:
        return local_lang
    return request.accept_languages.best_match(app.config())


if __name__ == "__main__":
    app.run(debug=True)

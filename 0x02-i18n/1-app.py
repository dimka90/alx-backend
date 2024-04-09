#!/usr/bin/env python
"""
Localization module
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """localization app configuration"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCAL = "en"
    DEFAULT_TIME_ZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    """ Route the index page """
    return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)

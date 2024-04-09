#!/usr/bin/env python
"""
Localization module
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """localization app configuration"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCAL = "en"
    DEFAULT_TIME_ZONE = "UTC"


app.config.from_object(Config)

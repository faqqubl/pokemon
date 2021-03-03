# -*- coding: utf-8 -*-
"""Pokemon app."""
import os

from dotenv import load_dotenv
from flask import Flask

from pokemon.config import Config

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


def create_app():
    """Create Flask app.

    Returns:
        object: flask application object
    """
    app = Flask(__name__)
    app.config.from_object(Config())

    from pokemon.apis import api  # noqa: E402

    api.init_app(app)

    return app

# -*- coding: utf-8 -*-
"""Pokemon app."""
import os
import secrets

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Construct Config Class.

    Args:
        object (object): ...
    """

    DEBUG = os.getenv("DEBUG", False)
    TESTING = os.getenv("TESTING", False)
    CSRF_ENABLED = os.getenv("CSRF_ENABLED", True)
    secret_key = secrets.token_hex(16)
    SECRET_KEY = secret_key

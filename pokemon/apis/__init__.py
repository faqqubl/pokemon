# -*- coding: utf-8 -*-
"""Pokemon app."""
from flask_restx import Api

from pokemon.apis.pokemon import api as ns1

api = Api(
    title="Pokemon API",
    version="1.0",
    description="Pokemon API",
    ordered=True,
    # All API metadatas
)

api.add_namespace(ns1, path="/api")

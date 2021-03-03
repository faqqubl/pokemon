# -*- coding: utf-8 -*-
"""Pokemon app."""
from flask import jsonify
from flask import make_response
from flask import request
from flask_restx import fields
from flask_restx import marshal
from flask_restx import Namespace
from flask_restx import Resource

from pokemon.apis.external_apis.poke_api import PokeApiRestClient
from pokemon.core.pokemon import Pokemon

api = Namespace("Pokemon", description="Pokemon API related operations")

pokemon_by_parameter_data_resource = api.model(
    "pokemon resource",
    {"id": fields.Integer(), "name": fields.String(), "image": fields.String()},
)

pokemon_by_parameter_general_resource = api.model(
    "pokemon general resource",
    {
        "total": fields.Integer(),
        "limit": fields.Integer(),
        "offset": fields.Integer(),
        "data": fields.List(fields.Nested(pokemon_by_parameter_data_resource)),
    },
)

pokemon_by_name_stats_resource = api.model(
    "stats resource",
    {
        "speed": fields.Integer(),
        "special-defense": fields.Integer(),
        "special-attack": fields.Integer(),
        "defense": fields.Integer(),
        "attack": fields.Integer(),
    },
)

pokemon_by_name_resource = api.model(
    "pokemon by name resource",
    {
        "abilities": fields.List(fields.String()),
        "base_experience": fields.Integer(),
        "forms": fields.List(fields.String()),
        "height": fields.Integer(),
        "id": fields.Integer(),
        "location_area_encounters": fields.String(),
        "moves": fields.List(fields.String()),
        "name": fields.String(),
        "order": fields.Integer(),
        "species": fields.List(fields.String()),
        "sprites": fields.List(fields.String()),
        "stats": fields.Nested(pokemon_by_name_stats_resource),
        "types": fields.List(fields.String()),
        "weight": fields.Integer(),
    },
)


@api.route("/pokemon")
class PokemonByParameters(Resource):
    """Provide Pokemons by parameters data.

    Args:
        Resource (Resource): [description]

    Returns:
        list: list of pokemon.
    """

    @api.doc(
        params={
            "q": {"description": "Pokemons name to search", "type": "string"},
            "limit": {
                "description": "Number of Pokemons to get",
                "type": "integer",
            },
            "offset": {
                "description": "offset",
                "type": "integer",
            },
        }
    )
    def get(self):
        """Get."""
        try:
            poke_name = request.args.get("q")
            limit = request.args.get("limit")
            offset = request.args.get("offset")

            exist_parameters = (
                (poke_name is not None) and (limit is not None) and (offset is not None)
            )
            if exist_parameters:
                limit = int(limit)
                offset = int(offset)
                poke_api_rest_client = PokeApiRestClient()
                pokemons = poke_api_rest_client.get_all_pokemons()["results"]
                if pokemons:
                    p = Pokemon()
                    pokemons_by_name = p.filter_pokemons_by_name(poke_name, pokemons)
                    pokemons_by_offset = poke_api_rest_client.get_pokemons_by_offset(
                        offset
                    )["results"]

                    pokemons_name_list = p.filter_pokemons_by_limit(
                        limit, pokemons_by_name, pokemons_by_offset
                    )

                    pokemons_data = poke_api_rest_client.get_pokemons_by_name_list(
                        pokemons_name_list
                    )
                    total = len(pokemons_data)

                    for p_data in pokemons_data:
                        p_data["image"] = p_data["sprites"]["front_default"]

                    data = {
                        "total": total,
                        "limit": limit,
                        "offset": offset,
                        "data": pokemons_data,
                    }
                    return make_response(
                        marshal(data, pokemon_by_parameter_general_resource), 200
                    )

                return []
            return make_response(
                jsonify(
                    {
                        "error": "Bad request. Parameters 'q', 'limit' and 'offset' must exist."
                    }
                ),
                400,
            )

        except ValueError:
            return make_response(
                jsonify(
                    {
                        "error": (
                            "Invalid parameter format. 'limit' and 'offset' should be Integer."
                        )
                    }
                ),
                400,
            )
        except Exception as e:
            return make_response(jsonify({"error": f"Something went wrong. {e}"}), 400)


@api.route("/pokemon/<string:pokemon_name>")
class PokemonByName(Resource):
    """Provide Pokemons by name data.

    Args:
        Resource (Resource): [description]

    Returns:
        pokemon.
    """

    @api.param("pokemon_name", "Pokemon name")
    def get(self, pokemon_name):
        """Get."""
        try:
            poke_api_rest_client = PokeApiRestClient()
            pokemon_data = poke_api_rest_client.get_pokemon_by_name(pokemon_name)
            if pokemon_data:
                abilities_list = []
                forms_list = []
                moves_list = []
                sprites_list = []
                types_list = []

                for abilities in pokemon_data["abilities"]:
                    abilities_list.append(abilities["ability"]["name"])
                pokemon_data["abilities"] = abilities_list
                for forms in pokemon_data["forms"]:
                    forms_list.append(forms["name"])
                pokemon_data["forms"] = forms_list
                for move in pokemon_data["moves"]:
                    moves_list.append(move["move"]["name"])
                pokemon_data["moves"] = moves_list
                pokemon_data["species"] = [pokemon_data["species"]["name"]]

                sprites_list.append(pokemon_data["sprites"]["back_default"])
                sprites_list.append(pokemon_data["sprites"]["back_shiny"])
                sprites_list.append(pokemon_data["sprites"]["front_default"])
                sprites_list.append(pokemon_data["sprites"]["front_shiny"])
                pokemon_data["sprites"] = sprites_list
                stats = {
                    "speed": pokemon_data["stats"][5]["base_stat"],
                    "special-defense": pokemon_data["stats"][4]["base_stat"],
                    "special-attack": pokemon_data["stats"][3]["base_stat"],
                    "defense": pokemon_data["stats"][2]["base_stat"],
                    "attack": pokemon_data["stats"][1]["base_stat"],
                }
                pokemon_data["stats"] = stats
                for types in pokemon_data["types"]:
                    types_list.append(types["type"]["name"])
                pokemon_data["types"] = types_list

                return make_response(
                    marshal(pokemon_data, pokemon_by_name_resource), 200
                )
            return make_response(jsonify({}), 200)
        except Exception as e:
            return make_response(jsonify({"error": f"Something went wrong. {e}"}), 400)

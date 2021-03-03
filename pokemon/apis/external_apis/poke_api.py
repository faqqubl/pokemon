# -*- coding: utf-8 -*-
"""Pokemon app."""
import json

import requests

from pokemon.apis.external_apis.constants import URI_POKEAPI


class PokeApiRestClient(object):
    """Poke api rest client class."""

    def __init__(self):
        """Init."""

    def get_all_pokemons(self):
        """Get all pokemons.

        Returns:
            All pokemons data (dict)
        """
        endpoint_all_pokemons = f"{URI_POKEAPI}pokemon/"
        response = requests.get(endpoint_all_pokemons)

        if len(response.content) != 0 and response.status_code == 200:
            pokemons = json.loads(response.content.decode("utf-8"))
            return pokemons
        else:
            return []

    def get_pokemons_by_offset(self, offset):
        """Get pokemons by offset.

        Args:
            offset(int): offset
        Returns:
            Pokemons by offset data (list)
        """
        endpoint = f"{URI_POKEAPI}pokemon/"
        params = {"offset": offset}
        response = requests.get(endpoint, params=params)
        if len(response.content) != 0 and response.status_code == 200:
            pokemons = json.loads(response.content.decode("utf-8"))
            return pokemons
        else:
            return []

    def get_pokemons_by_name_list(self, pokemons_name_list):
        """Get pokemons by name list.

        Args:
            pokemons_name_list(list): list of dict of pokemons -> [{"name": "pokemonName",...}, {"name": "pokon", ...}]

        Returns:
            pokemons data list of dict
        """
        pokemons_data_list = []
        for pokemon in pokemons_name_list:
            pokemon_data = self.get_pokemon_by_name(pokemon["name"])
            if pokemon_data:
                pokemons_data_list.append(pokemon_data)
        return pokemons_data_list

    def get_pokemon_by_name(self, name):
        """Get Pokemon data by name.

        Args:
            name(str): pokemon name to search
        Returns:
            pokemon data
        """
        endpoint = f"{URI_POKEAPI}pokemon/{name}"
        response = requests.get(endpoint)
        if len(response.content) != 0 and response.status_code == 200:
            pokemon_data = json.loads(response.content.decode("utf-8"))
            return pokemon_data
        else:
            return []

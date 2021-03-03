# -*- coding: utf-8 -*-
"""Pokemon app."""


class Pokemon(object):
    """Pokemon class."""

    def __init__(self):
        """Init."""

    def filter_pokemons_by_name(self, name, pokemons):
        """Filter pokemons by name.

        Args:
            name(string): pokemon name to search
            pokemons(list): pokemons list of dict data.

        Returns:
            pokemons filtered by name (dict)
        """
        pokemons = list(filter(lambda x: (name in x["name"]), pokemons))
        return pokemons

    def filter_pokemons_by_limit(self, limit, pokemons_by_name, pokemons_by_offset):
        """Filter pokemons by limit.

        Args:
            limit(int): limit of pokemons
            pokemons_by_name(list): pokemons by name list of dict.
            pokemons_by_offset(list): pokemons by offset list of dict
        Returns:
            pokemons list -> [{"name": "pokemonName",...} , {"name": "pokemonName2", ...}]
        """
        pokemons_list = []
        aux_limit = limit
        for poke_by_name in pokemons_by_name:
            if aux_limit <= 0:
                break
            name = poke_by_name["name"]
            for poke_by_offset in pokemons_by_offset:
                if name == poke_by_offset["name"]:
                    pokemons_list.append(poke_by_name)
                    aux_limit = aux_limit - 1
                    break

        return pokemons_list

# -*- coding: utf-8 -*-
"""Pokemon app."""
import unittest

from pokemon.core.pokemon import Pokemon


class PokemonTest(unittest.TestCase):
    """Test class for Pokemon."""

    def setUp(self):
        """Set up."""
        self.p = Pokemon()

    def test_filter_pokemons_by_name(self):
        """Test filter pokemons by name."""
        pokemons_data = [
            {"name": "wobbuffet"},
            {"name": "bulbasaur"},
            {"name": "pikachu"},
            {"name": "ivysaur"},
            {"name": "charmeleon"},
            {"name": "venusaur"},
        ]
        pokemon_name_to_search = "saur"

        pokemons_expected = [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]

        pokemons_obtained = self.p.filter_pokemons_by_name(
            pokemon_name_to_search, pokemons_data
        )
        self.assertEqual(pokemons_obtained, pokemons_expected)

    def test_filter_pokemons_by_name_non_existent(self):
        """Test filter pokemons by name nonexistent."""
        pokemons_data = [
            {"name": "wobbuffet"},
            {"name": "bulbasaur"},
            {"name": "pikachu"},
            {"name": "ivysaur"},
            {"name": "charmeleon"},
            {"name": "venusaur"},
        ]
        pokemon_name_to_search = "facundo"

        pokemons_expected = []

        pokemons_obtained = self.p.filter_pokemons_by_name(
            pokemon_name_to_search, pokemons_data
        )
        self.assertEqual(pokemons_obtained, pokemons_expected)

    def test_filter_pokemons_by_limit(self):
        """Test filter pokemons by limit."""
        pokemons_data = [
            {"name": "wobbuffet"},
            {"name": "bulbasaur"},
            {"name": "pikachu"},
            {"name": "ivysaur"},
            {"name": "charmeleon"},
            {"name": "venusaur"},
        ]
        limit = 2

        pokemons_to_search = [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]
        pokemons_expected = [{"name": "bulbasaur"}, {"name": "ivysaur"}]

        pokemons_obtained = self.p.filter_pokemons_by_limit(
            limit, pokemons_to_search, pokemons_data
        )
        self.assertEqual(pokemons_obtained, pokemons_expected)

    def test_filter_pokemons_by_limit_equal_zero(self):
        """Test filter pokemons by limit equal zero."""
        pokemons_data = [
            {"name": "wobbuffet"},
            {"name": "bulbasaur"},
            {"name": "pikachu"},
            {"name": "ivysaur"},
            {"name": "charmeleon"},
            {"name": "venusaur"},
        ]
        limit = 0

        pokemons_to_search = [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]
        pokemons_expected = []

        pokemons_obtained = self.p.filter_pokemons_by_limit(
            limit, pokemons_to_search, pokemons_data
        )
        self.assertEqual(pokemons_obtained, pokemons_expected)

    def test_filter_pokemons_by_limit_greater_than_pokemons_to_obtain(self):
        """Test filter pokemons by limit greater than pokemons to obtain."""
        pokemons_data = [
            {"name": "wobbuffet"},
            {"name": "bulbasaur"},
            {"name": "pikachu"},
            {"name": "ivysaur"},
            {"name": "charmeleon"},
            {"name": "venusaur"},
        ]
        limit = 4

        pokemons_to_search = [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]
        pokemons_expected = [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]

        pokemons_obtained = self.p.filter_pokemons_by_limit(
            limit, pokemons_to_search, pokemons_data
        )
        self.assertEqual(pokemons_obtained, pokemons_expected)

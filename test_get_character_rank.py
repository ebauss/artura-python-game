from unittest import TestCase
import game


class TestGetCharacterRank(TestCase):
    def test_get_character_rank_below_level_3(self):
        character = {'ranks': ['Fighter', 'Hero', 'Dark Knight'], 'level': 2}
        expected = "Hero"
        actual = game.get_character_rank(character)
        self.assertEqual(actual, expected)

    def test_get_character_rank_above_level_3(self):
        character = {'ranks': ['Fighter', 'Hero', 'Dark Knight'], 'level': 5}
        expected = "Dark Knight"
        actual = game.get_character_rank(character)
        self.assertEqual(actual, expected)

    def test_get_character_rank_check_character_dictionary_not_modified(self):
        character = {'ranks': ['Fighter', 'Hero', 'Dark Knight'], 'level': 2}
        expected = {'ranks': ['Fighter', 'Hero', 'Dark Knight'], 'level': 2}
        game.get_character_rank(character)
        self.assertEqual(character, expected)

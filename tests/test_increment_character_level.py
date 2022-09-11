from unittest import TestCase
import game


class TestIncrementCharacterLevel(TestCase):
    def test_increment_character_level_one(self):
        character = {'level': 1}
        game.increment_character_level(character)
        expected = {'level': 2}
        self.assertEqual(character, expected)

    def test_increment_character_level_two(self):
        character = {'level': 2}
        game.increment_character_level(character)
        expected = {'level': 3}
        self.assertEqual(character, expected)

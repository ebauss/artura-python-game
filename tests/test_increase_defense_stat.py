from unittest import TestCase
import game


class TestIncreaseDefenseStat(TestCase):
    def test_increase_defense_stat(self):
        character = {'defense_stat': 20}
        game.increase_defense_stat(character)
        expected = {'defense_stat': 40}
        self.assertEqual(character, expected)

from unittest import TestCase
import game


class TestIncreaseLevelUpExp(TestCase):
    def test_increase_level_up_exp(self):
        character = {'level_up_exp': 20}
        game.increase_level_up_exp(character)
        expected = {'level_up_exp': 40}
        self.assertEqual(character, expected)

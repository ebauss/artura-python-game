from unittest import TestCase
import game


class TestIncreaseMaxHp(TestCase):
    def test_increase_max_hp(self):
        character = {'Max HP': 20}
        game.increase_max_hp(character)
        expected = {'Max HP': 40}
        self.assertEqual(character, expected)

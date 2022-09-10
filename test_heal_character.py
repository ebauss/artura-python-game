from unittest import TestCase
import game


class TestHealCharacter(TestCase):
    def test_heal_character_not_exceed_max_hp(self):
        character = {'Current HP': 100, 'Max HP': 200}
        game.heal_character(character, 50)
        expected = {'Current HP': 150, 'Max HP': 200}
        self.assertEqual(character, expected)

    def test_heal_character_exceed_max_hp(self):
        character = {'Current HP': 100, 'Max HP': 200}
        game.heal_character(character, 150)
        expected = {'Current HP': 200, 'Max HP': 200}
        self.assertEqual(character, expected)

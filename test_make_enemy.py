from unittest import TestCase
from unittest.mock import patch
import game


class TestMakeEnemy(TestCase):
    @patch('random.choice', side_effect=[game.make_wraith])
    def test_make_enemy_level_one(self, _):
        test_character_dictionary = {"level": 1}
        expected = {'Current HP': 50,
                    'Max HP': 50,
                    'attack_stat': 10,
                    'defense_stat': 5,
                    'enemy_description': 'A wraith is an undead creature whose name originated in \n'
                                         'Scottish folklore. A type of ghost or spirit, wraiths \n'
                                         'were traditionally said to be the embodiment of souls \n'
                                         'who are either on the verge of death, or who have \n'
                                         'recently passed on.',
                    'level': 1,
                    'name': 'Wraith',
                    'percent_accuracy': 0.5,
                    'skills': ['Soul Sucker', 'Spirit Strike', 'Chilling Scream']}
        actual = game.make_enemy(test_character_dictionary)
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=[game.make_dragon])
    def test_make_enemy_level_two(self, _):
        test_character_dictionary = {"level": 2}
        expected = {'Current HP': 100,
                    'Max HP': 100,
                    'attack_stat': 15,
                    'defense_stat': 15,
                    'enemy_description': 'A large creature with bat like wings. They can breathe '
                                         'fire.',
                    'level': 2,
                    'name': 'Dragon',
                    'percent_accuracy': 0.5,
                    'skills': ['Dragons Breathe', 'Tail Whip', 'Bite']}
        actual = game.make_enemy(test_character_dictionary)
        self.assertEqual(actual, expected)

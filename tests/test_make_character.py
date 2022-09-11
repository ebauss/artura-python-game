import io
from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Evon', '1'])
    def test_make_character_with_name_evon_class_mage(self, _, mock_stdout):
        actual = make_character()
        expected = {'Current HP': 70,
                    'Max HP': 70,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'attack_stat': 50,
                    'character_class': 'Mage',
                    'current_exp': 0,
                    'defense_stat': 10,
                    'level': 1,
                    'level_up_exp': 50,
                    'name': 'Evon',
                    'percent_accuracy': 0.4,
                    'ranks': ['Initiate', 'Adept', 'Grand Master'],
                    'skills': ['Blizzard', 'Flame Strike', 'Water Prison']}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Chris', '2'])
    def test_make_character_with_name_chris_class_ninja(self, _, mock_stdout):
        actual = make_character()
        expected = {'Current HP': 150,
                    'Max HP': 150,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'attack_stat': 20,
                    'character_class': 'Ninja',
                    'current_exp': 0,
                    'defense_stat': 20,
                    'level': 1,
                    'level_up_exp': 50,
                    'name': 'Chris',
                    'percent_accuracy': 0.95,
                    'ranks': ['Genin', 'Chunin', 'Jonin'],
                    'skills': ['Shuriken Throw', 'Dagger Strike', 'Assassinate']}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Felix', '3'])
    def test_make_character_with_name_felix_class_warrior(self, _, mock_stdout):
        actual = make_character()
        expected = {'Current HP': 200,
                    'Max HP': 200,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'attack_stat': 30,
                    'character_class': 'Warrior',
                    'current_exp': 0,
                    'defense_stat': 30,
                    'level': 1,
                    'level_up_exp': 50,
                    'name': 'Felix',
                    'percent_accuracy': 0.7,
                    'ranks': ['Fighter', 'Hero', 'Dark Knight'],
                    'skills': ['Execute', 'Heroic Strike', 'Charge']}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Bryan', '4'])
    def test_make_character_with_name_bryan_class_class4(self, _, mock_stdout):
        actual = make_character()
        expected = {'Current HP': 100,
                    'Max HP': 100,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'attack_stat': 25,
                    'character_class': 'Archer',
                    'current_exp': 0,
                    'defense_stat': 15,
                    'level': 1,
                    'level_up_exp': 50,
                    'name': 'Bryan',
                    'percent_accuracy': 0.9,
                    'ranks': ['Hunter', 'Ranger', 'Bow Master'],
                    'skills': ['Rapid Fire', 'Poison Arrow', 'Penetrating Arrow']}
        self.assertEqual(expected, actual)

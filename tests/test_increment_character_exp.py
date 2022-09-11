import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestIncrementCharacterExp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_increment_character_exp_level_one(self, mock_stdout):
        character = {'current_exp': 0, 'level_up_exp': 40}
        enemy = {'level': 1, 'name': 'test_enemy'}
        game.increment_character_exp(character, enemy)
        expected = {'current_exp': 25, 'level_up_exp': 40}
        self.assertEqual(character, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_increment_character_exp_level_two(self, mock_stdout):
        character = {'current_exp': 0, 'level_up_exp': 80}
        enemy = {'level': 2, 'name': 'test_enemy'}
        game.increment_character_exp(character, enemy)
        expected = {'current_exp': 40, 'level_up_exp': 80}
        self.assertEqual(character, expected)

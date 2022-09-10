import io
from unittest import TestCase
from unittest.mock import patch

import game


class TestGetUserAttackSkillChoice(TestCase):
    test_character = {'skills': ['skill1', 'skill2', 'skill3']}
    test_enemy = {'name': 'test_enemy'}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_get_user_attack_skill_choice_minimum(self, _, mock_stdout):
        expected = "skill1"
        actual = game.get_user_attack_skill_choice(self.test_character, self.test_enemy)
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_get_user_attack_skill_choice_maximum(self, _, mock_stdout):
        expected = "skill3"
        actual = game.get_user_attack_skill_choice(self.test_character, self.test_enemy)
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_get_user_attack_skill_choice_middle(self, _, mock_stdout):
        expected = "skill2"
        actual = game.get_user_attack_skill_choice(self.test_character, self.test_enemy)
        self.assertEqual(actual, expected)

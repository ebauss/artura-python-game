import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestGetUserDirectionChoice(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', '1'])
    def test_get_user_direction_choice_invalid(self, _, mock_stdout):
        expected = "1"
        actual = game.get_user_direction_choice()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_get_user_direction_choice_valid_minimum(self, _, mock_stdout):
        expected = "1"
        actual = game.get_user_direction_choice()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['4'])
    def test_get_user_direction_choice_valid_maximum(self, _, mock_stdout):
        expected = "4"
        actual = game.get_user_direction_choice()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_get_user_direction_choice_valid_middle(self, _, mock_stdout):
        expected = "3"
        actual = game.get_user_direction_choice()
        self.assertEqual(actual, expected)

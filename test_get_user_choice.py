import io
from unittest import TestCase
from unittest.mock import patch
import game
from game import get_user_choice


class TestGetUserChoice(TestCase):
    list_length_three = ['1', '2', '3']
    list_length_four = ['1', '2', '3', '4']

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_length_three_minimum(self, _):
        actual = get_user_choice(self.list_length_three)
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_choice_length_three_maximum(self, _):
        actual = get_user_choice(self.list_length_three)
        expected = "3"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_length_four_minimum(self, _):
        actual = get_user_choice(self.list_length_four)
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_length_four_maximum(self, _):
        actual = get_user_choice(self.list_length_four)
        expected = "4"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch.object(game, "exit")
    @patch('builtins.input', side_effect=['q', '1'])
    def test_get_user_choice_quit_lowercase(self, mock, _, mock_stdout):
        get_user_choice(self.list_length_three)
        mock.assert_called()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch.object(game, "exit")
    @patch('builtins.input', side_effect=['Q', '1'])
    def test_get_user_choice_quit_uppercase(self, mock, _, mock_stdout):
        get_user_choice(self.list_length_three)
        mock.assert_called()

    @patch('builtins.input', side_effect=['ffff', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_value_invalid(self, mock_stdout, _):
        expected = "Invalid input. Please try again.\n"
        get_user_choice(self.list_length_three)
        self.assertEqual(mock_stdout.getvalue(), expected)

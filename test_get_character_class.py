import io
from unittest import TestCase
from unittest.mock import patch
from game import get_character_class


class TestGetCharacterClass(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["1"])
    def test_get_character_class_class1(self, _, mock_stdout):
        expected = "1"
        actual = get_character_class()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["2"])
    def test_get_character_class_class2(self, _, mock_stdout):
        expected = "2"
        actual = get_character_class()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["3"])
    def test_get_character_class_class3(self, _, mock_stdout):
        expected = "3"
        actual = get_character_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_character_class_class4(self, _, mock_stdout):
        expected = "4"
        actual = get_character_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["6", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_character_class_invalid(self, mock_stdout, _):
        expected = "Please enter a number between 1 - 4 representing the class that you wish to play: " \
                   "\n1"
        return_value = get_character_class()
        actual = mock_stdout.getvalue() + return_value
        self.assertEqual(actual, expected)

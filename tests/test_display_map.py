import io
from unittest import TestCase
from unittest.mock import patch
from game import display_map


class TestDisplayMap(TestCase):
    some_rows = 3
    some_columns = 3

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_top_left_corner(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = "[X] [ ] [ ]\n[ ] [ ] [ ]\n[ ] [ ] [B]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_top_right_corner(self, mock_stdout):
        character = {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = "[ ] [ ] [X]\n[ ] [ ] [ ]\n[ ] [ ] [B]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_bottom_left_corner(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 2, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = "[ ] [ ] [ ]\n[ ] [ ] [ ]\n[X] [ ] [B]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_bottom_right_corner(self, mock_stdout):
        character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = "[ ] [ ] [ ]\n[ ] [ ] [ ]\n[ ] [ ] [X]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_center(self, mock_stdout):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = "[ ] [ ] [ ]\n[ ] [X] [ ]\n[ ] [ ] [B]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_check_rows_not_modified(self, mock_stdout):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = 3
        self.assertEqual(self.some_rows, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_check_columns_not_modified(self, mock_stdout):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = 3
        self.assertEqual(self.some_columns, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_check_character_dictionary_not_modified(self, mock_stdout):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        display_map(self.some_rows, self.some_columns, character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(character, expected)

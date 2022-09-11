import io
from unittest import TestCase
from unittest.mock import patch

from game import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    board = {(0, 0): "Empty room", (0, 1): "Room with a cozy fireplace",
             (1, 0): "Room containing a rusty car",
             (1, 1): "Room filled completely with random items"}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_minimum_condition(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        describe_current_location(self.board, character)
        expected = "Area description: Empty room\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_maximum_condition(self, mock_stdout):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        describe_current_location(self.board, character)
        expected = "Area description: Room filled completely with random items\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_middle_condition(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        describe_current_location(self.board, character)
        expected = "Area description: Room with a cozy fireplace\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_check_board_dictionary_not_modified(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        describe_current_location(self.board, character)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_check_character_dictionary_not_modified(self, mock_stdout):
        character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        describe_current_location(self.board, character)
        expected = {(0, 0): "Empty room", (0, 1): "Room with a cozy fireplace",
                            (1, 0): "Room containing a rusty car",
                            (1, 1): "Room filled completely with random items"}
        self.assertEqual(expected, self.board)

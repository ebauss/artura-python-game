from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    some_rows = 2
    some_columns = 2

    def test_validate_move_north_boundary(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertFalse(validate_move(self.some_rows, self.some_columns, character, "1"))

    def test_validate_move_east_boundary(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertFalse(validate_move(self.some_rows, self.some_columns, character, "2"))

    def test_validate_move_south_boundary(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertFalse(validate_move(self.some_rows, self.some_columns, character, "3"))

    def test_validate_move_west_boundary(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertFalse(validate_move(self.some_rows, self.some_columns, character, "4"))

    def test_validate_move_valid_move(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertTrue(validate_move(self.some_rows, self.some_columns, character, "3"))

    def test_validate_move_check_rows_not_modified(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        validate_move(self.some_rows, self.some_columns, character, "3")
        expected = 2
        self.assertEqual(self.some_rows, expected)

    def test_validate_move_check_columns_not_modified(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        validate_move(self.some_rows, self.some_columns, character, "3")
        expected = 2
        self.assertEqual(self.some_columns, expected)

    def test_validate_move_check_character_dictionary_not_modified(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        validate_move(self.some_rows, self.some_columns, character, "3")
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(character, expected)

    def test_validate_move_check_direction_string_not_modified(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "South"
        validate_move(self.some_rows, self.some_columns, character, "3")
        expected = "South"
        self.assertEqual(direction, expected)

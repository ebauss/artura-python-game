from unittest import TestCase
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    some_rows = 2
    some_columns = 2

    def test_check_if_goal_attained_true(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertTrue(check_if_goal_attained(self.some_rows, self.some_columns, character))

    def test_check_if_goal_attained_false(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertFalse(check_if_goal_attained(self.some_rows, self.some_columns, character))

    def test_check_if_goal_attained_check_rows_not_modified(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        check_if_goal_attained(self.some_rows, self.some_columns, character)
        expected = 2
        self.assertEqual(expected, self.some_rows)

    def test_check_if_goal_attained_check_columns_not_modified(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        check_if_goal_attained(self.some_rows, self.some_columns, character)
        expected = 2
        self.assertEqual(expected, self.some_columns)

    def test_check_if_goal_attained_check_character_dictionary_not_modified(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        check_if_goal_attained(self.some_rows, self.some_columns, character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(character, expected)

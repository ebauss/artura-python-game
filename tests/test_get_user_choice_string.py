from unittest import TestCase
import game


class TestGetUserChoiceString(TestCase):
    direction_choice_list = ['North', "East", "South", "West"]

    def test_get_user_choice_string_directions(self):
        expected = "\t[1] North\n\t[2] East\n\t[3] South\n\t[4] West\n\t[q/Q] Quit\n"
        actual = game.get_user_choice_string(self.direction_choice_list)
        self.assertEqual(actual, expected)

    def test_get_user_choice_string_choice_list_not_modified(self):
        game.get_user_choice_string(self.direction_choice_list)
        expected = ['North', "East", "South", "West"]
        actual = self.direction_choice_list
        self.assertEqual(actual, expected)

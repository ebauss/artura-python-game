from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character, "1")
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(character, expected)

    def test_move_character_east(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        move_character(character, "2")
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(character, expected)

    def test_move_character_south(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        move_character(character, "3")
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(character, expected)

    def test_move_character_west(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character, "4")
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(character, expected)

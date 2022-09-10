from unittest import TestCase
from game import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_true(self):
        self.assertTrue(is_alive({'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}))

    def test_is_alive_false(self):
        self.assertFalse(is_alive({'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 0}))

    def test_is_alive_check_character_dictionary_not_modified(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        is_alive(character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(character, expected)

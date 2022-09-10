from unittest import TestCase
import game


class TestCanFightBoss(TestCase):
    def test_can_fight_boss_true(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 9, 'level': 3}
        expected = True
        actual = game.can_fight_boss(10, 10, character)
        self.assertEqual(actual, expected)

    def test_can_fight_boss_false(self):
        character = {'X-coordinate': 6, 'Y-coordinate': 9, 'level': 3}
        expected = False
        actual = game.can_fight_boss(10, 10, character)
        self.assertEqual(actual, expected)

    def test_can_fight_boss_false(self):
        character = {'X-coordinate': 6, 'Y-coordinate': 6, 'level': 3}
        expected = {'X-coordinate': 6, 'Y-coordinate': 6, 'level': 3}
        game.can_fight_boss(10, 10, character)
        self.assertEqual(character, expected)
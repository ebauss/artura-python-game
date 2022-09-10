from unittest import TestCase
from unittest.mock import patch
import game


class TestGetRandomEnemySkill(TestCase):
    test_enemy = {'skills': ['skill1', 'skill2', 'skill3']}

    @patch('random.choice', side_effect=['skill1'])
    def test_get_random_enemy_skill_minimum(self, _):
        expected = 'skill1'
        actual = game.get_random_enemy_skill(self.test_enemy)
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['skill3'])
    def test_get_random_enemy_skill_maximum(self, _):
        expected = 'skill3'
        actual = game.get_random_enemy_skill(self.test_enemy)
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['skill2'])
    def test_get_random_enemy_skill_middle(self, _):
        expected = 'skill2'
        actual = game.get_random_enemy_skill(self.test_enemy)
        self.assertEqual(actual, expected)

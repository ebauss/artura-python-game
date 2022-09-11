from unittest import TestCase
import game


class TestIncreaseAttackStat(TestCase):
    def test_increase_attack_stat(self):
        character = {'attack_stat': 20}
        game.increase_attack_stat(character)
        expected = {'attack_stat': 40}
        self.assertEqual(character, expected)

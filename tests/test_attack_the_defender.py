import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestAttackTheDefender(TestCase):
    attack_skill = 'test attack'

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.random', side_effect=[0.5])
    # Test for base attack + bonus attack
    def test_attack_the_defender_base_and_bonus_success(self, _, mock_stdout):
        attacker = {'name': 'test_attacker', 'attack_stat': 50, 'defense_stat': 50, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        defender = {'name': 'test_defender', 'attack_stat': 50, 'defense_stat': 10, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        game.attack_the_defender(attacker, defender, self.attack_skill)
        expected = {'name': 'test_defender', 'attack_stat': 50, 'defense_stat': 10, 'Current HP': 0,
                    'percent_accuracy': 0.9}
        self.assertEqual(defender, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.random', side_effect=[0.5])
    # Test for base attack only
    def test_attack_the_defender_base_only_success(self, _, mock_stdout):
        attacker = {'name': 'test_attacker', 'attack_stat': 60, 'defense_stat': 60, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        defender = {'name': 'test_defender', 'attack_stat': 60, 'defense_stat': 60, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        game.attack_the_defender(attacker, defender, self.attack_skill)
        expected = {'name': 'test_defender', 'attack_stat': 60, 'defense_stat': 60, 'Current HP': 40,
                    'percent_accuracy': 0.9}
        self.assertEqual(defender, expected)

    @patch('random.random', side_effect=[0.95])
    @patch('sys.stdout', new_callable=io.StringIO)
    # Test for attack missing the defender
    def test_attack_the_defender_attack_missed(self, mock_stdout, _):
        attacker = {'name': 'test_attacker', 'attack_stat': 100, 'defense_stat': 100, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        defender = {'name': 'test_defender', 'attack_stat': 100, 'defense_stat': 100, 'Current HP': 50,
                    'percent_accuracy': 0.9}
        game.attack_the_defender(attacker, defender, self.attack_skill)
        expected = "test attack did not hit. No damage taken.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

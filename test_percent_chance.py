from unittest import TestCase
from unittest.mock import patch
from game import percent_chance


class TestPercentChance(TestCase):
    @patch('random.random', side_effect=[0.10])
    def test_percent_chance_true(self, _):
        percentage = 0.20
        self.assertTrue(percent_chance(percentage))

    @patch('random.random', side_effect=[0.50])
    def test_percent_chance_false(self, _):
        percentage = 0.20
        self.assertFalse(percent_chance(percentage))

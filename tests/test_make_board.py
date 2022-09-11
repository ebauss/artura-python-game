from unittest import TestCase
from unittest.mock import patch
import game


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=['A village ', 'that is abandoned ', 'and is filled with despair.',
                                         'A town ', 'that is in a dire state ', 'with pools of blood everywhere.',
                                         'A cave ', 'with a full moon ', 'and is filled with shadows.',
                                         'A forest ', 'that is plundered ', 'and is filled with misery.'])
    def test_make_board(self, _):
        some_rows = 2
        some_columns = 2
        expected = {(0, 0): 'A village that is abandoned and is filled with despair.',
                    (0, 1): 'A town that is in a dire state with pools of blood everywhere.',
                    (1, 0): 'A cave with a full moon and is filled with shadows.',
                    (1, 1): 'A forest that is plundered and is filled with misery.'}
        actual = game.make_board(some_rows, some_columns)
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['A village ', 'that is abandoned ', 'and is filled with despair.',
                                         'A town ', 'that is in a dire state ', 'with pools of blood everywhere.',
                                         'A cave ', 'with a full moon ', 'and is filled with shadows.',
                                         'A forest ', 'that is plundered ', 'and is filled with misery.'])
    def test_not_make_board(self, _):
        some_rows = 0
        some_columns = 0
        expected = {}
        actual = game.make_board(some_rows, some_columns)
        self.assertEqual(actual, expected)

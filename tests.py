import unittest
from tic import TicTacToe


class TicTacToeSpec(unittest.TestCase):
    def test_when_x_outside_board_then_error(self):
        tic_tac_toe = TicTacToe()
        with self.assertRaises(Exception):
            tic_tac_toe.play(5, 2)


if __name__ == '__main__':
    unittest.main()

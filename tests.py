import unittest
from source import TicTacToe


class TicTacToeSpec(unittest.TestCase):
    def test_when_x_outside_board_then_error(self):
        tic_tac_toe = TicTacToe()
        with self.assertRaises(Exception): tic_tac_toe.play(5, 2)

    def test_when_y_outside_board_then_error(self):
        tic_tac_toe = TicTacToe()
        self.assertRaises(Exception, tic_tac_toe.play, 2, 5)

    def test_when_occupied_then_error(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play(2, 1)
        with self.assertRaises(Exception):
            tic_tac_toe.play(2, 1)


if __name__ == '__main__':
    unittest.main()

import unittest

from tic import TicTacToe


class TicTacToeSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe = TicTacToe()

    def testWhen_x_outside_board_then_error(self):
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(5, 2)

    def test_when_y_outside_board_then_error(self):
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(2, 5)

    def test_when_field_is_occupied_then_error(self):
        self.tic_tac_toe.play(2, 2)
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(2, 2)


if __name__ == '__main__':
    unittest.main()

import unittest

from tic import TicTacToe


class TicTacToeSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe = TicTacToe()

    def test_when_x_outside_board_then_error(self) -> None:
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(5, 2)

    def test_when_y_outside_board_then_error(self) -> None:
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(2, 5)

    def test_when_field_is_occupied_then_error(self) -> None:
        self.tic_tac_toe.play(2, 2)
        with self.assertRaises(Exception):
            self.tic_tac_toe.play(2, 2)

    def test_first_turn_when_next_player_is_x(self) -> None:
        self.assertEqual('X', self.tic_tac_toe.next_player())

    def test_last_turn_was_x_then_next_player_is_o(self) -> None:
        self.tic_tac_toe.play(1, 1)
        self.assertEqual('O', self.tic_tac_toe.next_player())

    def test_play_no_winner(self) -> None:
        actual: str = self.tic_tac_toe.play(1, 1)
        self.assertEqual('No winner!', actual)

    def test_whole_horizontal_line_then_winner(self) -> None:
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 1)  # X
        self.tic_tac_toe.play(2, 2)  # O
        actual: str = self.tic_tac_toe.play(3, 1)  # X
        self.assertEqual('The winner is X', actual)

    def test_whole_vertical_line_then_winner(self):
        self.tic_tac_toe.play(2, 1)  # X
        self.tic_tac_toe.play(1, 1)  # O
        self.tic_tac_toe.play(3, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 2)  # X
        actual: str = self.tic_tac_toe.play(1, 3)  # O
        self.assertEqual('The winner is O', actual)


if __name__ == '__main__':
    unittest.main()

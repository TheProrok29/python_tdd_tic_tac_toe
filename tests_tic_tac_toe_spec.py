import unittest

from tic import TicTacToe
from mongo_config import TicTacToeCollection


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

    def test_whole_vertical_line_then_winner(self) -> None:
        self.tic_tac_toe.play(2, 1)  # X
        self.tic_tac_toe.play(1, 1)  # O
        self.tic_tac_toe.play(3, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 2)  # X
        actual: str = self.tic_tac_toe.play(1, 3)  # O
        self.assertEqual('The winner is O', actual)

    def test_top_bottom_diagonal_line_then_winner(self) -> None:
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(3, 1)  # O
        self.tic_tac_toe.play(2, 2)  # X
        self.tic_tac_toe.play(2, 1)  # O
        actual: str = self.tic_tac_toe.play(3, 3)  # X
        self.assertEqual('The winner is X', actual)

    def test_bottom_top_diagonal_line_then_winner(self) -> None:
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(1, 3)  # O
        self.tic_tac_toe.play(3, 2)  # X
        self.tic_tac_toe.play(2, 2)  # O
        self.tic_tac_toe.play(3, 3)  # X
        actual: str = self.tic_tac_toe.play(3, 1)  # O
        self.assertEqual('The winner is O', actual)

    def test_all_boxes_are_fill_then_no_winner(self) -> None:
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(1, 3)  # X
        self.tic_tac_toe.play(2, 1)  # O
        self.tic_tac_toe.play(2, 3)  # X
        self.tic_tac_toe.play(2, 2)  # O
        self.tic_tac_toe.play(3, 1)  # X
        self.tic_tac_toe.play(3, 3)  # O
        actual: str = self.tic_tac_toe.play(3, 2)
        self.assertEqual('The result is draw!', actual)

    def test_when_crated_then_mongo_has_db_name_tic_tac_toe(self):
        collection = TicTacToeCollection()
        self.assertEqual('tic_tac_toe', collection.get_db_name())

    def test_when_crated_then_mongo_collection_name_game(self):
        collection = TicTacToeCollection()
        self.assertEqual('game', collection.get_db_collection_name())


if __name__ == '__main__':
    unittest.main()

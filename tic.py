from typing import List


class TicTacToe:
    def __init__(self):
        self.board: List[List[str]] = [['O', 'O', 'O'],
                                       ['O', 'O', 'O'],
                                       ['O', 'O', 'O']]
        self.last_player: str = 'O'

    @staticmethod
    def _check_axis(axis: int) -> None:
        if axis < 1 or axis > 3:
            raise Exception('Outside the board')

    def _set_box(self, x: int, y: int) -> None:
        if self.board[x - 1][y - 1] == 'O':
            self.board[x - 1][y - 1] = 'X'
        else:
            raise Exception('Field is occupied')

    def next_player(self) -> str:
        if self.last_player == 'X':
            return 'O'
        else:
            return 'X'

    def _is_winner(self) -> bool:
        size: int = len(self.board)
        for index in range(size):
            if self.board[0][index] + self.board[1][index] + self.board[2][index] == self.last_player * size:
                return True
            return False

    def play(self, x: int, y: int) -> str:
        self._check_axis(x)
        self._check_axis(y)
        self.last_player = self.next_player()
        self._set_box(x, y)
        if self._is_winner():
            return f'The winner is {self.last_player}'
        return 'No winner!'

from typing import List


class TicTacToe:
    def __init__(self):
        self.board: List[List[str]] = [['-', '-', '-'],
                                       ['-', '-', '-'],
                                       ['-', '-', '-']]
        self.last_player: str = 'O'

    @staticmethod
    def _check_axis(axis: int) -> None:
        if axis < 1 or axis > 3:
            raise Exception('Outside the board')

    def _set_box(self, x: int, y: int) -> None:
        if self.board[y - 1][x - 1] == '-':
            self.board[y - 1][x - 1] = self.last_player
        else:
            raise Exception('Field is occupied')

    def next_player(self) -> str:
        if self.last_player == 'X':
            return 'O'
        else:
            return 'X'

    def _is_winner(self, x: int, y: int) -> bool:
        size: int = len(self.board)
        player_total: str = self.last_player * size
        horizontal = vertical = diagonal_t_b = diagonal_b_t = ''
        for index in range(size):
            horizontal += self.board[index][x - 1]
            vertical += self.board[y - 1][index]
            diagonal_t_b += self.board[index][index]
            diagonal_b_t += self.board[index][size - index - 1]
        if (horizontal == player_total or
                vertical == player_total or
                diagonal_t_b == player_total or
                diagonal_b_t == player_total):
            return True
        return False

    def _draw_board(self) -> None:
        [print(row) for row in self.board]
        print('\n')

    def _is_board_full(self) -> bool:
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == '-':
                    return False
        return True

    def play(self, x: int, y: int) -> str:
        self._check_axis(x)
        self._check_axis(y)
        self.last_player = self.next_player()
        self._set_box(x, y)
        self._draw_board()
        if self._is_winner(x, y):
            return f'The winner is {self.last_player}'
        elif self._is_board_full():
            return 'The result is draw!'
        return 'No winner!'

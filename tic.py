class TicTacToe:
    def __init__(self):
        self.board = [['O', 'O', 'O'],
                      ['O', 'O', 'O'],
                      ['O', 'O', 'O']]

    @staticmethod
    def _check_axis(axis: int) -> None:
        if axis < 1 or axis > 3:
            raise Exception('Outside the board')

    def _set_box(self, x: int, y: int) -> None:
        if self.board[x - 1][y - 1] == 'O':
            self.board[x - 1][y - 1] = 'X'
        else:
            raise Exception('Field is occupied')

    def play(self, x: int, y: int) -> None:
        self._check_axis(x)
        self._check_axis(y)
        self._set_box(x, y)

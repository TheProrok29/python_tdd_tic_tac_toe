class TicTacToe:
    def __init__(self):
        self.board = [['O', 'O', 'O'],
                      ['O', 'O', 'O'],
                      ['O', 'O', 'O']]

    def play(self, x: int, y: int) -> None:
        if x < 1 or x > 3:
            raise Exception('X outside the board')
        elif y < 1 or y > 3:
            raise Exception('Y outside the board')
        if self.board[x - 1][y - 1] == 'O':
            self.board[x - 1][y - 1] = 'X'
        else:
            raise Exception('Field is occupied')

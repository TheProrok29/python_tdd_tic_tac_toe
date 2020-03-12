class TicTacToe:

    def play(self, x: int, y: int) -> None:
        if x < 1 or x > 3:
            raise Exception('X outside the board')

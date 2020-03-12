class TicTacToe:

    def play(self, x: int, y: int) -> None:
        if x < 1 or x > 3:
            raise Exception('X outside the board')
        elif y < 1 or y > 3:
            raise Exception('Y outside the board')

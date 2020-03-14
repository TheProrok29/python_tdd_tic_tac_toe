class TickTackToeBean:
    def __init__(self, turn, x, y, player):
        self._turn = turn
        self._x = x
        self._y = y
        self._player = player

    def get_turn(self):
        return self._turn

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_player(self):
        return self._player

    def __eq__(self, other):
        if self == other:
            return True
        if other == None or type(self) != type(other):
            return False
        if self._player != other._player:
            return False
        if self._turn != other.turn:
            return False
        if self._x != other._x:
            return False
        if self._y != other._y:
            return False
        return True

    def __hash__(self):
        result = self._turn
        result = 31 * result + self._x
        result = 31 * result + self._y
        result = 31 * result + self._player
        return result

    def __str__(self):
        return f'Turn: {self._turn}; X: {self._x}; Y: {self._y}; Player: {self._player}'

from tic_tac_toe_bean import TickTackToeBean
import unittest


class TickTackToeBeanSpec(unittest.TestCase):

    def setUp(self) -> None:
        self.turn = 17
        self.x = 2
        self.y = 3
        self.player = 'X'
        self.bean = TickTackToeBean(self.turn, self.x, self.y, self.player)

    def test_when_created_then_id_is_stored(self):
        self.assertEqual(self.turn, self.bean.get_turn())

    def test_when_created_then_x_is_stored(self):
        self.assertEqual(self.x, self.bean.get_x())

    def test_when_created_then_y_is_stored(self):
        self.assertEqual(self.y, self.bean.get_y())

    def test_when_created_then_player_is_stored(self):
        self.assertEqual(self.player, self.bean.get_player())


if __name__ == '__main__':
    unittest.main()

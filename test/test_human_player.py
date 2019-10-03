from unittest import TestCase, main, mock
from xrudderai.human_player import HumanPlayer
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand

class TestHumanPlayer(TestCase):

    def setUp(self):
        self.humanplayer = HumanPlayer("x")

    def test_take_turn_place(self):
        with mock.patch('builtins.input', return_value="p b8"):
            assert isinstance(self.humanplayer.take_turn(), PlaceCommand)

    def test_take_turn_move(self):
        with mock.patch('builtins.input', return_value="m b8 b9"):
            assert isinstance(self.humanplayer.take_turn(), MoveCommand)

    def test_no_moves_left(self):
        self.humanplayer.move_count = 30
        self.humanplayer.tokens_left = 0
        self.assertEqual(self.humanplayer.has_moves_left(), False)

    def test_token_symbol(self):
        self.assertEqual(self.humanplayer.symbol, "x")

if __name__ == '__main__':
    main()
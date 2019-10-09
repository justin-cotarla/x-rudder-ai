from unittest import TestCase, main, mock
from xrudderai.human_player import HumanPlayer
from xrudderai.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand

class TestHumanPlayer(TestCase):

    def setUp(self):
        self.human_player = HumanPlayer("x")
        Player.MOVE_COUNT = 30

    def test_take_turn_place(self):
        with mock.patch('builtins.input', return_value="p b8"):
            assert isinstance(self.human_player.take_turn(), PlaceCommand)

    def test_take_turn_move(self):
        with mock.patch('builtins.input', return_value="m b8 b9"):
            assert isinstance(self.human_player.take_turn(), MoveCommand)

    def test_no_moves_left(self):
        Player.MOVE_COUNT = 0
        self.human_player.tokens_left = 0
        self.assertFalse(self.human_player.has_actions_left())

    def test_uneven_actions_left(self):
        Player.MOVE_COUNT = 0
        second_player = HumanPlayer("o")
        second_player.tokens_left = 0

        self.assertFalse(second_player.has_actions_left())
        self.assertTrue(self.human_player.has_actions_left())

    def test_token_symbol(self):
        self.assertEqual(self.human_player.symbol, "x")

if __name__ == '__main__':
    main()
from src.board import Board
from src.player import Player
from src.token import Token
import unittest

class BoardTests(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("x")
        self.player2 = Player("o")
        self.token1 = Token(self.player1)
        self.token2 = Token(self.player2)

        self.board = Board(10, 12)
        self.board.grid[8][8] = self.token1

    def test_no_winner(self):
        self.assertEqual(self.board.get_winner(), None)

    def test_winner(self):
        self.board.grid[2][2] = self.token1
        self.board.grid[4][2] = self.token1
        self.board.grid[3][3] = self.token1
        self.board.grid[2][4] = self.token1
        self.board.grid[4][4] = self.token1

        self.assertEqual(self.board.get_winner(), self.player1)

    def test_winner_but_strikethrough(self):
        self.board.grid[2][2] = self.token1
        self.board.grid[4][2] = self.token1
        self.board.grid[3][3] = self.token1
        self.board.grid[2][4] = self.token1
        self.board.grid[4][4] = self.token1

        self.board.grid[3][2] = self.token2
        self.board.grid[3][4] = self.token2

        self.assertEqual(self.board.get_winner(), None)

    def test_false_winner_pattern(self):
        self.board.grid[2][2] = self.token1
        self.board.grid[4][2] = self.token1
        self.board.grid[3][3] = self.token1
        self.board.grid[2][4] = self.token2
        self.board.grid[4][4] = self.token1

        self.assertEqual(self.board.get_winner(), None)

if __name__ == '__main__':
    unittest.main()
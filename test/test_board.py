from unittest import TestCase, mock, main
from xrudderai.board import Board

class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(10, 12)

        mock_player1 = mock.MagicMock()
        mock_player2 = mock.MagicMock()

        mock_token1 = mock.MagicMock()
        mock_token2 = mock.MagicMock()

        mock_token1.player = mock_player1
        mock_token1.__str__.return_value = "X"

        mock_token2.player = mock_player2
        mock_token2.__str__.return_value = "O"

        self.mock_player1 = mock_player1
        self.mock_player2 = mock_player2
        self.mock_token1 = mock_token1
        self.mock_token2 = mock_token2

    def test_place_token(self):
        self.board.place_token(self.mock_token1, 2, 4)
        
        self.assertEqual(self.board.grid[4][2], self.mock_token1)
        self.assertEqual(self.board.grid[4][3], None)

    def test_place_token_out_of_range(self):
        self.assertRaises(IndexError, self.board.place_token, self.mock_token1, 12, 4)

    def test_place_token_occupied(self):
        self.board.place_token(self.mock_token1, 2, 4)
        self.assertRaises(ValueError, self.board.place_token, self.mock_token1, 2, 4)

    def test_move_token(self):
        self.board.place_token(self.mock_token1, 2, 4)
        self.board.move_token(self.mock_player1, 2, 4, 3, 5)
        print(self.board)
        
        self.assertEqual(self.board.grid[5][3], self.mock_token1)
        self.assertEqual(self.board.grid[4][2], None)

    def test_move_token_non_existant_token(self):
        self.assertRaises(LookupError, self.board.move_token, self.mock_player1, 2, 4, 3, 5)

    def test_move_token_wrong_player(self):
        self.board.place_token(self.mock_token1, 2, 4)
        
        self.assertRaises(ValueError, self.board.move_token, self.mock_player2, 2, 4, 3, 5)


    def test_no_winner(self):
        self.assertEqual(self.board.get_winner(), None)

    def test_winner(self):
        self.board.grid[2][2] = self.mock_token1
        self.board.grid[4][2] = self.mock_token1
        self.board.grid[3][3] = self.mock_token1
        self.board.grid[2][4] = self.mock_token1
        self.board.grid[4][4] = self.mock_token1    

        self.assertEqual(self.board.get_winner(), self.mock_player1)

    def test_winner_but_strikethrough(self):
        self.board.grid[2][2] = self.mock_token1
        self.board.grid[4][2] = self.mock_token1
        self.board.grid[3][3] = self.mock_token1
        self.board.grid[2][4] = self.mock_token1
        self.board.grid[4][4] = self.mock_token1

        self.board.grid[3][2] = self.mock_token2
        self.board.grid[3][4] = self.mock_token2

        self.assertEqual(self.board.get_winner(), None)

if __name__ == '__main__':
    main()
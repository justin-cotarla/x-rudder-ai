from src.player import Player
from src.token import Token

class Board:

    grid = []
    rows = 0
    columns = 0

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[None]*columns for n in range(rows)]

    def get_winner(self):
        for row in range(self.rows - 2):
            for column in range(self.columns - 2):
                token_topleft = self.grid[row][column]
                token_topright = self.grid[row][column + 2]
                token_middle = self.grid[row + 1][column + 1]
                token_bottomright = self.grid[row + 2][column]
                token_bottomleft = self.grid[row + 2][column + 2]

                token_middleleft = self.grid[row + 1][column]
                token_middleright = self.grid[row + 1][column + 2]

                x = [token_topleft, token_topright, token_middle, token_bottomright, token_bottomleft]
                if any(token is None for token in x):
                    continue

                possible_winning_player = token_topleft.player
                if possible_winning_player == token_topright.player == token_middle.player == token_bottomright.player == token_bottomleft.player:
                    if (token_middleleft is None) | (token_middleright is None):
                        return possible_winning_player
                    if (token_middleleft.player == possible_winning_player) & (token_middleright.player == possible_winning_player):
                        return possible_winning_player

        return None
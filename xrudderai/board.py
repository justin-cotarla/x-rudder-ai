from xrudderai.player import Player
from xrudderai.token import Token


class Board:
    ASCII_A = 65

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[None] * columns for n in range(rows)]

    def __str__(self):
        output = "\n    ┌"

        for idx in range(self.columns * 2 - 1):
            output = output + ("───" if idx % 2 == 0 else "┬")

        output = output + "┐\n"

        for row_idx, row in reversed(list(enumerate(self.grid))):

            row_label = row_idx + 1
            output = output + " {} │".format(row_label if row_label >= 10 else "{} ".format(row_label))

            for token_idx, token in enumerate(row):
                output = output + (" {} ".format(str(token)) if token else "   ")
                output = output + "│"

            output = output + "\n"
            if row_idx != 0:
                output = output + "    ├"
                for idx in range(self.columns * 2 - 1):
                    output = output + ("───" if idx % 2 == 0 else "┼")
                output = output + "┤\n"

        output = output + "    └"
        for idx in range(self.columns * 2 - 1):
            output = output + ("───" if idx % 2 == 0 else "┴")

        output = output + "┘\n    "

        for letter in list(map(chr, range(self.ASCII_A, self.ASCII_A + self.columns))):
            output = output + "  {} ".format(letter)

        return output

    def place_token(self, token, x, y):
        if x < 0 or x >= self.columns or y < 0 or y >= self.rows:
            raise IndexError("Position is out of bounds.")

        if self.grid[y][x] != None:
            raise ValueError("Position is already occupied.")

        self.grid[y][x] = token

    def move_token(self, player, x1, y1, x2, y2):
        token = self.grid[y1][x1]
        if token == None:
            raise LookupError("Token does not exist")

        if player != token.player:
            raise ValueError("Token does not belong to player")

        if x1 - x2 == 0 and y1 - y2 == 0:
            raise ValueError("Null move")

        if abs(x1 - x2) > 1 or abs(y1 - y2) > 1:
            raise ValueError("Token move out of range")

        self.place_token(token, x2, y2)
        self.grid[y1][x1] = None

    def get_winner(self):
        for row in range(self.rows - 2):
            for column in range(self.columns - 2):
                token_top_left = self.grid[row][column]
                token_top_right = self.grid[row][column + 2]
                token_middle = self.grid[row + 1][column + 1]
                token_bottom_right = self.grid[row + 2][column + 2]
                token_bottom_left = self.grid[row + 2][column]

                token_middle_left = self.grid[row + 1][column]
                token_middle_right = self.grid[row + 1][column + 2]

                x = [token_top_left, token_top_right, token_middle, token_bottom_right, token_bottom_left]
                if any(token is None for token in x):
                    continue

                possible_winning_player = token_top_left.player
                if all(token.player == possible_winning_player for token in x):
                    if (token_middle_left is None) or (token_middle_right is None):
                        return possible_winning_player
                    if (token_middle_left.player == possible_winning_player) or (
                            token_middle_right.player == possible_winning_player):
                        return possible_winning_player

        return None

    def calculate_heuristic(self, player, opponent):

        # positive means player is winning
        # negative means opponent is winning

        heuristic = 0
        for row in range(self.rows - 2):
            for column in range(self.columns - 2):

                # calculate heuristic for local 3x3

                token_top_left = self.grid[row][column]
                token_top_right = self.grid[row][column + 2]
                token_middle = self.grid[row + 1][column + 1]
                token_bottom_right = self.grid[row + 2][column + 2]
                token_bottom_left = self.grid[row + 2][column]

                token_middle_left = self.grid[row + 1][column]
                token_middle_right = self.grid[row + 1][column + 2]

                winning_positions = [token_top_left, token_top_right, token_middle, token_bottom_right, token_bottom_left]
                horizontal_positions = [token_middle_left, token_middle_right]

                # Step 1 - keep a count of tokens from each player in 3x3 in winning positions

                winning_player_count = 0
                winning_opponent_count = 0
                for token in winning_positions:
                    if token is None:
                        continue
                    if token.player == opponent:
                        winning_opponent_count += 1
                    if token.player == player:
                        winning_player_count += 1

                # Step 2 - if both player and opponent have tokens in winning positions, skip this 3x3

                if winning_player_count > 0 and winning_opponent_count > 0:
                    continue

                # Step 3 - keep a count of tokens from each player in horizontal positions

                horizontal_opponent_count = 0
                horizontal_player_count = 0
                for token in horizontal_positions:
                    if token is None:
                        continue
                    if token.player == opponent:
                        horizontal_opponent_count += 1
                    if token.player == player:
                        horizontal_player_count += 1

                # Step 4 - return if this is a winning 3x3

                # Player win
                if winning_player_count == 5 and horizontal_opponent_count != 2:
                    return float('inf')

                # Opponent win
                if winning_opponent_count == 5 and horizontal_player_count != 2:
                    return float('-inf')

                # Step 5

                player_heuristic = 0
                opponent_heuristic = 0

                if horizontal_opponent_count != 2:
                    player_heuristic = (10 ** (winning_player_count + horizontal_player_count))

                if horizontal_player_count != 2:
                    opponent_heuristic = (10 ** (winning_opponent_count + horizontal_opponent_count))

                # include negation - IRINA
                heuristic += player_heuristic - opponent_heuristic

        return heuristic

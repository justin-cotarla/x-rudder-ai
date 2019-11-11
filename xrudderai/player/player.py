from abc import ABC, abstractmethod
from xrudderai.move_command import MoveCommand
from xrudderai.place_command import PlaceCommand
from xrudderai.config import GAME_COLUMNS, GAME_ROWS

class Player(ABC):

    move_count = 30

    def __init__(self, symbol):
        self.symbol = symbol
        self.tokens_left = 15
        super().__init__()

    @abstractmethod
    def take_turn(self):
        pass

    def placed_token(self):
        self.tokens_left -= 1

    def moved_token(self):
        Player.move_count -= 1

    def has_actions_left(self):
        return self.tokens_left > 0 or Player.move_count > 0

    def _is_in_bounds(self, x, y):
        return (x >= 0 and
            x <= GAME_COLUMNS - 1 and
            y >= 0 and
            y <= GAME_ROWS - 1)

    def _determine_possible_moves(self, grid):
        moves = []

        for x in range(GAME_COLUMNS):
            for y in range(GAME_ROWS):
                # Placing tokens
                if grid[y][x] == None and self.tokens_left > 0:
                    moves.append(PlaceCommand(x, y))
                    continue

                # Moving tokens in all possible configurations
                if grid[y][x] != None and grid[y][x].player == self and Player.move_count > 0:
                    for sx in range(x-1, x+3):
                        for sy in range(y-1, y+3):
                            if self._is_in_bounds(sx, sy) and grid[sy][sx] == None:
                                moves.append(MoveCommand(x, y, sx, sy))
        return moves
from abc import ABC, abstractmethod
from xrudderai.move_command import MoveCommand
from xrudderai.place_command import PlaceCommand

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

    def _determine_possible_moves(self, grid):
        moves = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Placing tokens
                if grid[i][j] == None and self.tokens_left > 0:
                    moves.append(PlaceCommand(j, i))
                    continue

                # Moving tokens
                if grid[i][j] != None and grid[i][j].player == self and Player.move_count > 0:
                    # Move up
                    if i > 0 and grid[i-1][j] == None:
                        moves.append(MoveCommand(j, i, j, i-1))

                    if i < len(grid) - 1 and grid[i+1][j] == None:
                        moves.append(MoveCommand(j, i, j, i+1))

                    if j > 0 and grid[i][j-1] == None:
                        moves.append(MoveCommand(j, i, j-1, i))
                        
                    if j < len(grid[i]) - 1 and grid[i][j+1] == None:
                        moves.append(MoveCommand(j, i, j+1, i))
                        
        return moves
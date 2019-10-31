from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand
import random

class AIPlayer(Player):
    def __init__(self, symbol, board):
        self.board = board
        super().__init__(symbol)

    def take_turn(self):
        return PlaceCommand('a', '1')

    # Use Depth-Limited Search with Cutoff = n
    def __search_next_states(self, state, n):
        pass

    def __heuristic(self, square):
        return random.randint(0, 100)



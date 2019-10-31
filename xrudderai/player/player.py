from abc import ABC, abstractmethod

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
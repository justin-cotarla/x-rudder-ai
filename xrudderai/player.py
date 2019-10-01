from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, symbol):
        self.symbol = symbol
        self.move_count = 0
        self.tokens_left = 15
        super().__init__()

    @abstractmethod
    def take_turn(self):
        pass

    def has_moves_left(self):
        return self.tokens_left > 0 or self.move_count < 30
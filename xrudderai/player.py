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

    def placed_token(self):
        self.tokens_left -= 1

    def moved_token(self):
        self.move_count += 1

    def can_place_token(self):
        return self.tokens_left > 0

    def can_move_token(self):
        return self.move_count < 30

    def has_moves_left(self):
        return self.can_place_token() or self.can_move_token()
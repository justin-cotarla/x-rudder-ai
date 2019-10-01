<<<<<<< HEAD
from abc import ABC, abstractmethod

class Player(ABC):

    move_count = 0
    tokens_left = 15
    symbol = ''

    def __init__(self, symbol):
        self.symbol = symbol
        super().__init__()

    @abstractmethod
    def take_turn(self):
        pass

    def has_moves_left(self):
        if (self.tokens_left > 0 or self.move_count < 30):
            return True
        else:
            return False
=======
class Player():
    symbol = ''

    def __init__(self, symbol):
        self.symbol = symbol
>>>>>>> 53df92aa30bcf20d9f125fbafd3cb2f2455d5c31

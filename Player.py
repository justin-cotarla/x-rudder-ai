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
    
    
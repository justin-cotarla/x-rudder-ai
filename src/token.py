from src.player import Player

class Token:
    player = Player('x')

    def __init__(self, player):
        self.player = player

    def __str__(self):
        print(self.player.symbol)
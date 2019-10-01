from xrudderai.player import Player

class Token:

    def __init__(self, player):
        #player = Player('x')
        self.player = player

    def __str__(self):
        return self.player.symbol

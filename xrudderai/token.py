from xrudderai.humanplayer import HumanPlayer

class Token:
    player = HumanPlayer('x')

    def __init__(self, player):
        self.player = player

    def __str__(self):
        print(self.player.symbol)

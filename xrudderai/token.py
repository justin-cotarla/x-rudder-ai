class Token:

    def __init__(self, player):
        self.player = player

    def __str__(self):
        return self.player.symbol

from humanplayer import HumanPlayer

class Token:
    player = HumanPlayer('x')

    def __init__(self, player):
        self.player = player

    def __str__(self):
        return self.player.symbol


# human = HumanPlayer('x')
# token = Token(human)

# print(token.__str__())
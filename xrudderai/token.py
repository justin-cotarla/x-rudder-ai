<<<<<<< HEAD
from humanplayer import HumanPlayer

class Token:
    player = HumanPlayer('x')
=======
from xrudderai.player import Player

class Token:
    player = Player('x')
>>>>>>> 53df92aa30bcf20d9f125fbafd3cb2f2455d5c31

    def __init__(self, player):
        self.player = player

    def __str__(self):
<<<<<<< HEAD
        return self.player.symbol


# human = HumanPlayer('x')
# token = Token(human)

# print(token.__str__())
=======
        print(self.player.symbol)
>>>>>>> 53df92aa30bcf20d9f125fbafd3cb2f2455d5c31

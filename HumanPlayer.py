from Player import Player
import re

class HumanPlayer(Player):

    def take_turn(self):
        
        turn = ''
        while turn == '':
            turn = input("Play your turn: ")

            place = re.search("[p] [a-mA-M](1[0]|[1-9])$", turn)
            move = re.search("[m] [a-mA-M](1[0]|[1-9])[ ][a-mA-M](1[0]|[1-9])$", turn)

            if (place):
                print("You would like to place your token")
                return turn
            elif (move):
                print("You would like to move your token")
                return turn
            else:
                print("Invalid move, please try again.")
                turn = ''

#human = HumanPlayer('x')
#human.take_turn()

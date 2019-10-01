from player import Player
from placecommand import PlaceCommand
from movecommand import MoveCommand
import re

class HumanPlayer(Player):

    def take_turn(self):
        
        while True:
            turn = input("Please enter your turn: ")

            place = re.search("[p] [a-mA-M](1[0]|[1-9])$", turn)
            move = re.search("[m] [a-mA-M](1[0]|[1-9])[ ][a-mA-M](1[0]|[1-9])$", turn)
            command = turn.split()

            if (place):
                coord = command[1]
                x = coord[0:1]
                y = coord[1:]
                return PlaceCommand(x, y)
            elif (move):
                source = command[1]
                target = command[2]
                source_x = source[0:1]
                source_y = source[1:]
                target_x = target[0:1]
                target_y = target[1:]
                return MoveCommand(source_x, source_y, target_x, target_y)
            else:
                print("Invalid move, please try again.\n")

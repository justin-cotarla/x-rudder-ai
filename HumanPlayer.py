from player import Player
#from placecommand import PlaceCommand
#from movecommand import MoveCommand
import re

class HumanPlayer(Player):

    def take_turn(self):
        
        turn = ''
        while turn == '':
            turn = input("Play your turn: ")

            place = re.search("[p] [a-mA-M](1[0]|[1-9])$", turn)
            move = re.search("[m] [a-mA-M](1[0]|[1-9])[ ][a-mA-M](1[0]|[1-9])$", turn)
            command = turn.split()

            if (place):
                print("You would like to place your token")
                coord = command[1]
                x = coord[0:1]
                y = coord[1:]
                #return PlaceCommand(x, y)
                print("x: "+x+", y: "+ y)
            elif (move):
                print("You would like to move your token")
                source = command[1]
                target = command[2]
                source_x = source[0:1]
                source_y = source[1:]
                target_x = target[0:1]
                target_y = target[1:]
                #return MoveCommand(source_x, source_y, target_x, targey_y)
                print("source x: "+source_x+" and source y: "+source_y+"\ntarget x: "+target_x+" and target y: "+target_y)
            else:
                print("Invalid move, please try again.")
                turn = ''
                command = ''

player = HumanPlayer('x')
player.take_turn()
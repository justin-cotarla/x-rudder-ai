from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand
import re

class HumanPlayer(Player):

    def take_turn(self):
        
        while True:
            turn = input("Please enter your turn: ")

            place = re.search("[p] [a-mA-M](1[0]|[1-9])$", turn)
            move = re.search("[m] [a-mA-M](1[0]|[1-9]) [a-mA-M](1[0]|[1-9])$", turn)
            command = turn.split()

            if place:
                if self.tokens_left > 0:
                    coord = command[1]
                    x = coord[0]
                    y = coord[1:]
                    return PlaceCommand(x, y)
                
                print('You are out of tokens.')
            elif move:
                if Player.move_count > 0:
                    source = command[1]
                    target = command[2]
                    source_x = source[0]
                    source_y = source[1:]
                    target_x = target[0]
                    target_y = target[1:]
                    return MoveCommand(source_x, source_y, target_x, target_y)

                print('You are out of moves.')
            else:
                print("Invalid move, please try again.\n")

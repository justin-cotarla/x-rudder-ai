import random
from xrudderai.board import Board
from xrudderai.player.ai_player import AIPlayer
from xrudderai.player.human_player import HumanPlayer
from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.token import Token
from xrudderai.config import GAME_COLUMNS, GAME_ROWS, PLAYER_1_COLOUR, PLAYER_2_COLOUR, DEFAULT_COLOUR

# For fun
MANUAL = '1'
AUTOMATIC = '2'

class Game:
    def __init__(self, mode, human_start):
        self.board = Board(GAME_ROWS, GAME_COLUMNS)
        # Index 0 for Player 1, index 1 for Player 2
        self.current_player = 0

        if mode == '1':
            self.players = (
                HumanPlayer("o", PLAYER_1_COLOUR),
                HumanPlayer("o", PLAYER_2_COLOUR)
            )
        else:
            opponent = HumanPlayer("o", PLAYER_1_COLOUR)
            self.players = (
                AIPlayer("o", PLAYER_2_COLOUR, self.board, opponent),
                opponent
            )

            if human_start:
                self.players = tuple(reversed(self.players))

    def start(self):
        while self.__is_game_over() == False:
            try:
                player = self.players[self.current_player]

                print(self.board)
                print("{}****** Player {}'s turn ******{}".format(
                    player.colour,
                    self.current_player + 1,
                    DEFAULT_COLOUR
                ))
                print("Tokens left: {}\nMoves left: {}\n".format(player.tokens_left, Player.move_count))

                self.__play_turn(player)

                if self.players[1 - self.current_player].has_actions_left():
                    self.current_player = 1 - self.current_player
            except Exception as e:
                print("Error: {}".format(e))
       
    def __play_turn(self, player):
        player_move = player.take_turn()
            
        if isinstance(player_move, PlaceCommand):
            token = Token(player)
            self.board.place_token(token, player_move.target_x, player_move.target_y)
            player.placed_token()
        else:
            self.board.move_token(
                player,
                player_move.source_x,
                player_move.source_y,
                player_move.target_x,
                player_move.target_y,
            )
            player.moved_token()

    def __is_game_over(self):
        winner = self.board.get_winner()
        if winner:
            # Display final state of the board
            print(self.board)
            print(f"\nPlayer {self.players.index(winner) + 1} wins!")
            return True
        
        # Check if it is a draw
        player1 = self.players[0]
        player2 = self.players[1]
        if not player1.has_actions_left() and not player2.has_actions_left():
            # Display final state of the board
            print(self.board)
            print("\nThe game has ended in a draw.")
            return True

        return False
          

if __name__ == '__main__':
    print('''
    ┌────────────────────────────────────────────────────┐
    │                     WELCOME TO                     │
    │                                                    │
    │        )       (                                   │ 
    │     ( /(       )\ )        (     (                 │ 
    │     )\())     (()/(   (    )\ )  )\ )   (   (      │ 
    │    ((_)\  ___  /(_)) ))\  (()/( (()/(  ))\  )(     │ 
    │    __((_)|___|(_))  /((_)  ((_)) ((_))/((_)(()\    │ 
    │    \ \/ /     | _ \(_))(   _| |  _| |(_))   ((_)   │ 
    │     >  <      |   /| || |/ _` |/ _` |/ -_) | '_|   │ 
    │    /_/\_\     |_|_\ \_,_|\__,_|\__,_|\___| |_|     │
    │                                                    │
    │               (╯°□°)╯︵ ┻━┻ ﾉ(°-°ﾉ)                │
    │                                                    │
    └────────────────────────────────────────────────────┘

    To play a turn, use "p <x><y>" to place a token or "m <x1><y1> <x2><y2>" to move a token.

    Please select a mode to begin:
    * [1] Manual
    * [2] Automatic
    ''')

    while True:
        mode = input('Enter game mode (1 or 2): ')
        if mode == MANUAL or mode == AUTOMATIC:
            break

        print('Sorry, this is not a valid mode. Please try again.\n')

    human_start = True
    if mode == AUTOMATIC:
        while True:
            selection = input('''
    Enter starting player:
    * [1] Human
    * [2] AI
    * [3] Random
    ''')

            if selection == '1':
                human_start = True
                break
            elif selection == '2':
                human_start = False
                break
            elif selection == '3':
                human_start = random.choice([True, False])
                break
            else:
                print('Sorry, this is not a valid selection. Please try again.\n')

    game = Game(mode, human_start)
    game.start()

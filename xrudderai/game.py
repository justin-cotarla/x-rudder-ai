from xrudderai.board import Board
from xrudderai.human_player import HumanPlayer
from xrudderai.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.token import Token

# For fun
TEXT_COLOUR = ('\033[92m', '\033[94m', '\033[0m')

class Game:
    def __init__(self, mode):
        self.players = (
            HumanPlayer("{}o{}".format(TEXT_COLOUR[0], TEXT_COLOUR[2])),
            HumanPlayer("{}o{}".format(TEXT_COLOUR[1], TEXT_COLOUR[2]))
        )
        self.board = Board(10, 12)
        # Index 0 for Player 1, index 1 for Player 2
        self.current_player = 0

    def start(self):
        while self.__is_game_over() == False:
            try:
                player = self.players[self.current_player]

                print(self.board)
                print("{}****** Player {}'s turn ******{}".format(
                    TEXT_COLOUR[self.current_player],
                    self.current_player + 1,
                    TEXT_COLOUR[2]
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
    * [2] Automatic (Coming Soon)
    ''')

    while True:
        mode = input('Enter game mode (1 or 2): ').lower()
        if mode == '1':
            break

        print('Sorry, this is not a valid mode. Please try again.\n')
    
    game = Game(mode)
    game.start()

from xrudderai.board import Board
from xrudderai.human_player import HumanPlayer
from xrudderai.place_command import PlaceCommand
from xrudderai.token import Token

class Game:
    def __init__(self, mode):
        if mode == 'manual':
            self.players = [HumanPlayer('x'), HumanPlayer('o')]
            self.board = Board(10, 12)
            # Index 0 for Player 1, index 1 for Player 2
            self.current_player = 0

    def start(self):
        while self.__is_game_over() == False:
            try:
                player = self.players[self.current_player]
                print(self.board)
                print("\n****** Player {}'s turn ******".format(self.current_player + 1))
                print("Tokens left: {}\nMoves left: {}\n".format(player.tokens_left, 30 - player.move_count))

                self.__play_turn(player)

                if self.players[1 - self.current_player].has_moves_left:
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
            print(f"Player {self.players.index(winner) + 1} wins!")
            return True
        
        # Check if it is a draw
        player1 = self.players[0]
        player2 = self.players[1]
        if not player1.has_moves_left() and not player2.has_moves_left():
            print("The game has ended in a draw.")
            return True

        return False
          

if __name__ == '__main__':
    print('''
    +----------------------------------------------------+
    |                     WELCOME TO                     |
    |                                                    |
    |        )       (                                   | 
    |     ( /(       )\ )        (     (                 | 
    |     )\())     (()/(   (    )\ )  )\ )   (   (      | 
    |    ((_)\  ___  /(_)) ))\  (()/( (()/(  ))\  )(     | 
    |    __((_)|___|(_))  /((_)  ((_)) ((_))/((_)(()\    | 
    |    \ \/ /     | _ \(_))(   _| |  _| |(_))   ((_)   | 
    |     >  <      |   /| || |/ _` |/ _` |/ -_) | '_|   | 
    |    /_/\_\     |_|_\ \_,_|\__,_|\__,_|\___| |_|     |
    |                                                    |
    |               (╯°□°)╯︵ ┻━┻ ﾉ(°-°ﾉ)                |
    |                                                    |
    +----------------------------------------------------+

    Please select a mode to begin:
    * Manual
    * Automatic (Coming Soon)
    ''')

    mode = input('Enter game mode: ').lower()
    
    if mode != 'manual':
        print('Sorry, this is not a valid mode. Please try again.')
        exit()

    game = Game(mode)
    game.start()


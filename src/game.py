
class Game:
    def __init__(self, mode: str) -> None:
        if mode == 'manual':
            self.players = [Player(), Player()]
            self.board = Board()
            # Index 0 for Player 1, index 1 for Player 2
            self.current_player = 0

    def start(self) -> None:
        while self.__is_game_over() == False:
            player_move = self.players[self.current_player].take_turn()
            # If placing token
            
            # If moving token

            print(self.board)
            self.current_player = 1 - self.current_player

    def __is_game_over(self) -> bool:
        winner = self.board.get_winner()
        if winner:
            print(f"Player {self.players.index(winner) + 1} wins!")
            return True
        
        # Check if it is a draw
        player1 = self.players[0]
        player2 = self.players[1]
        if (
            player1.tokens_left == 15 and
            player2.tokens_left == 15 and
            player1.move_count == 30 and
            player2.move_count == 30
        ):
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

    mode = input().lower()
    
    if mode != 'manual':
        print('Sorry, this is not a valid mode. Please try again.')
        exit()

    game = Game(mode)
    game.start()


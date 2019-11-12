from xrudderai.board import Board
from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand
from xrudderai.token import Token
import random
import sys
import time

class AIPlayer(Player):
    def __init__(self, symbol, board, opponent):
        self.board = board
        self.opponent = opponent
        super().__init__(symbol)

    def take_turn(self):
        start = time.time()

        depth = 2
        best_move = None
        best_score = -sys.maxsize

        possible_moves = self._determine_possible_moves(self.board.grid)
        for move in possible_moves:
            score = 0
            if isinstance(move, PlaceCommand):
                self.board.grid[move.target_y][move.target_x] = Token(self)
                score = self.__minimax(self.board.grid, depth - 1, False)
                # score = self.__alpha_beta_prune(self.board.grid, depth - 1, False, -sys.maxsize, sys.maxsize)
                self.board.grid[move.target_y][move.target_x] = None
            else:
                self.board.grid[move.source_y][move.source_x] = None
                self.board.grid[move.target_y][move.target_x] = Token(self)
                score = self.__minimax(self.board.grid, depth - 1, False)
                # score = self.__alpha_beta_prune(self.board.grid, depth - 1, False, -sys.maxsize, sys.maxsize)
                self.board.grid[move.target_y][move.target_x] = None
                self.board.grid[move.source_y][move.source_x] = Token(self)

            if score > best_score:
                best_move = move
                best_score = score
            
        print("Time to make move: {}".format(time.time() - start))
        return best_move

    def __minimax(self, grid, depth, maximizing):
        if depth == 0:
            return self.__calculate_heuristic(grid)

        if maximizing:
            heuristic = 0
            score = -sys.maxsize
            possible_moves = self._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, False)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, False)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self)

                score = max(heuristic, score)
        else:
            heuristic = 0
            score = sys.maxsize
            possible_moves = self.opponent._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self.opponent)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self.opponent)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self.opponent)

                score = min(heuristic, score)

        return score

    def __alpha_beta_prune(self, grid, depth, maximizing, a, b):
        if depth == 0:
            return self.__calculate_heuristic(grid)

        if maximizing:
            heuristic = 0
            score = -sys.maxsize
            possible_moves = self._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__alpha_beta_prune(self.board.grid, depth - 1, False, a, b)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__alpha_beta_prune(self.board.grid, depth - 1, False, a, b)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self)

                score = max(heuristic, score)
                a = max(heuristic, a)
                if b <= a:
                    break
        else:
            heuristic = 0
            score = sys.maxsize
            possible_moves = self.opponent._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self.opponent)
                    heuristic = self.__alpha_beta_prune(self.board.grid, depth - 1, True, a, b)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self.opponent)
                    heuristic = self.__alpha_beta_prune(self.board.grid, depth - 1, True, a, b)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self.opponent)

                score = min(heuristic, score)
                b = min(heuristic, b)
                if b <= a:
                    break

        return score

    def __calculate_heuristic(self, grid):
        # positive means player is winning
        # negative means opponent is winning

        heuristic = 0
        for row in range(len(grid) - 2):
            for column in range(len(grid[row]) - 2):

                token_top_left = grid[row][column]
                token_top_right = grid[row][column + 2]
                token_middle = grid[row + 1][column + 1]
                token_bottom_right = grid[row + 2][column + 2]
                token_bottom_left = grid[row + 2][column]

                token_middle_left = grid[row + 1][column]
                token_middle_right = grid[row + 1][column + 2]

                winning_positions = [token_top_left, token_top_right, token_middle, token_bottom_right, token_bottom_left]
                horizontal_positions = [token_middle_left, token_middle_right]

                # Step 1 - keep a count of tokens from each player in 3x3 in winning positions - if both player and opponent have tokens in winning positions, skip this 3x3

                winning_player_count = 0
                winning_opponent_count = 0

                for token in winning_positions:
                    if token is None:
                        continue
                    if token.player != self:
                        winning_opponent_count += 1
                    if token.player == self:
                        winning_player_count += 1
                    if winning_player_count > 0 and winning_opponent_count > 0:
                        continue


                # Step 2 - keep a count of tokens from each player in horizontal positions

                horizontal_opponent_count = 0
                horizontal_player_count = 0
                
                for token in horizontal_positions:
                    if token is None:
                        continue
                    if token.player != self:
                        horizontal_opponent_count += 1
                    if token.player == self:
                        horizontal_player_count += 1

                # Step 3 - return if this is a winning 3x3

                # Player win
                if winning_player_count == 5 and horizontal_opponent_count != 2:
                    return float('inf')

                # Opponent win
                if winning_opponent_count == 5 and horizontal_player_count != 2:
                    return float('-inf')

                # Step 4

                player_heuristic = 0
                opponent_heuristic = 0

                if horizontal_opponent_count != 2:
                    player_heuristic = (10 ** winning_player_count) + (10 ** horizontal_player_count)

                if horizontal_player_count != 2:
                    opponent_heuristic = (10 ** winning_opponent_count) + (10 ** horizontal_opponent_count)

                heuristic += player_heuristic - opponent_heuristic

        return heuristic

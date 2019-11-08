from xrudderai.board import Board
from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand
from xrudderai.token import Token
import random
import sys

class AIPlayer(Player):
    def __init__(self, symbol, board, opponent):
        self.board = board
        self.opponent = opponent
        super().__init__(symbol)

    def take_turn(self):
        depth = 3
        best_move = None
        best_score = 0
        possible_moves = self._determine_possible_moves(self.board.grid)

        for move in possible_moves:
            score = 0
            if isinstance(move, PlaceCommand):
                self.board.grid[move.target_y][move.target_x] = Token(self)
                score = self.__minimax(self.board.grid, depth, True)
                # score = self.__alpha_beta_prune(self.board.grid, depth, True, -sys.maxsize, sys.maxsize)
                self.board.grid[move.target_y][move.target_x] = None
            else:
                self.board.grid[move.source_y][move.source_x] = None
                self.board.grid[move.target_y][move.target_x] = Token(self)
                score = self.__minimax(self.board.grid, depth, True)
                # score = self.__alpha_beta_prune(self.board.grid, depth, True, -sys.maxsize, sys.maxsize)
                self.board.grid[move.target_y][move.target_x] = None
                self.board.grid[move.source_y][move.source_x] = Token(self)

            if score > best_score:
                best_move = move
                best_score = score
            

        return best_move

    def __minimax(self, grid, depth, maximizing):
        if depth == 0:
            return self.__calculate_heuristic(grid)

        if maximizing:
            heuristic = 0
            score = -sys.maxsize
            possible_moves = self.opponent._determine_possible_moves(grid)
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
            possible_moves = self._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self)

                score = min(heuristic, score)

        return score

    def __alpha_beta_prune(self, grid, depth, maximizing, a, b):
        if depth == 0:
            return self.__calculate_heuristic(grid)

        if maximizing:
            heuristic = 0
            score = -sys.maxsize
            possible_moves = self.opponent._determine_possible_moves(grid)
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
                a = max(heuristic, a)
                if b < a:
                    break
        else:
            heuristic = 0
            score = sys.maxsize
            possible_moves = self._determine_possible_moves(grid)
            for move in possible_moves:
                if isinstance(move, PlaceCommand):
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                else:
                    self.board.grid[move.source_y][move.source_x] = None
                    self.board.grid[move.target_y][move.target_x] = Token(self)
                    heuristic = self.__minimax(self.board.grid, depth - 1, True)
                    self.board.grid[move.target_y][move.target_x] = None
                    self.board.grid[move.source_y][move.source_x] = Token(self)

                score = min(heuristic, score)
                b = min(heuristic, b)
                if b < a:
                    break

        return score

    def __calculate_heuristic(self, board):
        return random.randint(0, 100)

    def __move_and_execute(self, move, fn):
        score = 0
        if isinstance(move, PlaceCommand):
            self.board.grid[move.target_y][move.target_x] = Token(self)
            score = fn
            self.board.grid[move.target_y][move.target_x] = None
        else:
            self.board.grid[move.source_y][move.source_x] = None
            self.board.grid[move.target_y][move.target_x] = Token(self)
            score = fn
            self.board.grid[move.target_y][move.target_x] = None
            self.board.grid[move.source_y][move.source_x] = Token(self)

        return score
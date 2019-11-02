from xrudderai.player.player import Player
from xrudderai.place_command import PlaceCommand
from xrudderai.move_command import MoveCommand
import random

class AIPlayer(Player):
    def __init__(self, symbol, board):
        self.board = board
        super().__init__(symbol)

    def take_turn(self):
        return PlaceCommand('a', '1')

    def __minimax(self, board, depth, maximizing):
        if depth == 0:
            return self.__calculate_heuristic(board)

        if maximizing:
            score = -sys.maxsize
            possible_moves = []
            for move in possible_moves:
                heuristic = self.__minimax(board, depth - 1, False)
                score = max(heuristic, score)

            return score

        score = sys.maxsize
        possible_moves = []
        for move in possible_moves:
            heuristic = self.__minimax(board, depth - 1, True)
            score = min(heuristic, score)

        return score

    def __alpha_beta_prune(self, board, depth, maximizing, a, b):
        if depth == 0:
            return self.__calculate_heuristic(board)

        if maximizing:
            score = -sys.maxsize
            possible_moves = self.__determine_possible_moves()
            for move in possible_moves:
                heuristic = self.__alpha_beta_prune(board, depth - 1, False)
                score = max(heuristic, score)
                a = max(heuristic, a)
                if b < a:
                    break

            return score

        score = sys.maxsize
        possible_moves = self.__determine_possible_moves()
        for move in possible_moves:
            heuristic = self.__alpha_beta_prune(board, depth - 1, True)
            score = min(heuristic, score)
            b = min(heuristic, b)
            if b < a:
                break

        return score

    def __determine_possible_moves(self):
        return []

    def __calculate_heuristic(self, board):
        return random.randint(0, 100)

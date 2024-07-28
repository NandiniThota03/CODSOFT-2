import math
import random

class TicTacToeAI:
    def __init__(self):
        self.player = 'O'
        self.ai = 'X'

    def minimax(self, board, depth, is_maximizing):
        scores = {'X': 1, 'O': -1, 'tie': 0}

        winner = self.check_winner(board)
        if winner != ' ':
            return scores[winner]

        if self.is_full(board):
            return scores['tie']

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves(board):
                board[move] = self.ai
                score = self.minimax(board, depth + 1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves(board):
                board[move] = self.player
                score = self.minimax(board, depth + 1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def best_move(self, board):
        best_score = -math.inf
        move = None
        for i in self.available_moves(board):
            board[i] = self.ai
            score = self.minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
        return move

    def check_winner(self, board):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] and board[a] != ' ':
                return board[a]
        return ' '

    def available_moves(self, board):
        return [i for i in range(9) if board[i] == ' ']

    def is_full(self, board):
        return all(cell != ' ' for cell in board)

from ai import TicTacToeAI

class TicTacToeGame:
    def __init__(self):
        self.board = [' '] * 9
        self.ai = TicTacToeAI()
        self.current_player = 'X'  # AI starts first

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if not self.is_game_over():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'X':
                    self.ai_move()

    def ai_move(self):
        position = self.ai.best_move(self.board)
        if position is not None:
            self.board[position] = 'X'
            self.current_player = 'O'

    def is_game_over(self):
        winner = self.ai.check_winner(self.board)
        if winner != ' ':
            return True
        if ' ' not in self.board:
            return True
        return False

    def get_winner(self):
        return self.ai.check_winner(self.board)

    def get_board(self):
        return self.board

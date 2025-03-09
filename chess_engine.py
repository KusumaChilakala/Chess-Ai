import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def get_legal_moves(self):
        return list(self.board.legal_moves)

    def make_move(self, move_uci):
        move = chess.Move.from_uci(move_uci)
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def is_game_over(self):
        return self.board.is_game_over()

    def get_winner(self):
        if self.board.is_checkmate():
            return "Black wins" if self.board.turn == chess.WHITE else "White wins"
        return "Draw"

    def reset_board(self):
        self.board.reset()

    def display_board(self):
        print(self.board)

if __name__ == "__main__":
    game = ChessGame()
    game.display_board()

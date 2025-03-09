import chess
import chess.engine

class ChessAI:
    def __init__(self, stockfish_path):
        """Initialize the AI with Stockfish engine."""
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    def get_best_move(self, board):
        """Get the best move for the current board position."""
        result = self.engine.play(board, chess.engine.Limit(time=0.5))  # Adjust time limit if needed
        return result.move

    def close_engine(self):
        """Close the Stockfish engine properly."""
        self.engine.quit()

if __name__ == "__main__":
    # Define Stockfish path (Ensure it's correctly named as "stockfish.exe")
    stockfish_path = r"C:\Users\aishw\OneDrive\Desktop\chess ai\stockfish.exe"
    
    # Initialize AI
    ai = ChessAI(stockfish_path)

    # Create a new chess board
    board = chess.Board()

    # Print initial board position
    print("Initial Board Position:")
    print(board)

    # Get AI's best move
    ai_move = ai.get_best_move(board)
    print(f"AI Move: {ai_move}")

    # Make AI's move on the board
    board.push(ai_move)

    # Print updated board position
    print("\nBoard After AI's Move:")
    print(board)

    # Close Stockfish engine
    ai.close_engine()

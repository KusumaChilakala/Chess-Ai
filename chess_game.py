import pygame
import chess
import chess.engine
import os

# Constants
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)
DOT_COLOR = (0, 0, 0)  # Black dots for move directions

# Map chess pieces to image filenames
PIECE_IMAGES = {
    'P': 'wp.png', 'p': 'bp.png',
    'R': 'wr.png', 'r': 'br.png',
    'N': 'wn.png', 'n': 'bn.png',
    'B': 'wb.png', 'b': 'bb.png',
    'Q': 'wq.png', 'q': 'bq.png',
    'K': 'wk.png', 'k': 'bk.png'
}

class ChessGame:
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Game with AI")
        self.board = chess.Board()

        # Load piece images
        self.piece_images = {key: pygame.transform.scale(pygame.image.load(os.path.join("images", value)), (SQUARE_SIZE, SQUARE_SIZE))
                             for key, value in PIECE_IMAGES.items()}
        
        # Stockfish path
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")

        self.selected_square = None
        self.valid_moves = []

    def draw_board(self):
        """Draw the chess board and pieces."""
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(self.screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Highlight valid moves with dotted lines
        for move in self.valid_moves:
            x = (move % 8) * SQUARE_SIZE + SQUARE_SIZE // 2
            y = (7 - (move // 8)) * SQUARE_SIZE + SQUARE_SIZE // 2
            for i in range(-15, 20, 5):  # Dotted line effect
                pygame.draw.circle(self.screen, DOT_COLOR, (x + i, y), 2)
                pygame.draw.circle(self.screen, DOT_COLOR, (x - i, y), 2)
                pygame.draw.circle(self.screen, DOT_COLOR, (x, y + i), 2)
                pygame.draw.circle(self.screen, DOT_COLOR, (x, y - i), 2)

        # Draw pieces
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                x = (square % 8) * SQUARE_SIZE
                y = (7 - (square // 8)) * SQUARE_SIZE
                self.screen.blit(self.piece_images[piece.symbol()], (x, y))

    def handle_click(self, pos):
        """Handle mouse clicks for moving pieces."""
        col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
        clicked_square = chess.square(col, 7 - row)

        if self.selected_square is None:
            piece = self.board.piece_at(clicked_square)
            if piece and piece.color == self.board.turn:
                self.selected_square = clicked_square
                self.valid_moves = [move.to_square for move in self.board.legal_moves if move.from_square == clicked_square]
        else:
            move = chess.Move(self.selected_square, clicked_square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.valid_moves = []
                pygame.time.delay(500)  # Small delay before AI move
                self.make_ai_move()
            else:
                self.selected_square = None
                self.valid_moves = []

    def make_ai_move(self):
        """Let AI make its move using Stockfish."""
        if not self.board.is_game_over():
            result = self.engine.play(self.board, chess.engine.Limit(time=0.5))
            self.board.push(result.move)

    def run(self):
        """Main game loop."""
        running = True
        while running:
            self.draw_board()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

        pygame.quit()
        self.engine.quit()

if __name__ == "__main__":
    ChessGame().run()

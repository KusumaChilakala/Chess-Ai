import pygame
import chess
import ai

WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8
WHITE, BLACK = (255, 255, 255), (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess AI Game")

game = chess.Board()
ai_player = ai.ChessAI("stockfish.exe")

def draw_board():
    colors = [WHITE, BLACK]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def get_square_from_pos(pos):
    x, y = pos
    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
    return chess.square(col, 7 - row)

running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            square = get_square_from_pos(pygame.mouse.get_pos())
            move_uci = input("Enter move in UCI format (e.g., e2e4): ")
            
            move = chess.Move.from_uci(move_uci)
            if move in game.legal_moves:
                game.push(move)
                
                if not game.is_game_over():
                    ai_move = ai_player.get_best_move(game)
                    game.push(ai_move)
                    print(f"AI played: {ai_move}")
    
    if game.is_game_over():
        print("Game Over!")
        running = False

pygame.quit()
ai_player.close()

import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK, COLS, ROWS
from checkers.game import Game
from algorithm.Random import get_random_move
import subprocess
import sys

pygame.init()
pygame.font.init()
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

font = pygame.font.Font(None, 36)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    pygame.mixer.init()
    pygame.mixer.music.load("assets\\boop.mp3")

    winner_message_shown = False

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        if game.turn == WHITE:
            new_board = get_random_move(game.get_board(), game)
            game.ai_move(new_board)

        winner = game.winner()
        if winner is not None and not winner_message_shown:
            winner_message_shown = True
            if winner == BLACK:
                winneraffiche = "Félicitation! Vous avez gagné!"
                subprocess.run(["python", "interface3.py", str(winneraffiche)])
                run = False
                pygame.quit()
                sys.exit()
            else:
                winneraffiche = "J'ai gagnée!!. Meilleure chance la prochaine fois !"
                subprocess.run(["python", "interface3.py", str(winneraffiche)])
                run = False
                pygame.quit()
                sys.exit()
        game.update()

if __name__ == "__main__":
    main()

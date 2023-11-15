# Import necessary libraries
import pygame
import sys
import subprocess

# Initialize Pygame at the beginning of your script
pygame.init()

def back_to_main():
    pygame.quit()
    subprocess.run(["python", "interface2.py"])

def win_screen(winner):
    # Remove pygame.init() from here

    pygame.mixer.init()
    pygame.mixer.music.load("assets\win.mp3")
    pygame.mixer.music.play()

    screen = pygame.display.set_mode((1366, 768))
    screen_width, screen_height = screen.get_size()

    background = pygame.image.load("assets\\win.jpg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        screen.blit(background, (0, 0))

        font = pygame.font.SysFont("Gagalin", 48, italic=True, bold=True)
        text = font.render(f"{winner}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40))

        screen.blit(text, text_rect)

        button_font = pygame.font.SysFont("Gagalin", 36, italic=True, bold=True)
        button_color = "#E6C8B4"
        text_color = "black"
        return_button = pygame.Rect(500, screen_height - 100, 200, 50)
        pygame.draw.rect(screen, button_color, return_button)

        return_text = button_font.render("ALLER ", True, text_color)
        text_center = return_text.get_rect(center=return_button.center)
        screen.blit(return_text, text_center)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if return_button.collidepoint(mouse_pos):
                    back_to_main()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        winner = sys.argv[1]
        win_screen(winner)
        print(f"Winner from sys.argv: {winner}")
    else:
        print("No winner specified.")

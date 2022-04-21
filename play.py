import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS

def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    running = True
    # game = Game()
    game_clock = pygame.time.Clock()

    while running:
        delta = game_clock.tick(FPS)



if __name__ == "__main__":
    main()
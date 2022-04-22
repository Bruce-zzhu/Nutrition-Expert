from numpy import disp
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS, FOOD_STATS
from src.game import Game

from src.entities.food import *

stage: str


def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    font = pygame.font.SysFont("Arial", 24)

    running = True
    game = Game()
    game_clock = pygame.time.Clock()
    while running:
        delta = game_clock.tick(FPS)
        events = pygame.event.get()
        game.handle_input(events)
        game.update(delta)
        game.render(display, font)
        pygame.display.update()
        for e in events:
            if e.type == pygame.QUIT:
                running = False
        break


if __name__ == "__main__":
    main()

import random
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS
import json

FOODS = "./food_list.json"
NFOOD_PER_NUTRIENT = 9

with open(FOODS) as f:
    properties = json.loads(PROPS)


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


def generate_food():
    random.randint(0, 9)
    return this_food

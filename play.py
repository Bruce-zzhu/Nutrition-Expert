import random
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS
import json

from src.entities.food import Healthy, Water, Unhealthy

FOODS = "./food_list.json"

stage: str

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
    rand_fname = FOODS["nutrients"][stage][
        random.randint(0, len(FOODS["nutrients"][stage]))
    ]
    for food in FOODS["foods"]:
        if rand_fname == food["name"]:
            match food["type"]:
                case "healthy":
                    return Healthy(food)
                case "water":
                    return Water(food)
                case "unhealthy":
                    return Unhealthy(food)
    return False

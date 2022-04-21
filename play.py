import random
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS
import json

from src.entities.food import Healthy, Water, Unhealthy

FOODS = "./food_list.json"

stage: str

with open(FOODS) as f:
    food_props = json.loads(FOODS)


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


def generate_food(x: int):
    rand_fname = food_props["nutrients"][stage][
        random.randint(0, len(food_props["nutrients"][stage]))
    ]
    for food in food_props["foods"]:
        if rand_fname == food["name"]:
            img = pygame.image.load(food_props["image_url"])
            match food["type"]:
                case "healthy":
                    return Healthy(food, x, img.get_width(), img.get_height())
                case "water":
                    return Water(food, x, img.get_width(), img.get_height())
                case "unhealthy":
                    return Unhealthy(food, x, img.get_width(), img.get_height())
    return False

import random
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS, FOOD_STATS
import json

from src.entities.food import *

stage: str

food_path = FOOD_STATS["FOODS"]
with open(food_path, "r") as f:
    FOOD_PROPS = json.loads(f.read())


def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    font = pygame.font.SysFont("Arial", 24)

    running = True
    # game = Game()
    game_clock = pygame.time.Clock()

    while running:
        delta = game_clock.tick(FPS)

        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                running = False
        break


if __name__ == "__main__":
    main()


def generate_food(x: int):
    rand_fname = FOOD_PROPS["nutrients"][stage][
        random.randint(0, len(FOOD_PROPS["nutrients"][stage]))
    ]
    for food in FOOD_PROPS["foods"]:
        if rand_fname == food["name"]:
            img = pygame.image.load(FOOD_PROPS["image_url"])
            if food["type"] == "healthy":
                return Healthy(
                    [
                        FOOD_PROPS["nutrients"].keys(),
                        food,
                        x,
                        img.get_width(),
                        img.get_height(),
                    ]
                )
            elif food["type"] == "water":
                return Water(
                    [
                        FOOD_PROPS["nutrients"].keys(),
                        food,
                        x,
                        img.get_width(),
                        img.get_height(),
                    ]
                )
            elif food["type"] == "unhealthy":
                return Unhealthy(
                    [
                        FOOD_PROPS["nutrients"].keys(),
                        food,
                        x,
                        img.get_width(),
                        img.get_height(),
                    ]
                )
    return False

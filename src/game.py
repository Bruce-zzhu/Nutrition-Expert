from dis import dis
import enum
import json
import random
from numpy import isin
import pygame
from pygame import Color, Vector2
from random import randint
from pygame.locals import K_RIGHT, K_SPACE, K_DOWN, K_UP, K_LEFT, K_ESCAPE
from src.entities.player import Player
from src.constants import FOOD_STATS, SCREEN_W, SCREEN_H, BLACK, WHITE
from src.constants import FOOD_STATS, FPS, SCREEN_W
from src.entities.food import *

food_path = FOOD_STATS["FOODS"]
with open(food_path, "r") as f:
    FOOD_PROPS = json.loads(f.read())

## placeholder stage value
# stage = nutrients.vit_c
stage = "vit_c"


class Game:
    entities: list
    mode: enum

    time_passed: int

    def __init__(self):
        self.start_game()
        time_passed = 0

    def start_game(self):
        print("Start a new game.")
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)
        self.mode = None

    def set_mode(self, mode):
        self.mode = mode

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # menu
                # if event.key == K_UP:
                #     pass
                # elif event.key == K_DOWN:
                #     pass
                if event.key == K_LEFT:
                    self.player.move_left()
                elif event.key == K_RIGHT:
                    self.player.move_right()
                elif event.key == K_ESCAPE:
                    print("Game exited")
                    pygame.quit()
                    exit()

            if event.type == K_UP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()

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

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        # load background
        picture = pygame.image.load("assets/image/background.png")
        picture = pygame.transform.scale(picture, (SCREEN_W, SCREEN_H))
        display.blit(picture, (0, 0))

        for obj in self.entities:
            if isinstance(obj, Player):
                obj.render(display)

        self.render_text(
            display, font, "Nutrition Expert", WHITE, (SCREEN_W // 2 - 70, 25)
        )
        self.render_text(
            display, font, f"Satisation level: {self.player.satiation}", WHITE, (50, 25)
        )
        self.render_text(
            display, font, f"Hydration level: {self.player.hydration}", WHITE, (50, 50)
        )

    def update(self, delta):
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]
            # delete the food that has been eaten
            if obj.expired:
                del self.entities[i]

            # Execute entity logic
            obj.tick(delta, self.entities)
            obj.move(delta)


def generate_food(stage: str):
    x = randint(0, SCREEN_W)
    rand_fname = FOOD_PROPS["nutrients"][stage][
        randint(0, len(FOOD_PROPS["nutrients"][stage]))
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


def update(self, delta):
    for i in range(len(self.entities) - 1, -1, -1):
        obj = self.entities[i]
        # delete the food that has been eaten
        if obj.expired:
            del self.entities[i]

        # Execute entity logic
        obj.tick(delta, self.entities)
        obj.move(delta)

    # generate food every 2 seconds
    if self.time_passed == 0:
        generate_food(self.stage)
    self.time_passed = self.time_passed // (FPS * 2) + 1

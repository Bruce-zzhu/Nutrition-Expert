from collections import defaultdict
from play import FOODS
import pygame

from src.entities.entity import Entity

from src.constants import SCREEN_H, FOOD_STATS, F_PARAMS


class Food(Entity):
    satiation: int
    score: int
    eaten: bool

    def __init__(self, params):
        Entity.__init__(self, params.append(0))
        eaten = False
        self.velocity = (0, FOOD_STATS["FOOD_VEL"])

    def tick(self, delta, objects):
        if self.eaten or self.y < 0 or self.y > SCREEN_H:
            self.kill()


class Healthy(Food):
    nutrition: dict

    def __init__(self, params):
        super(self, params)
        score = FOOD_STATS["H_SCORE"]
        satiation = FOOD_STATS["SATIATION"]
        nutrition = defaultdict(int)
        for nutrient in params[F_PARAMS["NUTRIENTS"]]:
            nutrition[nutrient] = params[F_PARAMS["FOOD"]][nutrient]


class Water(Food):
    hydration: int

    def __init__(self, params):
        super(self, params)
        hydration = FOOD_STATS["HYDRATION"]
        score = FOOD_STATS["W_SCORE"]
        satiation = 0


class Unhealthy(Food):
    hydration: int
    nutrition: dict

    def __init__(self, params):
        super(self, params)
        score = FOOD_STATS["U_SCORE"]
        hydration = -FOOD_STATS["HYDRATION"]
        nutrition = defaultdict(int)
        nutrition["fibre"] = FOOD_STATS["U_FIBRE"]
        satiation = FOOD_STATS["SATIATION"]

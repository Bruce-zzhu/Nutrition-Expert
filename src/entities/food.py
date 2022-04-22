from collections import defaultdict
from play import FOODS
import pygame

from src.entities.entity import Entity

from src.constants import FOOD_STATS, F_PARAMS


class Food(Entity):
    satiation: int
    score: int
    eaten: bool

    def __init__(self, params):
        Entity.__init__(self, params.append(0))
        eaten = False
        self.velocity = (0, FOOD_STATS["FOOD_VEL"])

    def add_stats(self):
        pass


class Healthy(Food):
    nutrition: dict

    def __init__(self, params):
        super(self, params)
        score = FOOD_STATS["H_SCORE"]
        satiation = FOOD_STATS["SATIATION"]
        nutrition = defaultdict(int)
        for nutrient in params[F_PARAMS["NUTRIENTS"]]:
            nutrition[nutrient] = params[F_PARAMS["FOOD"]][nutrient]

    def add_stats(self):
        return


class Water(Food):
    hydration: int

    def __init__(self, params):
        super(self, params)
        hydration = FOOD_STATS["HYDRATION"]
        score = FOOD_STATS["W_SCORE"]
        satiation = 0

    def add_stats(self):
        return


class Unhealthy(Food):
    hydration: int
    fibre: int

    def __init__(self, params):
        super(self, params)
        score = FOOD_STATS["U_SCORE"]
        hydration = -FOOD_STATS["HYDRATION"]
        fibre = 2
        satiation = FOOD_STATS["SATIATION"]

    def add_stats(self):
        return

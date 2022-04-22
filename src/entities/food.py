from collections import defaultdict
import pygame

from src.entities.entity import Entity

FOOD_VEL = 5

## food __init__ param order
P_NUTRIENTS = 0
P_FOOD = 1
P_X = 2
P_WIDTH = 3
P_HEIGHT = 4


class Food(Entity):
    satiation: int
    score: int
    eaten: bool

    def __init__(self, params):
        Entity.__init__(self, params.append(0))
        eaten = False
        self.velocity = (0, FOOD_VEL)

    def add_stats(self):
        pass


class Healthy(Food):
    nutrition: dict

    def __init__(self, params):
        super(self, params)
        score = 10
        satiation = 5
        nutrition = defaultdict(int)
        for nutrient in params[P_NUTRIENTS]:
            nutrition[nutrient] = params[P_FOOD][nutrient]

    def add_stats(self):
        return


class Water(Food):
    hydration: int

    def __init__(self, params):
        super(self, params)
        hydration = 10

    def add_stats(self):
        return


class Unhealthy(Food):
    hydration: int
    fibre: int

    def __init__(self, params):
        super(self, params)
        hydration = -10
        fibre = 2

    def add_stats(self):
        return

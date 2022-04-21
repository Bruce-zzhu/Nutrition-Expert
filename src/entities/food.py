import pygame

from src.entities.entity import Entity

FOOD_VEL = 5


class Food(Entity):
    satiation: int
    score: int
    eaten: bool
    location: tuple

    def __init__(self, food_props, x, width, height):
        Entity.__init__(self, food_props["image_url"], x, 0, width, height)
        eaten = False
        location = (x, 0)
        self.velocity = (0, FOOD_VEL)

    def add_stats(self):
        pass


class Healthy(Food):
    def __init__(self, food_props, x, width, height):
        super(self, food_props, x, width, height)

    def add_stats(self):
        return


class Water(Food):
    def __init__(self, food_props, x, width, height):
        super(self, food_props)

    def add_stats(self):
        return


class Unhealthy(Food):
    def __init__(self, food_props, x, width, height):
        super(self, food_props)

    def add_stats(self):
        return

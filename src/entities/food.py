from abc import ABCMeta, abstractmethod
import pygame

from src.entities.entity import Entity


class Food(Entity, metaclass=ABCMeta):
    satiation: int
    score: int
    eaten: bool
    location: tuple

    @abstractmethod
    def __init__(self, food_props):
        Entity.__init__(self, food_props["image_url"])

    @abstractmethod
    def add_stats(self):
        pass


class Healthy(Food):
    def __init__(self, food_props):
        super(self, food_props)

    def add_stats(self):
        return


class Water(Food):
    def __init__(self, food_props):
        super(self, food_props)

    def add_stats(self):
        return


class Unhealthy(Food):
    def __init__(self, food_props):
        super(self, food_props)

    def add_stats(self):
        return

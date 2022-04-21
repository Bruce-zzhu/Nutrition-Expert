from abc import ABCMeta, abstractmethod
import pygame


class Food(pygame.sprite.Sprite, metaclass=ABCMeta):
    image_url: str
    satiation: int
    score: int
    eaten: bool
    location: tuple

    @abstractmethod
    def __init__(self, food_props):
        pygame.sprite.Sprite.__init__(self)

    @abstractmethod
    def add_scores(self):
        pass

from abc import ABCMeta, abstractmethod
from tokenize import String
from xmlrpc.client import boolean


class Food(metaclass=ABCMeta):
    image_url: String
    satiation: int
    score: int
    eaten: bool
    location: tuple

    @abstractmethod
    def __init__(properties):
        pass

    @abstractmethod
    def add_scores(self):
        pass

from src.entities.player import Player

class player:
    satiation: int
    hydration: int
    scores: int
    location: tuple(int,int)


    def __init__(self):
        self.satiation = 0
        self.hydration = 100
        self.scores = 100
        self.location = (0,0)

    def eat(score):
        scores+=score


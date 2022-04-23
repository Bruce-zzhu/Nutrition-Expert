from collections import defaultdict
import pygame

# from enum import Enum

from src.entities.entity import Entity

from src.constants import *

# nutrients = Enum("nutrients", "vit_c calc fibre")
class Food(Entity):
    satiation: int
    score: int
    eaten: bool
    stage: str

    def __init__(self, params):
        super().__init__(
            params[F_PARAMS["X"]],
            0,
            params[F_PARAMS["WIDTH"]],
            params[F_PARAMS["HEIGHT"]],
            params[F_PARAMS["FOOD"]]["image_url"],
        )

        self.eaten = False
        self.velocity.x = 0
        self.velocity.y = FOOD_STATS["FOOD_VEL"]
        self.image = pygame.transform.scale(
            self.image, (FOOD_STATS["MAX_SIZE"], FOOD_STATS["MAX_SIZE"])
        )
        self.stage = params[F_PARAMS["STAGE"]]

    def tick(self, delta: int, objects: "list"):
        if self.eaten or self.y < 0 or self.y > SCREEN_H:
            self.kill()

    def render(self, practice: bool, display: pygame.Surface):
        super.render()
        if practice and isinstance(self, Healthy):
            scoreFont = pygame.font.Font(FOOD_STATS["FONT"], FOOD_STATS["FONT_SIZE"])
            scoreText = scoreFont.render(
                self.nutrition[self.stage] + self.score, 0, BLACK
            )
            scoreRect = scoreText.get_rect(center=(self.x, self.y))
            display.blit(scoreText, scoreRect)


class Healthy(Food):
    nutrition: dict

    def __init__(self, params):
        super().__init__(params)
        self.score = FOOD_STATS["H_SCORE"]
        self.satiation = FOOD_STATS["SATIATION"]
        self.nutrition = defaultdict(int)
        self.nutrition[self.stage] = params[F_PARAMS["FOOD"]][self.stage]


class Water(Food):
    hydration: int

    def __init__(self, params):
        super().__init__(params)
        self.hydration = FOOD_STATS["HYDRATION"]
        self.score = FOOD_STATS["W_SCORE"]
        self.satiation = 0


class Unhealthy(Food):
    hydration: int
    nutrition: dict

    def __init__(self, params):
        super().__init__(params)
        self.score = FOOD_STATS["U_SCORE"]
        self.hydration = -FOOD_STATS["HYDRATION"]
        self.nutrition = defaultdict(int)
        self.nutrition["fibre"] = FOOD_STATS["U_FIBRE"]
        self.satiation = FOOD_STATS["SATIATION"]
        print(type(self.image))

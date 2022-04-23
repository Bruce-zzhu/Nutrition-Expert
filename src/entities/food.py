from asyncio import Handle
from collections import defaultdict
from gettext import install
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
        self.width = FOOD_STATS["MAX_SIZE"] * self.width / self.height
        self.height = FOOD_STATS["MAX_SIZE"]
        self.image = pygame.transform.scale(
            self.image,
            (self.width, self.height),
        )
        self.stage = params[F_PARAMS["STAGE"]]

    def tick(self, delta: int, objects: "list"):
        if self.eaten or self.y < 0 or self.y > SCREEN_H:
            self.kill()

    def render(self, display: pygame.Surface, practice: bool):
        Entity.render(self, display)
        if not practice:
            scoreFont = pygame.font.SysFont(
                ["helvetica", "arial"], FOOD_STATS["FONT_SIZE"], bold=True
            )

            if isinstance(self, Healthy) or isinstance(self, Unhealthy):
                scoreOutline = scoreFont.render(
                    str(self.nutrition[self.stage] + (self.score)), 0, WHITE
                )
                if isinstance(self, Healthy):

                    scoreText = scoreFont.render(
                        str(self.nutrition[self.stage] + (self.score)), 0, GREEN
                    )
                else:
                    scoreText = scoreFont.render(
                        str(self.nutrition[self.stage] + (self.score)), 0, RED
                    )
            else:
                scoreOutline = scoreFont.render("0", 0, WHITE)
                scoreText = scoreFont.render("0", 0, BLACK)

            scoreRect = scoreText.get_rect(
                center=(
                    self.x + self.width / 2,
                    self.y + self.height / 2,
                )
            )
            display.blit(scoreOutline, (scoreRect.x - 2, scoreRect.y - 2))
            display.blit(scoreOutline, (scoreRect.x - 2, scoreRect.y + 2))
            display.blit(scoreOutline, (scoreRect.x + 2, scoreRect.y - 2))
            display.blit(scoreOutline, (scoreRect.x + 2, scoreRect.y + 2))
            display.blit(scoreText, (scoreRect.x, scoreRect.y))


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

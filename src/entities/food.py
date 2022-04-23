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
        if practice:
            scoreColor: tuple
            scoreFont = pygame.font.SysFont(
                ["helvetica", "arial"], FOOD_STATS["FONT_SIZE"], bold=True
            )

            if isinstance(self, Healthy) or isinstance(self, Unhealthy):
                scoreVal = f"{self.nutrition[self.stage] + self.score}"
                if isinstance(self, Healthy):
                    scoreNutr = self.stage
                    scoreVal += FOOD_STATS["UNITS"][self.stage]
                    scoreColor = GREEN
                else:
                    scoreColor = RED
            else:
                scoreVal = "0"
                scoreColor = BLUE

            if isinstance(self, Healthy):
                # print scoreNutr
                self.printWithOutline(
                    display,
                    scoreColor,
                    scoreFont,
                    scoreNutr,
                    (self.x + self.width / 2, self.y - self.height),
                )

            # print scoreVal
            self.printWithOutline(
                display,
                scoreColor,
                scoreFont,
                scoreVal,
                (self.x + self.width / 2, self.y - self.height / 2),
            )

    def printWithOutline(
        self,
        display: pygame.Surface,
        printColor: tuple,
        printFont: pygame.font.Font,
        printText: str,
        printCenter: tuple,
    ):
        outline = printFont.render(printText, 0, WHITE)
        fill = printFont.render(printText, 0, printColor)
        printRect = fill.get_rect(center=printCenter)
        display.blit(outline, (printRect.x - 2, printRect.y - 2))
        display.blit(outline, (printRect.x - 2, printRect.y + 2))
        display.blit(outline, (printRect.x + 2, printRect.y - 2))
        display.blit(outline, (printRect.x + 2, printRect.y + 2))
        display.blit(fill, (printRect.x, printRect.y))


class Healthy(Food):
    nutrition: dict

    def __init__(self, params):
        super().__init__(params)
        self.score = FOOD_STATS["H_SCORE"]
        self.satiation = FOOD_STATS["SATIATION"]
        self.nutrition = defaultdict(int)
        self.nutrition[self.stage] = params[F_PARAMS["FOOD"]][self.stage]
        self.score += self.nutrition[self.stage]


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
        self.score += self.nutrition[self.stage]

import pygame
from src.constants import SCREEN_W, F_PARAMS


class Entity(pygame.Rect):
    velocity: pygame.Vector2
    image: pygame.Surface
    expired: bool  # for entity to disappear or not

    def __init__(self, params):
        super().__init__(
            params[F_PARAMS["X"]],
            params[F_PARAMS["Y"]],
            params[F_PARAMS["WIDTH"]],
            params[F_PARAMS["HEIGHT"]],
        )
        image = pygame.image.load(params[F_PARAMS["FOOD"]]["image_url"])
        self.velocity = pygame.Vector2()  # (0, 0)
        self.expired = False
        self.image = pygame.transform.smoothscale(
            image, (params[F_PARAMS["WIDTH"]], params[F_PARAMS["WIDTH"]])
        )

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))

    def move(self, delta: int):
        """delta: time between frames"""
        clamp_x = max(self.x + round(self.velocity.x * delta), 0)
        clamp_x = min(clamp_x, SCREEN_W - self.width)
        self.update(
            clamp_x, self.y + round(self.velocity.y * delta), self.width, self.height
        )

    def boundary_check(self):
        return self.x <= 0 or self.x >= SCREEN_W - self.width

    def tick(self, delta: int, objects: "list"):
        pass

    def kill(self):
        self.expired = True

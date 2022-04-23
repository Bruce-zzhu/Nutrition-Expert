import pygame
from src.constants import SCREEN_W


class Entity(pygame.Rect):
    velocity: pygame.Vector2
    image: pygame.Surface
    expired: bool  # for entity to disappear or not

    def __init__(self, x, y, width, height, image: str):
        super().__init__(x, y, width, height)
        self.velocity = pygame.Vector2()  # (0, 0)
        self.expired = False
        self.image = pygame.transform.smoothscale(
            pygame.image.load(image), (width, height)
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

    def tick(self, delta: int, objects: "list"):
        pass

    def kill(self):
        self.expired = True

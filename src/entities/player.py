import pygame
from pygame.image import load as loadImg
from src.constants import (
    FULL_VALUE,
    PLAYER_SPEED,
    PLAYER_IMAGE_PATH,
    PLAYER_DEFAULT_IMG,
)
from src.entities.food import Food, Healthy, Unhealthy, Water
from src.entities.entity import Entity


class Player(Entity):

    satiation: int
    hydration: int
    scores: int
    move_direction: int
    speed: int

    def __init__(self):
        super().__init__(500, 600, 55, 55, PLAYER_IMAGE_PATH + PLAYER_DEFAULT_IMG)
        self.image = loadImg(PLAYER_IMAGE_PATH + PLAYER_DEFAULT_IMG)
        self.satiation = 0
        self.hydration = FULL_VALUE
        self.scores = 0
        self.speed = PLAYER_SPEED
        self.move_direction = 0  # -1 for left; 0 for stop; 1 for right

    def move_left(self):
        image_path: str
        if self.move_direction >= 0:
            image_path = PLAYER_IMAGE_PATH + "Run_0.png"
        else:
            img_idx = self.image[-5:-4]
            image_path = PLAYER_IMAGE_PATH + "Run_" + str((img_idx + 1) % 4) + ".png"
        self.image = pygame.transform.flip(loadImg(image_path), True, False)
        self.move_direction = -1

    def move_right(self):
        image_path: str
        if self.move_direction <= 0:
            image_path = PLAYER_IMAGE_PATH + "Run_0.png"
        else:
            img_idx = self.image[-5:-4]
            image_path = PLAYER_IMAGE_PATH + "Run_" + str((img_idx + 1) % 4) + ".png"
        self.image = loadImg(image_path)
        self.move_direction = 1

    def stop_moving(self):
        image_path: str
        if self.move_direction != 0:
            image_path = PLAYER_IMAGE_PATH + "Idle_0.png"
        else:
            img_idx = self.image[-5:-4]
            image_path = PLAYER_IMAGE_PATH + "Idle_" + str((img_idx + 1) % 4) + ".png"
        self.image = loadImg(image_path)
        self.move_direction = 0

    def is_full(self):
        return self.satiation == FULL_VALUE

    def is_dehydrated(self):
        return self.hydration == 0

    def eat(self, food: Food):
        scores += food.scores
        satiation += food.satiation
        food.eaten = True
        if isinstance(food, Healthy) or isinstance(food, Unhealthy):
            scores += food.nutrition["stage"]
        if isinstance(food, Water) or isinstance(food, Unhealthy):
            hydration += food.hydration
        if isinstance(food, Unhealthy):
            self.image = PLAYER_IMAGE_PATH + "Dead.png"

    def tick(self, delta: int, objects: "list"):
        self.velocity.x = self.speed * self.move_direction

        # check colliction with food
        for obj in objects:
            if isinstance(obj, Food) and self.colliderect(obj):
                self.eat(obj)

        if self.satiation == FULL_VALUE or self.hydration == 0:
            self.kill()

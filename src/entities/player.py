import pygame
from src.constants import (
    FULL_VALUE,
    PLAYER_SPEED,
    PLAYER_IMAGE_PATH,
    PLAYER_DEFAULT_IMG,
    PLAYER_SIZE,
)
from src.entities.food import Food, Healthy, Unhealthy, Water
from src.entities.entity import Entity


class Player(Entity):
    full_image_path: str
    satiation: int
    hydration: int
    scores: int
    move_direction: int
    speed: int
    ticks: int

    def __init__(self):
        super().__init__(
            500, 600, PLAYER_SIZE, PLAYER_SIZE, PLAYER_IMAGE_PATH + PLAYER_DEFAULT_IMG
        )
        self.full_image_path = PLAYER_IMAGE_PATH + PLAYER_DEFAULT_IMG
        self.image = self.loadImg()
        self.satiation = 0
        self.hydration = FULL_VALUE
        self.scores = 0
        self.speed = PLAYER_SPEED
        self.move_direction = 0  # -1 for left; 0 for stop; 1 for right
        self.ticks = 0

    def move_left(self):
        self.move_direction = -1

    def move_right(self):
        self.move_direction = 1

    def stop_moving(self):
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
        face_right = self.velocity.x >= 0

        self.velocity.x = self.speed * self.move_direction
        self.ticks = (self.ticks + 1) % 18

        if self.ticks == 0:
            img_idx = self.full_image_path[-5:-4]
            if not img_idx.isdigit:
                img_idx = 0

            if self.move_direction != 0:
                self.full_image_path = (
                    PLAYER_IMAGE_PATH + "Run_" + str((int(img_idx) + 1) % 4) + ".png"
                )
            else:
                self.full_image_path = (
                    PLAYER_IMAGE_PATH + "Idle_" + str((int(img_idx) + 1) % 4) + ".png"
                )
            if not face_right:
                self.image = pygame.transform.flip(self.loadImg(), True, False)
            else:
                self.image = self.loadImg()

        # check colliction with food
        for obj in objects:
            if isinstance(obj, Food) and self.colliderect(obj):
                self.eat(obj)

        if self.satiation == FULL_VALUE or self.hydration == 0:
            self.kill()

    def loadImg(self):
        image = pygame.image.load(self.full_image_path)
        image = pygame.transform.chop(
            image,
            (
                (image.get_width() / 2, image.get_height()),
                (image.get_width(), image.get_height()),
            ),
        )
        return pygame.transform.scale(image, (self.width, self.height))

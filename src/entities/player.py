from pygame.transform import flip
from src.constants import FULL_VALUE, PLAYER_SPEED, IMAGE_FOLDER
from src.entities.food import Food, Healthy, Unhealthy, Water
from src.entities.entity import Entity


class Player(Entity):

    satiation: int
    hydration: int
    scores: int
    move_direction: int
    speed: int
    image: str

    def __init__(self):
        super().__init__(500, 600, 55, 55, IMAGE_FOLDER + "Idle_1.png")
        self.image = IMAGE_FOLDER + "Idle_1.png"
        self.satiation = 0
        self.hydration = FULL_VALUE
        self.scores = 0
        self.speed = PLAYER_SPEED
        self.move_direction = 0  # -1 for left; 0 for stop; 1 for right

    def move_left(self):
        if self.move_direction >= 0:
            self.image = flip(IMAGE_FOLDER + "Run_0.png", True, False)
        else:
            img_idx = self.image[-5:-4]
            self.image = flip(
                IMAGE_FOLDER + "Run_" + str((img_idx + 1) % 4) + ".png", True, False
            )
        self.move_direction = -1

    def move_right(self):
        if self.move_direction <= 0:
            self.image = IMAGE_FOLDER + "Run_0.png"
        else:
            img_idx = self.image[-5:-4]
            self.image = IMAGE_FOLDER + "Run_" + str((img_idx + 1) % 4) + ".png"
        self.move_direction = 1

    def stop_moving(self):
        if self.move_direction != 0:
            self.image = IMAGE_FOLDER + "Idle_0.png"
        else:
            img_idx = self.image[-5:-4]
            self.image = IMAGE_FOLDER + "Idle_" + str((img_idx + 1) % 4) + ".png"
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
            self.image = IMAGE_FOLDER + "Dead.png"

    def tick(self, delta: int, objects: "list"):
        self.velocity.x = self.speed * self.move_direction

        # check colliction with food
        for obj in objects:
            if isinstance(obj, Food) and self.colliderect(obj):
                self.eat(obj)

        if self.satiation == FULL_VALUE or self.hydration == 0:
            self.kill()

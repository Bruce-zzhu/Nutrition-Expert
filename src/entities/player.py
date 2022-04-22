from src.constants import FULL_VALUE, PLAYER_SPEED
from src.entities.food import Food, Healthy, Unhealthy, Water
from src.entities.entity import Entity

class Player(Entity):
    
    satiation: int
    hydration: int
    scores: int
    move_direction: int
    speed: int

    def __init__(self):
        super().__init__(500, 600, 55, 55, "assets/image/meat.jpg")
        self.satiation = 0
        self.hydration = FULL_VALUE
        self.scores = 0
        self.speed = PLAYER_SPEED
        self.move_direction = 0 # -1 for left; 0 for stop; 1 for right

    def eat(score):
        scores+=score

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

    def eat(food: Food):
        scores += food.scores
        satiation += food.satiation
        food.eaten = True
        if isinstance(food, Healthy) or isinstance(food, Unhealthy):
            scores += food.nutrition["stage"]
        if isinstance(food, Water) or isinstance(food, Unhealthy):
            hydration += food.hydration

    def tick(self, delta: int, objects: 'list'):
        self.velocity.x = self.speed * self.move_direction

        # check colliction with food
        for obj in objects:
            if isinstance(obj, Food) and self.colliderect(obj):
                self.eat(obj)

        if self.satiation == FULL_VALUE or self.hydration == 0:
            self.kill()

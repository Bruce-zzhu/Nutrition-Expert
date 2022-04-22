SCREEN_W = 1200
SCREEN_H = 700

# The target framerate of our game. Set to 0 for no limit
FPS = 144

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# player properties
PLAYER_SPEED = 0.75
PLAYER_IMAGE_PATH = "assets/image/player/"
PLAYER_DEFAULT_IMG = "Idle_0.png"
PLAYER_SIZE = 100
FULL_VALUE = 100

FOOD_IMAGE_PATH = "assets/image/foods/"
FOOD_STATS = {
    "FOODS": "./food_list.json",
    "FOOD_VEL": 0.5,
    "FOOD_FREQ": 0.5,
    "H_SCORE": 10,
    "W_SCORE": 0,
    "U_SCORE": -25,
    "HYDRATION": 10,
    "SATIATION": 5,
    "U_FIBRE": 2,
    "SHRINKAGE": 4,
    "MAX_SIZE": 50,
}

F_PARAMS = {"NUTRIENTS": 0, "FOOD": 1, "X": 2, "WIDTH": 3, "HEIGHT": 4, "STAGE": 5}

SCREEN_W = 1200
SCREEN_H = 700

# The target framerate of our game. Set to 0 for no limit
FPS = 144

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# player properties
PLAYER_SPEED = 0.8
PLAYER_IMAGE_PATH = "assets/image/player/"
PLAYER_DEFAULT_IMG = "Idle_0.png"
FULL_VALUE = 100

FOOD_IMAGE_PATH = "assets/image/foods/"

FOOD_STATS = {
    "FOODS": "./food_list.json",
    "FOOD_VEL": 5,
    "H_SCORE": 10,
    "W_SCORE": 0,
    "U_SCORE": -25,
    "HYDRATION": 10,
    "SATIATION": 5,
    "U_FIBRE": 2,
}

F_PARAMS = {"NUTRIENTS": 0, "FOOD": 1, "X": 2, "WIDTH": 3, "HEIGHT": 4, "Y": 0}


# nutrients
VIT_C = "Vitamin_C"
CALCIUM = "Calcium"
FIBRE = "Fibre"


# game status & menu state
GAME = "game"
MENU = "menu"
MAIN_MENU = "main_menu"
SELECT_MENU = "select_mode"
START_READY = "start_game"
INTRO_MENU = "intro_menu"
BACK = "Back"
START = "Start"
PRACTICE = "Practice"
import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Game Resolution
screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "assets/font/HyFWoolBall-2.ttf"

# Main Menu image
picture = pygame.image.load("assets/image/foods/background.png")
picture = pygame.transform.scale(picture, (screen_width, screen_height))
screen.blit(picture, (0, 0))


# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Main Menu
def main_menu():

    menu = True
    selected = "Select Mode"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "Select Mode"
                elif event.key == pygame.K_DOWN:
                    selected = "Introduction"

                if event.key == pygame.K_RETURN:
                    if selected == "Select Mode":
                        # select vc mode
                        print("Select Mode")

                    if selected == "Introduction":
                        # select fibre mode
                        print("Introduction")

        # Main Menu UI

        title = text_format("Nutrition-Expert", font, 100, white)

        # select Select Mode in the menu
        if selected == "Select Mode":
            text_sm = text_format("Select Mode" + " " * 7 + "1", font, 75, yellow)
        else:
            text_sm = text_format("Select Mode" + " " * 7 + "1", font, 75, white)

        # select Calcium in the menu
        if selected == "Introduction":
            text_introduction = text_format(
                "Introduction" + " " * 7 + "2", font, 75, yellow
            )
        else:
            text_introduction = text_format(
                "Introduction" + " " * 7 + "2", font, 75, white
            )

        title_rect = title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 20))
        screen.blit(text_sm, (screen_width / 6, 180))
        screen.blit(text_introduction, (screen_width / 6, 280))
        pygame.display.update()
        clock.tick(FPS)

        pygame.display.set_caption("Nutrition-Expert")


# Initialize the Game
main_menu()
pygame.quit()
quit()

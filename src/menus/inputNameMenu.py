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

# ====================================================

COLOR_INACTIVE = pygame.Color(yellow)
COLOR_ACTIVE = pygame.Color(yellow)
FONT = pygame.font.Font(None, 32)


class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color(yellow)
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        self.color = COLOR_ACTIVE
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:

                print(self.text)
                self.text = ""

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width() + 40)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 50, self.rect.y + 20))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 4)


# ====================================================

# Main Menu
def main_menu():

    menu = True
    selected = "Enter"

    clock = pygame.time.Clock()
    input_box1 = InputBox(80, 150, 340, 60)
    input_boxes = [input_box1]

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "Enter"
                elif event.key == pygame.K_DOWN:
                    selected = "Back"
                elif event.key == pygame.K_RETURN:
                    if selected == "Enter":
                        print(input_box1.text)
                    if selected == "Back":
                        print("Back")

                elif event.key == pygame.K_BACKSPACE:
                    input_box1.text = input_box1.text[:-1]
                else:
                    input_box1.text += event.unicode
                # Re-render the text.
                input_box1.txt_surface = FONT.render(
                    input_box1.text, True, input_box1.color
                )

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        # select Enter in the menu
        if selected == "Enter":
            text_enter = text_format("Enter" + " " * 7 + "1", font, 75, yellow)
        else:
            text_enter = text_format("Enter" + " " * 7 + "1", font, 75, white)

        # select Calcium in the menu
        if selected == "Back":
            text_back = text_format("Back" + " " * 7 + "2", font, 75, yellow)
        else:
            text_back = text_format("Back" + " " * 7 + "2", font, 75, white)

        title = text_format("Please Input User Name", font, 90, yellow)
        title_rect = title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 20))
        screen.blit(text_enter, (screen_width / 2 - (title_rect[2] / 2), 250))
        screen.blit(text_back, (screen_width / 2 - (title_rect[2] / 2), 350))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Nutrition-Expert")


if __name__ == "__main__":
    # Initialize the Game
    main_menu()
    pygame.quit()
    quit()

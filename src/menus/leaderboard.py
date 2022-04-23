import pygame
from pygame.locals import *
import os



# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=1080
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "assets/font/HyFWoolBall-2.ttf"
font_size = 40
line_margin = 60

# Main Menu image
picture = pygame.image.load("assets/image/background.png")
picture = pygame.transform.scale(picture,(screen_width,screen_height))
screen.blit(picture,(0,0))

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

# Text format for leaderboard username and score display
def text_format_for_listing(text_to_display):
    return text_format(text_to_display, font, font_size, white)

# Main Menu
def main():
    running = True

    while running:

        ### SET LEADERBOARD DATA ###
        username = {
            1: "top1 nameeeeee",
            2: "nameeeee",
            3: "22",
            4: "namaajsnxkjnlksx",
            5: "0ijnbjijnnk"
        }
        score = {
            1: "12",
            2: "3211",
            3: "111",
            4: "22",
            5: "9292"
        }

        # pygame.QUIT listener
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        # Set display title
        title = text_format("Game Leaderboard", font, 100, white)
        title_rect = title.get_rect()
        title_pos_horizontal = screen_width/2 - (title_rect[2]/2)
        title_position = (title_pos_horizontal, 20)

        selectable_back = text_format("Back", font, font_size, yellow)
        selectable_back_pos = (title_pos_horizontal, 160)

        # Screen blit for leaderboard username and score display
        def get_position_for_username_line(line_number):
            base = 180
            return (title_pos_horizontal, base + line_margin * line_number)

        def get_position_for_score_line(line_number):
            base = 200
            return (title_rect.right, base + line_margin * line_number)

        # Set screen blits
        screen.blit(title, title_position)
        screen.blit(selectable_back, selectable_back_pos)

        
        for i in range(1, len(username) + 1):
            # Make Surfaces and update username and score dictionaries
            username[i] = text_format_for_listing(username[i])
            score[i] = text_format_for_listing(score[i])

            # Set screen blits for usernames and scores
            screen.blit(username[i], get_position_for_username_line(i))
            screen.blit(score[i], get_position_for_score_line(i))

        # Update display
        pygame.display.update()
        clock.tick(FPS)

        ### END OF LEADERBOARD WHILE LOOP ###

#Initialize the Game
main()
pygame.quit()
quit()
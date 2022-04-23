from unicodedata import name
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
line_margin = 50

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
            2: "bruce",
            3: "22"
        }
        score = {
            1: "12",
            2: "123",
            3: "111"
        } 
        
        time = {
            "score":"123",
            "username": "bruce"
        }

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                        print("back to main menu")
        
        # Set display title
        title = text_format("Leaderboard", font, 100, white)
        title_rect = title.get_rect()
        title_pos_horizontal = screen_width/2 - (title_rect[2]/2)
        title_position = (title_pos_horizontal, 20)

        selectable_back = text_format("Press Enter Back To Main Menu", font, font_size, yellow)
        selectable_back_pos = (title_pos_horizontal, 485)

        name = text_format("Your record: "+ time['username']+" ( "+time['score']+" )", font, font_size, yellow)
        name_pos = (title_pos_horizontal, 125)
        
        history = text_format("TOP 3", font, 65, white)
        history_pos = (title_pos_horizontal, 205)

        # Screen blit for leaderboard username and score display
        def get_position_for_username_line(line_number):
            base = 240
            return (title_pos_horizontal, base + line_margin * line_number)

        def get_position_for_score_line(line_number):
            base = 240
            return (title_rect.right+170, base + line_margin * line_number)

        # Set screen blits
        screen.blit(name, name_pos)
        screen.blit(selectable_back, selectable_back_pos)
        
        screen.blit(history, history_pos)
        screen.blit(title, title_position)
        

        
        for i in range(1, len(username) + 1):
            # Make Surfaces and update username and score dictionaries
            if username[i] != time['username']:
                username[i] = text_format(username[i], font, 35, white)
                score[i] = text_format(score[i], font, 35, white)
            else:
                
                username[i] = text_format(username[i], font, 45, yellow)
                score[i] = text_format(score[i], font, 45, yellow)
                
            

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
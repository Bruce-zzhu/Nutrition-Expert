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

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "src/menu/Retro.ttf"

# Main Menu image

picture = pygame.image.load("assets/image/background.png")
picture = pygame.transform.scale(picture,(screen_width,screen_height))
screen.blit(picture,(0,0))


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and selected !="quit":
                    selected="start"
                elif event.key==pygame.K_DOWN and selected !="start":
                    selected="quit"
                elif event.key!=pygame.K_RETURN:
                    selected="history"



                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        #start the game
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()
                    if selected=="history":
                        #给出记录
                        print("history")

        # Main Menu UI
        
        title=text_format("Nutrition-Expert", font, 100, white)
        menu=text_format("Menu", font, 85, white)

        #select start in the menu
        if selected=="start":
            text_start=text_format("Start"+" "*40+"1", font, 75, yellow)
        else:
            text_start = text_format("Start"+" "*40+"1", font, 75, white)

        #select history in the menu
        if selected=="history":
            text_history=text_format("History"+" "*36+"2", font, 75, yellow)
        else:
            text_history = text_format("History"+" "*36+"2", font, 75, white)

        #select quit in the menu
        if selected=="quit":
            text_quit=text_format("Quit"+" "*43+"3", font, 75, yellow)
        else:
            text_quit = text_format("Quit"+" "*43+"3", font, 75, white)

        
        title_rect=title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 20))
        screen.blit(text_start, (screen_width/5, 240))
        screen.blit(text_history, (screen_width/5, 300))
        screen.blit(text_quit, (screen_width/5, 360))
        pygame.display.update()
        clock.tick(FPS)
        
        

        pygame.display.set_caption("Nutrition-Expert")

#Initialize the Game
main_menu()
pygame.quit()
quit()

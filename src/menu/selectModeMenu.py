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
font = "assets/font/HyFWoolBall-2.ttf"

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
    selected="Vitamin C"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if (event.key==pygame.K_UP and selected =="Calcium") or (event.key==pygame.K_UP and selected =="Vitamin C"):
                    selected="Vitamin C"
                elif (event.key==pygame.K_UP and selected =="Fibre") or (event.key==pygame.K_DOWN and selected =="Vitamin C"):
                    selected="Calcium"
                elif (event.key==pygame.K_UP and selected =="Back") or (event.key==pygame.K_DOWN and selected =="Calcium"):
                    selected="Fibre"
                elif (event.key==pygame.K_DOWN and selected =="Back") or (event.key==pygame.K_DOWN and selected =="Fibre"):
                    selected="Back"


                if event.key==pygame.K_RETURN:
                    if selected=="Vitamin C":
                        #select vc mode
                        print("Vitamin C")

                    if selected=="Fibre":
                        #select fibre mode
                        print("Fibre")

                    if selected=="Calcium":
                        #select Ca mode
                        print("Calcium")
                    
                    if selected=="Back":
                        #back to last menu
                        print("Back")
                    

        # Main Menu UI
        
        title=text_format("Please Select Game Mode", font, 90, white)
        menu=text_format("Menu", font, 85, white)

        #select Vitamin C in the menu
        if selected=="Vitamin C":
            text_vc=text_format("Vitamin C"+" "*10+"1", font, 75, yellow)
        else:
            text_vc = text_format("Vitamin C"+" "*10+"1", font, 75, white)

        #select Calcium in the menu
        if selected=="Calcium":
            text_ca=text_format("Calcium"+" "*13+"2", font, 75, yellow)
        else:
            text_ca = text_format("Calcium"+" "*13+"2", font, 75, white)

        #select Fibre in the menu
        if selected=="Fibre":
            text_fibre=text_format("Fibre"+" "*16+"3", font, 75, yellow)
        else:
            text_fibre = text_format("Fibre"+" "*16+"3", font, 75, white)

        if selected=="Back":
            text_back=text_format("Back"+" "*16+"4", font, 75, yellow)
        else:
            text_back = text_format("Back"+" "*16+"4", font, 75, white)

        
        title_rect=title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 20))
        screen.blit(text_vc, (screen_width/6, 180))
        screen.blit(text_ca, (screen_width/6, 280))
        screen.blit(text_fibre, (screen_width/6, 380))
        screen.blit(text_back, (screen_width/6, 480))
        pygame.display.update()
        clock.tick(FPS)

        

        pygame.display.set_caption("Nutrition-Expert")

#Initialize the Game
main_menu()
pygame.quit()
quit()

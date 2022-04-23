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

def blit_text(text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = screen_width, screen_height
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "assets/font/Montserrat-Regular.ttf"
font_text = pygame.font.SysFont('Arial', 29)

# Main Menu image
picture = pygame.image.load("assets/image/foods/background.png")
picture = pygame.transform.scale(picture,(screen_width,screen_height))
screen.blit(picture,(0,0))


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def introduction():
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    print("Back")

        # Main Menu UI
        
        title=text_format("Introduction", font, 90, white)
        menu=text_format("Menu", font, 85, white)

        text_intro = " Nutrition Expert is designed to provide users the knowledge about food and nutrition.\n\n Game rules:\n 1. Select a specific nutrient that you are interested in\n 2. Move the character to eat the food that contains the chosen nutrient\n 3. The scores depend on how much the chosen nutrient the food contains \n 4. Each food (except for water) will increase character's satiation level\n 5. User's hydration level decreases by time. Drinking water increases the hydration level\n 6. Game ends when either user's satiation level is full or hydration level is 0\n 7. There is a leaderboard recording the top 5 users for each nutrient"
        
        #select back in the menu
        text_back=text_format("Press Enter Back To Main Menu ", font, 40, yellow)
        title_rect=title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2)-20, 20))
        screen.blit(text_back, (screen_width/10, 500))
        blit_text(text_intro, (screen_width/11, 150), font_text)
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Nutrition-Expert")

#Initialize the Game
if __name__ == '__main__':
    introduction()

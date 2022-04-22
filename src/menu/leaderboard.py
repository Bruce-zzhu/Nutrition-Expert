import pygame
from pygame.locals import *
import os

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
        # pygame.QUIT listener
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
<<<<<<< HEAD
=======
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and selected !="history":
                    selected="start"
                elif event.key==pygame.K_DOWN and selected !="start":
                    selected="history"
                elif event.key!=pygame.K_RETURN:
                    selected="practice"



                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        #start the game
                        print("Start")

                    if selected=="history":
                        print("history")

                    if selected=="practice":
                        #给出记录
                        print("practice")

        # Main Menu UI
        title=text_format("Nutrition-Expert", font, 100, white)
        menu=text_format("Menu", font, 85, white)

        #select start in the menu
        if selected=="start":
            text_start=text_format("Start"+" "*20+"1", font, 75, yellow)
        else:
            text_start = text_format("Start"+" "*20+"1", font, 75, white)

        #select history in the menu
        if selected=="practice":
            text_practice=text_format("Practice"+" "*16+"2", font, 75, yellow)
        else:
            text_practice = text_format("Practice"+" "*16+"2", font, 75, white)

        #select quit in the menu
        if selected=="history":
            text_history=text_format("History"+" "*18+"3", font, 75, yellow)
        else:
            text_history = text_format("History"+" "*18+"3", font, 75, white)

>>>>>>> dc1bde52b08548b3e793935c9a3312bb85bc3cc4
        
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
<<<<<<< HEAD

        ### END OF LEADERBOARD WHILE LOOP ###
=======
        
        

        pygame.display.set_caption("Nutrition-Expert")
>>>>>>> dc1bde52b08548b3e793935c9a3312bb85bc3cc4

#Initialize the Game
main()
pygame.quit()
quit()
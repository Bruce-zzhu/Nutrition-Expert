from lib2to3.pgen2.token import STAR
import pygame
from pygame.locals import *
import os
from src.constants import *
from src.menus.inputNameMenu import InputBox, FONT
from src.menus.introduction import blit_text


class Menu():
    def __init__(self):
        self.menu_state = SELECT_MENU
        self.game_stage = VIT_C
        self.input_box1 = InputBox(80, 150, 340, 60)
        self.input_boxes = [self.input_box1]
    
    def tick(self, clock, FPS):
        clock.tick(FPS)

    

    # Text Renderer
    def render_text(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText

    def render_background(self):
        # Main Menu image
        bg_img = pygame.image.load("assets/image/background.png")
        bg_img = pygame.transform.scale(bg_img, (SCREEN_W, SCREEN_H))
        return bg_img

    def main_menu_handle_input(self, events):
        game_status = MAIN_MENU
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.menu_state = SELECT_MENU
                elif event.key == pygame.K_DOWN:
                    self.menu_state = INTRO_MENU

                if event.key == pygame.K_RETURN:
                    if self.menu_state == SELECT_MENU:
                        game_status = SELECT_MENU
                        self.menu_state = VIT_C

                    if self.menu_state == INTRO_MENU:
                        game_status = INTRO_MENU
                        self.menu_state = BACK

        return game_status

    def render_main_menu(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

        title = self.render_text("Nutrition-Expert", font, 100, WHITE)

        # select Select Mode in the menu
        if self.menu_state == SELECT_MENU:
            text_sm = self.render_text(SELECT_MENU+" "*7+"1", font, 75, YELLOW)
        else:
            text_sm = self.render_text(SELECT_MENU+" "*7+"1", font, 75, WHITE)

        # select Calcium in the menu
        if self.menu_state == INTRO_MENU:
            text_introduction = self.render_text(
                INTRO_MENU+" "*7+"2", font, 75, YELLOW)
        else:
            text_introduction = self.render_text(
                INTRO_MENU+" "*7+"2", font, 75, WHITE)

        title_rect = title.get_rect()

        # Main Menu Text
        display.blit(title, (SCREEN_W/2 - (title_rect[2]/2), 20))
        display.blit(text_sm, (SCREEN_W/6, 180))
        display.blit(text_introduction, (SCREEN_W/6, 280))
        pygame.display.update()

        pygame.display.set_caption("Nutrition-Expert")

    def intro_menu_handle_input(self, events):
        game_status = INTRO_MENU
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_status = MAIN_MENU
                        self.menu_state = SELECT_MENU

        return game_status

    def render_intro_menu(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

        title = self.render_text("Introduction", font, 90, WHITE)
        menu = self.render_text("Menu", font, 85, WHITE)

        text_intro = " Nutrition Expert is designed to provide users the knowledge about food and nutrition.\n\n Game rules:\n 1. Select a specific nutrient that you are interested in\n 2. Move the character to eat the food that contains the chosen nutrient\n 3. The scores depend on how much the chosen nutrient the food contains \n 4. Each food (except for water) will increase character's satiation level\n 5. User's hydration level decreases by time. Drinking water increases the hydration level\n 6. Game ends when either user's satiation level is full or hydration level is 0\n 7. There is a leaderboard recording the top 5 users for each nutrient"


        # select back in the menu
        text_back = self.render_text("Press Enter Back To Main Menu ", font, 40, YELLOW)
        title_rect = title.get_rect()

        # Main Menu Text
        display.blit(title, (SCREEN_W/2 - (title_rect[2]/2), 20))
        display.blit(text_back, (SCREEN_W/10, 510))
        blit_text(text_intro, (SCREEN_W/11, 150), pygame.font.SysFont('Arial', 29))
        pygame.display.update()
        pygame.display.set_caption("Nutrition-Expert")

    def select_menu_handle_input(self, events):
        game_status = SELECT_MENU
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP and self.menu_state == CALCIUM) or (event.key == pygame.K_UP and self.menu_state == VIT_C):
                    self.menu_state = VIT_C
                elif (event.key == pygame.K_UP and self.menu_state == FIBRE) or (event.key == pygame.K_DOWN and self.menu_state == VIT_C):
                    self.menu_state = CALCIUM
                elif (event.key == pygame.K_UP and self.menu_state == BACK) or (event.key == pygame.K_DOWN and self.menu_state == CALCIUM):
                    self.menu_state = FIBRE
                elif (event.key == pygame.K_DOWN and self.menu_state == BACK) or (event.key == pygame.K_DOWN and self.menu_state == FIBRE):
                    self.menu_state = BACK

                if event.key == pygame.K_RETURN:
                    if self.menu_state == BACK:
                        game_status = MAIN_MENU
                        self.menu_state = SELECT_MENU
                    else:
                        game_status = START_READY
                        self.game_stage = self.menu_state
                        self.menu_state = START

        return game_status

    def render_select_menu(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

        title = self.render_text("Please Select Game Mode", font, 90, WHITE)
        menu = self.render_text("Menu", font, 85, WHITE)

        # select Vitamin C in the menu
        if self.menu_state == VIT_C:
            text_vc = self.render_text(VIT_C+" "*10+"1", font, 75, YELLOW)
        else:
            text_vc = self.render_text(VIT_C+" "*10+"1", font, 75, WHITE)

        # select Calcium in the menu
        if self.menu_state == CALCIUM:
            text_ca = self.render_text(CALCIUM+" "*13+"2", font, 75, YELLOW)
        else:
            text_ca = self.render_text(CALCIUM+" "*13+"2", font, 75, WHITE)

        # select Fibre in the menu
        if self.menu_state == FIBRE:
            text_fibre = self.render_text(FIBRE+" "*16+"3", font, 75, YELLOW)
        else:
            text_fibre = self.render_text(FIBRE+" "*16+"3", font, 75, WHITE)

        if self.menu_state == BACK:
            text_back = self.render_text(BACK+" "*16+"4", font, 75, YELLOW)
        else:
            text_back = self.render_text(BACK+" "*16+"4", font, 75, WHITE)

        title_rect = title.get_rect()

        # Main Menu Text
        display.blit(title, (SCREEN_W/2 - (title_rect[2]/2), 20))
        display.blit(text_vc, (SCREEN_W/6, 180))
        display.blit(text_ca, (SCREEN_W/6, 280))
        display.blit(text_fibre, (SCREEN_W/6, 380))
        display.blit(text_back, (SCREEN_W/6, 480))
        pygame.display.update()

        pygame.display.set_caption("Nutrition-Expert")

    def ready_menu_handle_input(self, events):
        game_status = START_READY
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.menu_state != BACK:
                        self.menu_state = START
                    elif event.key == pygame.K_DOWN and self.menu_state != START:
                        self.menu_state = BACK
                    elif event.key != pygame.K_RETURN:
                        self.menu_state = PRACTICE

                if event.key == pygame.K_RETURN:
                    if self.menu_state == START:
                        game_status = INPUT_MENU
                        self.menu_state = GO
                    elif self.menu_state == BACK:
                        game_status = SELECT_MENU
                        self.menu_state = VIT_C
                    elif self.menu_state == PRACTICE:
                        game_status = PRACTICE

        return game_status

    def render_ready_menu(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

        title = self.render_text("Please Start The Game", font, 90, WHITE)
        menu = self.render_text("Menu", font, 85, WHITE)

        # select start in the menu
        if self.menu_state == START:
            text_start = self.render_text(START+" "*16+"1", font, 75, YELLOW)
        else:
            text_start = self.render_text(START+" "*16+"1", font, 75, WHITE)

        # select practice in the menu
        if self.menu_state == PRACTICE:
            text_practice = self.render_text(
                PRACTICE+" "*12+"2", font, 75, YELLOW)
        else:
            text_practice = self.render_text(
                PRACTICE+" "*12+"2", font, 75, WHITE)

        # select back in the menu
        if self.menu_state == BACK:
            text_back = self.render_text(BACK+" "*17+"3", font, 75, YELLOW)
        else:
            text_back = self.render_text(BACK+" "*17+"3", font, 75, WHITE)

        title_rect = title.get_rect()

        # Main Menu Text
        display.blit(title, (SCREEN_W/2 - (title_rect[2]/2), 20))
        display.blit(text_start, (SCREEN_W/6, 180))
        display.blit(text_practice, (SCREEN_W/6, 280))
        display.blit(text_back, (SCREEN_W/6, 380))
        pygame.display.update()

        pygame.display.set_caption("Nutrition-Expert")

    def input_menu_handle_input(self, events):
        game_status = INPUT_MENU

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menu_state = GO
                    elif event.key == pygame.K_DOWN:
                        self.menu_state = BACK
                    
                    elif event.key == pygame.K_RETURN:
                        if self.menu_state == GO:
                            game_status = GAME
                        elif self.menu_state == BACK:
                            game_status = START_READY
                            self.menu_state = START

                    elif event.key == pygame.K_BACKSPACE:
                        self.input_box1.text = self.input_box1.text[:-1]
                    else:
                        self.input_box1.text += event.unicode
                    # Re-render the text.
                self.input_box1.txt_surface = FONT.render(
                    self.input_box1.text, True, self.input_box1.color)
        return game_status

    def render_input_menu(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

        for box in self.input_boxes:
            box.update()

        for box in self.input_boxes:
            box.draw(display)

        # select Enter in the menu
        if self.menu_state == GO:
            text_enter = self.render_text(GO+" "*7+"1", font, 75, YELLOW)
        else:
            text_enter = self.render_text(GO+" "*7+"1", font, 75, WHITE)

        # select Calcium in the menu
        if self.menu_state == BACK:
            text_back = self.render_text(BACK+" "*7+"2", font, 75, YELLOW)
        else:
            text_back = self.render_text(BACK+" "*7+"2", font, 75, WHITE)

        title = self.render_text("Please Input User Name", font, 90, YELLOW)
        title_rect = title.get_rect()

        # Main Menu Text
        display.blit(title, (SCREEN_W/2 - (title_rect[2]/2), 20))
        display.blit(text_enter, (SCREEN_W/2 - (title_rect[2]/2), 250))
        display.blit(text_back, (SCREEN_W/2 - (title_rect[2]/2), 350))
        pygame.display.update()
        pygame.display.set_caption("Nutrition-Expert")

    def leaderboard_handle_input(self, events):
        game_status = BOARD
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    game_status = MAIN_MENU
                    self.menu_state = VIT_C

        return game_status

    def rednder_leaderboard(self, display, font):
        bg_img = self.render_background()
        display.blit(bg_img, (0, 0))

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

        font_size = 40
        line_margin = 50

        # Set display title
        title = self.render_text("Leaderboard", font, 100, WHITE)
        title_rect = title.get_rect()
        title_pos_horizontal = SCREEN_W/2 - (title_rect[2]/2)
        title_position = (title_pos_horizontal, 20)

        selectable_back = self.render_text("Press Enter Back To Main Menu", font, font_size, YELLOW)
        selectable_back_pos = (title_pos_horizontal, 485)

        name = self.render_text("Your record: "+ time['username']+" ( "+time['score']+" )", font, font_size, YELLOW)
        name_pos = (title_pos_horizontal, 125)
        
        history = self.render_text("TOP 3", font, 65, WHITE)
        history_pos = (title_pos_horizontal, 205)

        # Screen blit for leaderboard username and score display
        def get_position_for_username_line(line_number):
            base = 240
            return (title_pos_horizontal, base + line_margin * line_number)

        def get_position_for_score_line(line_number):
            base = 240
            return (title_rect.right+170, base + line_margin * line_number)

        # Set display blits
        display.blit(name, name_pos)
        display.blit(selectable_back, selectable_back_pos)
        
        display.blit(history, history_pos)
        display.blit(title, title_position)
        

        
        for i in range(1, len(username) + 1):
            # Make Surfaces and update username and score dictionaries
            if username[i] != time['username']:
                username[i] = self.render_text(username[i], font, 35, WHITE)
                score[i] = self.render_text(score[i], font, 35, WHITE)
            else:
                
                username[i] = self.render_text(username[i], font, 45, YELLOW)
                score[i] = self.render_text(score[i], font, 45, YELLOW)
                
            

            # Set display blits for usernames and scores
            display.blit(username[i], get_position_for_username_line(i))
            display.blit(score[i], get_position_for_score_line(i))
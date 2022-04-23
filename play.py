import pygame
from src.game import Game
from src.menu import Menu
from src.constants import *
from src.entities.food import *


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/bgm.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    font_str = "assets/font/HyFWoolBall-2.ttf"
    font = pygame.font.SysFont("assets/font/HyFWoolBall-2.ttf", 70)

    running = True
    menu = Menu()
    game = Game()

    status = MAIN_MENU
    game_clock = pygame.time.Clock()
    while running:

        delta = game_clock.tick(FPS)
        events = pygame.event.get()

        if status == GAME or status == PRACTICE:
            game.isPractice = status == PRACTICE
            game.stage = menu.game_stage
            game.handle_input(events)
            game.update(delta)
            status = game.render(display, font)
        elif status == MAIN_MENU:
            status = menu.main_menu_handle_input(events)
            menu.render_main_menu(display, font_str)
        elif status == SELECT_MENU:
            status = menu.select_menu_handle_input(events)
            menu.render_select_menu(display, font_str)
        elif status == INTRO_MENU:
            status = menu.intro_menu_handle_input(events)
            menu.render_intro_menu(display, font_str)
        elif status == START_READY:
            status = menu.ready_menu_handle_input(events)
            menu.render_ready_menu(display, font_str)
        elif status == INPUT_MENU:
            status = menu.input_menu_handle_input(events)
            menu.render_input_menu(display, font_str)
        elif status == BOARD:
            status = menu.leaderboard_handle_input(events)
            menu.rednder_leaderboard(display, font_str)

        pygame.display.update()
        for e in events:
            if e.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

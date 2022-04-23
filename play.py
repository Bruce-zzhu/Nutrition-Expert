from dis import dis
from tkinter.tix import MAIN
import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS, GAME
from src.game import Game
from src.menu import Menu
from src.constants import GAME, MENU, MAIN_MENU, SELECT_MENU, START_READY, INTRO_MENU
from src.entities.food import *

stage: str


def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    font_str = "assets/font/HyFWoolBall-2.ttf"
    font = pygame.font.SysFont("assets/font/HyFWoolBall-2.ttf", 90)

    running = True
    menu = Menu()
    game = Game(menu.menu_state)

    status = MAIN_MENU
    game_clock = pygame.time.Clock()
    while running:
        delta = game_clock.tick(FPS)
        events = pygame.event.get()

        if status == GAME:
            game.stage = menu.game_stage
            game.handle_input(events)
            game.update(delta)
            game.render(display, font)
        elif status == MAIN_MENU:
            status = menu.main_menu_handle_input(events)
            menu.render_main_menu(display, font_str)
        elif status == SELECT_MENU:
            status = menu.select_menu_handle_input(events)
            menu.render_select_menu(display, font_str)
        elif status == START_READY:
            status = menu.ready_menu_handle_input(events)
            menu.render_ready_menu(display, font_str)
        elif status == INTRO_MENU:
            status = menu.intro_menu_handle_input(events)
            menu.render_intro_menu(display, font_str)

        pygame.display.update()
        for e in events:
            if e.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

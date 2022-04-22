import enum
import pygame
from pygame.locals import K_RIGHT, K_SPACE, K_DOWN, K_UP, K_LEFT, K_ESCAPE
from sqlalchemy import null
from src.entities.player import Player
from src.entities.food import Food

class Game:
    entities: list
    mode: enum

    def __init__(self):
        self.start_game()

    def start_game(self):
        print('Start a new game.')
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)
        self.mode = null

    def set_mode(self, mode):
        self.mode = mode

    def handle_input(self, events):
        for event in events:

            if event.type == pygame.KEYDOWN:
                # menu
                # if event.key == K_UP:                
                #     pass
                # elif event.key == K_DOWN:               
                #     pass
                if event.key == K_LEFT:
                    self.player.move_left()
                elif event.key == K_RIGHT:
                    self.player.move_right()
                elif event.key == K_ESCAPE:
                    print("Game exited")
                    pygame.quit()
                    exit()

            if event.type == K_UP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()
                
    def update(self, delta):
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]
            # delete the food that has been eaten
            if obj.expired:
                del self.entities[i]
            
            # Execute entity logic
            obj.tick(delta, self.entities)
            obj.move(delta)
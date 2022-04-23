import pygame
from pygame.locals import *
import os


# Game Initialization
pygame.init()

# Center the Game Application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Game Resolution
screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

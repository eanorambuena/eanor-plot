from engine.body import       *
from engine.core import       *
from engine.math_utils import *
from engine.clip import       *
import pygame

def load2screen(screen = pygame.Surface, file_name = "result.png"):
    bg = pygame.image.load(file_name).convert()
    screen.blit(bg, (0, 0))
    pygame.display.flip()

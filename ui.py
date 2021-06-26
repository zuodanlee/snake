import pygame
from pygame.locals import *

black = (0, 0, 0)
green = (0,255,0)
red = (255,0,0)

def redraw_game_window(win, snake, apple):
    win.fill(black)
    pygame.draw.rect(win, red, apple, border_radius=10)
    #pygame.draw.rect(win, green, snake, border_radius=10)
    for snake_block in snake:
        pygame.draw.rect(win, green, snake_block, border_radius=10)
    pygame.display.flip()

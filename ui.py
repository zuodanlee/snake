import pygame
from pygame.locals import *

from main import *

black = (0, 0, 0)
green = (0,255,0)
red = (255,0,0)
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50, True)
sub_font = pygame.font.SysFont("comicsans", 25, True)

def redraw_game_window(win, snake, apple):
    win.fill(black)
    pygame.draw.rect(win, red, apple, border_radius=10)
    for snake_block in snake:
        pygame.draw.rect(win, green, snake_block, border_radius=10)
    pygame.display.flip()

def draw_game_over(win):
    text_game_over = render_text("Game Over", font)
    win.blit(text_game_over, ((width/2)-(text_game_over.get_width()/2), (height/2)-(text_game_over.get_height()/2)))
    
    text_retry = render_text("Retry? (y/n)", sub_font)
    win.blit(text_retry, ((width/2)-(text_retry.get_width()/2), (height/2)+(text_game_over.get_height()/2)+10))
    pygame.display.flip()

def render_text(plaintext, font):
    return font.render(plaintext, 1, (255,255,255))

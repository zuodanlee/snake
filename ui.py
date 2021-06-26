import pygame
from pygame.locals import *

from main import *

white_overlay = (255, 255, 255, 50)
black_overlay = (0, 0, 0, 100)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (30, 30, 30)
green = (0,255,0)
red = (255,0,0)
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50, True)
sub_font = pygame.font.SysFont("comicsans", 25, True)

def redraw_game_window(win, snake, apple):
    win.fill(grey)
    pygame.draw.rect(win, red, apple, border_radius=10)
    for snake_block in snake:
        pygame.draw.rect(win, green, snake_block, border_radius=10)
    pygame.display.flip()

def draw_game_over(win):
    text_game_over = render_text("Game Over", font)
    text_retry = render_text("Retry? (y/n)", sub_font)
    popup_overlay = pygame.Surface((text_game_over.get_width()+40, text_game_over.get_height()+text_retry.get_height()+50), SRCALPHA)
    pygame.draw.rect(popup_overlay, black_overlay, (0, 0, text_game_over.get_width()+40, text_game_over.get_height()+text_retry.get_height()+50), border_radius=15)

    win.blit(popup_overlay, ((width/2)-(text_game_over.get_width()/2)-20, (height/2)-(text_game_over.get_height()/2)-20))
    win.blit(text_game_over, ((width/2)-(text_game_over.get_width()/2), (height/2)-(text_game_over.get_height()/2)))
    win.blit(text_retry, ((width/2)-(text_retry.get_width()/2), (height/2)+(text_game_over.get_height()/2)+10))
    pygame.display.flip()

def render_text(plaintext, font):
    return font.render(plaintext, 1, white)

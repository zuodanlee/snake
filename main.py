# global variables
size = width, height = 1080, 840
block_size = 40

if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    import ui
    from entities import Snake, Apple

    pygame.init()
    pygame.display.set_caption("Snake")
    win = pygame.display.set_mode(size)
    run = True

    snake = Snake(40, 40)
    apple = Apple()
    move_cooldown = 150

    # main loop
    while run:
        snake_block = snake.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            snake.turn("L")
        if keys[K_RIGHT]:
            snake.turn("R")
        if keys[K_UP]:
            snake.turn("U")
        if keys[K_DOWN]:
            snake.turn("D")

        if move_cooldown == 150:
            snake.move(apple)
            move_cooldown = 0
        else:
            move_cooldown += 1

        ui.redraw_game_window(win, snake.body, apple.get_pos())
    
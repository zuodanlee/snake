# global variables
size = width, height = 1080, 840
#size = width, height = 440, 240
block_size = 40

if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    import ui
    from entities import Snake, Apple

    pygame.init()
    pygame.display.set_caption("Snake")
    win = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    run = True

    alive = True
    snake = Snake(40, 40)
    apple = Apple(snake)
    framerate = 60
    max_move_cooldown = framerate/10
    move_cooldown = max_move_cooldown
    game_over = False

    # main loop
    while run:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if alive:
            ui.redraw_game_window(win, snake.body, apple.get_pos())
            keys = pygame.key.get_pressed()

            if keys[K_LEFT]:
                snake.turn("L")
            elif keys[K_RIGHT]:
                snake.turn("R")
            elif keys[K_UP]:
                snake.turn("U")
            elif keys[K_DOWN]:
                snake.turn("D")

            if move_cooldown == max_move_cooldown:
                alive = snake.move(apple)
                move_cooldown = 0
            else:
                move_cooldown += 1
                
        else:
            if not game_over:
                ui.draw_game_over(win)
                game_over = True
            else:
                keys = pygame.key.get_pressed()

                if keys[K_y]:
                    alive = True
                    snake = Snake(40, 40)
                    apple = Apple(snake)
                    move_cooldown = max_move_cooldown
                    game_over = False
                elif keys[K_n]:
                    run = False
    
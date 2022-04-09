import pygame
from button import Button
from common_data import refresh_menu, WIDTH, HEIGHT, FPS


def menu_run(running, screen, clock):
    refresh_menu(screen)
    start_button = Button(screen, WIDTH / 2 - 160, HEIGHT / 2 - 100, 300, 100, "START", 32, 85, 27)
    quit_button = Button(screen, WIDTH / 2 - 160, HEIGHT / 2, 300, 100, "NOT START", 32, 85, 27)
    start_button.draw()
    next_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        refresh_menu(screen)
        start_button.update()
        quit_button.update()
        if start_button.counter >= 1:
            running = False
            next_run = True
        if quit_button.counter >= 1:
            running = False
        pygame.display.flip()
        clock.tick(FPS)
    return next_run

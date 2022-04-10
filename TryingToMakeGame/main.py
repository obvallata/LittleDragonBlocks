import pygame
from common_data import AMOUNT_OF_CELLS, WIDTH, HEIGHT, FPS
from field import Field
from dragon import Dragon
from level_creation import run_lvl
from menu_run import menu_run
pygame.init()
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
while running:
    running = menu_run(running, screen, clock)
    running = run_lvl(0, running, screen, clock)
    running = run_lvl(1, running, screen, clock)
    running = run_lvl(2, running, screen, clock)
    running = run_lvl(3, running, screen, clock)
    running = run_lvl(4, running, screen, clock)
pygame.quit()

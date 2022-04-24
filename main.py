import pygame

from src.common_data import Globals
from src.level_creation import run_lvl
from src.menu_run import menu_run
pygame.init()
info = Globals()
size = width, height = info.WIDTH, info.HEIGHT
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

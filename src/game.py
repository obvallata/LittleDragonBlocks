from src.common_data import Globals
from src.interface import Interface
from src.level import Level
import pygame


class Game:
    def __init__(self, interface):
        self.game_info = Globals()
        self.interface = interface

    def start(self):
        pygame.init()
        pygame.display.set_caption("Little Dragon Blocks")
        size = self.game_info.WIDTH, self.game_info.HEIGHT
        self.interface.set_screen(pygame.display.set_mode(size))
        self.interface.set_clock(pygame.time.Clock())
        running = self.interface.menu_run(self.game_info, True)
        level_num = 0
        while running and level_num < 5:
            current_level = Level()
            current_level.set_num(level_num)
            running = current_level.__call__(self.interface, self.game_info, running)
            level_num += 1
            if level_num == 5:
                level_num = 0
                running = self.interface.menu_run(self.game_info, running)
        pygame.quit()


import pygame
from src.load_image import load_image


class Border(pygame.sprite.Sprite):
    def __init__(self, game_info, positions, num):
        pygame.sprite.Sprite.__init__(self)
        self.width = game_info.CELL_SIZE
        self.height = game_info.CELL_SIZE
        self.image = load_image("../img/bush.png", self.width, self.height)
        self.rect = self.image.get_rect()
        counter = 0
        for i in range(game_info.AMOUNT_OF_CELLS):
            for j in range(game_info.AMOUNT_OF_CELLS):
                if positions[i][j] == 1:
                    if counter == num:
                        self.rect.x = game_info.get_field_left(0) + j * game_info.CELL_SIZE
                        self.rect.y = game_info.get_field_top(0) + i * game_info.CELL_SIZE
                    counter += 1

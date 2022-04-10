import pygame
from common_data import info
from load_image import load_image


class Border(pygame.sprite.Sprite):
    def __init__(self, positions, num):
        pygame.sprite.Sprite.__init__(self)
        self.width = info.CELL_SIZE
        self.height = info.CELL_SIZE
        self.image = load_image("bush.png", self.width, self.height)
        self.rect = self.image.get_rect()
        counter = 0
        for i in range(info.AMOUNT_OF_CELLS):
            for j in range(info.AMOUNT_OF_CELLS):
                if positions[i][j] == 1:
                    if counter == num:
                        self.rect.x = info.get_field_left(0) + j * info.CELL_SIZE
                        self.rect.y = info.get_field_top(0) + i * info.CELL_SIZE
                    counter += 1

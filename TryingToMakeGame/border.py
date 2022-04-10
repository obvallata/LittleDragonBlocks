import pygame
from common_data import CELL_SIZE, AMOUNT_OF_CELLS, CELL_SIZE, FIELD_TOP, FIELD_LEFT
from load_image import load_image


class Border(pygame.sprite.Sprite):
    def __init__(self, positions, num):
        pygame.sprite.Sprite.__init__(self)
        self.width = CELL_SIZE
        self.height = CELL_SIZE
        self.image = load_image("bush.png", self.width, self.height)
        self.rect = self.image.get_rect()
        counter = 0
        for i in range(AMOUNT_OF_CELLS):
            for j in range(AMOUNT_OF_CELLS):
                if positions[i][j] == 1:
                    if counter == num:
                        self.rect.x = FIELD_LEFT[0] + j * CELL_SIZE
                        self.rect.y = FIELD_TOP[0] + i * CELL_SIZE
                    counter += 1

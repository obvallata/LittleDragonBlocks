import pygame
from common_data import AMOUNT_OF_CELLS, CELL_SIZE


class Field:
    def __init__(self, width=AMOUNT_OF_CELLS, height=AMOUNT_OF_CELLS):
        self.width = width
        self.height = height
        self.field = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = CELL_SIZE

    def set_view(self, left, top):
        self.left = left
        self.top = top

    def render(self, screen):
        y_pos = self.top
        for i in range(self.height):
            x_pos = self.left
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 153), pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (0, 204, 0), pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size), 2)
                x_pos += self.cell_size
            y_pos += self.cell_size
        pygame.draw.rect(screen, (0, 204, 0), pygame.Rect(self.left, self.top, self.cell_size * self.height,
                                                          self.cell_size * self.width), 4)

    def get_cell_pos(self, cell_number):
        return [self.cell_size[0] * cell_number, self.cell_size[1] * cell_number]

    def set_borders(self, positions):
        for i in range(AMOUNT_OF_CELLS):
            for j in range(AMOUNT_OF_CELLS):
                if positions[i][j] == 1:
                    self.field[i][j] = 2

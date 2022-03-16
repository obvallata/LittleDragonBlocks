import pygame


class Field():
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        y_pos = self.top
        for i in range(self.height):
            x_pos = self.left
            for j in range(self.width):
                pygame.draw.rect(screen, (204, 255, 153), pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (0, 204, 0), pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size), 2)
                x_pos += self.cell_size
            y_pos += self.cell_size
        pygame.draw.rect(screen, (0, 204, 0), pygame.Rect(self.left, self.top, self.cell_size * self.height,
                                                          self.cell_size * self.width), 4)



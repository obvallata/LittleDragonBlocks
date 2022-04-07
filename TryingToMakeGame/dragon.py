import pygame
from load_image import load_image
from common_data import AMOUNT_OF_CELLS, CELL_SIZE
from field import Field

START_POS_X = 800
START_POS_Y = 100


class Dragon(pygame.sprite.Sprite):
    def __init__(self, form, num_dragon=1, width=CELL_SIZE, height=CELL_SIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('img_1.png', height, width)
        self.rect = self.image.get_rect()
        self.num = num_dragon
        self.rect.x = START_POS_X
        self.rect.y = START_POS_Y + height * num_dragon
        self.size_x = width
        self.size_y = height
        self.is_active = False
        self.fits = True
        self.ready = False
        self.pos_on_field = [-1, -1]
        self.shape = [[0 for _ in range(AMOUNT_OF_CELLS)] for __ in range(AMOUNT_OF_CELLS)]
        for i in range(AMOUNT_OF_CELLS):
            for j in range(AMOUNT_OF_CELLS):
                self.shape[i][j] = form[i][j]

    def update(self, field, field_size, screen):
        field_left = field.left
        field_top = field.top
        mouse_state_abs = pygame.mouse.get_pos()
        if (self.rect.x <= mouse_state_abs[0] <= self.rect.x + self.size_x and
                self.rect.y <= mouse_state_abs[1] <= self.rect.y + self.size_y and pygame.mouse.get_pressed()[0]):
            self.is_active = True
        if self.is_active:
            self.rect.x = mouse_state_abs[0]
            self.rect.y = mouse_state_abs[1]
            active_cell = [-1, -1]
            self.fits = True
            if (field_left <= self.rect.x <= field_left + field_size and
                    field_top <= self.rect.y <= field_top + field_size):
                active_cell = [(field_left + field_size - self.rect.x) // CELL_SIZE,
                               (field_top + field_size - self.rect.y) // CELL_SIZE]
                for i in range(AMOUNT_OF_CELLS):
                    for j in range(AMOUNT_OF_CELLS):
                        if self.shape[i][j] == 1:
                            if active_cell[0] - j < 0 or active_cell[1] - i < 0:
                                self.fits = False
                            elif field.field[i + (3 - active_cell[1])][j + (3 - active_cell[0])] == 2:
                                self.fits = False
            else:
                self.fits = False
            if self.fits:
                self.pos_on_field = active_cell
            img_to_load = "img_1.png" * (not self.fits) + "Vladik_Artwork.png" * self.fits

            self.image = load_image(img_to_load, self.size_y, self.size_x)
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_f]:
            if self.fits and self.pos_on_field != [-1, -1]:
                self.rect.x = (3 - self.pos_on_field[0]) * CELL_SIZE + field_left
                self.rect.y = (3 - self.pos_on_field[1]) * CELL_SIZE + field_top
                self.ready = True
                for i in range(AMOUNT_OF_CELLS):
                    for j in range(AMOUNT_OF_CELLS):
                        if self.shape[i][j] == 1:
                            field.field[i + (3 - self.pos_on_field[1])][j + (3 - self.pos_on_field[0])] = 2
            else:
                self.rect.x = START_POS_X
                self.rect.y = START_POS_Y + self.size_y * self.num
            self.is_active = False

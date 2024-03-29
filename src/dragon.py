import pygame
from src.load_image import load_image

START_POS_X = 700
START_POS_Y = 20
STEP = 130


class Dragon(pygame.sprite.Sprite):
    def __init__(self, game_info, lvl_num, form, num_dragon=1, width=-1, height=-1):
        width = max(width, game_info.CELL_SIZE)
        height = max(height, game_info.CELL_SIZE)
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(game_info.get_image(lvl_num)[num_dragon - 1], height, width)
        self.rect = self.image.get_rect()
        self.num = num_dragon
        self.rect.x = START_POS_X
        self.rect.y = START_POS_Y + (num_dragon - 1) * STEP
        self.size_x = height
        self.size_y = width
        self.is_active = False
        game_info.active_dragon_exists = False
        self.fits = True
        self.ready = False
        self.pos_on_field = [-1, -1]
        self.shape = [[0 for _ in range(game_info.AMOUNT_OF_CELLS)] for __ in range(game_info.AMOUNT_OF_CELLS)]
        for i in range(game_info.AMOUNT_OF_CELLS):
            for j in range(game_info.AMOUNT_OF_CELLS):
                self.shape[i][j] = form[i][j]

    def update(self, game_info, field, field_size):
        field_left = field.left
        field_top = field.top
        mouse_state_abs = pygame.mouse.get_pos()
        if (self.rect.x <= mouse_state_abs[0] <= self.rect.x + self.size_x and
                self.rect.y <= mouse_state_abs[1] <= self.rect.y + self.size_y and pygame.mouse.get_pressed()[0]):
            if not game_info.active_dragon_exists:
                self.is_active = True
                game_info.active_dragon_exists = True
        if self.is_active:
            self.rect.x = mouse_state_abs[0]
            self.rect.y = mouse_state_abs[1]
            active_cell = [-1, -1]
            self.fits = True
            if (field_left <= self.rect.x <= field_left + field_size and
                    field_top <= self.rect.y <= field_top + field_size):
                active_cell = [(field_left + field_size - self.rect.x) // game_info.CELL_SIZE,
                               (field_top + field_size - self.rect.y) // game_info.CELL_SIZE]
                for i in range(game_info.AMOUNT_OF_CELLS):
                    for j in range(game_info.AMOUNT_OF_CELLS):
                        if self.shape[i][j] == 1:
                            if active_cell[0] - j < 0 or active_cell[1] - i < 0:
                                self.fits = False
                            elif field.field[i + (3 - active_cell[1])][j + (3 - active_cell[0])] == 2:
                                self.fits = False
            else:
                self.fits = False
            if self.fits:
                self.pos_on_field = active_cell
        key_state = pygame.mouse.get_pressed()[2]
        if key_state:
            if self.fits and self.pos_on_field != [-1, -1]:
                self.rect.x = (3 - self.pos_on_field[0]) * game_info.CELL_SIZE + field_left
                self.rect.y = (3 - self.pos_on_field[1]) * game_info.CELL_SIZE + field_top
                self.ready = True
                for i in range(game_info.AMOUNT_OF_CELLS):
                    for j in range(game_info.AMOUNT_OF_CELLS):
                        if self.shape[i][j] == 1:
                            field.field[i + (3 - self.pos_on_field[1])][j + (3 - self.pos_on_field[0])] = 2
            else:
                self.rect.x = START_POS_X
                self.rect.y = START_POS_Y + (self.num - 1) * STEP
            self.is_active = False
            game_info.active_dragon_exists = False
        if self.ready and self.is_active:
            for i in range(game_info.AMOUNT_OF_CELLS):
                for j in range(game_info.AMOUNT_OF_CELLS):
                    if self.shape[i][j] == 1:
                        field.field[i + (3 - self.pos_on_field[1])][j + (3 - self.pos_on_field[0])] = 0
            self.ready = False

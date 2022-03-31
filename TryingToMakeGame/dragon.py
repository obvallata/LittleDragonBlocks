import pygame
from load_image import load_image

AMOUNT_OF_CELLS = 4


class Dragon(pygame.sprite.Sprite):
    def __init__(self, name, height, width, form):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(name, height, width)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 100
        self.size_x = width
        self.size_y = height
        self.is_active = False
        self.shape = [[0 for _ in range(AMOUNT_OF_CELLS)] for __ in range(AMOUNT_OF_CELLS)]
        for i in range(AMOUNT_OF_CELLS):
            for j in range(AMOUNT_OF_CELLS):
                self.shape[i][j] = form[i][j]

    def update(self, field_left, field_top, field_size, screen):
        mouse_state_abs = pygame.mouse.get_pos()
        mouse_on_obj = False
        if self.rect.x <= mouse_state_abs[0] <= self.rect.x + self.size_x:
            if self.rect.y <= mouse_state_abs[1] <= self.rect.y + self.size_y:
                mouse_on_obj = True
        if mouse_on_obj and pygame.mouse.get_pressed()[0]:
            self.is_active = True
        if self.is_active:
            self.rect.x = mouse_state_abs[0]
            self.rect.y = mouse_state_abs[1]
            fits = True
            cell_size = field_size / AMOUNT_OF_CELLS
            if (field_left <= self.rect.x <= field_left + field_size and
                    field_top <= self.rect.y <= field_top + field_size):
                active_cell = [(field_left + field_size - self.rect.x) // cell_size,
                               (field_top + field_size - self.rect.y) // cell_size]
                for i in range(AMOUNT_OF_CELLS):
                    for j in range(AMOUNT_OF_CELLS):
                        if self.shape[i][j] == 1:
                            if active_cell[0] - j < 0:
                                fits = False
                            if active_cell[1] - i < 0:
                                fits = False
            else:
                fits = False
            img_to_load = "img_1.png" * (not fits) + "Vladik_Artwork.png" * fits
            self.image = load_image(img_to_load, self.size_y, self.size_x)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_f]:
            self.is_active = False

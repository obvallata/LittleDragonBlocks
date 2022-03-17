import pygame
import os


def load_image(name, height, width):
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    image = pygame.image.load(os.path.join(img_folder, name)).convert()
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (height, width))
    return image


class Dragon(pygame.sprite.Sprite):
    def __init__(self, name, height, width, form):
        AMOUNT_OF_CELLS = 4
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
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
        AMOUNT_OF_CELLS = 4
        mouse_state_abs = pygame.mouse.get_pos()
        mouse_on_obj = False
        if self.rect.x <= mouse_state_abs[0] <= self.rect.x + self.size_x:
            if self.rect.y <= mouse_state_abs[1] <= self.rect.y + self.size_y:
                mouse_on_obj = True
        if mouse_on_obj:
            mouse_left_is_pressed = pygame.mouse.get_pressed()[0]
            if mouse_left_is_pressed:
                self.is_active = True
        if self.is_active:
            self.rect.x = mouse_state_abs[0]
            self.rect.y = mouse_state_abs[1]
            mouse_state_rel = pygame.mouse.get_rel()
            self.rect.x += mouse_state_rel[0]
            self.rect.y += mouse_state_rel[1]
            if field_left <= self.rect.x <= field_left + field_size:
                if field_top <= self.rect.y <= field_top + field_size:
                    diff_x = (field_left + field_size - self.rect.x) // (field_size / AMOUNT_OF_CELLS)
                    diff_y = (field_top + field_size - self.rect.y) // (field_size / AMOUNT_OF_CELLS)
                    active_cell = [diff_x, diff_y]
                    fits = True
                    for i in range(AMOUNT_OF_CELLS):
                        for j in range(AMOUNT_OF_CELLS):
                            if self.shape[i][j] == 1:
                                if active_cell[0] - j < 0:
                                    fits = False
                                if active_cell[1] - i < 0:
                                    fits = False
                    if fits:
                        self.image = load_image("img.png", self.size_y, self.size_x)
                    else:
                        self.image = load_image("img_1.png", self.size_y, self.size_x)
                else:
                    self.image = load_image("img_1.png", self.size_y, self.size_x)
            else:
                self.image = load_image("img_1.png", self.size_y, self.size_x)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_f]:
            self.is_active = False


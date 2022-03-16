import pygame
import os


def load_image(name, height, width):
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    image = pygame.image.load(os.path.join(img_folder, name)).convert()
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (height, width))
    return image


class Dragon(pygame.sprite.Sprite,):

    def __init__(self, name, height, width):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(name, height, width)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 100
        self.size_x = width
        self.size_y = height
        self.is_active = False

    def update(self):
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
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_f]:
            self.is_active = False


import pygame
import os


def load_image(name, colorkey=None):
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    image = pygame.image.load(os.path.join(img_folder, name)).convert()
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (200, 200))
    # fullname = os.path.join(name)
    # image = pygame.image.load(fullname).convert()
    return image


class Dragon(pygame.sprite.Sprite):
    image = load_image("img.png")

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        pygame.sprite.Sprite.__init__(self)
        self.image = Dragon.image
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 100

import os
import pygame


def load_image(name, height, width):
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    image = pygame.image.load(os.path.join(img_folder, name)).convert()
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (height, width))
    return image

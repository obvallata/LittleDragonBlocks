import os
import pygame


def load_image(name, height, width):
    game_folder = os.path.dirname('LittleDragonBlocks')
    img_folder = os.path.join(game_folder, 'img')
    image = pygame.image.load(os.path.join(img_folder, name)).convert()
    image.set_colorkey((0, 0, 0))
    image = pygame.transform.scale(image, (height, width))
    return image

import pygame

AMOUNT_OF_CELLS = 4
WIDTH = 1024
HEIGHT = 768
FPS = 60
CELL_SIZE = 95

UNIQUE_SHAPES = [
    [[1, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 1, 1, 0],
     [1, 1, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0]],
    [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0]],
]
SHAPES = [[UNIQUE_SHAPES[0]],
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1]],
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1], UNIQUE_SHAPES[2], UNIQUE_SHAPES[3]],
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[3], UNIQUE_SHAPES[4]],
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1], UNIQUE_SHAPES[2], UNIQUE_SHAPES[5]]
          ]
BORDERS_PLACES = [
    [[1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1]],
    [[0, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 0, 0],
     [1, 1, 0, 0]],
    [[0, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 0, 0]],
    [[1, 0, 0, 1],
     [0, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]]
]

FIELD_TOP = [200, 200, 200]
FIELD_LEFT = [200, 200, 200]
AMOUNT_OF_DRAGONS = [1, 2, 4]
AMOUNT_OF_BORDERS = [12, 11, 2, 2, 4]
DRAGON_SIZES = [[[1, 1]],
                [[1, 1], [2, 2]],
                [[1, 1], [2, 2], [2, 2], [2, 1]]]

IMAGES = ['shape_1.png', 'shape_2.png', 'shape_2.png', 'shape_3.png']


def refresh_menu(screen):
    screen.fill((130, 130, 255))
    font = pygame.font.Font(pygame.font.match_font('optima'), 48)
    text_surface = font.render('Little Dragon Blocks', False, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH / 2, 100)
    screen.blit(text_surface, text_rect)

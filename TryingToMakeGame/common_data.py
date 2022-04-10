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
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1], UNIQUE_SHAPES[1], UNIQUE_SHAPES[2], UNIQUE_SHAPES[3]],
          [UNIQUE_SHAPES[0], UNIQUE_SHAPES[4], UNIQUE_SHAPES[5]],
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
    [[0, 0, 0, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 0, 0, 1],
     [0, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]]
]

FIELD_TOP = [200, 200, 200, 200, 200]
FIELD_LEFT = [200, 200, 200, 200, 200]
AMOUNT_OF_DRAGONS = [1, 2, 5, 3, 4]
AMOUNT_OF_BORDERS = [12, 11, 1, 1, 4]
DRAGON_SIZES = [[[1, 1]],
                [[1, 1], [2, 2]],
                [[1, 1], [2, 2], [2, 2], [1, 2], [2, 3]],
                [[1, 1], [3, 3], [3, 3]],
                [[1, 1], [2, 2], [1, 2], [3, 3]]]

IMAGES = [['shape_1.png'],
          ['shape_1.png', 'shape_2.png'],
          ['shape_1.png', 'shape_2.png', 'shape_2.png', 'shape_3.png', 'shape_4.png'],
          ['shape_1.png', 'shape_5.png', 'shape_6.png'],
          ['shape_1.png', 'shape_2.png', 'shape_3.png', 'shape_6.png']]


def refresh_menu(screen):
    screen.fill((130, 130, 255))
    font = pygame.font.Font(pygame.font.match_font('optima'), 48)
    text_surface = font.render('Little Dragon Blocks', False, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH / 2, 100)
    screen.blit(text_surface, text_rect)


LVL_INFO_FOR_USER = [['Level 1 new:', 'One dragon 1x1:', 'Your cursor pos', '==', 'dragon 1x1 pos.'],
                     ['Level 2 new:', 'One dragon 2x2:', 'Your cursor pos', '==',
                      'dragon 2x2', 'left top cell pos.'],
                     ['Level 3 new:', 'One dragon 1x2,', 'one dragon 2x3:', 'Your cursor pos', '==',
                      'dragon 1x2, ', 'dragon 2x3', 'left top cell pos.'],
                     ['Level 4 new:', 'One dragon 3x3,', 'one dragon 3x3', '(like right angle):', 'Your cursor pos',
                      '==', 'dragon 3x3, ', 'dragon 3x3', 'left top cell pos', '(invisible cell', 'for right-angle',
                      'dragon).'],
                     ['Level 5 new:', 'no new', 'dragons yet.']]
INFO_AMOUNT_LINES = [5, 6, 8, 12, 3]


def refresh_text(screen, lvl_num):
    font = pygame.font.Font(pygame.font.match_font('optima'), 28)
    for i in range(INFO_AMOUNT_LINES[lvl_num]):
        text_surface = font.render(LVL_INFO_FOR_USER[lvl_num][i], False, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 50 * (i + 1))
        screen.blit(text_surface, text_rect)

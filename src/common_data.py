import pygame

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


class Globals:
    def __init__(self):
        self.AMOUNT_OF_CELLS = 4
        self.WIDTH = 1024
        self.HEIGHT = 768
        self.FPS = 60
        self.CELL_SIZE = 95
        self.FIELD_TOP = [200, 200, 200, 200, 200]
        self.FIELD_LEFT = [200, 200, 200, 200, 200]
        self.AMOUNT_OF_DRAGONS = [1, 2, 5, 3, 4]
        self.AMOUNT_OF_BORDERS = [12, 11, 1, 1, 4]
        self.DRAGON_SIZES = [[[1, 1]],
                             [[1, 1], [2, 2]],
                             [[1, 1], [2, 2], [2, 2], [1, 2], [2, 3]],
                             [[1, 1], [3, 3], [3, 3]],
                             [[1, 1], [2, 2], [1, 2], [3, 3]]]
        self.INFO_AMOUNT_LINES = [5, 6, 8, 12, 3]
        self.SHAPES = [[UNIQUE_SHAPES[0]],
                       [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1]],
                       [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1], UNIQUE_SHAPES[1], UNIQUE_SHAPES[2], UNIQUE_SHAPES[3]],
                       [UNIQUE_SHAPES[0], UNIQUE_SHAPES[4], UNIQUE_SHAPES[5]],
                       [UNIQUE_SHAPES[0], UNIQUE_SHAPES[1], UNIQUE_SHAPES[2], UNIQUE_SHAPES[5]]
                       ]
        self.IMAGES = [['shape_1.png'],
                       ['shape_1.png', 'shape_2.png'],
                       ['shape_1.png', 'shape_2.png', 'shape_2.png', 'shape_3.png', 'shape_4.png'],
                       ['shape_1.png', 'shape_5.png', 'shape_6.png'],
                       ['shape_1.png', 'shape_2.png', 'shape_3.png', 'shape_6.png']]
        self.BORDERS_PLACES = [
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

    def get_field_top(self, num):
        return self.FIELD_TOP[num]

    def get_field_left(self, num):
        return self.FIELD_LEFT[num]

    def get_amount_of_dragons(self, num):
        return self.AMOUNT_OF_DRAGONS[num]

    def get_amount_of_borders(self, num):
        return self.AMOUNT_OF_BORDERS[num]

    def get_dragon_sizes(self, num):
        return self.DRAGON_SIZES[num]

    def get_shapes(self, num):
        return self.SHAPES[num]

    def get_image(self, num):
        return self.IMAGES[num]

    def get_border_places(self, num):
        return self.BORDERS_PLACES[num]


info = Globals()


def refresh_menu(screen):
    screen.fill((130, 130, 255))
    font = pygame.font.Font(pygame.font.match_font('optima'), 48)
    text_surface = font.render('Little Dragon Blocks', False, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (info.WIDTH / 2, 100)
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


def refresh_text(screen, lvl_num):
    font = pygame.font.Font(pygame.font.match_font('optima'), 28)
    for i in range(info.INFO_AMOUNT_LINES[lvl_num]):
        text_surface = font.render(LVL_INFO_FOR_USER[lvl_num][i], False, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 50 * (i + 1))
        screen.blit(text_surface, text_rect)
import pygame
from common_data import WIDTH, HEIGHT, FPS, AMOUNT_OF_CELLS, CELL_SIZE
from common_data import SHAPES, FIELD_TOP, FIELD_LEFT, AMOUNT_OF_DRAGONS
from common_data import DRAGON_SIZES, AMOUNT_OF_BORDERS, BORDERS_PLACES, refresh_text
from field import Field
from dragon import Dragon
from border import Border


def run_lvl(lvl_num, running, screen, clock):
    dragon_field = Field()
    dragon_field.set_view(FIELD_LEFT[lvl_num], FIELD_TOP[lvl_num])
    all_sprites = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    dragons_status = []
    for i in range(AMOUNT_OF_DRAGONS[lvl_num]):
        dragons_status.append(Dragon(lvl_num, SHAPES[lvl_num][i], i + 1, DRAGON_SIZES[lvl_num][i][0] * CELL_SIZE,
                                     DRAGON_SIZES[lvl_num][i][1] * CELL_SIZE))
        all_sprites.add(dragons_status[i])
    for i in range(AMOUNT_OF_BORDERS[lvl_num]):
        borders.add(Border(BORDERS_PLACES[lvl_num], i))
    dragon_field.set_borders(BORDERS_PLACES[lvl_num])
    next_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                next_run = False

        all_sprites.update(dragon_field, CELL_SIZE * AMOUNT_OF_CELLS)

        screen.fill((255, 204, 255))
        refresh_text(screen, lvl_num)
        dragon_field.render(screen)
        all_sprites.draw(screen)
        borders.draw(screen)
        can_we_go_next_lvl = True
        for i in range(AMOUNT_OF_DRAGONS[lvl_num]):
            if not dragons_status[i].ready:
                can_we_go_next_lvl = False
                break
        if can_we_go_next_lvl:
            next_run = True
            running = False
        pygame.display.flip()
        clock.tick(FPS)
    return next_run

import pygame
from common_data import WIDTH, HEIGHT, FPS, AMOUNT_OF_CELLS, CELL_SIZE
from common_data import SHAPES, FIELD_TOP, FIELD_LEFT, AMOUNT_OF_DRAGONS, DRAGON_SIZES
from field import Field
from dragon import Dragon


def run_lvl(lvl_num, running, screen, clock):
    dragon_field = Field()
    dragon_field.set_view(FIELD_LEFT[lvl_num], FIELD_TOP[lvl_num])
    all_sprites = pygame.sprite.Group()
    dragons_status = []
    for i in range(AMOUNT_OF_DRAGONS[lvl_num]):
        print(DRAGON_SIZES[i])
        dragons_status.append(Dragon(SHAPES[lvl_num][i], i + 1, DRAGON_SIZES[lvl_num][i][0] * CELL_SIZE,
                                     DRAGON_SIZES[lvl_num][i][1] * CELL_SIZE))
        all_sprites.add(dragons_status[i])
    next_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                next_run = False

        all_sprites.update(dragon_field, CELL_SIZE * AMOUNT_OF_CELLS, screen)

        screen.fill((255, 204, 255))
        dragon_field.render(screen)
        all_sprites.draw(screen)
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

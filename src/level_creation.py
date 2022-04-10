import pygame
from src.common_data import info, refresh_text
from src.field import Field
from src.dragon import Dragon
from src.border import Border


def run_lvl(lvl_num, running, screen, clock):
    dragon_field = Field()
    dragon_field.set_view(info.get_field_left(lvl_num), info.get_field_top(lvl_num))
    all_sprites = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    dragons_status = []
    for i in range(info.get_amount_of_dragons(lvl_num)):
        dragons_status.append(Dragon(lvl_num, info.get_shapes(lvl_num)[i], i + 1,
                                     info.get_dragon_sizes(lvl_num)[i][0] * info.CELL_SIZE,
                                     info.get_dragon_sizes(lvl_num)[i][1] * info.CELL_SIZE))
        all_sprites.add(dragons_status[i])
    for i in range(info.get_amount_of_borders(lvl_num)):
        borders.add(Border(info.get_border_places(lvl_num), i))
    dragon_field.set_borders(info.get_border_places(lvl_num))
    next_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                next_run = False

        all_sprites.update(dragon_field, info.CELL_SIZE * info.AMOUNT_OF_CELLS)

        screen.fill((255, 204, 255))
        refresh_text(screen, lvl_num)
        dragon_field.render(screen)
        all_sprites.draw(screen)
        borders.draw(screen)
        can_we_go_next_lvl = True
        for i in range(info.get_amount_of_dragons(lvl_num)):
            if not dragons_status[i].ready:
                can_we_go_next_lvl = False
                break
        if can_we_go_next_lvl:
            next_run = True
            running = False
        pygame.display.flip()
        clock.tick(info.FPS)
    return next_run

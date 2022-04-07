import pygame
from common_data import WIDTH, HEIGHT, FPS, AMOUNT_OF_CELLS, CELL_SIZE
from field import Field
from dragon import Dragon
from lvl_0 import SHAPES, FIELD_TOP, FIELD_LEFT


def run_lvl(running, screen, clock):
    dragon_field = Field()
    dragon_field.set_view(FIELD_LEFT, FIELD_TOP)
    all_sprites = pygame.sprite.Group()
    dragon_one = Dragon(SHAPES[1])
    all_sprites.add(dragon_one)
    next_run = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                next_run = False

        all_sprites.update(FIELD_LEFT, FIELD_TOP, CELL_SIZE * AMOUNT_OF_CELLS, screen)

        screen.fill((255, 204, 255))
        dragon_field.render(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    return next_run

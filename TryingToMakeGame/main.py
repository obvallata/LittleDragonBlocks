import pygame
from field import Field
from dragon import Dragon

pygame.init()
WIDTH = 1024
HEIGHT = 768
FPS = 60
AMOUNT_OF_CELLS = 4
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dragon_field = Field(AMOUNT_OF_CELLS, AMOUNT_OF_CELLS)
dragon_field.set_view(200, 200, 95)
all_sprites = pygame.sprite.Group()
dragon_shape = [[1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
dragon_one = Dragon('img_1.png', dragon_field.cell_size, dragon_field.cell_size, dragon_shape)
all_sprites.add(dragon_one)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(200, 200, 95 * AMOUNT_OF_CELLS, screen)

    screen.fill((255, 204, 255))
    dragon_field.render(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


